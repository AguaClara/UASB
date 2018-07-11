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

| Parameters | Value | Basis of Design |
| :-------: | :--------: | :--------------: |
| COD Removal Efficiency, ```COD_eff``` | 70% | Based on [Van Lier Report](https://courses.edx.org/c4x/DelftX/CTB3365STx/asset/Chap_4_Van_Lier_et_al.pdf)  |
| Percent of COD directed to Sludge Production ```Y_obs```| 11% to 23% | Based on [Anaerobic Reactors](https://www.iwapublishing.com/sites/default/files/ebooks/9781780402116.pdf) |
| Pressure ```P```| 1 atm | Biogas produced will be stored at very low pressure |
| Temperature ```T``` | 25 $^{\circ}$ C | Assuming optimal biological conditions |

#### Code
```python
def BiogasFlow(Q, COD_Load, Temp, COD_removal_eff):
    """Calculates the biogas production rate from the flow rate through the reactor, the COD concentration of the influent, the temperature of the reactor, and the removal efficieny of COD within the reactor

    For the doctest to pass, one must initialize the flow from UASB_design using UASB_Size(3 * u.ft, 7 * u.ft)

    >>> from aide_design.play import*
    >>> import math
    >>> BiogasFlow(UASB_design[2], 200 * (u.mg / u.L), 25 * u.degC)
    The volumetric methane production per second is 0.0013 liter / second
    The volumetric methane production per second is 112.3 liter / day
    [<Quantity(0.0012996707807037425, 'liter / second')>, <Quantity(112.29155545280335, 'liter / day')>]
    """
    COD_rem = COD_Load * COD_removal_eff #calculate COD broken down by reactor
    Y_obs = 0.23 # Upper limit of sludge production
    COD_CH4 = (Q * COD_rem) - (Y_obs * Q * COD_Load)
    # Calculating correction factor for operational temperature of the reactor
    T = Temp.to(u.degK)
    P = 1 * u.atm
    K_COD = 64 * (u.g / u.mol)
    R = 0.08206 * ((u.atm * u.L) / (u.mol * u.degK))
    K = (P * K_COD) / (R * T)
    #Calculate the volumetric flow rate of methane production
    Q_CH4 = COD_CH4 / K # per second
    Q_day = Q_CH4 * 86400 * (u.s / u.day) # per day

    print("The volumetric methane production per second is", Q_CH4, "\n" "The volumetric methane production per second is", Q_day)
    return [Q_CH4, Q_day]



# Flow rate through UASB reactor
Flow_design = UASB_design[2]
print(Flow_design)
# Amount of biogas production per second and per day
Temp = 25 * u.degC  # Assuming mesophilic conditions
#Approximate loading rates for domestic wastewater
COD_Load_min = 100 * (u.mg / u.L)
COD_Load_mid = 200 * (u.mg / u.L)
COD_Load_max = 300 * (u.mg / u.L)

Q_Biogas = BiogasFlow(Flow_design, COD_Load_mid, Temp)
#Calculating size of storage device
print (Q_Biogas)

doctest.testmod(verbose=True)

Size_Store = Q_Biogas[1].to(u.gal / u.day) * (u.day)
print("The size of the storage container to store one day worth of biogas production should be at least", Size_Store)
```

### Biogas Storage System

An important aspect of UASB design is the capture and storage of biogas produced during anaerobic digestion within the reactor.  As this gas is produced within the sludge blanket, it floats upwards through the settling zone and is captured within the lid space.  The UASB team considered many possible designs for this capture system.  These three options, along with Pros and Cons are detailed in the table below.

Table 4: List of advantages and disadvantages associated with different biogas storage systems.

| Type of Storage | Advantages | Disadvantages |
|:--------------- |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |:-------------------------------------------------------------------------------------------------------------------------- |
| Gas Bag         | (1) Flexible and easy connection on top of next to reactor (2) **Cheap and cost effective** (3) Easy to transport for reactor to kitchen use (4) Visual representation of gas volume | (1) Fragility and Leakage (2) Require frequent replacement - are these materials available locally?      |
| Fixed Lid       | (1) Durability (2) No concerns about movement (3) Can use prefabricated barrel                                                       | (1) Water displaced during gas compression may need to be recaptured, requiring additional information |
| Floating Lid    | (1) Water level moves with gas (2) Same concept as fixed lid (3) Visual representation of gas level            | (1) Low gas production will just cause water displacement (2) Track system hard to fabricate  |

After consideration of these options, the gas bag system was decided upon because it is cost effective and transportable for community settings where one community may share this resource.  This system is similar to other "bag" collection systems at traditional wastewater treatment facilities such as the Ithaca Area Wastewater Treatment Facility.

Schematically, gas will flow out the top lid of the reactor through a pipe into an intermediate volume as shown in Figure 5.  This space will hold biogas, where it can be released into a balloon for home usage, or flared off from the container.  A check valve will also be used in order to release excess gas produced to prevent dangerous buildup and pressurization of flammable gas.  The proposed design of the system is shown in Figure 9.

![Biogas_Close](https://github.com/AguaClara/UASB/blob/master/Images/Biogas%20Lid%20Closeup.jpg?raw=true)
<p align="center">Figure 8: Detailed view of the biogas capture lid on top of the UASB reactor.  The hydraulic seal is created by setting the water level above the base of the lid.  When biogas is produced, it is trapped under the lid.  As it builds up, it displaces fluid inside the reactor and pushes the free surface down.   </p>

![Biogas_Storage](https://github.com/AguaClara/UASB/blob/master/Images/Biogas%20Storage.jpg?raw=true)
<p align="center">Figure 9: Schematic of the proposed biogas storage system.  Collection first occurs in a rigid intermediate storage unit before flowing into a flexible storage bag.  If excess biogas builds up within the unit, a check valve will release this excess to prevent the dangerous pressure buildup  </p>

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
