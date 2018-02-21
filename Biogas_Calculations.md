## Biogas Calculations

### Introduction
Biogas is a mixture of methane, carbon dioxide, and other trace gases that are produced naturally through anaerobic breakdown of BOD. As waste runs through the UASB reactor, biogas is naturally produced, and rises up through the reactor. Biogas serves as a potential energy source, and if properly stored can be utilized for cooking, heating, or power generation. If biogas is not utilized in this way, it must be burned off with a pilot light or similar apparatus to reduce greenhouse gas emissions.

In order to capture biogas, we aimed to design a simple system that could be implemented in rural areas with small populations, and still provide biogas for home use in a simple and safe way. We also want to minimize any leakages of biogas to the environment, for safety and environmental concerns.


### Biogas Capture Design
The design we settled on utilizes a headspace in the top of the reactor for biogas collection. As biogas is produced in the blanket below, it rises, naturally stirring the tank water. The gas is diverted from the effluent line by small triangular pieces, and makes its way into the headspace, where it builds up over time.

As gas builds up, it is kept in the lid by a hydrodynamic seal with water inside the lid and along the outside of the headspace. The pressure from gas production will continue until an offgas even is initiated. If the pressure is not relieved, the gas buildup will push the water level below the ledge which the lid sits on and cause a failure of the lid.


### Design Parameters
The table below summarizes the parameters we chose for our design, and the reasons they were chosen.  These values are subject to change with future design.

Parameter| Value | Basis of Design
:------------- |:-------------|:--------
Height Reactor| 7 ft | Max allowed to fabricate in lab safely
Diameter Reactor |3 ft | Based on 1 L/s plant design
Height sludge blanket | 3.5 ft| Assumed half height of reactor
Height Headspace | TBD | Based on size calculations and effluent tube placement
Diameter Headspace | TBD| Based on size calculations
COD Load | 200 mg/L | Average value for municipal wastewater (extremely variable)


### Critical Assumptions

In designing the biogas capture, there are many areas of uncertainty that are challenging to characterize before we can collect data from our own reactor.  In order to minimize uncertainty and provide the most accurate calculations, we used a series of assumptions for these areas.  The assumed values, and their justification and sources are detailed in the table below.

Parameter| Value | Justification
:------------- |:-------------|:--------
WW_gen| 3 ml/s | Rule of thumb from Monroe
HRT |4 hrs | Previous lab test and literature review
COD Removal | 70% | Assumed efficiency of reactor in COD breakdown
Maximum Biogas Production | 37.8% | Calculated using stoichiometry (see Spring 2014 UASB report)
Average Biogas Production | 16% | Taken from average output of Aguaclara reactors (see Spring 2014 report)
Minimum Biogas Production | 6% | From lower bound in [Van Lier report](https://courses.edx.org/c4x/DelftX/CTB3365STx/asset/Chap_4_Van_Lier_et_al.pdf)
Max Stove Hours | 0.005 hrs/L Biogas | From biogas usage page on [SSWM](https://www.sswm.info/content/direct-use-biogas)
Min Stove Hours | 0.0022 hrs/L Biogas | From biogas usage page on [SSWM](https://www.sswm.info/content/direct-use-biogas)


```python
from aide_design.play import*
import math

#Assumptions Defined
Diameter = 3 * u.ft
Height = 7 * u.ft
COD_Load_min = 100 * u.mg/u.L
COD_Load_mid = 200 * u.mg/u.L
COD_Load_max = 300 * u.mg/u.L
```

### UASB Size
#### Function
```python
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

### Biogas Calculation
#### Function
```python
#Calculate Biogas Rate of Production (L/s) in UASB
def BiogasProd(Flow, COD_Load):
    COD = Flow * COD_Load
    COD_rem = COD * 0.7 #Assuming x% efficency of COD removal and conversion in reactor
    BGMax = COD_rem * 0.378 *(u.ml/u.mg) #Theoretical Productiom, from Fall 2014 UASB team report
    BGMin = COD_rem * 0.06 *(u.ml/u.mg) #Production using minimum value from Van Lier report
    BGAvg = COD_rem * 0.16 *(u.ml/u.mg) #Production using average value from Spring 2014 tests
    return [BGMax, BGAvg, BGMin]

#Calculate Energy Production from Biogas Produced
def EnergyProduction(Biogas):
    Biogas = Biogas.to(u.L/u.days)
    SM_high = Biogas * 60 * u.min / (200 * u.L) #Hours of stove usage, given maximum efficency of stove
    SM_low = Biogas * 60 * u.min / (450 * u.L)  #Hours of stove usage, given minimum efficency
    #KWH = Biogas / (700 * u.L/u.kwh) #Kilowatt Hours generated from biogas used
    return [SM_high,SM_low]
```

#### Outputs
```python
# Maximum and minimum amount of biogas produced
Biogas = BiogasProd(Flow_design, COD_Load_mid)
BGMax = Biogas[0]
BGAvg = Biogas[1]
BGMin = Biogas[2]
print("Maximum biogas production is", BGMax, "\n" "Average biogas production is", BGAvg, "\n"
      "Minimum biogas production is", BGMin)

# Total amount of stove time based on biogas production
NRGMax = EnergyProduction(BGMax)
NRGAvg = EnergyProduction(BGAvg)
NRGMin = EnergyProduction(BGMin)

print("Total minutes of stove use produced per day are between", NRGMax[0], "and", NRGMax[1], "\n"
      "Total minutes of stove use produced per day are between", NRGAvg[0], "and", NRGAvg[1], "\n"
      "Total minutes of stove use produced per day are between", NRGMin[0], "and", NRGMin[1])
```
