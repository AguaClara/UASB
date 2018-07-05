 
# Upflow Anaerobic Sludge Blanket (UASB) Design Manual


#### Spring 2018:
Zac Chen, Jennifer Jackson, Ian Cullings, and Ananya Gangadhar
#### Summer 2018:
Ian Cullings, Isa Kaminsky, Ananya Gangadhar


## Abstract
Since Spring 2017, the AguaClara Upflow Anaerobic Sludge Blanket (UASB) Team has been working on a detailed design of modified, pilot-scale UASB reactor originally proposed in an EPA P3 proposal. A UASB reactor treats wastewater anaerobically and produces biogas as a by-product. Working towards that goal, the team has created Python code to record the design process and calculations for this AguaClara UASB. This document serves as a master guide for the design process.

## Introduction

The contamination of ground and surface water sources by wastewater has adverse environmental and health affects. Biological degradation of wastewater by aerobic microbes lowers the dissolved oxygen content in natural waterways, preventing aquatic life from thriving and potentially creating dead zones. Additionally, it increases waterborne fecal matter content and increases the risk of exposure to pathogens ([Chong et. al, 2012](https://www.sciencedirect.com/science/article/pii/S0043135412002400?via%3Dihub)). The latter is of particular concern to rural communities without drinking water treatment, who may live downstream of wastewater outfalls.

Wastewater can also be an opportunity for energy recovery. According to recent estimates, the energy potential of wastewater and biosolids is more than ten times the energy needed for treatment. Most wastewater treatment facilities in the US do not optimize the recovery of energy and resources from biosolids ([Ghoneim et. al,  2016](http://ieeexplore.ieee.org/document/7577509/?reload=true)). While it is important to develop wastewater treatment technology to optimize current wastewater treatment for all individuals, the focus of this research was on small rural communities lacking water treatment systems.

Currently in the United States, effective municipal wastewater treatment facilities have long retention times, require large land areas, and have a high fixed cost per capita. Due to economy of scales, small systems have even higher fixed costs per capita and these high fixed costs make conventional wastewater treatment systems inaccessible for small communities. Many communities across the world forgo wastewater treatment altogether due to the high cost and instead discharge untreated wastewater to the environment ([Chong et. al, 2012](https://www.sciencedirect.com/science/article/pii/S0043135412002400?via%3Dihub)). Research and development of small-scale and decentralized wastewater treatment methods should be prioritized in order to make wastewater treatment accessible for all communities.

UASB reactors, used as a preliminary wastewater treatment process, clarify wastewater by removing suspended solids organic matter ([Chong et. al, 2012](https://www.sciencedirect.com/science/article/pii/S0043135412002400?via%3Dihub)). UASB reactors rely on gravity to clarify wastewater and biological processes to remove organic matter and convert it to biogas. They are less energy intensive than other forms of preliminary wastewater treatment that use aerobic processes. UASB reactors also produce methane as a by-product of anaerobic digestion.  This methane can be captured and burned for energy production or heating.

<!--- how we modified UASBs --->
In January 2017, a novel pilot scale UASB reactor design was created by AguaClara for the EPA People, Prosperity and the Planet (P3) [Student Design Competition proposal](https://docs.google.com/document/d/1geug1EyFjCRLQgO79vTOXUUFia3RBw3bhaIHPUiqu44/edit?usp=sharing). This reactor was designed to improve the accessibility of wastewater treatment for small communities. The proposed UASB reactor design identified areas to improve conventional reactor design, making the system cheaper and easier to fabricate and implement globally.  Later sections of this manual detail these changes and quantify their impact on the design.

Since submission of this proposal, there has been ongoing work to develop the final design of the reactor.  This document details the full design process, and is written to serve as a manual for the full UASB design.  As the design is completed, additional information will be added detailing a full fabrication plan for the reactor.

## Literature Review and Previous Work

### Conventional Wastewater Treatment Options
Municipal and industrial wastewater can be treated via biological, chemical, or thermal oxidation treatment processes. While all processes lead to the eventual breakdown of organic matter, biological treatment is more commonly used because the latter two treatment options require higher capital investment and operational costs due to the need of complex, and chemicals or energy inputs ([Mittal et. al, 2011](http://www.watertoday.org/Article%20Archieve/Aquatech%2012.pdf)). The two main types of biological treatment are the activated sludge process and anaerobic digestion. When compared to the activated sludge process, anaerobic digestion yields less sludge and reduces energy input ([Mittal et. al, 2011](http://www.watertoday.org/Article%20Archieve/Aquatech%2012.pdf)). Although there are some drawbacks to anaerobic digestion such as long solids retention time (SRT) and insufficient nutrient removal, the reduced energy input renders it the most feasible technology for small communities lacking proper water treatment  ([Chong et. al, 2012](https://www.sciencedirect.com/science/article/pii/S0043135412002400?via%3Dihub)).

### UASB Basics

![Conventional_UASB](/Images/Conventional_UASB.PNG)
<p align="center">Figure 1: A conventional UASB design.  Wastewater is pumped through the bottom of the reactor and flows upwards through the reactor.  Contact with sludge in the bed and blanket allows anaerobic organisms to break down organic matter, cleaning the wastewater.  This process  produces biogas, which rises up through the reactor and is collected in a funnel structure for eventual use. </p>

UASBs utilize mixed cultures of anaerobic microorganisms to biologically process and remove organic matter (OM), chemical oxygen demand (COD), biological oxygen demand (BOD), and suspended solids (SS).  They are designed to operate at short hydraulic retention times (HRT) and long solids retention time (SRT) to increase loading capacity and improve sludge stabilization.  Due to the dispersion of influent to maximize sludge contact as shown in Figure 1, UASBs can achieve optimal levels of primary treatment quite quickly compared to other anaerobic treatment processes.  In alternative processes such as anaerobic filters, anaerobic baffled reactors, and septic tanks, water passes over an exposed surface of sludge and organic matter is treated as it diffuses through ([Chong et. al, 2012](https://www.sciencedirect.com/science/article/pii/S0043135412002400?via%3Dihub)).

A by-product of anaerobic digestion within the reactor is biogas, a mixture of methane, carbon dioxide, and some trace gases.  After production in the digestion zone, methane travels upwards through the water and is caught in the cone of the Gas-Liquid-Solid Separator (GLSS).  From there, it is funneled upwards into a storage vehicle where it can later be burned for heat or energy generation.  More details on the biogas capture and usage can be found in the [Biogas Capture](#Biogas-Capture-System) section of the manual.

While UASBs are able to provide treatment quickly, like other anaerobic treatment methods, post-treatment is often required through trickling filters or secondary clarifiers to achieve ideal reduction BOD, COD, and nutrients ([Abbasi et. al, 2012](https://www.sciencedirect.com/science/article/pii/S1364032111005533)).

Typically, UASB reactors are large,  cylindrical or rectangular tanks 4-5 meters in height, constructed of reinforced concrete designed as shown to Figure 1.  While UASBs are traditionally used for large-scale, centralized wastewater treatment, their mechanism of treatment is operationally simple since there are no mechanized components which eases maintenance concerns.  In addition, the standard geometry readily allows for scaling of the design ([Van Lier et al., 2010](https://courses.edx.org/c4x/DelftX/CTB3365STx/asset/Chap_4_Van_Lier_et_al.pdf)).  Although fixed costs for the construction can still be significant, they can be reduced through use of alternative materials such as PVC.

Due to the higher operational capacity,  opportunity for resource recovery in biogas production, and overall simplicity of the system, UASB reactors were chosen as the basis for preliminary wastewater treatment for underserved and under-resourced communities.

### Problems Associated with UASBs

#### Biogas Escape
Conventional UASB reactors utilize an inverted funnel, known as a Gas-Liquid-Solid Separator (GLSS), to collect biogas as it is produced ([Narnoli et. al, 1997](https://www.sciencedirect.com/science/article/pii/S0043135497809876)). The design of the GLSS, however, is not gas-tight due to the free surface on the perimeter of the gas separator system as shown in Figure 1.  Gas that is able to travel around the edges of the GLSS can readily escape from the system.  Since methane is a potent greenhouse gas, all biogas should be captured to reduce negative environmental impacts ([Chong et. al, 2012](https://www.sciencedirect.com/science/article/pii/S0043135412002400?via%3Dihub)).

#### Solids Retention
To successfully process organic waste, UASB reactors heavily rely on the accumulation, concentration, and conglomeration of a large population of bacteria in order to form diverse microbial community known as granules.  Proper granulation and retention of these granules in a reactor is imperative to maximize the removal of COD and BOD and increase the overall effectiveness of UASB technologies ([Subramanyam et. al 2013](https://www.liebertpub.com/doi/abs/10.1089/ees.2012.0347)).  To prevent biomass escape and increase sludge retention, a tube settler is used for the effluent line.  Parallel plates within the tube settler also increase solids retention ([Chong et. al, 2012](https://www.sciencedirect.com/science/article/pii/S0043135412002400?via%3Dihub)).

#### Fats Buildup
Differences in density can cause surface buildup of fats, oils and grease (FOG) in the inactive sludge. The FOG can accumulate at the water surface open to the atmosphere, forming a thick layer of solid material which can be labor intensive to clean ([Van Lier et al.,  2010](https://courses.edx.org/c4x/DelftX/CTB3365STx/asset/Chap_4_Van_Lier_et_al.pdf), [Lettinga 1991](http://wst.iwaponline.com/content/24/8/87)). For UASB systems with an exit weir systems, this material can escape through these systems, polluting the effluent.  

## Methods and Design Process

### Overview of Proposed UASB and Methods
A schematic of the UASB with proposed design improvements is shown in Figure 2 and Figure 3.  The following sections give an overview of the component/aspect of interest, the design parameters associated with this component, and the code used to calculate the final parameters.  Work is ongoing on differing aspects of the design, but this manual represents the most up to date versions of the designs.

<div style="text-align:center">

![UASB_Side](/Images/AC_SideView.PNG)

<p align="center">Figure 2: The Side View of the proposed UASB </p>

</div>

<div style="text-align:center">

![UASB_Side](/Images/AC_FrontView.PNG)

</div>


<p align="center">Figure 3: The Front View of the proposed UASB with sloped bottom geometry.</p>

### Degritting System

### Size and Flow

The scale and dimensions of the pilot UASB reactor were loosely based on the size and scale of the 1  L/s sedimentation tank, using experience gained from fabrication. With the goal of constructing the reactor utilizing a 3 foot diameter PVC pipe and welded PVC sheets for the base, one of the primary concerns was structural stability.  While it was desirable to have a flat bottom geometry to maximize volume for biological processing, shear stress at the interface between the welded PVC sheets and pipe would lead to the rupture the bottom of the reactor.  Due to the complexities and time requirements required to determine the feasibility of this approach,  the team opted to model the bottom geometry for the pilot scale UASB reactor on that of the 1 L/s sedimentation tank since the UASB would also utilize a 3 foot diameter corrugated pipe that would support approximately a 7 foot tall column of water.  In following these designs, the pilot scale UASB reactor will also have a 60 $$ $^{\circ}$ $$ sloped bottom like the 1 L/s sedimentation tank as shown in Figure 3 and Figure 4.  More information on geometry and structure of the 1 L/s sedimentation tank can be found on the Fall 2016 1 L/s Final Report ([Herrara et al., 2016](https://www.overleaf.com/6186375zdpjfc#/20717591/)).
<div style="text-align:center">

 ![1LPS](https://github.com/AguaClara/UASB/blob/master/Images/1lps_plant.PNG?raw=true)

 </div>

 <p align="center">Figure 4: Schmematic of the 1 L/s sedimentation tank (Source: Herrara et al., 2016)</p>

This, however, will create a unique geometry and thus reduce the volume of reactor.  The following design parameters will serve to calculate the volume of the pilot scale UASB reactor and the flow rate through system.  It also must be noted that hydraulic residence time is based on contact time with the sludge to account for the amount of time raw wastewater spends being biologically treated rather than time in the whole reactor volume.


#### Design Parameters

Table 1: Design parameters for the size and flow calculations for the proposed UASB reactor.

|                 Design Parameter                 |        Value        |                                                                                                              Basis of Design                                                                                                               |
|:------------------------------------------------:|:-------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|        Hydraulic Residence Time ```HRT```        |        4 hrs        | From tracer tests conducted in [Fall 2016](https://www.overleaf.com/read/dnxfsrwdxbdf#/21165144/) and minimum values in literature ([Chong et. al, 2012](https://www.sciencedirect.com/science/article/pii/S0043135412002400?via%3Dihub)). |
|  Wastewater Generation per Person ```WW_gen```   |       3 mL/s        |                                                                                                         Rule of Thumb from Monroe                                                                                                          |
| Blackwater Generation per person ```WW_gen_bw``` |      0.6 mL/s       |                                                      Prof. Richardson's approximation for blackwater generation (based on idea that 20% of volume of mixed wastewater is blackwater)                                                       |
|               Center Space of Base               |        3 in         |                Based on semi-circle between the two sloped plates on the bottom of the [1 L/s plant design](https://www.overleaf.com/6186375zdpjfc) sedimentation tank shown in Figure 4 (more info in their Google Drive)                 |
|            Slope Angle of Base Plates            | 60 $$ $^{\circ}$ $$ |                                                    Based on the sloped plates used in the bottom of the [1 L/s plant design](https://www.overleaf.com/6186375zdpjfc) sedimentation tank                                                    |
|               Diameter of Reactor                |       3 feet        |                                                                             Based on size of corrugated pipe used for the body of the 1 L/s sedimentation tank                                                                             |
|              Height of the Reactor               |       7 feet        |                                                                                               Based on the maximum ceiling height of the lab                                                                                               |


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

    >>> from aide_design.play import*
    >>> import math
    >>> UASBSize(3 * u.ft, 7 * u.ft)
    The height of the bottom geometry is 0.7259 meter
    The volume of the sludge in the reactor is 520.8 liter
    The flow rate of the reactor is 0.03617 liter / second
    The number of people served by this reactor is 12
    The number of people served by this reactor if only blackwater is treated is 60
    [<Quantity(0.7259024934521162, 'meter')>, <Quantity(520.8127904536798, 'liter')>, <Quantity(0.036167554892616645, 'liter / second')>, 12, 60]
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
    vol_reactor = (math.pi * (diam / 2)**2 * height) - (2 * vol_cyl_wedge)
    vol_sludge = (math.pi * (diam / 2)**2 * height * 0.7) - (2 * vol_cyl_wedge)

    flow = vol_reactor / HRT
    people_served = int(flow / WW_gen)       #People served per reactor
    people_served_BW = int(flow / WW_gen_bw) #People served per reactor treating only blackwater

    output = [height_cyl_wedge.to(u.m), vol_reactor.to(u.L), flow.to(u.L/u.s), people_served, people_served_BW]

    print("The height of the bottom geometry is",height_cyl_wedge.to(u.m))
    print("The volume of the reactor is",vol_reactor.to(u.L))
    print('The volume of the sludge in the reactor is', vol_sludge.to(u.L))
    print('The average flow rate of the reactor is', flow.to(u.L/u.s))
    print('The number of people served by this reactor is', people_served)
    print('The number of people served by this reactor if only blackwater is treated is', people_served_BW)

    return output

import doctest
doctest.testmod(verbose=True)

Diameter = 3 * u.ft
Height = 7 * u.ft
UASB_design = UASBSize(Diameter, Height)
print(UASB_design)

```


### Influent Flow System
An ideal influent flow system is designed to prevent clogging and to ensure an even distribution of flow throughout the reactor.  A literature review was conducted to compare the various values for reactor design parameters. Table 2 includes relevant values, but is not an exhaustive list of our sources

One challenge for an influent flow system is combating pipe blockages. This involves the creation of a trash rack and grit capture mechanism, calculating the optimal pipe diameter, and possibly including a nozzle or aperture at the end of the pipe to ensure high velocity flows to prevent deposition of solids.

Top influent flow was chosen over bottom influent flow in order to decrease the frequency of clogs.  Bottom influent flow systems are more likely to clog if flow is low or not consistent.  This is because non-suspended particles may settle into the pipe.  Gravity will prevent particles in a top influent system from settling in the pipe. In addition, top influent flow is the most common choice for domestic wastewater treatment.

A literature review reveals a lack of knowledge in the UASB community on the area in the reactor served by each influent pipe, or the influence area. Values range from 1-4 $m^2$ (see table below) with little experimental evidence.  The idea is to have enough pipes so that the summed influence areas of the pipes is greater than the area of the bottom of the reactor.  Since the bottom of the proposed AguaClara reactor is less than 1 $m^2$, the total reactor area can be covered with the influence area of at least one influent pipe.  Two influent pipes are being considered, as they allow for better clog detection and prevention.

<div style="text-align:center">

![Slanted Straight Pipes Influent](/Images/rigid_slanted_infl_pipes.PNG)

</div>

<p align="center">Figure 5: Schematic of a top-influent 2 pipe system.  Flexible tubing is being considered over rigid PVC for ease of construction.  The flexible tubing would be held in place at the bottom of the reactor. </p>

<p align="center">
Table 2: Literature values for parameters associated with influent control system in traditional UASB reactors. </p>

| Parameter     | [Anaerobic Reactors Textbook](https://drive.google.com/drive/folders/1yP48lb38n-ZQb5PtMfpcJs9RIu4wKJ1f) | [Wastewater Treatment for Pollution Control and Reuse 3rd ed](http://accessengineeringlibrary.com/browse/wastewater-treatment-for-pollution-control-and-reuse-third-edition/c9780070620995ch07#c9780070620995ch07lev1sec01) | [Van Lier: Anaerobic Sewage Treatment using UASB Reactors](https://courses.edx.org/c4x/DelftX/CTB3365STx/asset/Chap_4_Van_Lier_et_al.pdf) |
|:--------------------------------------------------------------------------------- |:------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **Descending Sewage Velocity**                                                    | **$\leq$0.2 m/s**                                                                                       |                                                                                                                                                                                                                             |                                                                                                                                           |    
| **Diameter of pipe**                                                              | **75-100 mm** (from practical experience)                                                               |                                                                                                                                                                                                                             | **100 mm** (to allow gas bubbles to rise)                                                                                               
| **Nozzle Diameter**                                                               | **40-50 mm** (from practical experience)                                                               |                                                           |                                                                                                                                           |    
| **Exit Velocity**    | **$\geq$0.40 m/s**   |     | **over 0.3 m/s**  |    
|**Apertures**  | **2 openings with 25mm × 40mm cross section** | See Aperture Design Problem 7.12.1.6   | Single outlet point per pipe (for identification of clogs)   |
| **Influence Area**                                                                | **2.0-3.0 $m^2$ for COD 400-600 mg/L**                                                                  | **1 point per 3.7-4.0 $m^2$ floor area**                                                                                                                                                                                    | **1-4 $m^2$ per feed point**                                                                                                              |    
| **Settling Zone Surface**                                                         |                                                                                                         |                                                                                                                                                                                                                             | **75% of total surface**                                                                                                                  |    
| **Distance Between Exit Mouth and Water Level in Settler/ Headloss through unit** |    **0.20-0.30 m**                                                                                                     |               **2-3 m head loss** through unit for gravity feed with distribution from top of UASB through splitter boxes and weirs to divide and regulate the feed to each inlet channel and then to downtake pipe. Also see Example 7.2 | **50 cm**

It has been decided that from the following parameters an exit velocity of 0.3 m/s (Van Lier et al., 2010) will likely be used.

#### Influent Flow Calculations

Below are calculations used to determine the influence area of each pipe given the diameter and number of pipes.

```python
# function calculates the influence area of each pipe in the reactor
def influence_area(n_pipes, diam):
  ## n_pipes = number of influent pipes in UASB
  ## diam = diameter of UASB reactor
  ca = pc.area_circle(diam) # ca = cross sectional area at top
  ia = ca/n_pipes           # ia = influence area
  print('The influence area of each pipe is ', ia)
  return ia

  num_pipes = 2
  infl_area_UASBpipe = influence_area(num_pipes, diam_UASB)
  print('The influence area of each pipe is ', infl_area_UASBpipe)

```
#### Pulse Flow into the Reactor
Initial calculations showed that the flow into the reactor will be too small for a continuous flow system. An extremely small pipe would have been necessary to create the desired exit velocity from a continuous flow of 0.03 L/s.  A pulse-flow system will be explored instead, as suggested by Ed Gottlieb, the Industrial Pretreatment Coordinator at the Ithaca Area Wastewater Treatment Facility, in a meeting on April 11, 2018.  The basic idea is that a holding tank will accumulate wastewater until a certain amount is reached, releasing the water as a pulse into the reactor.  These incremental flows will be small compared to the overall height of the sludge bed.  This will achieve a much higher flow, allowing larger pipes to be used, and a higher exit velocity to be achieved.  Larger pipes are necessary to prevent clogging.  Two systems have been proposed for achieving pulse flow: a tipping bucket system, and a siphon.  The designs will be constructed as full-scale bench top tests to be performed over the summer, so that each can be compared.  The three proposed options are explored below.

#### Pulse Flow: Tipping bucket
![Tipping Bucket Design 1](/Images/Tipping_Bucket_Drawing_1.png)
<p align="center">Figure 6: A conceptual illustration of the dual tipping bucket design, created from PVC elbows.  As one bucket tips, the other fills up.  </p>

The inspiration for the tipping bucket design came from Ed Gottlieb, who referenced [tipping bucket systems ](https://www.youtube.com/watch?v=WdxXrvV6Lqo) that can be found in waterparks.  After discussion, the a new design was developed that inspired by rain gauges.  A demonstration of how it works can be seen [here](https://www.youtube.com/watch?v=qzKWzTe7CEg).  While the rain gauge continuously dumps water, this system would hold the wastewater until it contains enough water to deliver an adequate pulse flow.  It then dumps the water into funnels that connect to the influent pipes to the reactor.  This alternating, two-way design was chosen over a single tipping bucket for a number of reasons.  

So far, the current design solves the problems of flow splitting and deposition of solids due to incomplete tipping of bucket.  The benefit of the 2-bucket design is that no splitting of flow is needed, since each tip of the bucket will alternate flow between the two influent pipes. The main challenge with this design is that it does not allow for more than 2 influent pipes, and thus makes scaling up a significant issue.  Deposition of solids in the buckets is solved by using curved bottoms, allowing the buckets to tip completely, and eliminating a corner in which solids could settle. The design involves precise cutting of 4-6 inch diameter elbows.  2 design ideas are being considered - the plan is to test both at the same time in order to compare.  The pivot would be created by 2 pieces of flat PVC glued to the sides of the elbows, with a rod through them.  

Design values still need to be determined for the volume of the buckets, the funnel, and the pipes.  The bucket volume determines how often the bucket will tip, and how big the pulse to the reactor will be.  Tipping will ideally be minimized, since the more the bucket tips, the faster parts will wear down and need to be replaced.  The volume should not be too large, or particles may have a chance to settle while they are in the bucket.  Initial calculations are being done to determine how large of a pulse flow will be needed.  

#### Pulse Flow: Siphon
![Siphon](/Images/Siphon.PNG)
<p align="center">Figure 7: Proposed design for a siphon as a means to deliver pulse flow to the reactor. </p>

An alternate system of delivering pulse flow, as proposed by Professor Weber-Shirk, is through a siphon.  The proposed design involves a holding tank that drains from the bottom, and is siphoned off into a flow splitter box once a certain volume in the tank is reached.  Dr. Weber-Shirk suggests a 12 mm pipe would be sufficient for siphoning, as long as the siphon is preceded by at least 6 mm screens, which is the proposed screen size for the UASB reactor.  The IAWWTF uses 6 mm screens.  The main benefits of this design are that it includes no moving parts and can be scaled for larger reactors.  

The main challenges to this design include geometry, clogging, and flow division.  The current proposed geometry is U-bends, which prevent settling better than horizontal pipes.  Clogging may be a major issue with this design.  Monroe suggests at least 10 cm of head for the siphon to work, while literature suggests about 50 cm to prevent clogs.  Furthermore, it will be difficult to test the clogging issue in the lab, as testing with wastewater is infeasible.  Professor Richardson has suggested various wastewater "recipes" which may be useful for laboratory testing.  A flow splitting box/funnel was also proposed by Dr. Weber-Shirk and is illustrated above.  The design involves a box with a funnel-shaped opening to catch water from the siphon.  The box has a divider in the middle that separates the openings to two influent pipes.  The box will split the flow evenly between the two pipes as long as the volume of the pulse from the siphon reaches above the divider.  The design also notifies operators to a clog in an influent pipe, as the water on that side of the divider will not drain.  Initial calculations for the siphon design are underway.  Important values to consider are:  volume of WW held in the tank & siphon, which is equal to the volume that will dump into the flow splitter box; headloss between the flow splitter and the influent pipe discharge; diameters of the influent pipes; and required upflow velocity in the reactor.

#### Influent System Design

Over the Summer of 2018, the UASB team worked on designing these systems in preparation for fabrication for the fall.  This process began with determining the critical design parameters that constrained the design, which are summarized in table X below.  


<p align="center">Table X: Design parameters for UASB hydraulics </p>

| Parameter      | Value | Constrained? | Justification |
|:-------------- |:----- | ------------ | ------------- |
| Reactor Volume | 1221 Liters | Yes  | Based on max diameter and height to allow fabrication |
| Sludge Volume  | ~850 Liters | No | Roughly 70% of Reactor Volume.  Needs to be better constrained based on location of tube settler. |
| HRT | $\geq$ 4hrs | Yes, minimum  | Based on literature and lab scale test.  | |
| Average Flow Rate   | $\leq$ 0.08 L/s  | Yes, Maximum | Q = Volume / Hydraulic Residence Time  |
| Minimum Exit Velocity   | $\geq$ 0.03 m/s   | Yes | Minimum velocity needed to scour settling particles |    
| Maximum Exit Velocity | $\leq$ 1 m/s | No | Max velocity needed to prevent preferential pathways through sludge blanket.  Still very undetermined. |  
| Influent Pipe Inner Diameter | 75 - 100mm  | No | Based on literature values to prevent clogging in pipes.  Some flexibility. |
| Influent Pipe Length | ~8.5 feet | Yes| Roughly equal to height of reactor plus half of diameter (see influent pipe geometry) |

Initially, design included another design parameter, descending sewage velocity.  This value was constrained below 0.2 m/s the average rising velocity of air bubbles, in order to prevent these air bubbles brought in from the pulse flow from entering the reactor ([Anaerobic Reactors, 2007](https://drive.google.com/drive/folders/1yP48lb38n-ZQb5PtMfpcJs9RIu4wKJ1f)).  However, design of a large influent tank where the pulse flow enters, where the descending velocity would be much lower than 0.2 m/s, solves this problems without constraining pipe diameter or hydraulic head.  

Given these input parameters, we can solve for the headloss necessary to achieve desired flow using the following code:

#### Code

```python
# Calculates headloss in influent system based on dimensions of reactor

# Import required functions
from aide_design.play import*
import math

# Calculate size and flow dimensions
height = 7 * u.ft
diam = 3 * u.ft
UASB_design = UASBSize(diam, height)
vol = UASB_design[1]
min_HRT = 4 * u.hr
Q_avg = vol / min_HRT
print(Q_avg.to(u.L/u.s))

#Determine pipe inner diameter based on nominal diameter
nom_diam = 3  * u.inch
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

# Given volume of tipping bucket, determine time to fill bucket

dump_volume = 5 * u.L
filltime = dump_volume / Q_avg
print(filltime.to(u.min))


#dump_amount = 2 * total_hl * pc.area_circle(pipe_diam)
#print(dump_amount.to(u.L))


```

### Entrance Tank design

### Tipping Bucket Design

### Influent Pipe Geometry




### Biogas Production Calculations

As organic waste passes through the sludge blanket portion of the UASB reactor, it is broken down by anaerobic bacteria in a complex biological process that ends with methanogenesis.  A key product of this process is methane and carbon dioxide, which together are known as biogas.  This gas has a fairly high energy density, and can be burned for heating similar to propane.

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

Since biogas contains other gasses such as CO2, we must employ a correction factor to account for their contributions to the overall volume.  We assume that biogas is composed 75% of methane, as given in [Anaerobic Reactors](https://www.iwapublishing.com/sites/default/files/ebooks/9781780402116.pdf).

It is important to note that this equation only gives an approximation of the actual biogas produced, and a fairly inaccurate one at that.  Methanogensis is a very complicated biochemical process, and there are many other areas to consider that are not included in this equation, such as losses due to leakage, temperature effects, and the varying bacterial composition of the sludge blanket.  As most considerations are losses, we consider the value given by this equation an **overapproximation** and design accordingly.  For safety reasons, it is better to overestimate the volume produced rather than underestimate and design a system that will dangerously pressurize flammable gas.  Despite its problems, this equation still provides a good baseline value of the output biogas to inform the design process.

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
def BiogasFlow(Q, COD_Load, Temp):
    """Calculates the biogas production rate from the flow rate through the reactor, the COD concentration of the influent, and the temperature of the reactor

    For the doctest to pass, one must initialize the flow from UASB_design using UASB_Size(3 * u.ft, 7 * u.ft)

    >>> from aide_design.play import*
    >>> import math
    >>> BiogasFlow(UASB_design[2], 200 * (u.mg / u.L), 25 * u.degC)
    The volumetric methane production per second is 0.0013 liter / second
    The volumetric methane production per second is 112.3 liter / day
    [<Quantity(0.0012996707807037425, 'liter / second')>, <Quantity(112.29155545280335, 'liter / day')>]
    """
    # Calculating methane production by mass
    COD_Load = COD_Load.to(u.g / u.L)
    COD_eff = 0.7 # Assuming 70% efficency of COD removal and conversion in reactor
    COD_rem = COD_Load * COD_eff
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
| Gas Bag         | (1) Flexible and easy connection on top of next to reactor **(2) Cheap and cost effective** (3) Easy to transport for reactor to kitchen use (4) Visual representation of gas volume | (1) Fragility and Leakage (2) Require frequent replacement - are these materials available locally?      |
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

### Fats, Oils and Greases (FOG) Removal System
Typical wastewater from domestic sources contains many particles besides organic waste.  These include inorganics such as sand, rocks and clay that enter the wastewater system, along with organics that cannot be broken down by the anaerobic bacteria within the reactor.  Primary amongst these organics are fatty materials, including oils and greases.  These materials enter the wastewater stream mostly from cooking wastes that are poured directly down drains.

Fats are typically lighter than water and hydrophobic, causing them to float to the top of the UASB reactor and accumulate within the biogas capture lid.  If not removed, they will build up in this lid and hinder reactor efficiency.  Therefore, a successful UASB system must include an easy removal system for these materials.  Fats removed during domestic wastewater treatment are typically sent to a landfill for disposal.

The design process began with characterizing the rate at which fats would buildup within the reactor to determine how often they would have to be removed. However, this buildup rate is highly variable and depends on both the nature of wastewater and FOG removal efficiency during screening. Ed Gottlieb, a plant operator at the Ithaca Area Wastewater Treatment Facility (IAWWTF), informed the team that the IAWWTF skims its clarifiers once a month for FOG removal. With this information, the team decided to focus on designing a simple system that can remove FOG whenever the plant operators deem it necessary.

The team considered three possible systems for FOG removal:
* A mechanical or gravitational separator before influent that captured and removed fat particles
* Dosing of a coagulant to bind fat particles and make them easier to remove
* An outflow pipe or siphon coming out of the removable lid with a valve to allow discharge of water containing fats

After brainstorming these options, the team quickly ruled out the first two options, and they were complicated and either required mechanical parts or chemical dosing, which go against the design philosophy of the project to make the UASB simple and cheap to install and operate.

Thus, the team decided to design a small outflow pipe from the biogas lid.  In talking with Mr. Gottlieb, it seems a greater velocity will be needed to remove fat particles, as they will tend to spread over the water surface and congeal into mats.  Design for this system is still ongoing, and the team is researching siphon systems, as well as working to determine the dimensions of this pipe system.

In addition to these methods, the system will always have a failsafe system to remove fats.  Since the biogas lid is removable, fats can be manually skimmed off the top.  This was determined to be undesirable for a number of reasons.  First, it requires direct human input, which increases work for the community, and requires more training on usage.  Second, opening the system in this way depressurizes it, and releases any captured biogas produced within.  Finally, this requires close human contact with wastewater, which is a undesirable job and increases risk of infections or accidental discharge of wastewater.  However it offers a removal option if errors occur with designed systems.


### Sludge Sampling and Removal System

<br>
<div style="text-align:center">

![UASB_Side](/Images/Sludge_Weir.PNG)

 <p align="center">Figure 10: Schematic of the sludge sampling system. </p>

</div>

As long as it is continuously fed wastewater as "food", the UASB sludge blanket will continue to grow over time, filling the sludge volume and eventually rising upwards into the effluent zone.  To control and monitor this growth, our design incorporates a sludge weir system (see Figure 10).


The sludge weir consists of a tube jutting out of the reactor at a downwards angle.  This weir is implemented at the top of anticipated height of the sludge blanket, so as to capture bacterial growth above this limit.

The weir is designed with two valves to control flow.  The first valve is in line with the reactor wall, and will be left open during reactor operation, allowing for excess sludge to settle into the tube over time.  Ideally, the tube itself will be partially transparent, allowing direct monitoring of sludge levels and composition without release of wastewater.  When it is necessary for sludge to be removed from the system, this valve will be shut, and the outer valve will be opened to allow discharge of sludge material.

### Other Sampling Ports

For testing purposes, the first model of the UASB will include multiple sampling ports placed at different heights along the reactor.  These will be similar in design to the sludge weir, but smaller in diameter, and only used for testing purposed, not large scale sludge removal.  The ultimate number and location of these system will be determined once further research into sampling techniques is complete.

Another important concern for the reactor is inorganic removal. Inorganics such as sand, rocks, plastics, and other materials will inevitably enter the wastewater stream.  Those that are not removed in the degritting system will enter the reactor.  Since these materials are often denser than water, they will settle in the reactor and remain within the system indefinitely.  In order to remove these materials, a final inorganics weir will be added to the bottom of the reactor.  While this weir will most likely only be used sporadically, it is an important system to remove materials that would otherwise build up and hinder reactor performance.

#### Design Parameters of Sampling Ports and Sludge Weirs

The dimensions of the sludge weir are not incredibly important design parameters, and were thus set to values that seemed reasonable.  These systems will be tested in our first design and changed accordingly.  These parameters are set in the table below.

<p align="center">
Table 6: Design parameters for sludge sampling systems.
</p>

|       Parameter        |  Value   |               Basis of Design                |
|:----------------------:|:--------:|:--------------------------------------------:|
|  Sludge Weir Diameter  | 6 in |     Based on Floc Hopper in 1 L/s plant      |
|   Sludge Weir Length   |   To be determined    | Based on desired volume of sludge per sample |
| Sampling Port Diameter |   To be determined    |          Based on fabrication specs          |
| Number of Sampling Ports                       |  To be determined      | Based on  number of sampling sites needed   |

### Hydrogen Sulfide Removal system

Another important aspect of design is a removal system for hydrogen sulfide ($H_2 S$).  Hydrogen sulfide is naturally produced in anaerobic digestion of sulphates, which occur in low quantities in typical wastewater.  Hydrogen sulfide is highly flammable, toxic, and corrosive, making it very dangerous in large qualities within the reactor.  

Hydrogen sulfide is typically removed using an oxidizing agent, such as iron oxide or biological sources such as crop husks.  These can be incorporated into the reactor in multiple ways including:
* Dosing of a chemical compound in the influent of the reactor
* Exposing biogas to solid oxidizing agents such as steel wool

Design of this section is ongoing, but will likely involve a solid oxidizing agent to reduce costs and complexities associated with chemical dosing.

### Effluent Flow System
Based on settling tests conducted on the lab scale UASB reactors during Summer 2017, it was determined that a lower capture velocity than that used in AguaClara drinking water plants can sufficiently settle sludge granules and other solids in a UASB reactor (Chen, 2017). As such, fewer plate settlers are required in the UASB than in the 1 L/s plant sedimentation tank.  To reduce costs and fabrication time associated with constructing the sloped body of the 1 L/s sedimentation tank to house multiple large plates as shown in Figure 4, a new effluent and solid settling system was designed.

In this system, the body of the UASB reactor would leave the 3 foot diameter corrugated pipe intact rather than having to cut, rotate, and PVC weld to achieve the bend in the body of the reactor.  Instead, a sloped tube, or tube settler, would be inserted into the side of reactor to allow effluent to leave the reactor.  Inside this tube, a smaller set of plates would be placed to promote settling as shown in Figure 2.

#### Design Parameters
<p align="center">
Table 7: Design parameters for calculations of the tube settler size, the number of plates required and overall height of the settling arm. </p>

Parameter| Value | Basis of Design
:------------- |:-------------|:--------
Height of Sludge Blanket ```height_blanket``` | 3.5 ft| Assumed half the height of reactor
Distance Between Plate Settlers ```plate_space```| 2.5 cm | Based on Sedimentation Tank Design
Angle of Tube Settler ```angle``` | 60 degrees | Based on sedimentation tank design
Thickness of Plates ```thickness_sed_plate```| 2 mm| Taken from corrugated plastic thickness

The code below serves to calculate the size of the tube settler, the number of plates required, and the overall height of the settling arm.

#### Code
```python
# Design Parameters
height_blanket = 3.5 * u.ft
plate_space = 2.5 * u.cm
angle = 60 * u.deg
thickness_sed_plate = 2 * u.mm
flow = UASB_design[2]

# Assumptions
diam_sludge_weir = 6 * u.inch ## size of sludge weir used in 1L/s sed tank
sep_dist = 12 * u.inch  ## Arbitrary distance set to constrain the available space required for the tube settler since the tube settler has to set the water level inside the reactor but also have the entrance be above the sludge blanket
water_elevation = 6.5 * u.ft  ## figure out from previous reports


# velocity between plate settlers
diam_tube = np.array([8,10]) * u.inch

B = (plate_space + thickness_sed_plate).to(u.cm)

velocity_active_up = (flow * np.sin(angle)/(pc.area_circle(diam_tube))).to(u.mm/u.s)
print("The vertical velocity component beneath the plate settlers is in the range", velocity_active_up.magnitude,velocity_active_up.units )

velocity_plate_up = velocity_active_up * B / plate_space
print("The vertical velocity component between the plate settlers is in the range", velocity_plate_up.magnitude, velocity_plate_up.units)

velocity_plate = (velocity_plate_up / np.sin(angle)).to(u.mm/u.s)
print("The velocity between the plate settlers is in the range", velocity_plate.magnitude, velocity_plate.units)


# Parameters for tube settler
height_tube_settler = (height_blanket + diam_sludge_weir + sep_dist + 0.5*diam_tube).to(u.inch)  # height of the center of the tube setler
print("The height of the center of the tube settler where is attaches to the body of the reactor is in the range",height_tube_settler.magnitude, height_tube_settler.units)

length_tube_settler_vertical = (water_elevation - height_tube_settler).to(u.inch)
print("The vertical length of the tube settler is in the range", length_tube_settler_vertical.magnitude, length_tube_settler_vertical.units)

length_tube_settler = (length_tube_settler_vertical / np.sin(angle)).to(u.cm)
print("The length of the tube setter is in the range",length_tube_settler.magnitude, length_tube_settler.units)

projected_area = (((length_tube_settler * np.cos(angle)
                  ) + (plate_space/np.sin(angle))) * diam_tube).to(u.m**2)
print("The projected area of the plates is in the range", projected_area.magnitude, projected_area.units)

velocity_capture = (plate_space.to(u.mm) * velocity_plate_up.to(u.mm/u.s))/(length_tube_settler.to(u.mm) * np.sin(angle) * np.cos(angle) + plate_space.to(u.mm))
print("The capture veloctiy is in the range", velocity_capture.magnitude, velocity_capture.units)

number_plate_settler = np.floor(diam_tube / (plate_space.to(u.inch) + thickness_sed_plate.to(u.inch)))
print("The number of plate settlers is in the range", number_plate_settler.magnitude, number_plate_settler.units)
```

## 2018 EPA Expo in Washington, D.C.

On April 7 and 8,  UASB team members Ananya Gangadhar and Jennifer Jackson presented the Phase 1 UASB work at the EPA's National Sustainable Design Expo.  The Expo was part of a larger event, the USA Science and Engineering Festival at the Walter E. Washington Convention Center in Washington, D.C.  Ananya and Jennifer, along with Professor Ruth Richardson and other AguaClara members, presented the current UASB Reactor design.

![UASB_EPA_expo](/Images/EPA_Expo.jpg)
<p align="center">Figure 11: From left to right -  Jennifer Jackson, Ananya Gangadhar, and Sidney Lok at the EPA Expo. </p>

![EPA_poster](/Images/epa_poster.PNG)
<p align="center">Figure 12:  The poster that was presented at the EPA Expo. </p>

## Future Work

A rough timeline of the project is summarized below.  The overall goal is for design work to be complete by the end of Summer 2018.  During Fall 2018, the subteam will become a fabrication team and build the completed reactor.  After that the UASB will be implemented and tested at the Ithaca Wastewater Plant, and data gathered from this testing will inform future design.  Once design is complete and the system has been proven, the finished product will be shipped to Honduras for field testing, and then implemented in rural communities full time.

#### Summer 2018
* Conduct benchtop tests for influent system
* Finish final design components (sampling ports, inorganics removal, degritting system, hydrogen sulfide removal)
* Make complete fusion model
* Design data collection methods
* Make fabrication plan

#### Fall 2018
* Find fabrication space for UASB
* Fabricate Reactor

## Bibliography
Abbasi, T., & Abbasi, S. A. (2012). Formation and impact of granules in fostering clean energy production and wastewater treatment in upflow anaerobic sludge blanket (UASB) reactors. Renewable and Sustainable Energy Reviews, 16(3), 1696–1708. https://doi.org/10.1016/j.rser.2011.11.017

Chen, Z. (2017, August). Upflow Anaerobic Sludge Blanket, Summer 2017.

Chong, S., Sen, T. K., Kayaalp, A., & Ang, H. M. (2012). The performance enhancements of upflow anaerobic sludge blanket (UASB) reactors for domestic sludge treatment – A State-of-the-art review. Water Research, 46(11), 3434–3470. https://doi.org/10.1016/j.watres.2012.03.066

Ghoneim, W. A. M., Helal, A. A., & Wahab, M. G. A. (2016). Renewable energy resources and recovery opportunities in wastewater treatment plants. In 2016 3rd International Conference on Renewable Energies for Developing Countries (REDEC) (pp. 1–8). https://doi.org/10.1109/REDEC.2016.7577509

Herrara, D., Hua, Y., Kim, S. M., & Yang, F. (2016, December). Prefabrication 1 L/s, Fall 2016.

Kim, A., Chen, Y., & Evan, G. (n.d.). Upflow Anaerobic Sludge Blanket, Fall 2016.

Lettinga, G., & Pol, L. W. H. (1991). UASB-Process Design for Various Types of Wastewaters. Water Science and Technology, 24(8), 87–107.

Mittal, A. (2011). Biological Wastewater Treatment. Water Today. Retrieved from http://www.academia.edu/7451295/Biological_Wastewater_Treatment

Narnoli, S. K., & Mehrotra, I. (1997). Sludge blanket of UASB reactor: Mathematical simulation. Water Research, 31(4), 715–726. https://doi.org/10.1016/S0043-1354(97)80987-6

Subramanyam, R. (2013). Physicochemical and Morphological Characteristics of Granular Sludge in Upflow Anaerobic Sludge Blanket Reactors. Environmental Engineering Science, 30(5), 201–212. https://doi.org/10.1089/ees.2012.0347

Van Lier, J. B., Vashi, A., Van Der Lubbe, J., & Heffernan, B. (2010). Anaerobic Sewage Treatment using UASB Reactors: Engineering and Operational Aspects. In Environmental Anaerobic Technology (Vols. 1–0, pp. 59–89). IMPERIAL COLLEGE PRESS. https://doi.org/10.1142/9781848165434_0004
