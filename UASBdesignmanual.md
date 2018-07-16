# UASB Design Manual

## Summer 2018

###Ian Cullings, Ananya Gangadhar, Isa Kaminsky

## Introduction

This document serves to detail the entire design process of the UASB system.  While each semester the team has worked on differing parts of the reactor, and solved different problems within, this document will collect all of these decisions into one place so that future readers can understand the design process of the UASB.  As such, this is a working document and will continuously be edited as designs are changed and new ideas are introduced.

## Reactor Tank

Initial design of the UASB models the 1 L/s plant closely, and thus assumed the use of a 3" diameter PVC pipe for the base of the tank, as the design required a bend in the pipe for the plate settlers.  Since the UASB system requires no bends and is completely vertical, it was proposed to use a prefabricated plastic tank instead.  

The advantages of the prefabricated tank include:
* Lower overall costs
* Easier fabrication of bottom and top of tank (tank is already sealed)
* Higher structural stability (particularly at bottom of tank)
* Possible prefabrication of inlet and outlet system

The disadvantages include:
* Tanks are harder to source outside of the US and might require shipping in
* Since tanks are prefabricated, it becomes challenging to fabricate pieces inside the tank (which are more easily accessible in a PVC pipe)
* Most prefab tanks are made of High Density Polyethylene (HDPE) rather than PVC.  Will require additional costs for welding rod and other materials.

The other design parameters are listed in the table below:
| Parameter | Value | Constraint                                                                            |
| --------- | ----- | ------------------------------------------------------------------------------------- |
| Height    | ~7ft  | Max height to still fit within lab space.  Could change based on fabrication location |
| Diameter  | 3ft   | No constraint. Chosen based on 1 L/s design   |

Precursory searches across Honduran suppliers found tanks of similar dimensions in HDPE, easing that concern.  Given that, it was decided to move forward purchasing a HDPE tank and using that for the initial design.  After local testing, the team will reevaluate the design based on materials available in Honduras and make any necessary changes.

The current plan is to purchase an HDPE tank similar to [this](https://www.plastic-mart.com/product/17049/300-gallon-plastic-tank-rotoplas-590314-590315) for fabrication of the first reactor.  After determining the location this system will be fabricated in, a final decision will be made on the dimensions of the tank and the tank will be purchased in preparation for fabrication in Fall 2018.

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
Table 3: Design parameters for biogas production.

|                        Parameters                        |      Value      |                                                                              Basis of Design                                                                               |
|:--------------------------------------------------------:|:---------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|          COD Removal Efficiency, ```COD_eff```           |       70%       |                                 Based on [Van Lier Report](https://courses.edx.org/c4x/DelftX/CTB3365STx/asset/Chap_4_Van_Lier_et_al.pdf)                                  |
| Percent of COD directed to Sludge Production ```Y_obs``` |       23%       | Based on [Anaerobic Reactors](https://www.iwapublishing.com/sites/default/files/ebooks/9781780402116.pdf).  Chose highest value of removal to get minimum production value |
|                     Pressure ```P```                     |      1 atm      |                                                            Biogas produced will be stored at very low pressure                                                             |
|                   Temperature ```T```                    | 25 $^{\circ}$C  |                                                                   Assuming optimal biological conditions                                                                   |
|            Methane Percentage `Methane_frac`             |       75%       |              Given in [Anaerobic Reactors](https://www.iwapublishing.com/sites/default/files/ebooks/9781780402116.pdf).                                                                                                                                                              |


#### Code
```python
from aide_design.play import*
def BiogasFlow(Q, COD_Load, Temp, COD_removal_eff):

    # Calculate ideal COD production
    COD_rem = COD_Load * COD_removal_eff #calculate COD broken down by reactor
    Y_obs = 0.23 # Upper limit of sludge production
    Biogas_flowrate_mass = (Q * COD_rem) - (Y_obs * Q * COD_Load) #Gives mass of total biogas produced per unit time
    Methane_frac = 0.75 # Assume 75% of biogas is methane
    Methane_flowrate_mass = Biogas_flowrate_mass * 0.75 # apply correction factor for methane percentage of biogas
    # Calculate correction factor for operational temperature of the reactor
    T = Temp.to(u.degK)
    P = 1 * u.atm
    K_COD = 64 * (u.g / u.mol)
    R = 0.08206 * ((u.atm * u.L) / (u.mol * u.degK))
    K = (P * K_COD) / (R * T)
    #Calculate the volumetric flow rate of methane production
    Methane_flowrate_vol = Methane_flowrate_mass / K # per second
    return [Methane_flowrate_vol, Methane_flowrate_mass]

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
print(Q_Biogas[0].to(u.L/u.day))
print(Q_Biogas[1].to(u.kg/u.day))
```

### Biogas Storage System

#### Lid design

##### Design 1: Hydraulic Seal

##### Design 2: Full Seal

#### Capture System Design

An important aspect of UASB design is the capture and storage of biogas produced during anaerobic digestion within the reactor.  As this gas is produced within the sludge blanket, it floats upwards through the settling zone and is captured within the lid space.  The UASB team considered many possible designs for this capture system.  These three options, along with Pros and Cons are detailed in the table below.

Table 4: List of advantages and disadvantages associated with different biogas storage systems.

| Type of Storage | Advantages | Disadvantages |
|:--------------- |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |:-------------------------------------------------------------------------------------------------------------------------- |
| Gas Bag         | (1) Flexible and easy connection on top of next to reactor (2) **Cheap and cost effective** (3) Easy to transport for reactor to kitchen use (4) Visual representation of gas volume | (1) Fragility and Leakage (2) Require frequent replacement - are these materials available locally?      |
| Fixed Lid       | (1) Durability (2) No concerns about movement (3) Can use prefabricated barrel                                                       | (1) Water displaced during gas compression may need to be recaptured, requiring additional information |
| Floating Lid    | (1) Water level moves with gas (2) Same concept as fixed lid (3) Visual representation of gas level            | (1) Low gas production will just cause water displacement (2) Track system hard to fabricate  |

After consideration of these options, the gas bag system was decided upon because it is cost effective and transportable for community settings where one community may share this resource.  This system is similar to other "bag" collection systems at traditional wastewater treatment facilities such as the Ithaca Area Wastewater Treatment Facility.

Research is ongoing on the best type of gas bag to use.  Currently, the goal is to find a collection system that does not require pressure to inflate.  While previously the team focused on an inflatable balloon, the bag is preferable as it does not require additional pressure to inflate, and instead just increases in volume as the number of moles of gas increases.  This would require a bag with a large enough volume to hold multiple days worth of biogas.  The bag should also have some capability to stretch like a balloon, so that if it is emptied late and exposed to pressure, it will not explode.  

The full collection system, pictured below, will consist of two exit valves.  The first is a manual valve leading to a tube connected to the gas bags.  Each gas bag will be sealed onto the pipe, and as gas is produced within the reactor it will enter these bags and fill them.  Once the bags are full, an operator can close the manual valve, remove the bags, add new bags in their place, and finally reopen the manual valve.  

The second exit valve is a check valve, which automatically opens when the interior is at a certain pressure.  This valve will serve as a safety for the system by venting gas when the interior reaches too high pressure.  Calculations run below calculate the maximum pressure attained when the bags are full, or if the valve is left closed.  

```python

def filltime(Q_biogas, Bag_Vol):
    bag_filltime = Bag_Vol / Q_biogas
    return filltime

def Pressure_gain(Biogas_flowrate_mass, Temp, Lid_Vol, Bag_Vol):
    #Takes in flowrate of biogas in mass units, temperature, volume of lid space without fluid, and volume of bags when fully inflated and gives the initial pressure when the bags are full, and the pressure gain per unit time.

    #Translate mass production of biogas to moles
    Biogas_flowrate_moles = Biogas_flowrate_mass * (1 / 16.04) * (u.moles / u.grams)

    #Calculate


    return

def Fluid_Pressure(WW_Height, WW_density):
    #Takes in height of wastewater in UASB and density to give the fluid pressure at the bottom of a tank using P = pgh formula

    return
```

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
