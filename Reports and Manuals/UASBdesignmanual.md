# UASB Design Manual

## Summer 2018

### Ian Cullings, Ananya Gangadhar, Isa Kaminsky

## Introduction

This document serves to detail the entire design process of the UASB system.  While each semester the team has worked on differing parts of the reactor, and solved different problems within, this document will collect all of these decisions into one place so that future readers can understand the design process of the UASB.  As such, this is a working document and will continuously be edited as designs are changed and new ideas are introduced.

## Reactor Tank

Initial design of the UASB models the 1 L/s plant closely, and thus assumed the use of a 3' diameter PVC pipe for the base of the tank, as the design required a bend in the pipe for the plate settlers.  Since the UASB system requires no bends and is completely vertical, it was proposed to use a prefabricated plastic tank instead.  

The advantages of the prefabricated tank are:

* Lower overall costs
* Easier fabrication of bottom and top of tank (since the tank is already sealed)
* Higher structural stability, particularly at bottom of tank
* Possible prefabrication of inlet and outlet system

The disadvantages include:
* Tanks are harder to source outside of the US and might require shipping. However, manufacturers in Honduras were found so this should not be a huge concern.
* Since tanks are prefabricated with lids, it becomes challenging to attach pieces inside the tank. While using a PVC pipe would provide better access to the interior of the tank, the goal is to avoid any modifications within the reactor altogether.
* Most prefabricated tanks are made of High Density Polyethylene (HDPE) rather than PVC. Additional costs will be required for welding rod and other materials.


*Table 1: Basic Reactor Design Parameters*
| Parameter | Value | Constraint                                                                            |
| --------- | ----- | ------------------------------------------------------------------------------------- |
| Height    | ~7ft  | Max height to still fit within lab space.  Could change based on fabrication location |
| Diameter  | 3ft   | No constraint. Chosen based on 1 L/s design   |

A preliminary search among Honduran suppliers found tanks of similar dimensions made of HDPE. The team thus decided to move forward with purchasing an HDPE tank for initial design testing. After local testing, the design can be modified if needed to accommodate materials found in Honduras.

The current plan is to purchase an HDPE tank similar to [this](https://www.plastic-mart.com/product/17049/300-gallon-plastic-tank-rotoplas-590314-590315) for fabrication of the first reactor. A final decision regarding the tank model to be used will be made in Fall 2018 after reviewing the constraints of the location we build in.


### Size and Dimensions


#### Calculations
```python
from aide_design.play import*

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

doctest.testmod(verbose=True)

# Run with current design parameters
UASB_design = UASB_Size(3 * u.ft, 7 * u.ft, 4 * u.hr, 0.7)
print(UASB_design[0])
print("The total volume of the reactor is", UASB_design[0], "\n" "The average flow rate through the system is", UASB_design[1], "\n" "The number of people served by this reactor is", UASB_design[2])
```



## Influent System

One crucial element of the UASB design is the structure of the influent system.  This will deliver wastewater into the reactor and maintain flow to prevent clogging and overflowing.

### Continuous versus Pulse Flow

In Spring 2018, when design of the influent system began, the team began by assuming flow into the reactor would be continuous and at a roughly constant rate. This was already a major assumption, as wastewater production will rise in the day and lower at night  However, doing the initial calculations, this would require a pipe diameter on the order of 10 mm, which would clog easily and create major problems with the flow system.  During a meeting with Ed Gottlieb, an operator at the Ithaca Area Wastewater Treatment Plant, the idea of a pulse flow system was suggested, which would collect wastewater, then deliver it in larger "pulses" to achieve the hydraulic parameters needed.  Mr. Gottlieb's suggested two possible systems: a tipping bucket or a siphon system.  

### Tipping Bucket versus Siphon System

The summer team researched siphons and discussed with Monroe potential design flaws, specifically the diameter of pipe that should be used. The main concern was that if too large a pipe was used, water would be able to pass through the siphon before it had filled to the level needed to create a pulse of a specific volume. Ultimately, the team was unable to find detailed enough engineering guidelines on how to design for a siphon using pulse flow. Given this, and given that the addition of an entrance tank required only one tipping bucket, the team settled on the tipping bucket design.

### Tipping Bucket Design

Based on a target pulse volume of 10-20 L, design centered around using a 5-gallon bucket for tipping.  The bucket will tip through a shaft system that is off-center, and will be mounted on a bracket system on the inside of a holding tank.  This tank will completely contain the tipping bucket so as to prevent any loss of wastewater during the dump.

Monroe and the team came up with a couple of design choices for the tipping bucket:

1. Weld two blocks of PVC to the sides of the 5-gallon bucket. Drill a rod into each block without penetrating the bucket. These rods are used to mount the bucket at a certain height inside the holding tank.

**(Insert design drawing here)**

   * **Pros**: Requires fewer materials. Is easier to fabricate.
   * **Cons**: Will need to align both rods perfectly. The welded sections will experience considerable shear. Replacing the bucket will be challenging.

2. Drill two holes in the bucket at an off-centered axis. Attach two screws to the bucket through these holes and use the screws to mount the bucket in the holding tank.

**(Insert design drawing here)**

* **Pros**: Less shearing
* **Cons**: Drilling holes makes the bucket vulnerable to leaks. Ease of replacement is still an issue

3. Weld two brackets onto the inner wall of the holding tank. Put a hose clamp around the bucket and mount the bucket via the clamp onto two small rollers. These rollers are placed into the brackets.

* **Pros**: Easily adjustable system allows for testing multiple pivot locations
* **Cons**: Challenging fabrication, requires extra parts

The team first decided to go with option 3 due to the modularity it provided.  However upon further discussion during fabrication, the team decided to fabricate a system using 80-20 bars that would be simpler to make and provide more modularity.

### Experimental Frame Design

The frame is made up of four bars that form a rectangle around the circumference of the bucket, two vertical bars perpendicular to the rectangle that extend parallel to the sides of the bucket, and one bar between the two vertical bars that is beneath the bucket for support.

**(Insert image of frame here)**

Originally, when the height of the pivots was lowered, the vertical bars would extend further than the base of the bucket (as seen in Figure X below). This added a slight counterweight that affected the tipping of the bucket, and so the vertical bars were cut to fit the different heights of the pivot. (The weight of the bracket itself could not be eliminated.)

In Figure X below, there are brackets on the vertical bars that support the bottom of the bucket. These were eliminated when the affect of the bottom bar as a counterweight was discovered.

<center><img src="https://raw.githubusercontent.com/AguaClara/UASB/master/Images/Tipping%20Bucket-%20Brackets%20Labeled.png">
<p>
<em>Figure X: Tipping bucket mounted on the aluminum frame</em>
</p>
</center>

Two short cylindrical rods are attached on either side of the frame such that the frame can be adjusted to shorten or widen the distance between the rods. These rods are the pivots for the tipping bucket. Placing the pivots off-centered shifts the center of gravity of the bucket-frame system. Thus, when water fills the bucket beyond a certain height, the bucket-frame tips and empties into the tank below.

**(insert image of pivots)**

The pivots themselves are mounted on two rectangular brackets with some room to roll around. This rolling motion will greatly decrease friction as the bucket tips, which in turn will reduce mechanical wearing of the parts.

<center><img src="https://raw.githubusercontent.com/AguaClara/UASB/master/Images/Tipping%20Bucket-%20Labeled.png">
<p>
<em>Cylindrical "roller pivots" mounted on rectangular brackets</em>
</p>
</center>

*Table Z: Tipping Bucket Trial Results*


| Trial | Horizontal Pivot Position (from center) (cm) | Vertical Position (center of pivot to base of bucket) (cm)  | Height Filled (cm)| Volume Filled (L)| Emptied Completely|
| -------- | ----------------|--------------- | --------- | ---------| -------|
| 1    | 0.25  | 16.5 | 21 | 14.8 | yes |
| 2 | 0.5 | 16.5| 22 | 15.56 | yes|
|3   | 0.5  | 19.3  |  x | x | no|
|4   | 0.5  | 18.5  |  x |  x | no |
|5   | 0.75  |  18.5 |  22 | 15.56  | yes |
| 6  |   0.75|   15.5|  22 | 15.56  | yes  |
|7   |  0.5 |  15.5 | 23  | 16.26  | yes |

The calculation for the volume in Liters filled of the bucket is shown below.

```python
from aide_design.play import*
bucket_height = 23 * u.cm
bucket_diam = 30* u.cm
area = pc.area_circle(bucket_diam)
vol = area * bucket_height
print(vol.to(u.L))
 ```

Trial 7 of the tipping bucket yielded the more successful results in that the bucket filled the most, while still emptying out all the way. Trials where the bucket did not empty completely were voided because water left in the bucket would cause a build-up of organic matter. Further testing will need to be done once a final design has been decided.

#### Hydraulic Parameters

Another important aspect of the influent design process was the hydraulics.  The below section details the design process and lists the hydraulic calculation to ensure proper flow through the system.

Built within the design of the influent systems are a number of hydraulic constraints that must be met for the flow to work properly.  These are summarized in Table X below.

<p align="center">Table X: Design parameters for UASB hydraulics </p>

| Parameter                        | Value           | Constrained? | Justification                                                                                                                                                                                                |
|:-------------------------------- |:--------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Reactor Volume                   | 1221 Liters     | Yes          | Based on max diameter and height to allow fabrication                                                                                                                                                        |
| Sludge Volume                    | ~850 Liters     | No           | Roughly 70% of Reactor Volume.  Needs to be better constrained based on location of tube settler.                                                                                                            |
| HRT                              | $\geq$ 4hrs     | Yes, minimum | Based on literature and lab scale test.                                                                                                                                                                      |
| Descending Sewage Velocity       | $\leq$ 0.2 m/s  | Yes, Maximum | Maximum velocity that will allow air bubbles to rise out of reactor.  Must only be achieved in beginning of influent pipe systems, not throughout.                                                           |
| Average Flow Rate                | $\leq$ 0.08 L/s | Yes, Maximum | Q = Volume / Hydraulic Residence Time                                                                                                                                                                        |
| Minimum Exit Velocity            | $\geq$ 0.03 m/s | Yes          | Minimum velocity needed to scour settling particles                                                                                                                                                          |
| Maximum Exit Velocity            | $\leq$ 1 m/s    | No           | Max velocity needed to prevent preferential pathways through sludge blanket.  Still very undetermined.                                                                                                       |
| Influent Pipe Inner Diameter     | 75 - 100mm      | No           | Based on literature values to prevent clogging in pipes.  Some flexibility.                                                                                                                                  |
| Influent Pipe Length             | ~8.5 feet       | Yes          | Roughly equal to height of reactor plus half of diameter (see influent pipe geometry)                                                                                                                        |
| Bucket Dump Volume               | ~20 L           | No           | Constraints are: time to fill bucket and relative volume to reactor capacity. A large dump volume allows more time for the bucket to fill, slowing down wear and tear. But the dump volume should also be a relatively small fraction of the total reactor volume. 20 L chosen as it is the volume of easily available buckets while fulfilling these constraints |
| Wastewater Generation per Person | 10.8 L/hr       | No           | Rule of Thumb from Monroe   |

### Hydraulic Calculations

Given the constraints above, the team worked on designing a system using the tipping bucket that could meet all this criteria and be easier to fabricate.  The functions below run all necessary calculations, allowing testing of many possible systems to find the optimal solution.

```python
from aide_design.play import*
import doctest

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

doctest.testmod(verbose=True)

Diameter = 3 * u.ft
Height = 7 * u.ft
HRT = 4 * u.hr
Percentage_sludge = 0.7 #Assume 70% of reactor is sludge
UASB_design = UASB_Size(Diameter, Height, HRT, Percentage_sludge)
print(UASB_design)

def bucket_filltime(flowrate_avg, dump_vol):
  """Takes in average flow rate into tipping bucket and the fill volume before one dump and calculates the average time it takes the bucket to fill and dump.
  >>> from aide_design.play import*
  >>> bucket_filltime(0.068 * (u.L/u.s), 16.26 * u.L)
  [<Quantity(239.1, 'second')>]
  """
  filltime = dump_vol / flowrate_avg
  return filltime.to(u.s)

doctest.testmod(verbose=True)

bucket_dump_vol = 23 * u.cm * pc.area_circle(30*u.cm)
print(bucket_dump_vol.to(u.L))
filltime = bucket_filltime(0.068 * u.L/u.s, bucket_dump_vol)
print(filltime.to(u.s))



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
  if pipe_vol.to_base_units >= dump_vol.to_base_units
    headgain = dump_vol / pc.area_circle(pipe_ID)
  else
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

### Potential Designs

Design for the influent system has not been settled on yet, and there are a few options.

#### Design 1: Side Influent Pipe Entry

The main working design over the summer focused on having the influent pipes enter from the side of the reactor.  Figure X below shows this system.

(INCOMPLETE)

#### Design Two: Top Influent Pipe Entry

(INCOMPLETE)

### Flow Control Tests

#### Optimal Flow Patterns

Given that there has not been a design of a UASB on this scale, the scientific literature offered little information on flow patterns through a sludge blanket.  An understanding of flow through this system is important for the following reasons:

* An exit velocity of over 0.3 m/s is required to scour waste that may settle around the pipe exits and clog the system.
* Increasing the exit velocity can provide enough force to partially fluidize the bed, raising it up and completely surrounding it in wastewater. Fluidizing the bed increases the surface area of the granules that comes in contact with the wastewater, improving biological treatment.  This same principle is used in the [Anaerobic Fluidized Bed Reactor](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4441917/), which was investigated by AguaClara but ultimately rejected as it required pumps to run.
* Depending on the geometry of the reactor and velocity of influent wastewater, preferential flow pathways may form in the sludge blanket.  Preferential flow reduces the contact between wastewater and the granules, and in extreme cases creates **dead zones** (areas where no wastewater enters eventually causing sludge death).  


#### Tapioca Tests

To attempt to model and understand flow patterns within the UASB system, the team ran tests through a model sludge bed within a scaled down model UASB.  

The first UASB was modeled using a simple plastic beaker. Tapioca that had been soaked in water for 1.0 hours was used to model the sludge blanket. The beaker was filled to approximately 70% of its volume with the expanded tapioca. A 0.25 inch metal influent pipe was attached to tubing which was attached to a pump. Water was pumped into the beaker through the tube and the influent pipe, which emptied into the bottom center of the beaker perpendicular to the base of the beaker. Red dye enters the influent tube from another pump to allow for a better visualization of the flow patterns.

<center><img src="https://github.com/AguaClara/UASB/blob/master/Tapioca%20Test.JPG?raw=true">
<p>
<em>Figure 8: Set Up of the Tapioca Experiment Using One Influent Pipe</em>
</p>
</center>

Multiple tests will be run at different flow rates which will be calculated based on the exit velocities of interest. In addition, test will be run using both one and two influent pipes, and the results will be compared.

Below is the code used to calculate the flow rate needed to produce certain exit velocities from the influent pipe, as well as the code used to calculate the amount of water dumped per pulse.

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
# Calculate exit velocity from pipes given pipe dimensions and change in hydraulic head
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
 ```
#### Tests to Run
 For 3/8 inch influent pipes:
 | Target Exit Velocity (m/s) | Flow Rate (ml/s) (1 Pipe) | Flow Rate (2 Pipes) |
| -------------------------- | ------------------------- | ------------------- |
| 0.3                        |                           |                     |
| 1                          |                           |                     |
| 2                          |                           |                     |
| 5                          |                           |                     |


## Biogas Capture

As organic waste passes through the sludge blanket portion of the UASB reactor, it is broken down by anaerobic bacteria in a complex biological process that ends with methanogenesis.  A key product of this process is methane and carbon dioxide, which together are known as biogas.  This gas has a fairly high energy density, and can be burned for heating similar to propane.  Capturing this biogas is an important design process for the UASB, as it allows the UASB to produce a valuable product that can provide heating or cooking energy for the communities served by the UASB.

This section is broken into two sections.  **Biogas Production Calculations** details our model of biogas production to quantify how much biogas is produced over time.  **Biogas Storage System** details our design of the biogas storage system.

### Biogas Production Calculations

Biogas production is quantified using the following equation, taken from the [Anaerobic Reactors](https://www.iwapublishing.com/sites/default/files/ebooks/9781780402116.pdf):

$COD_{CH_4} = Q(S_o-S) - Y_{obs} Q S_o$

Where:

$COD_{CH_4}$ is the mass of COD converted to methane ($kgCOD_{CH4} / day$)

$Q$ is the average influent flow ($m^3 / day$)

$S_o$ is the influent COD concentration ($kgCOD/m^3$)

$S$ is the effluent COD concentration ($kgCOD/m^3$)

$Y_{obs}$ is the coefficient of solid production within the system in terms of COD (the amount of sludge created from input COD) ($kgCOD_{sludge}/kgCOD_{applied}$)
* In the literature, $Y_{obs}$ ranges from 0.11 to 0.23.  To assume lower production, we chose the highest value for our calculations (as this is the removal of COD)

Next, this methane mass can be converted to volumetric production as follows:

$Q_{CH4} = \frac{COD_{CH4}}{K(t)}$

Where

$Q_{CH4}$ = volumetric methane production ($m^3 / day$)

and

$K(t)$ = correction factor for operational temp of reactor ($kgCOD/m^3$)

$K(t)$ is defined using the ideal gas law:

$K(t) = \frac{P * K_{COD}}{R * (273 + T)}$

$P$ = atmospheric pressure (1 atm)

$K_{COD}$ = COD corresponding to 1 mole of CH4 ($\frac{64g COD}{mole}$)

$R$ = Ideal Gas Constant = 0.08206 ${\frac{atm*L}{mol*K}}$

$T$ = Temperature ( ${^\circ}C$)

Since biogas contains other gases such as CO2, we must employ a correction factor to account for their contributions to the overall volume.  We assume that biogas is composed 75% of methane, as given in [Anaerobic Reactors](https://www.iwapublishing.com/sites/default/files/ebooks/9781780402116.pdf).

It is important to note that this equation only gives an approximation of the actual biogas produced, and a fairly inaccurate one at that.  Methanogensis is a very complicated biochemical process, and there are many other areas to consider that are not included in this equation, such as losses due to leakage, temperature effects, and the varying bacterial composition of the sludge blanket.  As most considerations are losses, we consider the value given by this equation an **overapproximation** and design accordingly.  For safety reasons, it is better to overestimate the volume produced rather than underestimate and design a system that will produce flammable gas.  Despite its problems, this equation still provides a good baseline value of the output biogas to inform the design process.

#### Design Parameters
*Table 2: Design parameters for biogas production.*

|                        Parameters                        |                 Value                 |                                              Basis of Design                                              |
|:--------------------------------------------------------:|:-------------------------------------:|:---------------------------------------------------------------------------------------------------------:|
|          COD Removal Efficiency, ```COD_eff```           |                  70%                  | Based on [Van Lier Report](https://courses.edx.org/c4x/DelftX/CTB3365STx/asset/Chap_4_Van_Lier_et_al.pdf) |
| Percent of COD directed to Sludge Production ```Y_obs``` |              23%               | Based on [Anaerobic Reactors](https://www.iwapublishing.com/sites/default/files/ebooks/9781780402116.pdf).  Chose highest value of removal to get minimum production value |
|                     Pressure ```P```                     |                 1 atm                 |                            Biogas produced will be stored at very low pressure                            |
|                   Temperature ```T```                    |            25 $^{\circ}$ C            |                                  Assuming optimal biological conditions                                   |


#### Code
```python
from aide_design.play import*
def BiogasFlow(Q, COD_Load, Temp, COD_removal_eff):

    # Calculate ideal COD production
    COD_rem = COD_Load * COD_removal_eff #calculate COD broken down by reactor
    Y_obs = 0.23 # Upper limit of sludge production
    COD_CH4 = (Q * COD_rem) - (Y_obs * Q * COD_Load) #Gives mass CH_4 produced per unit time

    # Calculate correction factor for operational temperature of the reactor
    T = Temp.to(u.degK)
    P = 1 * u.atm
    K_COD = 64 * (u.g / u.mol)
    R = 0.08206 * ((u.atm * u.L) / (u.mol * u.degK))
    K = (P * K_COD) / (R * T)
    #Calculate the volumetric flow rate of methane production
    Q_CH4 = COD_CH4 / K # per second
    return Q_CH4

# Flow rate through UASB reactor
Flow_design = UASB_design[1]
print(Flow_design)
Temp = 25 * u.degC  # Assuming mesophilic conditions
Removal_eff = 0.7 # 70% removal efficiency

#Approximate loading rates for domestic wastewater
COD_Load_min = 100 * (u.mg / u.L)
COD_Load_mid = 200 * (u.mg / u.L)
COD_Load_max = 300 * (u.mg / u.L)

Q_Biogas = BiogasFlow(Flow_design, COD_Load_mid, Temp, 0.7)
#Calculating size of storage device
print(Q_Biogas.to(u.L/u.day))
```

### Biogas Storage System

#### Lid design

##### Design 1: Hydraulic Seal

##### Design 2: Full Seal

#### Capture System Design


An important aspect of UASB design is the capture and storage of biogas produced during anaerobic digestion within the reactor.  As this gas is produced within the sludge blanket, it floats upwards through the settling zone and is captured within the lid space.  The UASB team considered many possible designs for this capture system.  These three options, along with their pros and cons are detailed in the table below.

*Table 3: Comparison between different types of biogas capture systems*

| Type of Storage | Advantages | Disadvantages |
|:--------------- |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |:-------------------------------------------------------------------------------------------------------------------------- |
| Gas Bag         | (1) Flexible and easy connection on top of next to reactor (2) **Cheap and cost effective** (3) Easy to transport for reactor to kitchen use (4) Visual representation of gas volume | (1) Fragility and Leakage (2) Require frequent replacement - are these materials available locally?      |
| Fixed Lid       | (1) Durability (2) No concerns about movement (3) Can use prefabricated barrel                                                       | (1) Water displaced during gas compression may need to be recaptured, requiring additional information |
| Floating Lid    | (1) Water level moves with gas (2) Same concept as fixed lid (3) Visual representation of gas level            | (1) Low gas production will just cause water displacement (2) Track system hard to fabricate  |

After consideration of these options, the gas bag system was decided upon because it is cost effective and transportable for community settings where one community may share this resource.  This system is similar to other "bag" collection systems at traditional wastewater treatment facilities such as the Ithaca Area Wastewater Treatment Facility.

Schematically, gas will flow out the top lid of the reactor through a pipe into


#### Code
```python
def Dim_Storage(day_prod, time_stor, time_fail, diam_lid):
  """Takes the daily volume of biogas produced (volume per time), the numbers of days for desired storage, and the time required before critical lid failure and returns the volume required for the temporary storage system and the dimensions for the lid required to retain a set amount of biogas before failure"""

  day_prod = day_prod.to_base_units()
  time_stor = time_stor.to_base_units()
  vol_stor = day_prod * time_stor

  time_fail = time_fail.to_base_units()
  vol_fail = day_prod * time_fail

  diam_lid = diam_lid.to_base_units()
  area_lid = 0.25 * math.pi * (diam_lid)**2
  height_lid = ( vol_fail / area_lid ).to(u.ft)

  return[vol_stor, height_lid]

day_prod = Q_Biogas[1]
time_stor = 2 * u.day
time_fail = 12 * u.hr
diam_lid = 2.5 * u.ft

size_stor = Dim_Storage(day_prod, time_stor, time_fail, diam_lid)
vol_stor = size_stor[0].to(u.gal)
height_lid = size_stor[1]

print("The storage volume required to store", time_stor, "of biogas is", vol_stor, "\n" "The height of lid to prevent failure before", time_fail, "is", height_lid)
```

#### Effluent Tube Settler


### EPA Funding Assurance
This publication [article] was developed under Assistance Agreement No. SU-83926801 awarded by the U.S. Environmental Protection Agency to Cornell University. It has not been formally reviewed by EPA. The views expressed in this document are solely those of [name of recipient or names of authors] and do not necessarily reflect those of the Agency. EPA does not endorse any products or commercial services mentioned in this publication.
