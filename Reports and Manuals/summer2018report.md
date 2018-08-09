# Upflow Anaerobic Sludge Blanket Research and Design Report

## Summer 2018

### Ian Cullings, Isa Kaminsky, Ananya Gangadhar


## Index
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Abstract](#abstract)
- [Introduction](#introduction)
- [Previous Work](#previous-work)
- [Influent Flow System](#influent-flow-system)
  - [Tipping Bucket versus Siphon System](#tipping-bucket-versus-siphon-system)
  - [Hydraulic Parameters](#hydraulic-parameters)
  - [Hydraulic Code](#hydraulic-code)
  - [Tipping Bucket Design](#tipping-bucket-design)
  - [Influent Tank Design](#influent-tank-design)
  - [Influent System Geometry <a name="InfSysGeo"></a>](#influent-system-geometry-a-nameinfsysgeoa)
    - [Design 1: Side Entry](#design-1-side-entry)
    - [Design 2: Top Entry](#design-2-top-entry)
- [Benchtop Testing](#benchtop-testing)
  - [Tapioca Tests](#tapioca-tests)
    - [Goals](#goals)
- [Biogas Capture System](#biogas-capture-system)
- [Biogas Capture](#biogas-capture)
  - [Biogas Production Calculations](#biogas-production-calculations)
    - [Design Parameters](#design-parameters)
    - [Code](#code)
  - [Biogas Storage System](#biogas-storage-system)
    - [Lid design](#lid-design)
      - [Design 1: Hydraulic Seal](#design-1-hydraulic-seal)
      - [Design 2: Full Seal](#design-2-full-seal)
    - [Capture System Design](#capture-system-design)
    - [Code](#code-1)
- [Fabrication Manual](#fabrication-manual)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Abstract
Since Spring 2017, the AguaClara Upflow Anaerobic Sludge Blanket (UASB) Team has been working on a detailed design of modified, pilot-scale UASB reactor originally proposed in an EPA P3 proposal. A UASB reactor treats wastewater anaerobically and produces biogas as a by-product. Working towards that goal, the team has created Python code to record the design process and calculations for this AguaClara UASB.

Over the summer of 2018, the UASB team's main goal has been to finish a complete design of a UASB wastewater treatment system, and fabricate an influent system.  Future teams will work on fabrication of the entire system and testing at the Ithaca Area Wastewater Plant before implementation in Honduras.

## Introduction

In many countries without proper access to wastewater treatment, such as Honduras, wastewater is directly released into the environment without treatment.  Typical domestic wastewater released this way contained organics and fecal matter which lead to many adverse affects on the environment and human health.  

Organic matter within wastewater is degraded by biologically by aquatic bacteria, consuming dissolved oxygen and harming life in the process.  In extreme cases this can deplete oxygen enough to create dead zones where aquatic species like fish are killed.  Nutrients such as nitrogen and phosphorus contained in wastewater can lead to explosive algal growth in waterways, which also depletes oxygen levels and can create dead zones through a process known as [eutrophication](https://oceanservice.noaa.gov/facts/eutrophication.html).

Finally, fecal matter from wastewater is a major contributor to the spread of infectious waterborne diseases including Cholera, Salmonella, and Diarrhea.  Pollution of waterways where others source their water from leads to the rapid spread of these diseases, particularly in areas downstream of other communities.

Currently in the United States effective municipal wastewater treatment facilities have long retention times, require large land areas, and have a high fixed cost per capita. Implementing these systems in smaller communities leads to high fixed costs per capita and large levels of infrastructure, both of which are often unattainable for smaller communities.  Because of this, many communities across the world forgo wastewater treatment altogether and discharge wastewater directly into the environment.  

UASB reactors, used as a preliminary wastewater treatment process, clarify wastewater by removing suspended solids organic matter ([Chong et. al, 2012](https://www.sciencedirect.com/science/article/pii/S0043135412002400?via%3Dihub)). UASB reactors rely on gravity to clarify wastewater and biological processes to remove organic matter and convert it to biogas. They are less energy intensive than other forms of preliminary wastewater treatment that use aerobic processes. UASB reactors also produce methane as a by-product of anaerobic digestion.  This methane can be captured and burned for energy production or heating.

In January 2017, a novel pilot scale UASB reactor design was created by AguaClara for the EPA People, Prosperity and the Planet (P3) [Student Design Competition proposal](https://docs.google.com/document/d/1geug1EyFjCRLQgO79vTOXUUFia3RBw3bhaIHPUiqu44/edit?usp=sharing). This reactor was designed to improve the accessibility of wastewater treatment for small communities. The proposed UASB reactor design identified areas to improve conventional reactor design, making the system cheaper and easier to fabricate and implement globally.  The team later applied for Phase II funding from the same operation to support development and implementation of addition reactors for testing.

Since submission of this proposal, there has been ongoing work to develop the final design of the reactor.  This document serves to inform readers on the design progress made over Summer 2018, and serves as a resource for future AguaClara team members and collaborators on all information related to the design of the UASB.  

## Previous Work

The Spring 2017 team wrote and submitted Phase I of the EPA P3 proposal, detailing a proposal to design a UASB system to provide effective wastewater treatment for small rural communities without access to wastewater infrastructure.  This proposal passed Phase I funding, providing funding for building the first model UASB reactor.  The team also conducted studies on using plate settlers, angled plastic sheets within the reactor that capture rising particles, where they concluded that they did not significantly impact solids retention.  They also found that biogas production within the reactor did not cause solids to rise out the effluent significantly.  The full details can be found in their [final research report](https://www.overleaf.com/8107719xzjdzswjvtyj#/28623295/).

The Fall 2017 team began the design process for the UASB.  The team worked on the influent system, biogas collection system, and the effluent lines, and created [design code in Jupyter notebooks](https://github.com/AguaClara/UASB/tree/master/Jupyter%20Notebook%20Files).  The team also had its initial meeting with Ed Gottlieb, an operator at the Ithaca Area Wastewater Treatment plant.  The team went over the design with Ed, and secured a space in the plant to set up and test the reactor using influent wastewater.  

In Spring 2018, the team focused more on specific components of the design, particularly the influent system and biogas storage.  While previously the team had assumed the system would have continuous flow, a deeper dive into the hydraulics revealed that this would require around 6 millimeter to achieve our desired exit velocity.  Given this, the team decided to move to a pulse flow system where wastewater is collected and then dumped all at once to achieve high flowrate.  

Meeting with Ed Gottlieb once again, he suggested two methods of pulse flow. The first is a tipping bucket system, where wastewater collects in a bucket on a pivot that will tip and dump all at once, then return to its original position.  The second suggestion was to use a siphon to pull water through a tube and into the reactor.  The rest of the semester was spent investigating these two systems to determine the most effective option.

During Spring 2018 the team also applied for Phase II of the EPA P3 Grant, this time for $75,000.  The application, found [here](https://docs.google.com/document/d/1ejsyrxgZOtswRr5hx-XJ22QQtn4LzLtoVheMF-YvFrs/edit), focused primarily on the design of a second testing reactor to run in parallel with new modifications to test the efficacy of the system.  This funding would also be used for establishing a testing system in Honduras for field data.

## Influent Flow System

One major design goal for the summer was to finish design of the influent system that delivers wastewater to the bottom of the reactor from a holding tank.

<center><img src="https://github.com/AguaClara/UASB/blob/master/Images/Influent%20Geo%20Slant.png?raw=true">
<p>
<em>Figure 1: Schematic of Influent System</em>
</p>
</center>

### Tipping Bucket versus Siphon System

One of the leading questions from the Spring 2018 semester was whether to use the tipping bucket of siphon system to deliver wastewater.  The summer team researched siphons and discussed with the AguaClara program director, Dr. Monroe Weber-Shirk, potential design flaws - specifically the diameter of pipe that should be used. The main concern was that if too large a pipe was used, water would be able to pass through the siphon before it had filled to the level needed to create a pulse of a specific volume.  The pros and cons of each system are listed below.

***Tipping Bucket***

**Pros:**
* Simple to manufacture, uses low cost parts that are easy to obtain
* Known system used in amusement parks, designs available

**Cons**
* Uses moving parts, which are subject to wear and may break over time much more rapidly than most systems
* Stirs up wastewater with each dump, increasing chance of splashing and potential bad odors


***Siphon System***

**Pros:**
* No moving parts

**Cons:**
* Potential for clogs and settling in standing  pipes
* Unknown system, little design guidelines on how it works


Ultimately, given the simplicity of the tipping bucket design, and the lack of documentation on siphons, the team decided to move forward with the tipping bucket system.  

### Hydraulic Parameters

Built within the design of the influent systems are a number of hydraulic constraints that must be met for the flow to work properly.  These are summarized in Table 1 below.

<p align="center">Table 1: Design parameters for UASB hydraulics </p>

| Parameter                        | Value           | Constrained? | Justification                                                                                                                                                                                                |
|:-------------------------------- |:--------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Reactor Volume                   | 1221 Liters     | Yes          | Based on max diameter and height to allow fabrication                                                                                                                                                        |
| Sludge Volume                    | ~850 Liters     | No           | Roughly 70% of Reactor Volume.  Needs to be better constrained based on location of tube settler.                                                                                                            |
| HRT                              | $\geq$ 4hrs  | Yes, minimum | Based on literature and lab scale test.                                                                                                                                                                      |
| Descending Sewage Velocity       | $\leq$ 0.2 m/s  | Yes, Maximum | Maximum velocity that will allow air bubbles to rise out of reactor.  Must only be achieved in beginning of influent pipe systems, not throughout.                                                           |
| Average Flow Rate                | $\leq$ 0.08 L/s | Yes, Maximum | Q = Volume / Hydraulic Residence Time                                                                                                                                                                        |
| Minimum Exit Velocity            | $\geq$ 0.03 m/s | Yes          | Minimum velocity needed to scour settling particles  at the end of the influent pipe                                                                                                                                                        |
| Maximum Exit Velocity            | $\leq$ 1 m/s    | No           | Max velocity needed to prevent preferential pathways through sludge blanket.  Still very undetermined.                                                                                                       |
| Influent Pipe Inner Diameter     | 75 - 100 mm      | No           | Based on literature values to prevent clogging in pipes.  Some flexibility.                                                                                                                                  |
| Influent Pipe Length             | ~8.5 feet       | Yes          | Roughly equal to height of reactor plus half of diameter of reactor (see [Influent System  Geometry](#InfSysGeo))                            |
| Bucket Dump Volume               | ~20 L           | No           | Constraints are: time to fill bucket and relative volume to reactor capacity. A large dump volume allows more time for the bucket to fill, slowing down wear and tear. But the dump volume should also be a relatively small fraction of the total reactor volume so as to be negligible in volume calculations. 20 L chosen as it is the volume of easily available 5-gallon buckets while fulfilling these constraints |
| Wastewater Generation per Person | 10.8 L/hr       | No           | Rule of Thumb from Monroe   |

From these constraints, the general head loss equation for a circular pipe can be used to determine the head loss needed to achieve the desired exit velocity, given a specific diameter of pipe.  The [head loss trick](https://aguaclara.github.io/Textbook/Review/Review_Fluid_Mechanics.html#head-loss-elevation-difference-trick) is used to do this, and has been used in all further calculations for minor loss coefficients in our design.

### Hydraulic Code

The code below calculates the important parameters for the influent system.  The parameterized functions allow for each function to be utilized for differing designs to allow the team to compare and contrast designs simply.  The functions below must be defined and then can be utilized in the following section.

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

def bucket_filltime(flowrate_avg, dump_vol):
    """Takes in average flow rate into tipping bucket and the fill volume
    before one dump and calculates the average time it takes
    the bucket to fill and dump.
    >>> from aide_design.play import*
    >>> bucket_filltime(0.068 * (u.L/u.s), 16.26 * u.L)
    [<Quantity(239.1, 'second')>]
    """
    filltime = dump_vol / flowrate_avg
    return filltime.to(u.s)

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

### Tipping Bucket Design

After discarding the idea of using siphons, the team started to design the tipping bucket system given these parameters.  Design began by looking into tipping bucket systems online but it was hard to find any detailed schematics since these buckets are mostly used only in water parks. The team was thus left with two choices: try to model a tipping bucket system mathematically, or create a physical model of the tipping bucket system and find the optimal design via trial and error. Due to constraints of time and expertise on the team, the latter was decided upon.


<center><img src="https://github.com/AguaClara/UASB/blob/master/Images/Timmy_the_Tipping_Bucket.jpg?raw=true">
<p>
<em>Figure 2: Timmy the Tipping Bucket</em>
</p>
</center>

Pictured above is the first design of the tipping bucket system.  It was created with a small plastic lab beaker, two screws, and 80-20 extrusion aluminum bars with connectors used to provide a pivot for the screws.  This was mostly created to give the team a general sense of how tipping buckets work, not to collect specific data.  This model offered a few insights for the design:

* Location of the pivot on the bucket is very important for operation.  
  - Height of the pieces controls how much water is collected before dumping.  
  - Horizontal positioning of the pivot determines the angle the bucket rests at and how soon it will tip.

* The bucket needs to be designed so that it will not rest completely tipped down, and return to its original position to fill in more wastewater.  
  - This can be achieved either by controlling the height of the bucket so that is cannot rotate completely (making it hit the bottom of the tank) or by controlling the rotation.
    - The rotation can either be controlled by adding a counterweight that will return the bucket to its original position, or adjusting the horizontal location of the pivot to ensure it will return.

After discussing the design more with Monroe, the team settled on a new design, pictured below:

<center><img src="https://github.com/AguaClara/UASB/blob/master/Images/Influent_Tank_Tipping_Bucket.png?raw=true">
<p>
<em>Figure 3: Influent System with Tipping Bucket</em>
</p>
</center>

This tipping bucket is created with a 5 gallon bucket (chosen as they are easy to purchase) with two plastic rods on either side, attached through a hose clamp.  These circular pieces will rest in the brackets on either side of the influent tank, where they can roll freely to allow the bucket to dump.  This greatly reduces friction and wear of mechanical parts.

<center><img src="https://github.com/AguaClara/UASB/blob/master/Images/Influent_System_Brackets_Pivots.png?raw=true">
<p>
<em>Figure 4: Rectangular bracket with the "roller pivot"</em>
</p>
</center>

There will be a hose clamp around the bucket that the roller pivots will be attached onto. The use of a hose clamp instead of directly welding the roller pivots to the bucket allows us to adjust the position of the pivots easily during initial benchtop tests without drilling new holes in the bucket. It will also allow easy replacement of the bucket system if necessary, since components of the tipping bucket system will eventually fail.

**ADD VIDEO HERE THAT EXPLAINS DESIGN**

This model became the first design of the tipping bucket.  However, after beginning fabrication, the team realized that the design would not work due to the geometry of the bucket and the attached pivot rods.  Since the bucket was circular, any placement of the rod off of the center would lead the rods to point orthogonally outwards and not form a straight pivot.  This is shown the figure below.


<center><img src="https://github.com/AguaClara/UASB/blob/master/Images/Tipping_Bucket_Off_Centered_Pivots.png?raw=true">
<p>
<em>Figure 5: Top view of tipping bucket showing the off-centered pivots</em>
</p>
</center>

After discussing this problem further, the team considered two possible options.  The first was to purchase a square bucket to use in the same manner.  The second was to create a frame for the bucket that would provide a straight pivot without hindering tipping.  Since materials were available, and it provided much more flexibility for testing, the team moved forward with the second option.

The frame is pictured below, attached to the 5-gallon bucket used within the system.  1-inch by 1-inch 80-20 aluminum extrusion bars were used to create a modular base around the bucket that could be easily extended or compressed to fit the dimensions of the bucket snugly.  

<center><img src="https://raw.githubusercontent.com/AguaClara/UASB/master/Images/Tipping%20Bucket-%20Brackets%20Labeled.png">
<p>
<em>Figure 6: Tipping bucket mounted on the aluminum frame for bench top testing</em>
</p>
</center>

Two additional pieces were then added extending down from the 80-20 square to the bottom of the bucket.  These pieces extended 1 inch below the bucket, allowing an L-bracket to be attached below.  This was securely attached to the bottom of the bucket, locking it in place.  When testing the bucket, this could be easily moved downwards, and the L-bracket moved up to hold the bucket in place.

Finally, a double sided screw piece was added to the pivot rods to allow them to attach to the 80-20 extrusion bars.  This piece was added by facing the rods with a lathe, and drilling the pieces in.  All of the this was done with the help of the shop managers.  With these pieces in, the rods can be easily moved laterally along the bucket and then tightened.

### Influent Tank Design

Another crucial part of the design  is the influent tank.  This tank will capture all wastewater from the tipping bucket, and distribute it evenly across both influent pipes for flow control.  To prevent any splashing of wastewater, the tipping bucket will be completely contained within the influent tank.

The crucial design aspects of the tank are listed below:

* The tank **must be tall enough** to completely contain the tipping bucket and prevent any splashing of wastewater out of the tank

* The tank **must be just wide enough** to contain the bucket and the two brackets.  If the tank is wider, that will require more material for longer roller pivots, and reduce the structural strength of the bucket (since deflection of a rod is proportional to some power of length)

* The dimensions of the tank must be such that they **create the required amount of hydraulic head from one dump of the tipping bucket**.  
This can be achieved by choosing the appropriate geometry at the bottom of the tank to ensure the required height increase of the water level per volume of dump.

* The tank **must evenly split flow between the two pipes**.  This can be designed by changing the geometry of the pipes based on where the water is dumped, but most importantly, there should always be a small volume of water in the tank even when all the water from one dump has been drained out. This is to provide enough volume within tank where the **descending sewage velocity is below 0.2 m/s** to allow air bubbles to escape.

* The tank should be **easy to source**. It should be easily purchasable at the correct dimensions, or easy to fabricate.


Summarized in a table:

| Parameter | Value | Justification |
|:-------------- |:-----  |------------- |
|Height|$\geq$ 40 cm| Height of bucket plus 4 cm error|
|Width|35 cm |30 cm for bucket diameter plus 5 cm for both pivot pieces|
|Length|$\geq$ 60 cm|Height of bucket plus extra space to allow free rotation.  Requires closer examination in fusion|




The team began by designing the tank as a simple, rectangular box.  However, given the constraints on the dimensions of the box, it was impossible to get the required hydraulic head gain from bucket, as summarized in the code below:

```python
from aide_design.play import*

width = 35 * u.cm
length = 60 * u.cm
area = width * length
bucket_vol = 15 * u.L  #Assuming the bucket fills 75%
head_gain = (bucket_vol / area).to(u.cm)
print("One dump of the bucket gives", head_gain, "of hydraulic head")
# Prints: One dump of the bucket gives
#7.143 centimeter of hydraulic head
```
Next, the team considered adding more material into the bottom of the tank (adding sloped walls, making it more pyramidal).  Since there would be less volume in the bottom of the tank, this would allow hydraulic head to be gained per dump of the bucket.  However, after running more calculations it was determined that it was very challenging to meet this criteria and still fit the bucket fully within the influent tank.

After further discussion with Monroe, a new design to solve this problem was suggested.  Instead of a sloped tank, the tank would remain rectangular, and larger pipes along the bottom would be added, which would then connect to the influent pipes.
<center><img src="https://github.com/AguaClara/UASB/blob/master/Images/Influent%20Tank.jpg?raw=true">
<p>
<em>Figure 7: Close up of the influent system showing the larger cylindrical pipe segments</em>
</p>
</center>

The addition of the cylindrical pipe segments serves two purposes:
1. The flow is split into two influent pipes almost equally.
2. Since the diameter of the cylinder segments is larger than that of the influent pipe, the descending sewage velocity in it will be lower. This allows air bubbles to escape from the wastewater which is desirable.



### Influent System Geometry <a name="InfSysGeo"></a>

There are two designs the team is considering for the influent system geometry.  Each is summarized below, and the design functions are utilized to check the important parameters for each system to allow the team to compare and contrast possible designs.

#### Design 1: Side Entry

Our first design for the system has the pipes enter from the side of the UASB, as pictured in the figure below.  This allows the influent tank to remain close to the water level, allowing water to build up in the tank with each dump.  However, a challenge of this design is supporting the influent tank, and it will need to be cleanly held in place on the side of the reactor.

<center><img src="https://github.com/AguaClara/UASB/blob/master/Images/Influent%20Geo%20Slant.png?raw=true">
<p>
<em>Figure 8: Schematic of Influent System with side entry</em>
</p>
</center>

**Design Parameters**
| Parameter                    | Value              | Notes                                                             |
| ---------------------------- | ------------------ | ----------------------------------------------------------------- |
| UASB Height                  | 7 ft               | Based on tank dimensions, unset                                   |
| UASB Diameter                | 3 ft               | Based on tank dimensions, unset                                   |
| Dump Volume                  | 16 Liters          | Calculated during tipping bucket tests                            |
| Minor Loss Coefficient       | 4                  | Design includes two elbows (1.5 each) plus 1 |
| Pipe Roughness               | 0.0015 mm          | Standard pipe roughness for PVC                                   |
| Temp                         | $\geq$16$^{\circ}$C | Minimum Temp in Honduras                                          |
| Large Influent Pipe Diameter |                    | Determined through Hydraulic Code to meet specifications          |
| Small Influent Pipe Diameter |                    | Determined through Hydraulic Code to meet specifications          |
| Total Pipe Length            | 10 feet            | Roughly UASB Height + UASB Diameter                               |
| Number of Influent Pipes     | 2                  | Used to increase influence area and prevent clogs                 |


**Hydraulic Code**
```python
# Required tools are imported and functions are defined in "Hydraulic Code" section

UASB_design = UASB_Size(3 * u.ft, 7 * u.ft, 4 * u.hr, 0.7)
#Size: 1401 Liters, Flow Rate: 0.068 Liters/second, People served: 22, People served for only blackwater: 113

filltime = bucket_filltime(UASB_design[1], 16 * u.L)
#filltime: 234.9 seconds (3.915 minutes)
```
The team then ensured that the velocity within the pipe is below 0.2 m/s, given the pipe diameter, to allow air bubbles to escape.  

```python
# Calculate the maximum velocity through the large diameter
# pipe when hydraulic head is largest after a dump
pipe_A = pc.area_circle(target_diam)
# incorporate all kinetic energy
# as minor loss
K_minor = 1
Temp = 16 * u.degC # minimum temp in Honduras
Nu = pc.viscosity_kinematic(Temp)
Pipe_Rough = 0.0015 * u.mm
FlowRate = pc.flow_pipe \
(target_diam, total_hl, pipe_hl, Nu, Pipe_Rough, K_minor)
Max_vel = (FlowRate / pipe_A).to(u.m / u.s)
print(Max_vel)

```

#### Design 2: Top Entry

Our second potential design has the influent tank directly on top of the UASB system, and the influent pipes coming straight down into the reactor.

**Advantages:**
* This design is easier to fabricate.
* There will likely be fewer clogging issues since there are no bends.

**Disadvantages:**
* This geometry will require some redesigning of our influent system since the influent tank will now be far above the water level in the reactor.
* Since the pipes will go straight through the biogas lid, this will also require the welds around the influent pipes to be gas tight.  

Since this design was only discussed towards the and of the summer, there are no hydraulic calculations or schematics for it yet. This is something that can be worked on in the future semesters.

## Benchtop Testing (Tapioca Tests)
### Goals
To attempt to model and understand flow patterns within the UASB system, the team ran tests through a model sludge bed within a scaled down model UASB system. Crushed tapioca was chosen to simulate the reactor sludge due to its similarity in texture and density to the actual reactor sludge.

The goal of the tapioca tests is to study the flow patterns within the UASB reactor by injecting dye, and to check for conditions under which the reactor is likely to fail - either due to clogging, or due to preferential flow which may create dead zones in the sludge.

Testing has begun with one influent pipe and eventually will be done with two influent pipes as well. If one influent pipe is sufficient to fluidize the sludge blanket, fabrication of the UASB would become a lot easier. However, the code would need to be updated to accommodate this change, and scaling up to larger reactors in the future would be more difficult.

### Setup
The first UASB was modeled using a simple plastic beaker. Tapioca that had been soaked in water for 1.0 hours was used to model the sludge blanket. The beaker was filled to approximately 70% of its volume with the expanded tapioca. A 0.25 inch metal influent pipe was attached to tubing which was attached to a pump. Water was pumped into the beaker through the tube and the influent pipe, which emptied into the bottom center of the beaker perpendicular to the base of the beaker. Red dye enters the influent tube from another pump to allow for a better visualization of the flow patterns.

Most observations for this test were made qualitatively, and the system was also raised up so that a cell phone camera could be used to record flow patterns from the bottom of the system.  

<center><img src="https://github.com/AguaClara/UASB/blob/master/Images/Tapioca%20Test.JPG?raw=true">
<p>
<em>Figure 9: Set Up of the Tapioca Experiment Using One Influent Pipe</em>
</p>
</center>

The tests that have been performed were done at a low flow rate of 6.33 mL/s, which translates to an exit velocity of 0.2 m/s. So far, the dyed water appeared to spread out along the bottom of the beaker, rather than puncturing the tapioca blanket. Multiple tests will be run at different flow rates which will be calculated based on the exit velocities of interest. In addition, test will be run using both one and two influent pipes, and the results will be compared.

### Code
Below is the code used to calculate the flow rate needed to produce certain exit velocities from the influent pipe, as well as the code used to calculate the amount of water dumped per pulse:

```python

# Import tools
from aide_design.play import*
import doctest

# Define functions
def find_pump_flowrate(exit_vel_target, pipe_innerdiam, num_pipes):
  """Finds flow rate for pump system to reach input exit velocity
  via the continuity equation Q = vA.
  Inputs are flow rate generated from pump,
  tubing inner diameter, and total number of pipes.  
  Flow rate is generated from table on confluence relating
  pump speed, pipe diameter and flow rate.  
  Does not account for head losses, water pressure, or
  change in head as they are negligible compared to pump speed.
  """
  inner_area = pc.area_circle(pipe_innerdiam)
  pump_Q = exit_vel_target * inner_area * num_pipes
  return pump_Q

def find_pump_vel():


  return

def bucket_dump_calcs(dump_volume, UASB_height, UASB_diameter):
  """Solves for the height of water added
  to the bottom of the reactor and the
  percentage of total volume added with
  each dump for tipping bucket case.  
  Inputs total dump volume and reactor
  volume.


  """
  Cross_area = pc.area_circle(UASB_diameter) #cross sectional area of c
  UASB_volume = UASB_height * pc.area_circle(UASB_diameter)
  height_added = dump_volume / Cross_area
  bucket_percent = (dump_volume / UASB_volume) * 100
  return [height_added, bucket_percent]

def pump_dump_calcs(pump_flowrate, pump_flowtime, UASB_height, UASB_diameter):
  """Solves for the height added per pump
  run and the dump percentage created by
  pump system for tapioca tests.  Inputs
  flowrate created by pump, total pump
  runtime, and the height and diameter of
  the model UASB


  """
  Vol_added = pump_flowrate * pump_flowtime
  Cross_area = pc.area_circle(UASB_diameter)
  height_added = Vol_added / Cross_area
  UASB_Volume = Cross_area * UASB_height
  pump_percent = (Vol_added / UASB_volume) * 100
  return [height_added, bucket_percent]

def find_upflow_vel(UASB_Flowrate_avg, UASB_CrossArea):
    """Finds average upflow velocity
     within the reactor using tipping
    bucket system.  Inputs are flowrate
    through reactor and the cross
    sectional area within the reactor.
    """
    avg_upflow_vel = UASB_Flowrate_avg / UASB_CrossArea
    return avg_upflow_vel

#Run doctest
doctest.testmod(verbose=True)

```


```python
#Run for target exit velocities
#Current setup ID is 1/4 inch (3/8 nom diam)
#and 1/8 inch (1/4 in nom diam)

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

## Biogas Capture System

As organic waste passes through the sludge blanket portion of the UASB reactor, it is broken down by anaerobic bacteria in a complex biological process that ends with methanogenesis.  A key product of this process is methane and carbon dioxide, which together are known as biogas.  This gas has a fairly high energy density, and can be burned for heating (just like propane).  Biogas capture is an important aspect of the UASB design since it allows the UASB to provide a valuable byproduct that can be used to fuel kitchens in the communities served. Also, it is important to prevent the release of this biogas into the atmosphere directly since methane is a harmful greenhouse gas.

This section is broken into two parts:  **Biogas Production** details our model of biogas production to quantify how much biogas is produced over time, and  **Biogas Storage** details our design of the biogas storage system.

### Biogas Production

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

It is important to note that this equation only gives an approximation of the actual biogas produced, and a fairly inaccurate one at that.  Methanogenesis is a very complicated biochemical process, and there are many other areas to consider that are not included in this equation, such as losses due to leakage, temperature effects, and the varying bacterial composition of the sludge blanket.  As most considerations are losses, we consider the value given by this equation an **overapproximation** and design accordingly.  For safety reasons, it is better to overestimate the volume produced rather than underestimate and design a system that will produce flammable gas.  Despite its problems, this equation still provides a good baseline value of the output biogas to inform the design process.

#### Design Parameters
*Table 2: Design parameters for biogas production.*

|                        Parameters                        |                 Value                 |                                              Basis of Design                                              |
|:--------------------------------------------------------:|:-------------------------------------:|:---------------------------------------------------------------------------------------------------------:|
|          COD Removal Efficiency, ```COD_eff```           |                  70%                  | Based on [Van Lier Report](https://courses.edx.org/c4x/DelftX/CTB3365STx/asset/Chap_4_Van_Lier_et_al.pdf) |
| Percent of COD directed to Sludge Production ```Y_obs``` |              23%               | Based on [Anaerobic Reactors](https://www.iwapublishing.com/sites/default/files/ebooks/9781780402116.pdf).  Chose highest value of removal to get minimum production value |
|                     Pressure ```P```                     |                 1 atm                 |                            Biogas produced will be stored at very low pressure                            |
|                   Temperature ```T```                    |            25 $^{\circ} C$             |                                  Assuming optimal biological conditions                                   |


#### Code
```python
from aide_design.play import*
import doctest
def BiogasFlow(Q, COD_Load, Temp, COD_removal_eff):
"""Calculates  molar, mass, and volumetric production rate of biogas within reactor.  Inputs are the flow rate of wastewater into the reactor (volume/time), the Carbonaceous Oxygen Demand of the influent wastewater (mass/volume), the average temperature inside the reactor, and the efficiency of COD removal within the system.  Mass rate conversion done using the ideal gas law.



"""
    COD_removed = COD_Load * COD_removal_eff #calculate COD broken down by reactor
    Y_obs = 0.23 # Upper limit of sludge production
    CH4prod_mass = (Q * COD_removed) - (Y_obs * Q * COD_Load) #Gives mass CH_4 produced per unit time
    CH4prod_moles = CH4prod_mass * 0.0623 * (u.mole/u.g) #Convert mass to moles using flipped atomic weight

    # Calculate correction factor for operational temperature of the reactor
    Pressure = 1 * u.atm
    K_COD = 64 * (u.g / u.mol)
    R = 0.08206 * ((u.atm * u.L) / (u.mol * u.degK))
    K = (P * K_COD) / (R * T)
    #Calculate the volumetric flow rate of methane production
    Q_CH4 = COD_CH4 / K # per second
    return Q_CH4

doctest.testmod(verbose=True)


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

### Biogas Storage

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


The team has begun preliminary discussions with Monroe regarding the Biogas Capture system. A meeting with Ed Gottlieb from the Ithaca wastewater plant has been scheduled for August 3, 2018 to discuss integrating the UASB plant into the Ithaca wastewater plant, as well as to discuss biogas collection. Research to find biogas storage bags is ongoing.

A possible biogas balloon has been found on [Amazon](https://www.amazon.com/PUXIN-Material-Biogas-Storage-Balloon/dp/B07FKS1W6J/ref=sr_1_1?ie=UTF8&qid=1532020224&sr=8-1&keywords=biogas+bag), although the details will be finalized only after the meeting with Ed.

## Documentation

Since the overall goal for the UASB project is to have a full design that can be fabricated in Honduras or other areas abroad, documentation of our entire design process is crucially important.  During this summer we have created two documents to meet this goal.

* The [UASB Design Manual](https://github.com/AguaClara/UASB/blob/master/Reports%20and%20Manuals/UASBdesignmanual.md) documents the entire design process for the UASB, and contains all relevant information on each component of the UASB and how the design was determined.
* The [UASB Fabrication Manual](https://github.com/AguaClara/UASB/blob/master/Reports%20and%20Manuals/UASBfabricationmanual.md) documents the entire process of fabricating the reactor.  This will serve as a full instruction manual for building the full UASB in the future.  

These documents will collect information from the semester reports and serve to easily transfer knowledge to any interested parties.  As of now they are working documents that are updated with each step forward in design.  

## Meeting with Ed 8/3/18

On August 3rd, 2018, the UASB team went to meet with Ed Gottlieb, an operator and our contact at the Ithaca Area Wastewater Treatment Facility (IAWWTF).  The full meeting notes can be found [here]().  The important notes are summarized below.

### Design Suggestions
Mr. Gottlieb offered a few other ideas to update our design.  For the influent system, he suggested attaching the influent system directly to the tank to make it one solid unit.  This attachment depends on the location of the influent tank, for a top influent system the tank can just be mounted on the top of the tank itself using a cylindrical pipe welded on to the top, but for the influent system coming in from the side of the tank, we would need to attach the tank to the side using a ring system.  This would of course need to be supported well since the tank would contain large loads of wastewater.
The influent pipe flow geometry was also discussed.  Mr. Gottlieb mentioned how in typical anaerobic digesters like the ones used in the IAWWTF, there is a mechanical mixer used to stir the water and increase digestion.  While our design will ideally not use mechanical parts, he suggested changing the exit port of the influent tube to create mixing through jets.  His design, sketched below, would cap the bottom of the pipe and cut holes in the sides every 90 degrees.  These holes would allow wastewater to exit at a high velocity and would split flow in four directions to increase the spread. The main concern for this design would be possible clogs in the systems.  Careful design of the sizing and spacing of the exit holes would be required to prevent this.  

<center><img src="https://github.com/AguaClara/UASB/blob/master/Images/Influent_jets_sketch.JPG?raw=true">
<p>
<em>Figure X: The proposed influent pipe slots to increase mixing</em>
</p>
</center>




### Sampling and Data collection

l

### Space for Pilot Reactor

Another important discussion from the meeting was the location for our pilot scale UASB.  

## Further Issues and Future Work


## Fabrication Manual

The team started to write a [fabrication manual](https://github.com/AguaClara/UASB/blob/master/UASBfabricationmanual.md) this summer that will document the total fabrication process so later teams can recreate the UASB system. This working document can be found in our Github repository.
