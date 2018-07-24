# UASB Design Manual

## Summer 2018

###Ian Cullings, Ananya Gangadhar, Isa Kaminsky

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
* Tanks are harder to source outside of the US and might require shipping in. However, we found manufacturers in Honduras so this should not be a huge concern.
* Since tanks are prefabricated with lids, it becomes challenging to attach pieces inside the tank. While using a PVC pipe would provide better access to the interior of the tank, our goal is to avoid any modifications within the reactor altogether.
* Most prefabricated tanks are made of High Density Polyethylene (HDPE) rather than PVC.  Will require additional costs for welding rod and other materials.


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

def UASBSize(diam, height):

    WW_gen = 3 * u.mL/u.s        #Wastewater generated per person, rule of thumb from Monroe
    WW_gen_bw = 0.6 * u.mL/u.s   #Assumes 20% of mixed wastewater
    HRT = 4 * u.hr               #Hydraulic Residence Time, determined from lab scale tests
    vol_reactor = (diam/2)**2 * math.pi * height
    flow = vol_reactor / HRT #Average flow rate through reactor given by volume and residence time
    people_served = int(flow / WW_gen)       #People served per reactor
    people_served_BW = int(flow / WW_gen_bw) #People served per reactor treating only blackwater
    output = [vol_reactor.to(u.L), flow.to(u.L/u.s), people_served, people_served_BW]
    return output

Diameter = 3 * u.ft
Height = 7 * u.ft
UASB_design = UASBSize(Diameter, Height)
print(UASB_design[1])

```



## Influent System

Assuming a pulse volume input of 10-20 L, we plan to use a 5-gallon bucket that will be mounted off-centered on some sort of shaft. The bucket can rotate about the shaft, and this entire setup will be enclosed within a holding tank.

Monroe and the team came up with a couple of design choices for the tipping bucket:

1. Weld two blocks of PVC to the sides of the 5-gallon bucket. Drill a rod into each block without penetrating the bucket. These rods are used to mount the bucket at a certain height inside the holding tank.

**(Insert design drawing here)**

   * **Pros**: Requires fewer materials. Is easier to fabricate.
   * **Cons**: Will need to align both rods perfectly. The welded sections will experience considerable shear. Replacing the bucket will be challenging.

2. Drill two holes in the bucket at an off-centered axis. Attach two screws to the bucket through these holes and use the screws to mount the bucket in the holding tank.

**(Insert design drawing here)**

* **Pros**: Less shearing
* **Cons**: Drilling holes makes the bucket vulnerable to leaks. Ease of replacement is still an issue

3. Weld two brackets onto the inner wall of the holding tank. Put a hose clamp around the bucket and mount the bucket via the clamp onto two small rollers. These rollers are placed in two

### Experimental Frame Design
In order to test the tipping bucket and find the right dimensions, the team fabricated a frame made of 80/20 extrusion bars that the bucket rests inside of. The benefit of using 80/20 bars is that they allow easy adjustment of the dimensions of our frame. Once the optimal orientation is decided upon after bench-top testing, the pivots can directly be screwed into the bucket minus the frame.

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
| Trial | Horizontal Pivot Position (from center) | Vertical Position (center of pivot to base of bucket) | Height Filled | Volume Filled |
| -------- | -------------------|-------------------- | --------- | ---------|
| 1    |   | 10 |
| 2 |  | 10 |  |  |
|3   |   |   |   |   |
|4   |   |   |   |   |
|5   |   |   |   |   |
|6   |   |   |   |   |
### Hydraulic Calculations

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



def calculate_head(target_exitvel, ):
"""Takes in desired exit velocity as well as pipe size and hydraulic parameters and calculates the hydraulic head needed to achieve this velocity using headloss function from aide_design.


"""


def head_gain_per_dump(dump_vol):



  return


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
Kminor = 4 #(1.5 * 2) from elbow joints in influent systems, plus 1 from headloss trick (assuming all flow out is lost kinetic energy) = 4
Temp = 23 * u.degC #average temp in Honduras
Nu = pc.viscosity_kinematic(Temp)
Pipe_Rough = 0.0015 * u.mm
total_hl = pc.headloss(pipe_flow, pipe_diam, pipe_length, Nu, Pipe_Rough, Kminor)
print(total_hl.to(u.cm))



```


### Flow Control Tests

#### Optimal Flow Patterns

Given that there has not been a design of a UASB on this scale, the scientific literature offered little information on flow patterns through a sludge blanket.  An understanding of flow through this system is important for the following reasons:

* An exit velocity of over 0.3 m/s is required to scour waste that may settle around the pipe exits and clog the system.
* Increasing the exit velocity can provide enough force to partially fluidize the bed, raising it up and completely surrounding it in wastewater. Fluidizing the bed increases the surface area of the granules that comes in contact with the wastewater, improving biological treatment.  This same principle is used in the [Anaerobic Fluidized Bed Reactor](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4441917/), which was investigated by AguaClara but ultimately rejected as it required pumps to run.
* Depending on the geometry of the reactor and velocity of influent wastewater, preferential flow pathways may form in the sludge blanket.  Preferential flow reduces the contact between wastewater and the granules, and in extreme cases creates **dead zones** (areas where no wastewater enters eventually causing sludge death).  


#### Tapioca Tests

To attempt to model and understand flow patterns within the UASB system, the team ran tests through a model sludge bed within a scaled down model UASB.  

The first UASB was modeled using a simple plastic beaker.
The model sludge blanket was created with

```python

# Calculate exit velocity from pipes given pipe dimensions and change in hydraulic head


```

### Influent System Geometry



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
