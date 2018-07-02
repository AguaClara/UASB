# Upflow Anaerobic Sludge Blanket (UASB) Design Manual

## Summer 2018

#### Ian Cullings, Isa Kaminsky, Ananya Gangadhar

Over Summer of 2018, the UASB team's main goal has been to finish a complete design of a UASB wastewater treatment system, and fabricate an influent system.  Future teams will work on fabrication of the entire system and testing at the Ithaca Area Wastewater Plant before implementation in Honduras.  

**_Juan's comments:_** You give very little background as to what's going on, and this section does not have a title. I believe this is an 'abstract'

### Influent Flow System

One major design goal for the summer was to finish the influent system that delivers wastewater to the bottom of the reactor.

**_Juan's comments:_** I think a figure would be very useful here, as it is extremely difficult to understand what's going on without being able to image the reactor

#### Continuous versus Pulse Flow

In Spring 2018, when design of the influent system began, the team began by assuming flow into the reactor would be continuous and at a roughly continuous rate. (This is already a major assumption, as wastewater production will rise in the day and lower at night.)  However, doing the initial calculations, this would require a pipe diameter on the order of 10 mm, which would clog easily and create major problems with the flow system.  During a meeting with Ed Gottlieb, an operator at the Ithaca Area Wastewater Treatment Plant, the idea of a pulse flow system was suggested, which would collect wastewater, then deliver it in larger "pulses" to achieve the hydraulic parameters needed.  Mr. Gottlieb's two suggested possible methods were: A tipping bucket system or a siphon.  

#### Tipping Bucket versus Siphon System


The summer team researched siphons and discussed with M-dawg potential design flaws, specifically the diameter of pipe that should be used. The main concern was that if too large a pipe was used, water would be able to pass through the siphon before it had filled to the level needed to create a pulse of a specific volume. Ultimately, the team was unable to find detailed enough engineering guidelines on how to design for a siphon using pulse flow. Given this, and given that the addition of an entrance tank required only one tipping bucket, the team settled on the tipping bucket design.

**_Juan's comments:_** Using 'M-dawg' is extremely inappropriate.

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
| Influent Pipe Inner Diameter     | 75 - 100mm      | No           | Based on literature values to prevent clogging in pipes.  Some flexibility.                                                                                                                                  |
| Influent Pipe Length             | ~8.5 feet       | Yes          | Roughly equal to height of reactor plus half of diameter (see influent pipe geometry)                                                                                                                        |
| Bucket Dump Volume               | ~20 L           | No           | Constrained by both time to fill bucket (should be larger) and fraction of reactor volume (should be smaller) 20 L chosen as it is the volume of easily available buckets while fulfilling these constraints |
| Wastewater Generation per Person | 10.8 L/hr       | No           | Rule of Thumb From M-dawg                                                                                                                                                                                    |

**_Juan's comments:_** Under 'bucket dump volume,' your 'should be larger' and 'should be smaller' are not clear. Are you referring to the time or the volume?

From these constraints, the general headloss equation (including the headloss trick) for a circular pipe can be used to determine the headloss needed to achieve our desired exit velocity, given a specific diameter of pipe.  

**_Juan's comments:_** `from aide_design import*` already imports math, you don't need to do that again. When you say KMinor = 4, what is your reasoning? Include a comment specifying why that is
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

Given these parameters, the team began to plan on how to properly design the tipping bucket system.  Design began by looking into tipping bucket systems online to research their design; however, since tipping buckets are generally only used in water parks, it was difficult to find any detailed design process for these systems. At this point, the team was left with two choices: try to complete a mathematical model of the tipping bucket system (using free-body diagrams), or create a physical model of the tipping bucket system and test it in many configurations to find the optimal design.  Given time constraints and lack of expertise, the team decided to fabricate a tipping bucket it and test it physically.

**_Juan's comments:_** "Given these parameters, the team began *planning the design of the tipping bucket system*" I don't think "plan on" is the best way to say that.

![Timmy_the_Tipping_Bucket](https://github.com/AguaClara/UASB/blob/master/Images/IMG_5759.jpg)

**_Juan's comments:_** This picture (which only shows up online, not in markdown preview) should be cleaned up a bit. It can be cropped a bit, and the background would be clear (as it can be in the lab) instead of cardboard.

Pictured above is the first design of the tipping bucket system.  It was created with a small plastic lab beaker, two screws, and 80-20 bars with connectors used to provide a pivot for the screws.  This was mostly created to give the team a general sense of how tipping buckets work, not to collect specific data.  This model offered a few insights for the design:

* Location of the pivot on the bucket is very important for operation.  Height of the pieces controls how much water is collected before dumping.  Horizontal positioning of the pivot determines the angle the bucket rests at and how soon it will tip.

* The bucket needs to be designed so that it will not rest completely tipped down.  This can be achieved either by controlling the height of the bucket so that is cannot rotate completely (making it hit the bottom of the tank) or by controlling the rotation, either through adding a counterweight that will return the bucket to its main position, or adjusting the horizontal location of the pivot to ensure it will return.

After discussing the design more with Monroe, the team settled on a new design, pictured below:

![Tipping Bucket Fusion Model](https://github.com/AguaClara/UASB/blob/master/Images/Screen%20Shot%202018-06-29%20at%201.33.27%20PM.png)

**_Juan's comments:_** This is cool but I have no idea what I'm looking at. Can you include one of those links online in fusion where we can spin things around and look inside? ![something like this one](https://myhub.autodesk360.com/ue28a131e/g/shares/SH7f1edQT22b515c761e7fb9f856bcad56c1) that Jonathan made of the 1 LPS plant.

**Add photo of fusion model of bucket**

This bucket is created with a 5 gallon bucket (chosen as they are easy to purchase) with two circular pieces on either side, attached through a hose clamp.  These circular pieces will rest in the brackets on either side of the entrance tank, where they can roll freely to allow the bucket to dump.  This removes friction and the some of the danger of breakdown over time.

**_Juan's comments:_** Circular pieces of what?

**Add photo of fusion model of brackets**

The addition of the hose clamp also allows for the pieces to be moved spatially around the bucket easily, allowing the team to test many different orientations of the pivot without drilling new holes in the bucket.  This also will allow easy replacement of the bucket system if necessary (important as pieces will inevitably break).

**_Juan's comments:_** The information you included in parentheses can be instead separated with a comma and the word 'as.' Generally, using extraneous parentheses in technical writing is frowned upon.

The next steps for this process are to order pieces for the bucket and test it physically to determine the optimal orientation of the pivot system.

#### Design of Influent Tank

Another crucial part of the design  is the influent tank.  This tank will capture all wastewater from the tipping bucket, and distribute it evenly across both influent pipes from flow control.  To prevent any splashing of wastewater, this tipping bucket will be completely contained within the influent tank.

The crucial design aspects of the tank are listed below:

* The tank **must be tall enough** to completely contain the tipping bucket, and prevent any "splashing" of wastewater out of the tank
* The tank **must be just wide enough** to contain the bucket and the two brackets.  If the tank is wider, that will require more material for the pivot bars, and reduce the structural strength of the bucket (by creating more torque on each bar)
* The dimensions of the tank must be such that they **create the required amount of hydraulic head from one dump of the tipping bucket**.  This can be constrained by adding or removing material from the bottom of the tank to increase water height added per volume of a dump
* **_Juan's comments:_** what do you mean adding or removing material? What kind of material are you adding or removing? How are you removing material from a tank?
* The tank **must evenly split flow between the two pipes**.  This can be designed ~~for~~ by changing the geometry of the pipes based on where the water is dumped, but most importantly there should always be a small volume of water in the tank even when all the water from one dump has been drained out.
* **_Juan's comments:_** Why? I believe this point should be combined with the next one.
* There should always be a small section of the tank where the **descending sewage velocity is below 0.2 m/s** to allow air bubbles to escape.    
* The tank should be **easy to source**, that is it can be purchased at the correct dimensions, or fabricated simply

**_Juan's comments:_** Some of the bullet points end in punctuation, some don't.


Summarized in a table:

| Parameter | Value | Justification |
|:-------------- |:-----  |------------- |
|Height|$\geq$ 40 cm| Height of bucket plus 4 cm error|
|Width|35 cm |30 cm for bucket diameter plus 5 cm for both pivot pieces|
|Length|$\geq$ 60 cm|Height of bucket plus extra space to allow free rotation.  Requires closer examination in fusion|

![Schematic of Influent System](https://github.com/AguaClara/UASB/blob/ff3b4e844a16a686811ad80eee5941520a022939/Images/Influent%20Geo%20Slant.png)

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

**_Juan's comments:_** Ah now your reference to adding material makes more sense. This explanation of adding material should be included before you talk about it in the bullet point above.

After further discussion with Monroe, a new design to solve this problem was suggested.  Instead of a sloped tank, the tank would be kept rectangular, and larger pipes along the bottom would be added, which would then connect to the influent pipes.  These pipes would retain most of the volume dumped and provide the needed hydraulic head, while not altering the tank geometry.  A fusion model of this model is pictured below.

**Add fusion model of full influent system**

**_Juan's comments:_** This image helps a bit but I still don't quite understand how this helps your problem. I think a bit more explanation is required. The idea is to have a future team member read through this all and understand your logic, else they will not be able to understand the design.

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

# Determine pipe inner diameter based on nominal diameter
nom_diam = 2.5  * u.inch
pipe_diam = pipe.ID_sch40(nom_diam)
print(pipe_diam.to(u.mm))

# Calculate hydraulic head needed to achieve desired exit velocity, accounting for major and minor losses
exit_vel = 1 * u.m / u.s #maximum exit velocity at the bottom of the system, variable
pipe_flow = exit_vel * pc.area_circle(pipe_diam)
pipe_length = (diam / 2) + height
Kminor = 4 # 1 from headloss trick, plus 2 * 1.5 for the two full elbows in the influent system
Temp = 23 * u.degC #average temp in Honduras
Nu = pc.viscosity_kinematic(Temp)

Pipe_Rough = 0.0015 * u.mm
total_hl = pc.headloss(pipe_flow, pipe_diam, pipe_length, Nu, Pipe_Rough, Kminor)
print(total_hl.to(u.cm))

# Calculate dimensions of storage tank
# bucket_diam = 30 * u.cm
#tank_width = 35 * u.cm # add 5 cm extra room
#tank_len = (dump_vol) / (total_hl * tank_width)

#print("For a headloss of " ,total_hl, "\n  coming from an exit velocity of ", exit_vel,  "\n Tank length is ", tank_len.to(u.cm), "\n Tank width is ", tank_width, "\n Volume per pulse is ", dump_vol)
```


With this given headloss, the dimensions of the larger pipe that will intersect with the influent pipes can be solved for.  This pipe needs to fill to the required head with one dump, while still allowing a small volume of water occupy the entrance tank, allowing even flow distribution.

**_Juan's comments:_** I don't think intersect is the right word here. Remember, people who have no idea what you're doing right now will read this and be expected to understand everything perfectly. Make it easy for them!


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


### Biogas Capture System

The team has begun preliminary discussions with M-dawg regarding the Biogas Capture system, and will be having

## Fabrication manual

The team started to write a fabrication manual this summer that will document the total fabrication process so later teams can recreate the UASB system. This working document can be found in our Github repository.
