## Biogas Storage
Biogas is a crucial aspect of the UASB design.  Recovered biogas produced during anaerobic digestion can be captured and stored, providing a cooking or heating source for the communities.  In order to maximize biogas production, it is very important to design a gas-tight capture system within the UASB, and an easy method of removing and utilizing this biogas.  Current design work focuses on creating this system, and a future design project will be creating biogas stoves that can use this product to cook meals.

Most UASB systems in place now use a gas-liquid-solid separator (pictured below).  This inverted cone collects biogas produced within the sludge blanket and diverts solids and liquids downwards to prevent contamination.  We decided to research and test differing designs, as this separator is challenging to fabricate, and difficult to attach within the reactor securely.  

![Conventional UASB](https://github.com/AguaClara/UASB/blob/master/Images/Conventional_UASB.PNG?raw=true)

<center>
Figure 1: Conventional UASB system with Gas Liquid Solid Separator
</center>

Following the proposed designs of the EPA P3 Phase I UASB proposal, the team has explored the idea of a removable biogas capture lid.  This concept, however, was flawed in its designs for the following reasons:

1. It is difficult to maintain a hydrostatic seal unless the lid is incredibly tall (i.e. storage volume is very large) as shown by the Spring 2017 [Final Report](https://www.overleaf.com/8107719xzjdzswjvtyj#/28623295/)
2. The height of the lid becomes a major design problem in a small scale system with a consolidated reactor and storage lid system as is constrains the location and placement of other components such as the tube settler arm.
3. Biogas buildup in a fixed lid system displaces water volume in the reactor which cannot be easily restored once biogas is used or released unless this water is captured.

For these reasons, the team is proposing a temporary gas storage system that is detached from the reactor. These have been widely implemented in [short term gas storage](http://www.susana.org/_resources/documents/default/2-1799-biogasplants.pdf) While this is a necessary step on the small scale, it is not necessarily the case for larger UASB reactors.

| Parameters | Value | Basis of Design |
| :-------: | :--------: | :--------------: |
Wastewater Generation ```WW_gen```| 3 ml/s | Rule of thumb from Monroe
Hydraulic Retention Time ```HRT``` |4 hrs | Previous lab test and literature review
| Removal Efficiency | 0.7 | Based on [Van Lier Report](https://courses.edx.org/c4x/DelftX/CTB3365STx/asset/Chap_4_Van_Lier_et_al.pdf)  |
| Percent of COD directed to Sludge Production ```Y_obs```| 0.11 to 0.23 | Based on [Anaerobic Reactors](https://www.iwapublishing.com/sites/default/files/ebooks/9781780402116.pdf) |
| Pressure ```P```| 1 atm | Biogas produced will be stored at very low pressure |
| Temperature ```T``` | 25 $^{\circ}$ C | Assuming mesophilic conditions |

### UASB Size


#### Function
```python
from aide_design.play import*
import math

Diameter = 3 * u.ft
Height = 7 * u.ft
COD_Load_min = 100 * u.mg/u.L
COD_Load_mid = 200 * u.mg/u.L
COD_Load_max = 300 * u.mg/u.L

def UASBSize(diam, height):
    """Takes the inputs of diameter and height. The bottom of the UASB is sloped
    at 60 degrees with a 3 inch space across the bottom of the UASB. Assumes that half the reactor
    contains the settled bed, which is used for the HRT. Returns five outputs: 1. height of the sloped
    sides of the bottom geometry, 2. volume of sludge in the reactor, 3. flow rate,
    4. number of people served with graywater, 5. number of people served with blackwater.
    """

    WW_gen = 3 * u.mL/u.s        #Wastewater generated per person, rule of thumb from Monroe
    WW_gen_bw = 0.6 * u.mL/u.s   #Assumes 20% of mixed wastewater
    HRT = 4 * u.hr               #Hydraulic Residence Time, determined from lab scale tests

    centerspace = 3 * u.inch     #Center space allows for a 3 inch pipe across the bottom
    phi = math.atan((diam/2)/(centerspace/2))
    angle = 60 * u.deg           #Angle of the sloped bottom

    height_cyl_hoof = diam/2 * np.tan(angle)    #Hoof is if the sloped bottom meets in the centerline
    height_cyl_wedge = height_cyl_hoof - ((centerspace/2) * math.tan(angle)) #Wedge is if the sloped bottom is offset from the centerline
    vol_cyl_wedge = height_cyl_wedge * (diam/2)**2 / 3 * ((
        3*math.sin(phi) - 3*phi*math.cos(phi) - math.sin(phi)**3)/(1-math.cos(phi)))
    vol_reactor = (math.pi * (diam / 2)**2 * height / 2) - (2 * vol_cyl_wedge)

    flow = vol_reactor / HRT
    people_served = int(flow / WW_gen)       #People served per reactor
    people_served_BW = int(flow / WW_gen_bw) #People served per reactor treating only blackwater

    output = [height_cyl_wedge.to(u.m), vol_reactor.to(u.L), flow.to(u.L/u.s), people_served, people_served_BW]

    print("The height of the bottom geometry is",height_cyl_wedge.to(u.m))
    print('The volume of the sludge in the reactor is', vol_reactor.to(u.L))
    print('The flow rate of the reactor is', flow.to(u.L/u.s))
    print('The number of people served by this reactor is', people_served)
    print('The number of people served by this reactor if only blackwater is treated is', people_served_BW)
    return output
```

#### Output
```python
UASB_design = UASBSize(Diameter, Height)
Flow_design = UASB_design[2]
```

### Biogas Production Calculations
As organic waste passes through the sludge blanket portion of the UASB reactor, it is broken down by anaerobic bacteria in a process known as methanogenesis.  A key product of this process is methane and carbon dioxide, which together are known as biogas.  This gas has a fairly high energy density, and can be burned for heating like propane.  

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

Since biogas contains other gasses such as CO2, we must employ a correction factor to account for their contributions to the overall volume.  We assume methane is 75%, as given in [Anaerobic Reactors](https://www.iwapublishing.com/sites/default/files/ebooks/9781780402116.pdf)

It is important to note that this equation only gives an approximation of the actual biogas produced, and a fairly inaccurate one at that.  Methanogensis is a very complicated biochemical process, and there are many other areas to consider that are not included in this equation, such as losses due to leakage, temperature effects, and the varying bacterial composition of the sludge blanket.  As most considerations are losses, we consider the value given by this equation an **overapproximation** and design accordingly.  Despite its problems, this equation still provides a good baseline value of the output biogas to inform the design process.

#### Function
```python

#Calculate Biogas Rate of Production (L/s and L/day) in UASB
def BiogasFlow(Q, COD_Load, Temp):
    # Calculating methane production by mass
    CO2_% = 0.25 #percentage of other gasses in total biogas
    COD_Load = COD_Load.to(u.g / u.L)
    COD_eff = 0.7
    COD_rem = COD_Load * COD_eff # Assuming 70% efficency of COD removal and conversion in reactor
    Y_obs = 0.23 # Upper limit of sludge production
    COD_CH4 = (Q * COD_rem) - (Y_obs * Q * COD_Load)
    # Calculating correction factor for operational temperature of the reactor
    T = Temp.to(u.degK)
    P = 1 * u.atm
    K_COD = 64 * (u.g / u.mol)
    R = 0.08206 * ((u.atm * u.L) / (u.mol * u.degK))
    K = (P * K_COD) / (R * T)
    #Calculate the volumetric flow rate of methane production
    Q_CH4 = (COD_CH4 * (1+CO2_%)) / K * CH4_% # per second
    Q_day = Q_CH4.to(u.day) # per day

    print("The volumetric methane production is per second is", Q_CH4, "\n" "The volumetric methane production is per second is", Q_day)
    return [Q_CH4, Q_day]
```

#### Outputs
```python
# Amount of biogas production per second and per day
Temp = 25 * u.degC  # Assuming mesophilic conditions
Q_Biogas = BiogasFlow(Flow_design, COD_Load_mid, Temp)
#Calculating size of storage device
Stor_Size = Q_Biogas[1].to(u.gal / u.day) * (u.day)
print("The size of the storage container to store one day worth of biogas production should be at least", Stor_Size)
prod = Q_Biogas[1]
```

###Storage Size
Safely and efficiently create short term storage for biogas produced so that it may be used
####Code
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
```
####Output
```python
day_prod = Q_Biogas[1]
time_stor = 2 * u.day
time_fail = 12 * u.hr
diam_lid = 2.5 * u.ft

size_stor = Dim_Storage(day_prod, time_stor, time_fail, diam_lid)
vol_stor = size_stor[0].to(u.gal)
height_lid = size_stor[1]

print("The storage volume required to store", time_stor, "of biogas is", vol_stor, "\n" "The height of lid to prevent failure before", time_fail, "is", height_lid)
```

### Conclusions
Based on the outputs of the calculations, it is very possible to utilize a prefabricated container to store biogas produced.  More specifically, an inverted [plastic industrial drum](http://www.thecarycompany.com/containers/drums/plastic) placed on the top of the UASB reactor to capture biogas that is produced.
