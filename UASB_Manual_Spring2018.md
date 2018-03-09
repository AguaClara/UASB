
# Upflow Anaerobic Sludge Blanket, Spring 2018
#### Zac Chen, Jennifer Jackson, Ian Cullings, and Ananya Gangadhar
#### March 9, 2018

## Abstract
Since Spring 2017, the AguaClara UASB has been working on a detailed design of modified, pilot-scale UASB reactor originally proposed in an EPA P3 proposal.  Working towards that goal, the team has created Python code to record the design process and calculations for this AguaClara UASB. This document serves as a master guide for the design process.

## Introduction
***May have to edit to better bit the context of what we're attempting to do which is design work but this offers a good source of context of WW treatment in general and where our project fits***
The contamination of ground and surface water sources by wastewater has adverse environmental and health affects. First, the biological degradation of wastewater by aerobic microbes lowers the dissolved oxygen content in natural waterways, preventing aquatic life from thriving and potentially creating dead zones. Additionally, it increases waterborne fecal matter content and increases the risk of exposure to pathogens ([Chong et. al, 2012](https://www.sciencedirect.com/science/article/pii/S0043135412002400?via%3Dihub)). The latter is of particular concern to individuals in the global south, as communities downstream of wastewater outfalls often have inadequate drinking water treatment.

Wastewater can also be an opportunity for energy recovery. According to recent estimates, the energy potential of wastewater and biosolids is more than ten times the energy needed for treatment ([Ghoneim et. al,  2016](http://ieeexplore.ieee.org/document/7577509/?reload=true)). Most wastewater treatment facilities in the US do not optimize the recovery of energy and resources from biosolids ([Ghoneim et. al,  2016](http://ieeexplore.ieee.org/document/7577509/?reload=true)). While it is important to develop wastewater treatment technology to optimize current wastewater treatment for all individuals, the focus of this research was on small communities in the global south. Such communities do not have widespread wastewater infrastructure, and therefore much of the wastewater is left untreated.

<!--- why conventional wastewater treatment is not appropriate for developing nations --->
Currently in the United States, effective municipal wastewater treatment facilities have long retention times, require large land areas, and have a high fixed cost per capita ([Chong et. al, 2012](https://www.sciencedirect.com/science/article/pii/S0043135412002400?via%3Dihub)). Due to economy of scales, small systems have even higher fixed costs per capita and these high fixed costs make conventional wastewater treatment systems inaccessible for small communities. Many cities in the global south forgo wastewater treatment altogether due to the high cost and instead discharge untreated wastewater to the environment ([Chong et. al, 2012](https://www.sciencedirect.com/science/article/pii/S0043135412002400?via%3Dihub)). Research and development of small-scale and decentralized wastewater treatment methods should be prioritized in order to make wastewater treatment accessible for all communities.

<!--- why uasb is an option --->
Upflow Anaerobic Sludge Blanket (UASB) reactors are conventionally used as a preliminary wastewater treatment process to clarify wastewater by removing suspended solids and reducing organic matter ([Chong et. al, 2012](https://www.sciencedirect.com/science/article/pii/S0043135412002400?via%3Dihub)). UASB reactors rely on gravity to clarify wastewater, biological processes to remove organic matter and convert it to biogas, and are less energy intensive than other forms of preliminary wastewater treatment that use aerobic processes. A byproduct of the biological processes in UASB reactors is methane. Methane is a potent greenhouse gas, but if collected, can be used as a fuel or burned and safely released into the atmosphere.

<!--- how we modified UASBs --->
In January 2017, a novel pilot scale UASB reactor design was created by AguaClara for the EPA People, Prosperity and the Planet (P3) [Student Design Competition proposal](https://docs.google.com/document/d/1geug1EyFjCRLQgO79vTOXUUFia3RBw3bhaIHPUiqu44/edit?usp=sharing). This reactor was designed to improve the accessibility of wastewater treatment for small communities. The proposed UASB reactor design identified areas to improve conventional reactor design including: (1) plate settlers, (2) submerged gas collection lid, (3) sludge weir, (4) submerged exit launder, and (5) fabrication methods.

Since this proposal, there has been ongoing work to determine the parameter and designs of specific components of the proposed UASB reactor.  This document serves as a manual for the full design process of the proposed UASB reactor.  Eventual fabrication of a pilot scale UASB will soon follow the completion of the proposed designs.

<!--- ## Literature Review and Previous Work
***This should be expanded on a little*** --->


### Conventional Wastewater Treatment Options
Municipal and industrial wastewater can be treated via biological, chemical oxidation, or thermal oxidation treatment processes. Biological treatment is commonly used because the latter two treatment options require higher capital investment and operational costs ([Mittal et. al, 2011](http://www.watertoday.org/Article%20Archieve/Aquatech%2012.pdf)). The two main types of biological treatment are the activated sludge process and anaerobic digestion. When compared to the activated sludge process, anaerobic digestion yields less sludge and reduces energy input ([Mittal et. al, 2011](http://www.watertoday.org/Article%20Archieve/Aquatech%2012.pdf)). Although there are some drawbacks to anaerobic digestion such as long solids retention time (SRT) and insufficient nutrient removal, the reduced energy input renders it the most feasible technology for communities in the global south ([Chong et. al, 2012](https://www.sciencedirect.com/science/article/pii/S0043135412002400?via%3Dihub)).

### UASB Basics

![Conventional_UASB](https://github.com/AguaClara/UASB/blob/master/Images/Conventional_UASB.PNG?raw=true)

<p align="center">Figure One: A Conventional UASB Design </p>

Upflow anaerobic sludge blanket (UASB) reactors are one example of high-rate anaerobic digesters. UASBs are used as primary clarification of wastewater, and therefore require post-treatment options such as trickling filters and secondary clarifiers to achieve ideal reduction of chemical oxygen demand (COD), suspended solids (SS), and nutrients ([Abbasi et. al, 2012](https://www.sciencedirect.com/science/article/pii/S1364032111005533)). High-rate anaerobic digesters, such as UASBs, are designed to operate at short hydraulic retention times (HRT) and long solids retention time (SRT) to increase loading capacity and improve sludge stabilization ([Chong et. al, 2012](https://www.sciencedirect.com/science/article/pii/S0043135412002400?via%3Dihub)). Due to these advantages, UASB reactors were chosen as the basis for preliminary wastewater treatment design for communities in the global south.

To successfully process organic waste, UASB reactors heavily rely on the accumulation, concentration, and conglomeration of a large population of these bacteria in order to form diverse microbial community known as granules.  Proper granulation and retention of these granules in a reactor is imperative to maximize the removal of COD and BOD and increase the overall effectiveness of UASB technologies ([Subramanyam et. al 2013](https://www.liebertpub.com/doi/abs/10.1089/ees.2012.0347)).  To prevent biomass escape and increase sludge retention, parallel plates, akin to those in AguaClara drinking water treatment facilities, can be used ([Chong et. al, 2012](https://www.sciencedirect.com/science/article/pii/S0043135412002400?via%3Dihub)).

A useful by product of this process is biogas, a mixture of methane, carbon dioxide, and some trace gases.  After production in the digestion zone, methane floats upwards through the water and is caught in the cone of the Gas Liquid Solid Separator.  From there, it is funneled upwards into a storage vehicle where it can later be burned for heat or energy generation.  More details on the biogas capture and usage can be found in the [Biogas Capture](#Biogas-Capture-System) section of the manual.

## Design Process

### Example Aspect of UASB
*Introduce the background for the particular set of calculation/code*
#### Design Parameters
*Place a table here with the design parameter (followed by the variable name in the code), the value for it, and the justification with a hyperlink, kinda like this*
| Design Parameter | Value | Basis of Design |
|:----------------:|:-----:|:---------------:|
| Poop ```poop```  | 17 jillion liters |  I'm lactose intolerant               |
#### Code
*Insert your code here*
```python
def Good_Func(input_code):
  #remember that functions need colons at the end
```


### Size and Flow

This document can be used to determine the number of people served based on size of UASB design. The reactor will have a 60 $$ $^{\circ}$ $$ sloped bottom for structural integrity, primarily based on the designs of the 1 L/s plant. The reactor will thus have a reduced volume from the two cylindrical hooves that have been removed from housing active granules.

#### Design Parameters
|               Design Parameter                |        Value        |                                         Justification of Parameter                                          |
|:---------------------------------------------:|:-------------------:|:-----------------------------------------------------------------------------------------------------------:|
|      Hydraulic Residence Time ```HRT```       |        4 hrs        |                  From tracer tests conducted in [Fall 2016](https://www.overleaf.com/read/dnxfsrwdxbdf#/21165144/) and minimum values in literature ([Chong et. al, 2012](https://www.sciencedirect.com/science/article/pii/S0043135412002400?via%3Dihub)).               |
| Wastewater Generation per Person ```WW_gen``` |       3 mL/s        |                                          Rule of Thumb from Monroe                                          |
|   Blackwater Generation per person ```WW_gen_bw``` |         0.6 mL/s        |               20% of mixed wastewater  From Prof. Richardson's estimation                       |
|             Center Space of Base              |        3 in         | Based on the [1 L/s plant design](https://www.overleaf.com/6186375zdpjfc) (more info in their Google Drive) |
|                  Slope Angle                  | 60 $$ $^{\circ}$ $$ |                  Based on the [1 L/s plant design](https://www.overleaf.com/6186375zdpjfc)                  |
|              Diameter of Reactor              |       3 feet        |             Based on size of corrugated pipe used for the body of the 1 L/s sedimentation tank              |
|             Height of the Reactor             |       7 feet        |                               Based on the maximum ceiling height of the lab                                |

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

Diameter = 3 * u.ft
Height = 7 * u.ft
UASB_design = UASBSize(Diameter, Height)
````

### Influent Flow System
Influent pipe design represents a new design challenge this semester.  A literature review was conducted to compare the various values for reactor design parameters. A table below includes relevant values, and is not an exhaustive list of our sources.

The issues that we intend to tackle this semester regarding the influent flow into the reactor include designs to combat pipe blockages. This involves the creation of a trash rack and grit capture mechanism, calculating the optimal pipe diameter, and possibly including a nozzle or aperture at the end of the pipe to ensure high velocity flows to prevent deposition of solids.

Top influent flow was chosen over bottom influent flow in order to decrease the frequency of clogs.  In addition, top influent flow is the most common choice for domestic wastewater treatment.  

A literature review reveals a lack of knowledge in the UASB community on the influence area of influent pipes.  Values range from 1-4 $m^2$ with little experimental evidence.  Since the bottom of the proposed AguaClara reactor is less than 1 $m^2$, the reactor can be covered by at least one influent pipe.  Two influent pipes are being considered especially, as they allow for better clog detection and prevention.   



| Parameter                                                                         | [Anaerobic Reactors Textbook](https://drive.google.com/drive/folders/1yP48lb38n-ZQb5PtMfpcJs9RIu4wKJ1f) | [Wastewater Treatment for Pollution Control and Reuse 3rd ed](http://accessengineeringlibrary.com/browse/wastewater-treatment-for-pollution-control-and-reuse-third-edition/c9780070620995ch07#c9780070620995ch07lev1sec01) | [Van Lier: Anaerobic Sewage Treatment using UASB Reactors](https://courses.edx.org/c4x/DelftX/CTB3365STx/asset/Chap_4_Van_Lier_et_al.pdf) |  
|:--------------------------------------------------------------------------------- |:------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **Descending Sewage Velocity**                                                    | **$\leq$0.2 m/s**                                                                                       |                                                                                                                                                                                                                             |                                                                                                                                           |     |     |     |
| **Diameter of pipe**                                                              | **75-100 mm** (from practical experience)                                                               |                                                                                                                                                                                                                             | **100 mm** (to allow gas bubbles to rise)                                                                                                 |     |     |     |
| **Nozzle Diameter**                                                               | **40-500 mm** (from practical experience)                                                               |                                                                                                                                                                                                                             |                                                                                                                                           |     |     |     |
| **Exit Velocity**                                                                 | **$\geq$0.40 m/s**                                                                                      |                                                                                                                                                                                                                             | **5 m/hr**                                                                                                                                |     |     |     |
| **Apertures**                                                                     | **2 openings with 25mm × 40mm cross section**                                                           | See Aperture Design Problem 7.12.1.6                                                                                                                                                                                        | Single outlet point per pipe (for identification of clogs)                                                                                |     |     |     |
| **Influence Area**                                                                | **2.0-3.0 $m^2$ for COD 400-600 mg/L**                                                                  | **1 point per 3.7-4.0 $m^2$ floor area**                                                                                                                                                                                    | **1-4 $m^2$ per feed point**                                                                                                              |     |     |     |
| **Settling Zone Surface**                                                         |                                                                                                         |                                                                                                                                                                                                                             | **75% of total surface**                                                                                                                  |     |     |     |
| **Distance Between Exit Mouth and Water Level in Settler/ Headloss through unit** |    **0.20-0.30 m**                                                                                                     |               **2-3 m head loss** through unit for gravity feed with distribution from top of UASB through splitter boxes and weirs to divide and regulate the feed to each inlet channel and then to downtake pipe. Also see Example 7.2 | **50 cm**
### Biogas Capture System

An important aspect of UASB design is the capture and storage of biogas produced during anaerobic digestion within the reactor.  As this gas is produced within the sludge blanket, it floats upwards through the settling zone and is captured within the lid space.  The UASB team considered many possible designs for this capture system.  These three options, along with Pros and Cons are detailed in the table below.

| Type of Storage | Pros                                                                                                                                                                           | Cons                                                                                                                       |
|:--------------- |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |:-------------------------------------------------------------------------------------------------------------------------- |
| Gas Bag         | (1) Flexible and easy connection on top of next to reactor **(2) Cheap and cost effective** (3) Easy to transport for reactor to kitchen use (4) Visual representation of gas volume | (1) Fragility and Leakage (2) Require frequent replacement - are these materials available locally?      |
| Fixed Lid       | (1) Durability (2) No concerns about movement (3) Can use prefabricated barrel                                                       | (1) Water displaced during gas compression may need to be recaptured, requiring additional information |
| Floating Lid    | (1) Water level moves with gas (2) Same concept as fixed lid (3) Visual representation of gas level            | (1) Low gas production will just cause water displacement (2) Track system hard to fabricate  |

After consideration of these options, we decided upon the gas bag system.  Gas will flow out the top lid of the reactor through a pipe into an intermediate volume.  This space will hold biogas, where it can be released into a balloon for home usage, or flared off from the container.


#### Design Parameters
| Parameters | Value | Basis of Design |
| :-------: | :--------: | :--------------: |
| COD Removal Efficiency, ```COD_eff``` | 70% | Based on [Van Lier Report](https://courses.edx.org/c4x/DelftX/CTB3365STx/asset/Chap_4_Van_Lier_et_al.pdf)  |
| Percent of COD directed to Sludge Production ```Y_obs```| 11% to 23% | Based on [Anaerobic Reactors](https://www.iwapublishing.com/sites/default/files/ebooks/9781780402116.pdf) |
| Pressure ```P```| 1 atm | Biogas produced will be stored at very low pressure |
| Temperature ```T``` | 25 $^{\circ}$ C | Assuming mesophilic conditions |

#### Code
```python
#Calculate Biogas Rate of Production (L/s and L/day) in UASB
def BiogasFlow(Q, COD_Load, Temp):
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

    print("The volumetric methane production is per second is", Q_CH4, "\n" "The volumetric methane production is per second is", Q_day)
    return [Q_CH4, Q_day]

# Flow rate through UASB reactor
Flow_design = UASB_design[2]
# Amount of biogas production per second and per day
Temp = 25 * u.degC  # Assuming mesophilic conditions
#Approximate loading rates for domestic wastewater
COD_Load_min = 100 * (u.mg / u.L)
COD_Load_mid = 200 * (u.mg / u.L)
COD_Load_max = 300 * (u.mg / u.L)

Q_Biogas = BiogasFlow(Flow_design, COD_Load_mid, Temp)
#Calculating size of storage device
Size_Store = Q_Biogas[1].to(u.gal / u.day) * (u.day)
print("The size of the storage container to store one day worth of biogas production should be at least", Size_Store)
```

### Sludge Sampling and Removal System

Another important part of the UASB design in the sludge weir system.  The sludge weir is a tube built out of the UASB, originating at the top of the sludge blanket.  This tube has a valve at the end of the cap, allowing sampling and discharge from the UASB as necessary.  This serves two purposes.  First of all, it allows removal of material from the sludge blanket.  Given that the sludge blanket is mostly biological material, it will constantly grow with inputs of wastewater, and this allows us to control the growth as necessary.  This allows sample collection throughout the lifetime of the reactor as well.

Additional small sludge sampling ports will be added as necessary to ensure different areas of the blanket can be sampled properly.

One final important system for design is the inorganics removal tube.  As wastewater flows into the system, materials such as sand, rocks, grit, and plastics will flow in and build up in the bottom of the reactor.  Since there is no way for these materials to be removed from the UASB, a drainage valve must be added so the reactor can periodically be cleaned.

#### Design Parameters

Design of these sections is ongoing, and the locations and dimensions of these sampling ports will be determined once flow and dimensional design is complete.


### Effluent Flow System
Based on settling tests conducted on the lab scale UASB reactors during Summer 2017, it was determined that a full cross section of plate settlers is not required.  Similar effluent quality can be achieved by a capture velocity that is equal to the upflow velocity, contrary to AguaClara drinking water plant designs.  

In light of this information, the proposed designs were altered to include a tube settler with plate inside.  This alteration served highly beneficial as it eases fabrication because it does not require a team to cut and weld two sections of pipe, and reduces fabrication time and associated costs.  

This document serves to calculate the size of the tube settler, the number of plates required, and the overall height of the settling arm.

#### Design Parameters
Parameter| Value | Basis of Design
:------------- |:-------------|:--------
Height of Sludge Blanket ```height_blanket``` | 3.5 ft| Assumed half the height of reactor
Distance Between Plate Settlers ```plate_space```| 2.5 cm | Based on Sedimentation Tank Design
Angle of Tube Settler ```angle``` | 60 degrees | Based on sedimentation tank design
Thickness of Plates ```thickness_sed_plate```| 2 mm| Taken from corrugated plastic thickness

#### Code
```python
# Design Parameters
height_blanket = 3.5 * u.ft
plate_space = 2.5 * u.cm
angle = 60 * u.deg
thickness_sed_plate = 2 * u.mm
flow = UASB_design[2]

# Assumptions
diam_sludge_weir = 6 * u.inch
sep_dist = 12 * u.inch
water_elevation = 6.5 * u.ft  ## figure out from previous reports


# velocity between plate settlers
diam_tube = np.array([8,10]) * u.inch

B = (plate_space + thickness_sed_plate).to(u.cm)

velocity_active_up = (flow * np.sin(angle)/(pc.area_circle(diam_tube))).to(u.mm/u.s)
print("The vertical velocity component beneath the plate settlers is", velocity_active_up.magnitude,velocity_active_up.units )

velocity_plate_up = velocity_active_up * B / plate_space
print("The vertical velocity component between the plate settlers is", velocity_plate_up.magnitude, velocity_plate_up.units)

velocity_plate = (velocity_plate_up / np.sin(angle)).to(u.mm/u.s)
print("The velocity between the plate settlers is", velocity_plate.magnitude, velocity_plate.units)


# Parameters for tube settler
height_tube_settler = (height_blanket + diam_sludge_weir + sep_dist + 0.5*diam_tube).to(u.inch)  # height of the center of the tube setler
print("The height of the center of the tube settler where is attaches to the body of the reactor is",height_tube_settler.magnitude, height_tube_settler.units)

length_tube_settler_vertical = (water_elevation - height_tube_settler).to(u.inch)
print("The vertical length of the tube settler is", length_tube_settler_vertical.magnitude, length_tube_settler_vertical.units)

length_tube_settler = (length_tube_settler_vertical / np.sin(angle)).to(u.cm)
print("The length of the tube setter is",length_tube_settler.magnitude, length_tube_settler.units)

projected_area = (((length_tube_settler * np.cos(angle)
                  ) + (plate_space/np.sin(angle))) * diam_tube).to(u.m**2)
print("The projected area of the plates is", projected_area.magnitude, projected_area.units)

velocity_capture = (plate_space.to(u.mm) * velocity_plate_up.to(u.mm/u.s))/(length_tube_settler.to(u.mm) * np.sin(angle) * np.cos(angle) + plate_space.to(u.mm))
print("The capture veloctiy is", velocity_capture.magnitude, velocity_capture.units)

number_plate_settler = np.floor(diam_tube / (plate_space.to(u.inch) + thickness_sed_plate.to(u.inch)))
print("The number of plate settlers is", number_plate_settler.magnitude, number_plate_settler.units)
```

### Other Considerations
Other considerations required are: (1) an efficient removal system for fats, oils, and grease that will build up at the top of the reactor, (2) another removal system at the bottom of the reactor to prevent buildup of inorganics.


## Future Work
Describe your plan of action for the next several weeks of research. Detail the next steps for this team. How can AguaClara use what you discovered for future projects? Your suggestions for challenges for future teams are most welcome. Should research in this area continue?

## Bibliography
Logan, B. E., Hermanowicz, S. W., & Parker,A. S. (1987). A Fundamental Model for Trickling Filter Process Design. Journal (Water Pollution Control Federation), 59(12), 1029–1042.
