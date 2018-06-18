## UASB Size Calculations
This document can be used to determine the number of people served based on size of UASB design. The reactor will have a 60 $$ $^{\circ}$ $$ sloped bottom for structural integrity, primarily based on the designs of the 1 L/s plant. The reactor will thus have a reduced volume from the two cylindrical hooves that have been removed from housing active granules.

```python
from aide_design.play import*
import math

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
    height_cyl_wedge = height_cyl_hoof - ((centerspace/2) * math.tan(angle))   #Wedge is if the sloped bottom is offset from centerline
    vol_cyl_wedge = height_cyl_wedge * (diam/2)**2 / 3 * ((
        3*math.sin(phi) - 3*phi*math.cos(phi) - math.sin(phi)**3)/(1-math.cos(phi)))
    vol_reactor = (math.pi * (diam / 2)**2 * height / 2) - (2 * vol_cyl_wedge)
    vol_reactor_total =

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

#### Test Calculations
The height of the reactor is limited to 7 feet due to fabrication constraint imposed by the ceiling height of the lab.  The diameter is limited to 3 feet as it is the largest pipe that can be obtained.

```python
UASB = UASBSize(3*u.ft, 7*u.ft)
```
