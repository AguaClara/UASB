
# Upflow Anaerobic Sludge Blanket, Spring 2018
#### Zac Chen, Jennifer Jackson, Ian Cullings, and Ananya Gangadhar
#### March 9, 2018

## Abstract
Briefly summarize your previous work, goals and objectives, what you have accomplished, and future work. (100 words max)

## Introduction
Explain how the completion of your challenge will affect AguaClara and the mission of providing safe drinking water (or sustainable wastewater treatment!). If this is a continuing team, how will your contribution build upon previous research? What needs to be further discovered or defined? If this is a new team, what prompted the inclusion of this team?

## Literature Review and Previous Work
Discuss what is already known about your research area based on both external work and that of past AguaClara Teams. Connect your objectives with what is already known and explain what additional contribution you intend to make. Make sure to add APA formatted in-text citations. If you mention the author(s) in your sentence, you can simply give the year of publication.[(Logan et. al. 1987)](http://www.jstor.org/stable/pdf/25043431.pdf?acceptTC=true)


## Design Process

### Size and Flow
*Introduce the background for the particular set of calculation/code*

This document can be used to determine the number of people served based on size of UASB design. The reactor will have a 60 $$ $^{\circ}$ $$ sloped bottom for structural integrity, primarily based on the designs of the 1 L/s plant. The reactor will thus have a reduced volume from the two cylindrical hooves that have been removed from housing active granules.
#### Design Parameters
*Place a table here with the design parameter, the value for it, and the justification with a hyperlink, kinda like this*

| Design Parameter | Value | Justification of Parameter |
| :----------------: | :-----: | :-------------: |
| Hydraulic Residence Time ```HRT```| 4 hrs | From tracer tests conducted in Fall 2016 and minimum values in literature |
| Wastewater Generation per Person ```WW_gen``` | 3 mL/s | Rule of Thumb from Monroe  |
| Percent of Mixed Water that is Blackwater  | 20%  | From Prof. Richardson's Estimations  |
| Center Space of Base  | 3 in  | Based on the [1 L/s plant design](https://www.overleaf.com/6186375zdpjfc) (more info in their Google Drive)  |
| Slope Angle  | 60 $$ $^{\circ}$ $$ | Based on the [1 L/s plant design](https://www.overleaf.com/6186375zdpjfc)  |
#### Code

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

UASB = UASBSize(3*u.ft, 7*u.ft)
````

### Influent Flow System

### Biogas Capture System

### Sludge Sampling and Removal System

### Effluent Flow System

### Other Considerations



## Future Work
Describe your plan of action for the next several weeks of research. Detail the next steps for this team. How can AguaClara use what you discovered for future projects? Your suggestions for challenges for future teams are most welcome. Should research in this area continue?

## Bibliography
Logan, B. E., Hermanowicz, S. W., & Parker,A. S. (1987). A Fundamental Model for Trickling Filter Process Design. Journal (Water Pollution Control Federation), 59(12), 1029–1042.
