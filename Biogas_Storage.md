## Biogas Storage
Following the proposed designs of the EPA P3 Phase I UASB proposal, the team has explored the idea of a removable biogas capture lid.  This concept, however, was flawed in its designs for the following reasons:

1. It is difficult to maintain a hydrostatic seal unless the lid is incredibly tall (i.e. storage volume is very large) as shown by the Spring 2017 [Final Report](https://www.overleaf.com/8107719xzjdzswjvtyj#/28623295/)
2. The height of the lid becomes a major design problem in a small scale system with a consolidated reactor and storage lid system as is constrains the location and placement of other components such as the tube settler arm.
3. Biogas buildup in a fixed lid system displaces water volume in the reactor which cannot be easily restored once biogas is used or released

For these reasons, the team is proposing a floating gas holder system that is detached from the reactor system. These have been widely implemented in [short term gas storage](http://www.susana.org/_resources/documents/default/2-1799-biogasplants.pdf) While this is a necessary step on the small scale, it is not necessarily the case for larger UASB reactors.

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
def BiogasProd(Q, COD_Load, Temp):
    COD_rem = COD_Load * 0.7 #Assuming x% efficency of COD removal and conversion in reactor
    COD_CH4 = (Q * COD_rem) - (Y_obs * Q * COD_Load) #Remember to define the variables further up
    T = Temp.to(u.degK)
    P = 1 * u.atm
    K_COD = 64 * (u.g / u.mol)
    R = 0.08206 * ((u.atm * u.L) / (u.mol * u.degK))
    K = 

    BGMax = COD_rem * 0.378 *(u.ml/u.mg) #Theoretical Productiom, from Fall 2014 UASB team report
    BGMin = COD_rem * 0.06 *(u.ml/u.mg) #Production using minimum value from Van Lier report
    BGAvg = COD_rem * 0.16 *(u.ml/u.mg) #Production using average value from Spring 2014 tests
    return [BGMax, BGAvg, BGMin]
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
```
