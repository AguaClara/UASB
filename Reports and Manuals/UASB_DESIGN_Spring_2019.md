

##Methods

##design for influent system

For the influent system, we have decided to move forward with the Summer 2018 team's plan for a tipping bucket that leads into separate pipes that then enter the reactor through the
 side. The summer 2018 UASB team suggested 2 pipes, but after considering the results of the tapioca tests performed by the fall 2018 team, the spring 2019 UASB team has decided to use four influent pipes to promote evenly distributed flow through the sludge blanket.

```python
# Import tools
from aide_design.play import*
import doctest

# Define functions
def UASB_Size(diam, height, HRT, sludge_percent):
    """Takes in diameter, height, average hydraulic residence time (HRT),
    and percentage of volume occupied by sludge blanket of model UASB.
    Outputs volume, required average flow rate, and the number of people served
     per reactor for both mixed wastewater and blackwater (pure toilet water)
    >>> from aide_design.play import*
    >>> UASB_Size(3 * u.ft, 7 * u.ft, 4 * u.hr, 0.7)
    [<Quantity(1401.1199563135376, 'liter')>,
     <Quantity(0.06810999787635252, 'liter / second')>, 22, 113]
    """
    WW_gen = 3 * u.mL/u.s
    #Wastewater generated per person, rule of thumb from Monroe
    WW_gen_bw = 0.6 * u.mL/u.s
    #Assumes 20% of mixed wastewater
    vol_reactor = (diam/2)**2 * math.pi * height
    vol_reactor_sludge = vol_reactor * sludge_percent
    #Calculate total volume of reactor containing sludge blanket
    # used in HRT calculation
    flow = vol_reactor_sludge / HRT
    #Average flow rate through reactor given by volume and residence time
    people_served = int(flow / WW_gen)  #People served per reactor
    people_served_BW = int(flow / WW_gen_bw)
    #People served per reactor treating only blackwater
    output = [vol_reactor.to(u.L), flow.to(u.L/u.s), \
    people_served, people_served_BW]
    return output
```

According to this function, based on our decided tank size of 3 ft diameter with 7 ft height, a 4 hr HRT, and 70% sludge percentage, the required average flowrate for sludge in the reactor is .068 l/s. The team then used average flow rate and desired exit velocity to calculate necessary headloss in order to find the necessary height of the tipping bucket. The summer 2018 listed acceptable ranges of exit velocity from .03 m/s (lower end to scour particles from inflent pipes)to 1 m/s (any faster likely to cause preferential pathways). Somewhat arbitrarily, the team picked .07 m/s as its desired exit velocity. The team also somewhat decided to use 3 in diameter influenet pipes in its design based on previous teams research.


  ```python

def calculate_head(target_exitvel, nom_diam, pipe_length, Kminor, Temp,
pipe_rough):
  """Takes in desired exit velocity as well as pipe size and hydraulic parameters
   and calculates the hydraulic head needed to achieve this velocity
   using head loss function from aide_design.
   Assumes use of schedule 40 pipes.


  """
  pipe_ID = pipe.ID_sch40(nom_diam)
  # Calculates pipe inner diameter from nominal diameter
  pipe_flow = target_exitvel * pc.area_circle(pipe_ID)
  #find flowrate based on exit velocity
  Nu = pc.viscosity_kinematic(Temp)
  headloss = pc.headloss(pipe_flow, pipe_ID, pipe_length, Nu, Pipe_rough, Kminor)
  return headloss

calculate_head(.07*u.m/u.s, 3*u.in, )
```


```python

def head_gain_per_dump(dump_vol, nom_diam, pipe_height, tank_width, tank_length):
  """Determines gain in hydraulic head per dump of tipping bucket
   based on geometry of influent system.  Assumes all water is
   added first to pipes, then additional volume fills the
   influent tank.  Pipe_height is total length of pipe above
   water level set by effluent line.  Assumes schedule 40 pipe.
   For influent system with no space in pipes above standing water level,
   set pipe height to 0.

  """
  pipe_ID = pipe.ID_sch40(nom_diam)
  pipe_vol = pc.area_circle(pipe_ID) * pipe_height
  if pipe_vol.to_base_units >= dump_vol.to_base_units:
    headgain = dump_vol / pc.area_circle(pipe_ID)
  else:
    tank_fill_vol = dump_vol - pipe_vol
    #volume filling influent tank after pipes are full
    tank_headgain = tank_fill_vol / (tank_width * tank_length)
    #calculate headgain from tank fill volume
    headgain = tank_headgain + pipe_height
  return headgain

def check_pipe_vel(exit_vel, large_pipe_diam, small_pipe_diam):
  """Check velocity of water flowing through larger
  influent pipe. Inputs are velocity through the smaller pipe
  (exit velocity calculated above), and diameter of each pipe.
  This is used to confirm that flow is below 0.2 m/s
  for a piece of the influent, to allow air bubbles to escape.

  """
  large_pipe_vel = \
  exit_vel * (small_pipe_diam ** 2) / (large_pipe_diam ** 2)
  return large_pipe_vel

  ```
**DETERMINING THE HEIGHT OF THE TIPPING BUCKET**
  In order to determine the height of the tipping bucket, the team started by determining the height at which the holding tank would need to be positioned so that it would empty out only once it was full, in order to ensure that each of the four inlet pipes will recieve an equal amount of water for each dump of the tipping bucket. In order for that to happen, the water level inside of the reactor must be level with the bottom of the holding tank. According to past team's research, the The reactor will be filled 50% with sludge, which will be 3.5 ft.  **DETERMINE HOW MUCH SLUDGE CAN BE EXPECTED TO EXPAND** Assuming that the tank is about 70% full of liquid, the height of the water in the tank would be 5 ft. Based on that calculation, the bottom of the holding tank should be at a height of 58.8 in to ensure the flow divider is completely filled before it begins emptying out.


```python

def height_bottom_holding_tank(percent_filled, height_reactor):
  height= percent_filled*height_reactor.to(u.inch)+1.2*u.inch
  return height

```

![Screen Shot 2019-02-17 at 1.25.33 PM](/assets/Screen%20Shot%202019-02-17%20at%201.25.33%20PM.png)

To make the UASB as compact as possible and reduce the horizontal distance influent waste water must travel and resulting settling, the holding tank will be directly attached to the side of the reactor. Since the holding tank will need to fill hold the tipping bucket system and about 16 L of waste water, it will need to be held up by additional supports on the ground. **material for supports? specific attachment? how many supports?**


The parameters for the holding tank, with a 5-gallon bucket mounted inside, are summarized in the table below:

| Parameter | Value | Justification |
|:-------------- |:-----  |------------- |
|Height|$\geq$ 40 cm| Height of bucket plus 4 cm error|
|Width|35 cm |30 cm for bucket diameter plus 5 cm for both pivot pieces|
|Length|$\geq$ 60 cm|Height of bucket plus extra space to allow free rotation.  Requires closer examination in fusion|


The holding tank will empty into the flow dividing tank, which is essentially just a smaller tank that is partitioned into four equal sections.

For the flow dividing tank, we chose a 6 gallon 14" by 10" by 10" polethylene tank. We chose that tank so that the four 3 inch diameter pipes could fit while minimizing the horizontal space around them to prevent settling as much as possible. The bucket will then be divided into four sections with 1.5"

Descending wastewater must go thoruogh the dividing tank at a rate slow enought to allow for gas bubbles to escape.
The bottom of the holding tank will then lead into the four influent pipes to decrease settling.




```python
```

Each inlet pipe will lead to a point on the bottom of the reactor, so that the four points of influence are as far away from each other as possible. The bottom of the UASB reactor has a diameter of 3 ft. So, if the center of the reactor is considered to be the origin, then the four points of influence on the bottom of the reactor in polar coordinates will be: (.75 ft, $pi$/4 rad), (.75 ft, 3$pi$/4 rad), (.75 ft, -$pi$/4 rad), (.75 ft, -3$pi$/4 rad)

```python
from aguaclara.play import *
(.75*u.ft, math.pi/2)
```
After the team decided on the locations for the points of influence on the bottom of the reactor, it moved on to deciding how to connect each pipe from the tipping bucket to its respective point of influence. In doing so, the team took effort to reduce headloss of the pipes and make the exiting velocity at each of the point of influence as equal as possible.

![Screen Shot 2019-02-17 at 12.41.38 PM](/assets/Screen%20Shot%202019-02-17%20at%2012.41.38%20PM.png)

The pipes carrying wastewater from the tipping bucket are vertical. Then, the water needs to be directed to enter the side of the reactor in the horizontal direction (horizontal entry was decided on for ease of fabrication, since it would be difficult to drill ellipses into the UASB reactor to allow for diagonal entry).  The  team considered using 135 degree elbows instead of 90 degree elbows for the change of direction  to reduce headloss. The team also considered to try to use diagonal pipes to minimize the amount of horizontal pipes, as settling is more likely to occur in horizontal pipes than diagonal pipes.However, after floating the idea at a technical feedback session, the team realized that such pipes may not be readily available in Honduras, and so it decided to use 90 degree elbows in the design.

Based on previous team's research, the influent pipes will be between 75 and 100 mm, so there will need to be four holes of that size drilled into the side of the reactor.

After the team made these design decisions, it turned to hydraulic code from previous teams to finalize dimensions of the reactor including height of tipping bucket, height of the canister, diameter of influent pipes. HOLD UP STUFF USING 80 20 extrustion bars
