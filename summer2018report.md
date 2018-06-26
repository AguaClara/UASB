# Upflow Anaerobic Sludge Blanket (UASB) Design Manual

## Summer 2018

#### Ian Cullings, Isa Kaminsky, Ananya Gangadhar

Over Summer of 2018, the UASB team has been continuing the design work of previous semesters to finish a complete design of a UASB wastewater treatment system.  After completion of this design, future teams will work on fabrication of the system and testing at the Ithaca Area Wastewater Plant before implementation in Honduras.  

### Influent Flow system

One major design goal for the summer was to finish the influent system that delivers wastewater to the bottom of the reactor.

#### Continuous versus Pulse Flow

In Spring 2018, when design of the influent system began, the team began by assuming flow into the reactor would be continuous and at a roughly continuous rate. (This is already a major assumption, as wastewater production will rise in the day and lower at night.)  However, doing the initial calculations, this would require a pipe diameter on the order of 10 mm, which would clog easily and create major problems with the flow system.  After meeting with Ed Gottlieb, an operator at the Ithaca Area Wastewater Treatment Plant, he suggested the idea of a pulse flow system, which would collect wastewater, then deliver it in larger "pulses" to achieve the hydraulic parameters.  Mr. Gottlieb suggested two possible methods to deliver the pulses: A tipping bucket system or a siphon.  

#### Tipping Bucket versus Siphon system

(**Add descriptions from spring 2018**)
#### Rejection of the Siphon System

The summer team researched siphons and discussed with M-dawg potential design flaws, specifically the diameter of pipe that should be used. The main concern was that if too large a pipe was used, water would be able to pass through the siphon before it had filled to the level needed to create a pulse of a specific volume. Ultimately, the team was unable to find detailed enough engineering guidelines on how to design for a siphon using pulse flow.

#### Tipping Bucket System



Given this, and given that the addition of an entrance tank required only one tipping bucket, the team settled on the tipping bucket design, rather then spending time fabricating and testing a siphon system that may not work at all.

#### Hydraulic Parameters

Built within the design of the influent systems are a number of hydraulic constraints that must be met for the flow to work properly.  These are summarized in Table 1 below.

<p align="center">Table 1: Design parameters for UASB hydraulics </p>

| Parameter      | Value | Constrained? | Justification |
|:-------------- |:----- | ------------ | ------------- |
| Reactor Volume | 1221 Liters | Yes  | Based on max diameter and height to allow fabrication |
| Sludge Volume  | ~850 Liters | No | Roughly 70% of Reactor Volume.  Needs to be better constrained based on location of tube settler. |
| HRT | $\geq$ 4hrs | Yes, minimum  | Based on literature and lab scale test.  | |
|Descending Sewage Velocity|$\leq$ 0.2 m/s|Yes, Maximum | Maximum velocity that will allow air bubbles to rise out of reactor.  Must only be achieved in beginning of influent pipe systems, not throughout.|
| Average Flow Rate   | $\leq$ 0.08 L/s  | Yes, Maximum | Q = Volume / Hydraulic Residence Time  |
| Minimum Exit Velocity   | $\geq$ 0.03 m/s   | Yes | Minimum velocity needed to scour settling particles |    
| Maximum Exit Velocity | $\leq$ 1 m/s | No | Max velocity needed to prevent preferential pathways through sludge blanket.  Still very undetermined. |  
| Influent Pipe Inner Diameter | 75 - 100mm  | No | Based on literature values to prevent clogging in pipes.  Some flexibility. |
| Influent Pipe Length | ~8.5 feet | Yes| Roughly equal to height of reactor plus half of diameter (see influent pipe geometry) |
|Bucket Dump Volume|~20 L| No| Constrained by both time to fill bucket (should be larger) and fraction of reactor volume (should be smaller) 20 L chosen as it is the volume of easily available buckets while fulfilling these constraints||

From these constraints, we can use the general headloss equation (including the headloss trick) for a circular pipe to determine the headloss needed to acheive our desired exit velocity, given a specific diameter of pipe.  

```python
# Calculates headloss in influent system based on dimensions of reactor

# Import required functions
from aide_design.play import*
import math
from UASB_size import*

# Calculate size and flow dimensions
height = 7 * u.ft
diam = 3 * u.ft
UASB_design = UASBSize(diam, height)
vol = UASB_design[1]
min_HRT = 4 * u.hr
Q_avg = vol / min_HRT
print(Q_avg.to(u.L/u.s))

#Determine pipe inner diameter based on nominal diameter

nom_diam = 2.5  * u.inch
pipe_diam = pipe.ID_sch40(nom_diam)
print(pipe_diam.to(u.mm))

# Calculate hydraulic head needed to achieve desired exit velocity, accounting for major and minor losses
exit_vel = 1 * u.m / u.s
pipe_flow = exit_vel * pc.area_circle(pipe_diam)
pipe_length = (diam / 2) + height
Kminor = 4
Temp = 23 * u.degC #average temp in Honduras
Nu = pc.viscosity_kinematic(Temp)
Pipe_Rough = 0.0015 * u.mm
total_hl = pc.headloss(pipe_flow, pipe_diam, pipe_length, Nu, Pipe_Rough, Kminor)
print(total_hl.to(u.cm))
 ```

#### Design of Tipping Bucket system

Given these parameters, the team began to plan on how to properly design the tipping bucket system.  Design began by looking into tipping bucket systems online to research their design, however since tipping buckets are generally only used in water parks, it was difficult to find any detailed design process for these systems.  At this point, the team was left with two choices: try to complete a mathematical model of the tipping bucket system (using free-body diagrams), or create a physical model of the tipping bucket system and test it in many configurations to find the optimal design.  Given time constraints and lack of expertise, the team decided to fabricate a tipping bucket it and test it physically.

**Add photo of first tipping bucket**

Pictured above is our first tipping bucket system.  It was created with a small plastic lab beaker, two screws, and 80-20 bars with connectors used to provide a pivot for the screws.  This was mostly created to give the team a general sense of how tipping buckets work, not to collect specific data.  This model offered a few insights for the design:

* Location of the pivot on the bucket is very important for operation.  Height of the pieces controls how much water is collected before dumping (but if the pieces are too high, they won't dump at all).  Horizontal positioning of the pivot determines the angle the bucket rests at and how easy it is to tip.

* The bucket needs to be designed so that it will not rest completely tipped down.  This can be achieved either by controlling the height of the bucket so that is cannot rotate completely (making it hit the bottom of the tank) or by controlling the rotation, either through adding a counterweight that will return the bucket to its main position, or adjusting the horizontal location of the pivot to ensure it will return.

After discussing the design more with Monroe, the team settled on a new design, pictured below:

**Add photo of fusion model of bucket**

This bucket is created with a 5 gallon bucket (chosen as they are easy to purchase) with two circular pieces on either side, attached through a hose clamp.  These circular pieces will rest in the brackets on either side of the entrance tank, where they can roll freely to allow the bucket to dump.  This removes friction and the some of the danger of breakdown over time.

**Add photo of fusion model of brackets**

The addition of the hose clamp also allows for the pieces to be moved spatially around the bucket easily, allowing the team to test many different orientations of the pivot without drilling new holes in the bucket.  This also will allow easy replacement of the bucket system if necessary (important as pieces will inevitably break).

Next steps for this process are to order pieces for the bucket and test it physically to determine the optimal orientation of the pivot system.


#### Design of Influent Tank

Another crucial part of the design  is the influent tank.  This tank will capture all wastewater from the tipping bucket, and distribute it evenly across both influent pipes from flow control.  To prevent any splashing of wastewater, this tipping bucket will be completely contained within the influent tank.

The crucial design aspects of the tank are listed below:
* The tank must be tall enough to completely contain the tipping bucket, and prevent any "splashing" of wastewater out of the tank
* The tank must be just wide enough to contain the bucket and the two brackets.  If the tank is wider, that will require more material for the pivot bars, and reduce the structural strength of the bucket (by creating more torque on each bar)
* The dimensions of the tank must be such that they create the required amount of hydraulic head from one dump of the tipping bucket.  This can be constrained by adding or removing material from the bottom of the tank to increase water height added per volume of a dump
* The tank must evenly split flow between the two pipes.  This can be designed for by changing the geometry of the pipes based on where the water is dumped, but most importantly there should always be a small volume of water in the tank even when all the water from one dump has been drained out.
* There should always be a small section of the tank where the descending sewage velocity is below 0.2 m/s to allow air bubbles to escape.    
* The tank should be easy to source, that is it can be purchased at the correct dimensions, or fabricated simply

Summarized in a table:

| Parameter | Value | Justification |
|:-------------- |:-----  |------------- |
|Height|$\geq$ 40 cm| Height of bucket plus 4 cm error|
|Width|35 cm |30 cm for bucket diameter plus 5 cm for both pivot pieces|
|Length|$\geq$ 60 cm|Height of bucket plus extra space to allow free rotation.  Requires closer examination in fusion|

**Add image of tank and bucket clearly defining l,w,h**

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

#### Code
Given these input parameters, we can solve for the headloss necessary to achieve desired flow using the following code:

```python
# Calculates headloss in influent system based on dimensions of reactor

# Import required functions
from aide_design.play import*
import math
from UASB_size import*

# Calculate size and flow dimensions
height = 7 * u.ft
diam = 3 * u.ft
UASB_design = UASBSize(diam, height)
vol = UASB_design[1]
min_HRT = 4 * u.hr
Q_avg = vol / min_HRT
print(Q_avg.to(u.L/u.s))

#Determine pipe inner diameter based on nominal diameter

nom_diam = 2.5  * u.inch
pipe_diam = pipe.ID_sch40(nom_diam)
print(pipe_diam.to(u.mm))

# Calculate hydraulic head needed to achieve desired exit velocity, accounting for major and minor losses
exit_vel = 1 * u.m / u.s
pipe_flow = exit_vel * pc.area_circle(pipe_diam)
pipe_length = (diam / 2) + height
Kminor = 4
Temp = 23 * u.degC #average temp in Honduras
Nu = pc.viscosity_kinematic(Temp)
Pipe_Rough = 0.0015 * u.mm
total_hl = pc.headloss(pipe_flow, pipe_diam, pipe_length, Nu, Pipe_Rough, Kminor)
print(total_hl.to(u.cm))



# Given volume of tipping bucket, determine time to fill bucket

dump_vol = 15 * u.L
filltime = dump_vol /
print(filltime.to(u.min))

#dump_amount = 2 * total_hl * pc.area_circle(pipe_diam)
#print(dump_amount.to(u.L))

# Calculate dimensions of storage tank
bucket_diam = 30 * u.cm
tank_width = 35 * u.cm #add 5 cm extra room
tank_len = (dump_vol) / (total_hl * tank_width)

print("For a headloss of " ,total_hl, "\n  coming from an exit velocity of ", exit_vel,  "\n Tank length is ", tank_len.to(u.cm), "\n Tank width is ", tank_width, "\n Volume per pulse is ", dump_vol)
```







### Biogas Capture System
