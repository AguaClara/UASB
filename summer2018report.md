# Upflow Anaerobic Sludge Blanket Research and Design Report

## Summer 2018

#### Ian Cullings, Isa Kaminsky, Ananya Gangadhar


### Abstract
Since Spring 2017, the AguaClara Upflow Anaerobic Sludge Blanket (UASB) Team has been working on a detailed design of modified, pilot-scale UASB reactor originally proposed in an EPA P3 proposal. A UASB reactor treats wastewater anaerobically and produces biogas as a by-product. Working towards that goal, the team has created Python code to record the design process and calculations for this AguaClara UASB. This document serves as a master guide for the design process.

Over the summer of 2018, the UASB team's main goal has been to finish a complete design of a UASB wastewater treatment system, and fabricate an influent system.  Future teams will work on fabrication of the entire system and testing at the Ithaca Area Wastewater Plant before implementation in Honduras.

**_Juan's comments:_** (RESOLVED-AG) You give very little background as to what's going on, and this section does not have a title. I believe this is an 'abstract'


## Influent Flow System

One major design goal for the summer was to finish the influent system that delivers wastewater to the bottom of the reactor from a holding tank.

**_Juan's comments: (AG - not a 100% sure I know what sort of image would be helpful here) I think a figure would be very useful here, as it is extremely difficult to understand what's going on without being able to image the reactor_**


#### Continuous versus Pulse Flow

When design of the influent system began in Spring 2018, the team assumed flow into the reactor would be continuous and at a roughly constant rate. (This is already a major assumption, as wastewater production will generally rise in the day and lower at night.)  However, doing the initial calculations, this would require a pipe diameter on the order of 10 mm, which would clog easily and create major problems with the flow system.  

During a meeting with Ed Gottlieb, an operator at the Ithaca Area Wastewater Treatment Plant, the idea of a pulse flow system was suggested, which would collect wastewater, then deliver it in larger "pulses" to achieve the hydraulic parameters needed.  Mr. Gottlieb's two suggested possible methods were: A tipping bucket system or a siphon.  

#### Tipping Bucket versus Siphon System

The summer team researched siphons and discussed with the AguaClara program director, Monroe, potential design flaws - specifically the diameter of pipe that should be used. The main concern was that if too large a pipe was used, water would be able to pass through the siphon before it had filled to the level needed to create a pulse of a specific volume.

Ultimately, the team was unable to find detailed enough engineering guidelines on how to design for a siphon using pulse flow. Given this, and given that the addition of an entrance tank required only one tipping bucket, the team settled on the tipping bucket design.

**_Juan's comments:_** (XD RESOLVED-AG) Using 'M-dawg' is extremely inappropriate.

#### Hydraulic Parameters

Built within the design of the influent systems are a number of hydraulic constraints that must be met for the flow to work properly.  These are summarized in Table 1 below.

<p align="center">Table 1: Design parameters for UASB hydraulics </p>

| Parameter                        | Value           | Constrained? | Justification                                                                                                                                                                                                |
|:-------------------------------- |:--------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Reactor Volume                   | 1221 Liters     | Yes          | Based on max diameter and height to allow fabrication                                                                                                                                                        |
| Sludge Volume                    | ~850 Liters     | No           | Roughly 70% of Reactor Volume.  Needs to be better constrained based on location of tube settler.                                                                                                            |
| HRT                              | $\geq$ 4hrs     | Yes, minimum | Based on literature and lab scale test.                                                                                                                                                                      |
| Descending Sewage Velocity       | $\leq$ 0.2 m/s  | Yes, Maximum | Maximum velocity that will allow air bubbles to rise out of reactor.  Must only be achieved in beginning of influent pipe systems, not throughout.                                                           |
| Average Flow Rate                | $\leq$ 0.08 L/s | Yes, Maximum | Q = Volume / Hydraulic Residence Time                                                                                                                                                                        |
| Minimum Exit Velocity            | $\geq$ 0.03 m/s | Yes          | Minimum velocity needed to scour settling particles                                                                                                                                                          |
| Maximum Exit Velocity            | $\leq$ 1 m/s    | No           | Max velocity needed to prevent preferential pathways through sludge blanket.  Still very undetermined.                                                                                                       |
| Influent Pipe Inner Diameter     | 75 - 100 mm      | No           | Based on literature values to prevent clogging in pipes.  Some flexibility.                                                                                                                                  |
| Influent Pipe Length             | ~8.5 feet       | Yes          | Roughly equal to height of reactor plus half of diameter (see influent pipe geometry)                                                                                                                        |
| Bucket Dump Volume               | ~20 L           | No           | Constraints are: time to fill bucket and relative volume to reactor capacity. A large dump volume allows more time for the bucket to fill, slowing down wear and tear. But the dump volume should also be a relatively small fraction of the total reactor volume. 20 L chosen as it is the volume of easily available buckets while fulfilling these constraints |
| Wastewater Generation per Person | 10.8 L/hr       | No           | Rule of Thumb from Monroe   |

**_Juan's comments:_** (RESOLVED-AG) Under 'bucket dump volume,' your 'should be larger' and 'should be smaller' are not clear. Are you referring to the time or the volume?

From these constraints, the general headloss equation (including the headloss trick) for a circular pipe can be used to determine the headloss needed to achieve our desired exit velocity, given a specific diameter of pipe.  

#### Design of Tipping Bucket system

Given these parameters, the team started to design the tipping bucket system.  Design began by looking into tipping bucket systems online; however, since tipping buckets are generally only used in water parks, it was difficult to find any detailed design processes for these systems. At this point, the team was left with two choices: try to complete a mathematical model of the tipping bucket system (using free-body diagrams), or create a physical model of the tipping bucket system and test it in many configurations to find the optimal design.  Given time constraints and lack of expertise, the team decided to fabricate a tipping bucket it and test it physically.

**_Juan's comments:_** (RESOLVED-AG)"Given these parameters, the team began *planning the design of the tipping bucket system*" I don't think "plan on" is the best way to say that.


<center><img src="https://github.com/AguaClara/UASB/blob/master/IMG_5759%20copy.png?raw=true">
<p>
<em>Figure 1: Timmy the Tipping Bucket</em>
</p>
</center>

**_Juan's comments:_** (AG + IK - Fixed!) This picture (which only shows up online, not in markdown preview) should be cleaned up a bit. It can be cropped a bit, and the background would be clear (as it can be in the lab) instead of cardboard.

Pictured above is the first design of the tipping bucket system.  It was created with a small plastic lab beaker, two screws, and 80-20 extrusion bars with connectors used to provide a pivot for the screws.  This was mostly created to give the team a general sense of how tipping buckets work, not to collect specific data.  This model offered a few insights for the design:

* Location of the pivot on the bucket is very important for operation.  Height of the pieces controls how much water is collected before dumping.  Horizontal positioning of the pivot determines the angle the bucket rests at and how soon it will tip.

* The bucket needs to be designed so that it will not rest completely tipped down.  This can be achieved either by controlling the height of the bucket so that is cannot rotate completely (making it hit the bottom of the tank) or by controlling the rotation, either through adding a counterweight that will return the bucket to its main position, or adjusting the horizontal location of the pivot to ensure it will return.

After discussing the design more with Monroe, the team settled on a new design, pictured below:

**_Juan's comments:_** (SORT OF RESOLVED - AG: I thought these labeled images might be more helpful to understand what's going on) This is cool but I have no idea what I'm looking at. Can you include one of those links online in fusion where we can spin things around and look inside? ![something like this one](https://myhub.autodesk360.com/ue28a131e/g/shares/SH7f1edQT22b515c761e7fb9f856bcad56c1) that Jonathan made of the 1 LPS plant.

<center><img src="https://github.com/AguaClara/UASB/blob/master/Images/Influent_Tank_Tipping_Bucket.png?raw=true">
<p>
<em>Figure 2: Influent System with Tipping Bucket</em>
</p>
</center>

This bucket is created with a 5 gallon bucket (chosen as they are easy to purchase) with two plastic rods on either side, attached through a hose clamp.  These circular pieces will rest in the brackets on either side of the entrance tank, where they can roll freely to allow the bucket to dump.  This greatly reduces friction and wear of mechanical parts.

<center><img src="https://github.com/AguaClara/UASB/blob/master/Images/Influent_System_Brackets_Pivots.png?raw=true">
<p>
<em>Figure 3: Rectangular bracket with the "roller pivot"</em>
</p>
</center>

The addition of the hose clamp also allows for the pieces to be moved spatially around the bucket easily, allowing the team to test many different orientations of the pivot without drilling new holes in the bucket.  This also will allow easy replacement of the bucket system if necessary, as important as pieces will inevitably break.

This model became the teams the first design to model the tipping bucket function.  However, after beginning fabrication, the team realized that the design would not work due to the geometry of the bucket and the attached pivot rods.  Since the bucket was circular, any placement of the rod off of the center would lead the rods to point orthogonally outwards and not form a straight pivot.  This is shown the figure below.


<center><img src="https://github.com/AguaClara/UASB/blob/master/Images/Tipping_Bucket_Off_Centered_Pivots.png?raw=true">
<p>
<em>Figure 4: Top view of tipping bucket showing the off-centered pivots</em>
</p>
</center>

After discussing this problem further, the team considered two possible options.  The first was to purchase a square bucket to use in the same manner.  The second was to create a frame for the bucket that would provide a straight pivot without hindering tipping.  Since materials were available, and it provided much more flexibility for testing, the team moved forward with the second option.

The frame is pictured below, attached to the 5-gallon bucket used within the system.  1-inch by 1-inch aluminum 80-20 bars were used to create a modular base around the bucket that could be easily extended or compressed to fit the dimensions of the bucket snugly.  

<center><img src="https://raw.githubusercontent.com/AguaClara/UASB/master/Images/Tipping%20Bucket-%20Brackets%20Labeled.png">
<p>
<em>Figure 5: Tipping bucket mounted on the aluminum frame for bench top testing</em>
</p>
</center>

Two additional pieces were then added extending down from the 80-20 square to the bottom of the bucket.  These pieces extended 1 inch below the bucket, allowing an L-bracket to be attached below.  This was securely attached to the bottom of the bucket, locking it in place.  When testing the bucket, this could be easily moved downwards, and the L-bracket moved up to hold the bucket in place.

Finally, a double sided screw piece was added to the pivot rods to allow them to attach to the 80-20 extrusion bars.  This piece was added by facing the rods with a lathe, and drilling the pieces in.  All of the this was done with the help of the shop managers.  With these pieces in, the rods can be easily moved laterally along the bucket and then tightened

#### Design of Influent Tank

Another crucial part of the design  is the influent tank.  This tank will capture all wastewater from the tipping bucket, and distribute it evenly across both influent pipes from flow control.  To prevent any splashing of wastewater, the tipping bucket will be completely contained within the influent tank.

The crucial design aspects of the tank are listed below:

* The tank **must be tall enough** to completely contain the tipping bucket, and prevent any "splashing" of wastewater out of the tank
* The tank **must be just wide enough** to contain the bucket and the two brackets.  If the tank is wider, that will require more material for longer roller pivots, and reduce the structural strength of the bucket (since deflection of a rod is proportional to some power of length)

* The dimensions of the tank must be such that they **create the required amount of hydraulic head from one dump of the tipping bucket**.  
This can be achieved by choosing the appropriate geometry at the bottom of the tank to ensure the required height increase of the water level per volume of dump.

**_Juan's comments: (RESOLVED-AG) What do you mean adding or removing material? What kind of material are you adding or removing? How are you removing material from a tank?_**

* The tank **must evenly split flow between the two pipes**.  This can be designed by changing the geometry of the pipes based on where the water is dumped, but most importantly, there should always be a small volume of water in the tank even when all the water from one dump has been drained out. This is to provide enough volume within tank where the **descending sewage velocity is below 0.2 m/s** to allow air bubbles to escape.

**_Juan's comments: (RESOLVED-AG) Why? I believe this point should be combined with the next one._**

* The tank should be **easy to source**, that is it can be purchased at the correct dimensions, or fabricated simply


Summarized in a table:

| Parameter | Value | Justification |
|:-------------- |:-----  |------------- |
|Height|$\geq$ 40 cm| Height of bucket plus 4 cm error|
|Width|35 cm |30 cm for bucket diameter plus 5 cm for both pivot pieces|
|Length|$\geq$ 60 cm|Height of bucket plus extra space to allow free rotation.  Requires closer examination in fusion|

<center><img src="https://github.com/AguaClara/UASB/blob/master/Images/Influent%20Geo%20Slant.png?raw=true">
<p>
<em>Figure 6: Schematic of Influent System</em>
</p>
</center>


The team began by designing the tank as a simple, rectangular box.  However, given the constraints on the dimensions of the box, it was impossible to get the required hydraulic head gain from bucket, as summarized in the code below:

```python
from aide_design.play import*

width = 35 * u.cm
length = 60 * u.cm
area = width * length
bucket_vol = 15 * u.L
head_gain = (bucket_vol / area).to(u.cm)
print("One dump of the bucket gives", head_gain, "of hydraulic head")
```
Next, the team considered adding more material into the bottom of the tank (adding sloped walls, making it more pyramidal).  Since there would be less volume in the bottom of the tank, this would allow hydraulic head to be gained per dump of the bucket.  However, after running more calculations it was determined that it was very challenging to meet this criteria and still fit the bucket fully within the entrance tank.

**_Juan's comments:(RESOLVED-AG) Ah now your reference to adding material makes more sense. This explanation of adding material should be included before you talk about it in the bullet point above._**

After further discussion with Monroe, a new design to solve this problem was suggested.  Instead of a sloped tank, the tank would remain rectangular, and larger pipes along the bottom would be added, which would then connect to the influent pipes.

<center><img src="https://github.com/AguaClara/UASB/blob/master/Images/Influent_Tank_Geometry.png?raw=true">
<p>
<em>Figure 7: Close up of the influent system showing the larger cylindrical pipe segments</em>
</p>
</center>

The addition of the cylindrical pipe segments serves two purposes:
1. The flow is split into two influent pipes almost equally.
2. Since the diameter of the cylinder segments is larger than that of the influent pipe, the descending sewage velocity in it will be lower. This allows air bubbles to escape from the wastewater which is desirable.


**_Juan's comments: (RESOLVED - AG) This image helps a bit but I still don't quite understand how this helps your problem. I think a bit more explanation is required. The idea is to have a future team member read through this all and understand your logic, else they will not be able to understand the design._**

### Hydraulic Code

The code below calculates the important parameters for the influent system.  The parameterized functions allow for each function to be utilized for differing designs to allow the team to compare and contrast designs simply.  The functions below must be defined and then can be utilized in the following section.

```python
# Import tools
from aide_design.play import*
import doctest

# Define functions
def UASB_Size(diam, height, HRT, sludge_percent):
    """Takes in diameter, height, average hydraulic residence time (HRT), and percentage of volume occupied by sludge blanket of model UASB. Outputs volume, required average flow rate, and the number of people served per reactor for both mixed wastewater and blackwater (pure toilet water)
    >>> from aide_design.play import*
    >>> UASB_Size(3 * u.ft, 7 * u.ft, 4 * u.hr, 0.7)
    [<Quantity(1401.1199563135376, 'liter')>, <Quantity(0.06810999787635252, 'liter / second')>, 22, 113]
    """
    WW_gen = 3 * u.mL/u.s        #Wastewater generated per person, rule of thumb from Monroe
    WW_gen_bw = 0.6 * u.mL/u.s   #Assumes 20% of mixed wastewater
    vol_reactor = (diam/2)**2 * math.pi * height
    vol_reactor_sludge = vol_reactor * sludge_percent #Calculate total volume of reactor containing sludge blanket, used in HRT calculation
    flow = vol_reactor_sludge / HRT #Average flow rate through reactor given by volume and residence time
    people_served = int(flow / WW_gen)       #People served per reactor
    people_served_BW = int(flow / WW_gen_bw) #People served per reactor treating only blackwater
    output = [vol_reactor.to(u.L), flow.to(u.L/u.s), people_served, people_served_BW]
    return output

def bucket_filltime(flowrate_avg, dump_vol):
    """Takes in average flow rate into tipping bucket and the fill volume before one dump and calculates the average time it takes the bucket to fill and dump.
    >>> from aide_design.play import*
    >>> bucket_filltime(0.068 * (u.L/u.s), 16.26 * u.L)
    [<Quantity(239.1, 'second')>]
    """
    filltime = dump_vol / flowrate_avg
    return filltime.to(u.s)

def calculate_head(target_exitvel, nom_diam, pipe_length, Kminor, Temp, pipe_rough):
  """Takes in desired exit velocity as well as pipe size and hydraulic parameters and calculates the hydraulic head needed to achieve this velocity using headloss function from aide_design.  Assumes use of schedule 40 pipes.


  """
  pipe_ID = pipe.ID_sch40(nom_diam)   # Calculates pipe inner diameter from nominal diameter
  pipe_flow = target_exitvel * pc.area_circle(pipe_ID) #find flowrate based on exit velocity
  Nu = pc.viscosity_kinematic(Temp)
  headloss = pc.headloss(pipe_flow, pipe_ID, pipe_length, Nu, Pipe_rough, Kminor)
  return headloss

def head_gain_per_dump(dump_vol, nom_diam, pipe_height, tank_width, tank_length):
  """Determines gain in hydraulic head per dump of tipping bucket based on geometry of influent system.  Assumes all water is added first to pipes, then additional volume fills the entrance tank.  Pipe_height is total length of pipe above water level set by effluent line.  Assumes schedule 40 pipe.  For influent system with no standing water in pipes, set pipe height to 0.


  """
  pipe_ID = pipe.ID_sch40(nom_diam)
  pipe_vol = pc.area_circle(pipe_ID) * pipe_height
  if pipe_vol.to_base_units >= dump_vol.to_base_units:
    headgain = dump_vol / pc.area_circle(pipe_ID)
  else:
    tank_fill_vol = dump_vol - pipe_vol #volume filling influent tank after pipes are full
    tank_headgain = tank_fill_vol / tank_width * tank_length #calculate headgain from tank fill volume
    headgain = tank_headgain + pipe_height
  return headgain

def check_pipe_vel(exit_vel, large_pipe_diam, small_pipe_diam):
  """Check velocity of water flowing through larger influent pipe.  Inputs are velocity through the smaller pipe (exit velocity calculated above), and diameter of each pipe.  This is used to confirm that flow is below 0.2 m/s for a piece of the influent, to allow air bubbles to escape.

  """
  large_pipe_vel = exit_vel * (small_pipe_diam ** 2) / (large_pipe_diam ** 2)
  return large_pipe_vel

```

### Influent System Geometry

There are two designs the team is considering for the influent system geometry.  Each is summarized below, and the design functions are utilized to check the important parameters for each system to allow the team to compare and contrast possible designs.


```python
# Determines pipe diameter needed to achieve necessary hydraulic head
# Input hydraulic head calculated in from headloss function and volume of dump

def find_pipe_diam(headloss, dump_volume, tank_area, water_height):
  pipe_filled = dump_volume - (tank_area * water_height) # amount of pipe filled with water in each dump
  pipe_area = pipe_filled / headloss
  diam = pc.diam_circle(pipe_area)
  return diam
  print(diam)
# Run function for influent system dimensions
dump_volume = 15 * u.L
len = 60 * u.cm
wid = 35 * u.cm
tank_area = len * wid
water_height = 2 * u.cm
pipe_hl = total_hl - water_height  # headloss just within the pipe, total headloss minus the height of water within the tank
target_diam = find_pipe_diam(pipe_hl, dump_volume, tank_area, water_height)
print(target_diam.to(u.cm))
# Determine nominal diameter for pipe based on inner diameters
#NOM_diam = pipe.ND_SDR_available(target_diam, sch40)

```
The team then ensured that the velocity within the pipe is below 0.2 m/s, given the pipe diameter, to allow air bubbles to escape.  

```python
# Calculate the maximum velocity through the large diameter pipe when hydraulic head is largest after a dump
pipe_A = pc.area_circle(target_diam)
K_minor = 1 # incorporate all kinetic energy as loss through headloss trick
Temp = 23 * u.degC # average temp in Honduras
Nu = pc.viscosity_kinematic(Temp)
Pipe_Rough = 0.0015 * u.mm
FlowRate = pc.flow_pipe(target_diam, total_hl, pipe_hl, Nu, Pipe_Rough, K_minor)
Max_vel = (FlowRate / pipe_A).to(u.m / u.s)
print(Max_vel)

```

#### Testing the Tipping Bucket
##### Tapioca Tests
To attempt to model and understand flow patterns within the UASB system, the team ran tests through a model sludge bed within a scaled down model UASB.

Testing has begun with one influent pipe and eventually will be done with two influent pipes as well. If one influent pipe is sufficient to fluidize the sludge blanket, fabrication of the UASB would become a lot easier. However, the code would need to be updated to accommodate this change, and scaling up to larger reactors in the future would be more difficult.

The first UASB was modeled using a simple plastic beaker. Tapioca that had been soaked in water for 1.0 hours was used to model the sludge blanket. The beaker was filled to approximately 70% of its volume with the expanded tapioca. A 0.25 inch metal influent pipe was attached to tubing which was attached to a pump. Water was pumped into the beaker through the tube and the influent pipe, which emptied into the bottom center of the beaker perpendicular to the base of the beaker. Red dye enters the influent tube from another pump to allow for a better visualization of the flow patterns.

<center><img src="https://github.com/AguaClara/UASB/blob/master/Tapioca%20Test.JPG?raw=true">
<p>
<em>Figure 8: Set Up of the Tapioca Experiment Using One Influent Pipe</em>
</p>
</center>

The tests that have been performed were done at a low flow rate of 6.33 mL/s, which translates to an exit velocity of 0.2 m/s. So far, the dyed water appeared to spread out along the bottom of the beaker, rather than puncturing the tapioca blanket. Multiple tests will be run at different flow rates which will be calculated based on the exit velocities of interest. In addition, test will be run using both one and two influent pipes, and the results will be compared.

Below is the code used to calculate the flow rate needed to produce certain exit velocities from the influent pipe, as well as the code used to calculate the amount of water dumped per pulse. Below the functions is the specific calculation used to determine the exit velocity

```python
from aide_design.play import*
def find_pump_exitv(exit_vel_target, pipe_innerdiam, num_pipes):
  """Finds flow rate for pump system to reach input exit velocity via the continuity equation Q = vA.  Inputs are flow rate generated from pump, tubing inner diameter, and total number of pipes.  Flow rate is generated from table on confluence relating pump speed, pipe diameter and flow rate.  Does not account for head losses, water pressure, or change in head as they are negligible compared to pump speed.
  """
  inner_area = pc.area_circle(pipe_innerdiam)
  pump_Q = exit_vel_target * inner_area * num_pipes
  return pump_Q

def dump_percentage_bucket(dump_volume, UASB_volume):
  """Solves for the percentage of total volume added with each dump for tipping bucket case.  Inputs total dump volume and reactor volume.


  """
  bucket_percent = (dump_volume / UASB_volume) * 100
  return bucket_percent

def dump_percentage_pump(pump_flowrate, pump_flowtime):
  """Solves for the dump percentage created by pump system for tapioca tests.  Inputs flowrate created by pump and the total time pump is run.  


  """
  pump_percent = ((pump_flowrate * pump_flowtime) / UASB_volume) * 100
  return pump_percent.

def find_upflow_vel(UASB_Flowrate_avg, UASB_CrossArea):
    """Finds average upflow velocity within the reactor using tipping bucket system.  Inputs are flowrate through reactor and the cross sectional area within the reactor.
    """
    avg_upflow_vel = UASB_Flowrate_avg / UASB_CrossArea
    return avg_upflow_vel

#Run for target exit velocities
#Current setup ID is 1/4 inch (3/8 nom diam) and 1/8 inch (1/4 in nom diam)

flowrate1mps = find_pump_exitv(0.3 * u.m/u.s, .25 * u.inch, 1)
print(flowrate1mps.to(u.ml/u.s))

vol_dump = 24 * u.ml
area = pc.area_circle(11*u.cm)
height = vol_dump / area
print((height.to(u.cm)))


v = (6.33 * u.ml/u.s) / ((math.pi)*(.125 * u.inch)**2)
print(v.to(u.m/u.s))

v2 = find_pump_exitv(.2 * u.m/u.s, .25 * u.inch, 1)
print(v2.to(u.ml/u.s))

```

### Biogas Capture System

The team has begun preliminary discussions with Monroe regarding the Biogas Capture system. A meeting with Ed Gottlieb from the Ithaca wastewater plant has been scheduled to discuss integrating the UASB plant into the Ithaca wastewater plant, as well as to discuss biogas collection. Research to find biogas storage bags is ongoing.

## Fabrication manual

The team started to write a fabrication manual this summer that will document the total fabrication process so later teams can recreate the UASB system. This working document can be found in our Github repository.
