# Upflow Anaerobic Sludge Blanket (UASB), Spring 2018
#### Zachary Chen, Ian Cullings, Ananya Gangadhar, Jennifer Jackson
#### March 9th, 2018

<div class="alert alert-block alert-danger">
Please do not delete any of my comments. Just address them in the manual and I will check them on the next submission. If you disagree with a comment, then explain why in your own comment below mine.
</div>

## Abstract
The Upflow Anaerobic Sludge Blanket (UASB) team focuses on designing pilot scale UASB systems for primary wastewater treatment in Honduras.  This manual details our complete design process, including each component system of the UASB and how we decided on the final design.  This semester, we have focused on finishing our design process, so that fabrication can take place over Summer 2018.

<div class="alert alert-block alert-danger">
Keep tenses consistent throughout

What does pilot-scale mean?

Maintain formal writing style.
</div>

## Introduction

Direct discharge of human wastewater into the environment causes severe contamination of ground and surface water sources, leading to many adverse effects on the environment and human health.  Biological degradation of organic wastes by aerobic microbes depletes dissolved oxygen within natural water systems, harming aquatic life and creating dead zones.  Discharging wastewater also increases the waterborne fecal matter content, increasing the risk of human exposure to pathogens. [(Chong et. al. 2012)](https://www.sciencedirect.com/science/article/pii/S0043135412002400).  The latter is of particular concern for communities in the Global South, as populations downstream of wastewater outfalls suffer from severely degraded and dangerous drinking water as a result.

<div class="alert alert-block alert-danger">
Try to avoid terms like "Global South." The Global Health fellows advised us that this is more of an outdated term and rather we should refer to areas as communities affected by waterborne illness or communities downstream of other communities' wastes. Global South is also ambiguous.
</div>

Wastewater treatment can also be used for energy production.  Anaerobic digestion of organic matter produces biogas, a mixture of methane and carbon dioxide that can be combusted for energy production.  Recent estimates have shown that wastewater can contain over ten times the amount of energy needed to break it down [(Ghoneim et al., 2016)](http://ieeexplore.ieee.org/abstract/document/7577509/?reload=true).  Most wastewater treatment plants in the US use purely aerobic treatment and thus to not take advantage of this opportunity [(Ghoneim et al., 2016)](http://ieeexplore.ieee.org/abstract/document/7577509/?reload=true).

<div class="alert alert-block alert-danger">
You do not need the first intext citation here. The one at the end of the paragraph encapsulates both sentences.

Revise last sentence.
</div>

Many communities in the Global South lack large scale wastewater treatment infrastructure like that of the United States, leaving much of their waste untreated.  Municipal treatment systems in the United States have long retention times, require large land areas, and have a high fixed cost per capita, making them inaccessible for much of the Global South [(Chong et. al. 2012)](https://www.sciencedirect.com/science/article/pii/S0043135412002400).  Our research and design have been focused on alleviating these problems by creating small-scale wastewater treatment systems, aimed at providing access for smaller rural communities.

<div class="alert alert-block alert-danger">
Great summary of problem and purpose, but consider also including values like sustainability etc.
</div>

Upflow Anaerobic Sludge Blanket (UASB) reactors are used for primary treatment of wastewater by removing suspended solids and reducing organic matter.  UASB reactors use gravity to move water through the reactor, where anaerobic microbes treat the wastewater biologically and produce biogas.  This is a far less energy intensive process than the aerobic treatment incorporated within most large scale wastewater systems in the US, and can produce net energy through the biogas released in the system.

<div class="alert alert-block alert-danger">
Avoid redefining acronyms that you have already defined.
</div>

## Literature Review and Previous Work
Zac Edit - Briefly outline the previous work done by the UASB team up until the Phase I grant, then focus on the design work done last semester.

Discuss what is already known about your research area based on both external work and that of past AguaClara Teams. Connect your objectives with what is already known and explain what additional contribution you intend to make. Make sure to add APA formatted in-text citations. If you mention the author(s) in your sentence, you can simply give the year of publication.[(Logan et. al. 1987)](http://www.jstor.org/stable/pdf/25043431.pdf?acceptTC=true)

<div class="alert alert-block alert-danger">
It seems like this section was forgotten. Remember to read through the report before submitting it so that there aren't errors like this.

This is an important part of this manual because it should summarize how a UASB works and what work AguaClara has done in the past.
</div>

## Design Manual



### UASB Basics

An Upflow Anaerobic Sludge Blanket reactor is a primary wastewater treatment reactor that uses anaerobic biological treatment to treat wastewater.  Water flows into the reactor from the bottom section, and flows upwards at a slow velocity.  This water first passes through the sludge blanket, a collection of methanogenic bacteria that accumulate into small spherical granules, forming a "blanket" of biological material.  As wastewater flows through this biological volume, known as the digestion zone, the bacteria break down organic matter for their metabolic processes.  This reduces both Biochemical Oxygen Demand (BOD) and Total Suspended Solids (TSS) of the wastewater.

<div class="alert alert-block alert-danger">
Where does the wastewater come from and what are the major companonents

Refer to Figure 1

Keep refining the technical writing. Minimize words for clarity and conciseness. Consider "The water first passes" rather than "this water"
</div>

![Conventional_UASB](https://github.com/AguaClara/UASB/blob/master/Images/Conventional_UASB.PNG?raw=true)

<p align="center">Figure One: A Conventional UASB Design </p>

<div class="alert alert-block alert-danger">
I think the convention for labeling figures is to use the number "Figure 1" rather than spell it out.
</div>

A useful by product of this process is biogas, a mixture of methane, carbon dioxide, and some trace gases.  After production in the digestion zone, methane floats upwards through the water and is caught in the cone of the Gas Liquid Solid Separator.  From there, it is funneled upwards into a storage vehicle where it can later be burned for heat or energy generation.  More details on the biogas capture and usage can be found in the [Biogas Capture](#Biogas-Capture-System) section of the manual.

<div class="alert alert-block alert-danger">
Consider naming the process instead of referring to "this process" in the first sentence.

</div>

After water runs through the digestion zone, it rises to the setting zone.  Here, excess solids that escaped the digestion zone are deflected downwards back to the sludge blanket.  Clarified wastewater leaves through an effluent line and is taken to further treatment systems.

<div class="alert alert-block alert-danger">
Consider a diagram that labels where the digestion and setting zones are.
</div>

![Front_View](https://github.com/AguaClara/UASB/blob/master/Images/AC_FrontView.PNG?raw=true)

![Side_View](https://github.com/AguaClara/UASB/blob/master/Images/AC_SideView.PNG?raw=true)

<div class="alert alert-block alert-danger">
Label these figures and add captions to make these meaningful. Also,refer to them in your text sections so that the reader knows when to look at them.
</div>

The AguaClara design deviates from the standard design in a number of way.  First is the scale of the system.  Most UASB reactors used in domestic or industrial settings are much larger than our pilot scale system, and handle much larger organic loads.  While the given principles will still hold, we are working on a fundamentally different scale from previous UASB reactors.

<div class="alert alert-block alert-danger">
Please give general differences in size and capacity
</div>

Another change from previous UASB systems is the addition of a sludge weir system.  This sludge weir is a downward angled tube connected to the reactor, connected at the interface between the digestion and settling zones.  This tube can be emptied with a valve when necessary.  This sludge weir will be an important feature for the testing process, as it will allow direct samples of the sludge blanket to be taken.  Functionally, it will also allow us to control the height of the sludge blanket and remove excess material if necessary. More details are in the [Sludge Sampling Section](#Sludge-Sampling-and-Removal-System).

<div class="alert alert-block alert-danger">
You refer to this section but nothing has been written, does that mean that you haven't gotten that far yet?
</div>

### Size and Flow Calculations
One of the most important parts of the UASB design in the size and dimensions of the reactor.  These dimensions, along with the flow rate, determine a number of important parameters including the Hydraulic Residence Time (HRT) and Upflow Velocity.  Given that we are aiming for a small scale system, which we can build within a laboratory setting, we decided upon the following constraints on our design:

Parameter| Value | Justification
:------------- |:-------------|:--------
Height | 7 ft| Max height within fabrication Headspace
Diameter  | 3 ft  | Dimensions of pipe used for fabrication
Hydraulic Residence Time | 4 hrs | Previous lab tests and literature review
Wastewater Generated Per Person| 3 ml/s | Rule of thumb used in AguaClara design  |   |

<div class="alert alert-block alert-danger">
Great!
</div>

To ensure the stability and safety of the reactor, given that it will be holding a large volume of water, we also need to design a stabilizing "valley" in the bottom of the tank.  This reduces the overall volume of the reactor, and is incorporated into our volume calculations below.

<div class="alert alert-block alert-danger">
How does the valley stabilize the reactor?
</div>

Volume and flow calculations:
```python
from aide_design.play import*
import math

def UASBSize(diam, height):
    """Takes the inputs of diameter and height. The bottom of the UASB is sloped at 60 degrees with a 3 inch space across the bottom of the UASB. Assumes that half the reactor contains the settled bed, which is used for the HRT. Returns five outputs: 1. height of the sloped sides of the bottom geometry, 2. volume of sludge in the reactor, 3. flow rate, 4. number of people served with graywater, 5. number of people served with blackwater.
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
    upflow_vel = flow / (math.pi*(diam/2)^2) #Velocity of water flowing up through reactor = Q/A

    output = [height_cyl_wedge.to(u.m), vol_reactor.to(u.L), upflow_vel.to(u.m/u.hr), flow.to(u.L/u.s), people_served, people_served_BW]

    print("The height of the bottom geometry is",height_cyl_wedge.to(u.m))
    print('The volume of the sludge in the reactor is', vol_reactor.to(u.L))
    print('The flow rate into the reactor is', flow.to(u.L/u.s))
    print('The number of people served by this reactor is', people_served)
    print('The number of people served by this reactor if only blackwater is treated is', people_served_BW)
    return output

```

<div class="alert alert-block alert-danger">
Define grey water/black water earlier in manual.

WW_gen_bw explanation is confusing

What tests have been done to set a HRT? This might be good to add in the lit review and previous work
</div>

Given our proposed design where:
* Diameter = 3 feet
* Height = 7 feet

```python
UASB = UASBSize(3 * u.ft, 7 * u.ft)
```

<div class="alert alert-block alert-danger">
What do the values that you just got mean? How will they lead into the next step?
</div>

### Biogas Capture System



### Sludge Sampling and Removal System

### Effluent Flow System

### Other Considerations

## Future Work
Describe your plan of action for the next several weeks of research. Detail the next steps for this team. How can AguaClara use what you discovered for future projects? Your suggestions for challenges for future teams are most welcome. Should research in this area continue?

<div class="alert alert-block alert-danger">
Why no future work included here?

Have you thought about constructability of the system? Looked at fabrication techniques?

Will this be similar to the 1 L/s system?

Is this a comprehensive summary of all the relevant design parameters and work done this semester?
</div>

## Bibliography
Chong, S., Sen, T. K., Kayaalp, A., and Ang, H. M. (2012). The performance enhancements of upflow anaerobic sludge blanket (UASB) reactors for domestic sludge treatment - A State-of-the-art review. Water Research, 46(11):3434-
3470.

Ghoneim, W. A. M., Helal, A. A., and Wahab, M. G. A. (2016). Renewable energy resources and recovery opportunities in wastewater treatment plants. In 2016 3rd International Conference on Renewable Energies for Developing
Countries (REDEC), pages 1-8.
