## UASB Design, Spring 2019
By Nina Blahut, Shania Fang,  Emily Liu, Kanha Matai
February 22, 2019

## Abstract
Since Spring 2017, the AguaClara Upflow Anaerobic Sludge Blanket (UASB) Team has been working on a detailed design for a pilot-scale, gravity-powered UASB reactor. A UASB reactor treats wastewater anaerobically and produces biogas as a by-product.

During [Perhaps during instead of over. This is just a stylistic preference] Spring 2019, the UASB-Design team's main goal will be [want to use future tense] to  finalize the design for the UASB and support the design with substantial Python code and CAD designs. So far, the team has completed a general CAD design on Onshape for the entire UASB reactor.

##Introduction
In the past, AguaClara has focused on creating sustainable and inexpensive drinking water treatment; however, it is currently expanding to wastewater treatment. The completion of a pilot UASB reactor that will be tested with influent [influent] wastewater entering [entering] Ithaca Area Wastewater Treatment Facility [Plant] (IAWWTF) will be a big step for AguaClara’s venture into sustainable wastewater treatment. [I suggest that you briefly explain that AguaClara only has experience in drinking water treatment since this intro is BEFORE literature review where that is explained. The assumed audience is not me, but someone who is unfamiliar with AguaClara] There is still much that needs to be further discovered and refined, such as whether or not the tipping bucket system will be useful in eliminating preferential pathways, the effluent system design, and the gas capture system.

## Literature Review and Previous Work

According to [US Geological Survey](https://water.usgs.gov/edu/wuww.html) (USGS), Wastewater is any kind of used water. This used water may include dissolved fecal and urine matter, harmful chemicals, pathogens, and many more pollutants. [where does all this stuff come from? ie mention sewage, industry, etc.] Because water is a natural solvent, it becomes difficult to separate the water from these harmful compounds. These compounds come from a variety of sources such as homes, factories, and farms. As a result, water pollution is a global issue yet many areas in the world still lack wastewater treatment plants.[What's wastewater?] Leaving wastewater untreated and releasing it directly back into the environment can produce devastating effects on both the environment and human health. [last sentence of the paragraph would probably work better as the 2nd to explain where the contaminants come from]

Wastewater can also contain decaying organic matter and nutrients such as phosphorus and nitrogen which can cause algae blooms and thus eutrophication. [to be specific... eutrophication (excess nutrients) causes algae blooms, which only create anoxic conditions when large amounts of algae die off and require lots of oxygen to decompose] To be specific, eutrophication is the process where excess nutrients, specifically phosphorus or nitrogen, can cause algae to bloom quickly and in large amounts thus creating anoxic conditions because when large amounts of algae die off, they require lots of oxygen to decompose. This negatively impacts the ecosystem because the lack of oxygen makes it harder for aquatic life to survive. At high concentrations,[at high concentrations, organic matter and nutrients are naturally found in low concentrations] these water pollutants are killing marine birds, crustaceans, sea weeds, and many other organisms.

Human health is also directly affected by a lack of wastewater treatment. Pathogens in wastewater are [are] destroying crop production, infecting our food supply, and [causing] causing water-borne diseases. Health risks associated with wastewater includes respiratory disease, cancer, diarrheal disease, a neurological disorder, and cardiovascular disease ([Mehtab Haseena, 2017](http://www.alliedacademies.org/articles/water-pollution-and-human-health-7925.html)).
[I think you can hyperlink these instead of just slapping them here. No links in the middle of paragraphs!]

Some of the biggest issues that wastewater treatment plants face today are energy consumption and environmental footprints. Wastewater facilities [typically] typically have [treatment processes that include] treatment processes that include preliminary treatment, sedimentation, chlorination, and processing sludge which are all electrically and fuel powered ([AOS, 2018](https://aosts.com/how-much-energy-does-wastewater-treatment-plant-use/)). Currently, [What year?] there are about 17,000 wastewater treatment plants in the US, and they use up about 3% of the nation’s total energy consumption([MGOE, 2019](https://www.mge.com/saving-energy/business/bea/article_detail.htm?nid=%202431)). However, not all countries have access to [to what?] the same resources or can afford the same [infrastructure(or technology, etc)] technology, which makes having universal wastewater treatment plants not feasible.

[Traditional] Traditional UASB reactors are used as a preliminary wastewater treatment process to remove suspended solids organic matter in wastewater (Chong et. al, 2012). UASB reactors, instead of using fuel or electricity, rely mainly on gravity and biological processes to remove organic matter and convert it to biogas. They are highly efficient in treating high COD loads, biogas formation, and provide good stabilization of solids([M.K. Daud, 2018](https://www.hindawi.com/journals/jchem/2018/1596319/)).They are less energy intensive than other forms of preliminary wastewater treatment that use aerobic processes. UASB reactors also produce methane as a byproduct of anaerobic digestion which can be captured and used for energy production or heating. However, these UASB reactors still rely on electricity.

AguaClara, on the other hand, has designed a UASB reactor that solely uses gravity. It’s main function is to improve the accessibility [and affordability?] and affordability of wastewater treatment for smaller communities that don’t have access to electricity. In January 2017, this gravity-powered UASB reactor was designed for the EPA People, Prosperity and the Planet (P3) Student Design Competition proposal. The proposed UASB reactor design focused on improving reactor design, making the system cheaper and easier to fabricate so [that] that it [could] could be created globally. The team later applied for Phase II funding from the same organization to support the development and implementation of additional reactors for testing and received a grant of $75,000.

**Summer 2018**
In Summer 2018 the team worked on [the] the hydraulic design of the UASB system and created a tipping bucket system which delivered wastewater [come on guys how did you miss this one? it's red on my atom] in large pulses at a high flow rate. The team had two possible designs for the influent system--one option was for influent tubes to enter either at the top of the UASB reactor, and the alternative was for influent tubes to enter the UASB reactor at the bottom [where? at the bottom?]. The team also focused on biogas storage and came up with three types of storage: Gas Bag, Fixed Lid, and Floating Lid. They later decided that a gas bag system was both cost effective and transportable for community systems.

**Fall 2018**
Preferential pathways in wastewater treatment when occur when incoming wastewater forms a tunnel through the sludge blanket instead of flowing evenly through the blanket; consequently, not all of the wastewater gets in contact with sludge granules, and it’s not effectively cleaned. [What did the team find? before you conclude anything... All you've done is say that they researched preferential pathways and explain what pref pathways are. I assume that pref pathways were a problem since it can be a problem in WW treatment in general but it is not explicitly said that Fall2018 UASB found pref flow to be a problem] In Fall 2018, the UASB team researched preferential pathways in UASBS by doing bench tests. The team fabricated a small scale UASB reactor used chia seeds, marbles, and tapioca to simulate sludge. UASB team found that preferential flow patterns were likely to occur. The team concluded that it will likely be necessary to have several influential pipes to promote the even distribution of wastewater flow and decrease preferential pathways.
[maybe a diagram/picture would help with this explanation] [ADD PICTURE FROM PREVIOUS RED DYE TESTS SHOWING PREFERENTIAL FLOW]

In the Spring 2019 semester, the team will focus on building and assembling a UASB pilot-scale reactor to be tested in Ithaca’s Wastewater Treatment Plant by the Summer of 2020.


## Methods

## Design for Influent System

In this section, the team will explain how it made decisions regarding the design for the influent system.

For the influent system, the team has decided to move forward with the Summer 2018 team's design in which a tipping bucket empties wastewater into a holding tank, which will then empty into a flow dividing bucket, into influent separate pipes, and finally into the side of the reactor. The team will also move forward with the Summer 2018 team’s plan to use a 300 gallon reactor tank that has a 36” diameter and 72” height. (https://www.plastic-mart.com/product/17049/300-gallon-plastic-tank-rotoplas-590314-590315)

In terms of materials for fabrication, the team has decided to use parts made of HDPE plastic because separate pieces of the UASB, such as the influent pipes and the 300 gallon reactor tank, will need to be welded together. HDPE was chosen because it is durable and corrosion resistant, and large tanks made of HDPE, unlike PVC, are available.  

A design for the tipping bucket was completed by the summer 2018 team.
![Summer 2018 tipping bucket design](https://github.com/AguaClara/UASB/blob/master/Images/Influent_Tank_Tipping_Bucket.png?raw=true)

Figure 2. Summer 2018 Final Tipping Bucket design

This semester, the team realized an issue with the previous team's tipping bucket design: the frame for the tipping bucket is metal. This is an issue because the metal frame would get wet from splashing and rust. To combat this issue, the team will alter the design of the tipping bucket, so that there are no metal parts. The revised tipping bucket will be made by welding HDPE plates to the sides of a 5 gallon HDPE bucket, then welding HDPE rods onto those plates, which will be used to mount the tipping bucket in the holding tank.

[attach at rough sketch of new tipping bucket design if possible NB]

Certain elements from the previous team's tipping bucket design, including the volume of the tipping bucket, the locations of the pivots with respect to the bucket's center, and the dimensions of the holding tank, will remain the same. The previous team determined the optimal location of pivots by performing tests with pivots in various positions and selecting the locations in which the tipping bucket filled the most while still emptying completely.

Table 1. Summer 2018 Tipping Bucket Trial Results
| Trial | Horizontal Pivot Position (from center) (cm) | Vertical Position (center of pivot to base of bucket) (cm)  | Height Filled (cm)| Volume Filled (L)| Emptied Completely|
| -------- | ----------------|--------------- | --------- | ---------| -------|
| 1    | 0.25  | 16.5 | 21 | 14.8 | yes |
| 2 | 0.5 | 16.5| 22 | 15.56 | yes|
|3   | 0.5  | 19.3  |  x | x | no|
|4   | 0.5  | 18.5  |  x |  x | no |
|5   | 0.75  |  18.5 |  22 | 15.56  | yes |
| 6  |   0.75|   15.5|  22 | 15.56  | yes  |
|7   |  0.5 |  15.5 | 23  | 16.26  | yes |

The calculation for the volume in Liters filled of the bucket is shown below.

```python
from aide_design.play import*
bucket_height = 23 * u.cm
bucket_diam = 30* u.cm
area = pc.area_circle(bucket_diam)
vol = area * bucket_height
print(vol.to(u.L))
 ```

Based on the Summer 2018 team's results, the pivots will be positioned 5 cm horizontal from the center of the tipping bucket and 15.5 cm above the base of the bucket (both measurements are made from the center of the pivot). The volume of one tip from the tipping bucket is expected to be 16.26 liters.


From the holding tank, wastewater will empty into a flow dividing bucket. The purpose of the flow dividing bucket is to ensure that the four influent pipes receive an equal inflow of wastewater.  The flow dividing bucket is partitioned into four equal sections. Each of the four sections then empties out into a separate inlet pipe. It is imperative that each section in the flow dividing bucket is full of wastewater before the wastewater starts flowing into the influent pipes. It is also desirable for the flow dividing tank to empty out completely between each dump of the tipping bucket as a de-clogging mechanism. These constraints mean that the flow dividing tank should be similar in volume to the tipping bucket, the bottom of the flow dividing tank should be in line with the water line in the reactor, and the diameter of influent pipes should be small enough so that the pipes only start emptying into the larger tank once the flow dividing tank is full. [WORK ON PYTHON DOCUMENTATION FOR THESE CONSTRAINTS!! NB]

The Summer 2018 UASB team suggested 2 influent pipes, but after considering the results of the tapioca tests performed by the Fall 2018 team, the Spring 2019 UASB team decided to use four influent pipes to promote even distribution of flow through the sludge blanket. The team also decided to use one inch inner diameter pipes for the  influent pipes. The team made that decision based on two constraints: a diameter much smaller than one inch would be more likely to cause clogging and a diameter much larger than one inch would be less effective in promoting even flow through influent tubes. Larger pipes will not restrict water flow as well as smaller pipes; thus, if the tipping bucket unevenly distributes the water into the flow dividing tank and leads to larger pipes, more water can enter certain pipes than others, which would result in more of an uneven flow in comparison to a flow dividing tank that leads to smaller pipes. These constraints will be explained in more depth in the python documentation. [GO BACK AND REPHRASE THIS ONCE WE HAVE WORKED OUT THE CODE MORE]


In order for that to happen, the water level inside of the reactor must be just above the bottom of the tipping bucket holding tank. Assuming that the tank is about 80% full of liquid, the height of the water in the tank would be roughly 5 ft[diagram showing the heights of water in both flow dividing tank and reactor would be helpful]. The team can set this level during the startup phase by adding water/sludge to the reactor until the desired height is reached. Based on that calculation, the team decided that the bottom of the holding tank/top of the flow dividing bucket should be at a height of 58.8 in to ensure the flow dividing bucket is completely filled before wastewater begins flowing into the inlet pipes.

For the flow dividing tank, we chose a 6 gallon 12" by 12" by 12" polyethylene tank (https://www.usplastic.com/catalog/item.aspx?itemid=124470). The bucket will be divided into four equally sized sections by walls of 1.5" thickness. We chose this tank so that four 3.5” diameter holes (to house influent pipes) and two 1.5” wide dividing walls could fit on the bottom area of the tank while also minimizing the horizontal space around holes because settling could occur there.


<img src="https://github.com/AguaClara/UASB/blob/master/Images/Top%20View%20Divide.png?raw=true">
Figure 3. A view from above of the holding tank, which leads into the flow dividing tank is shown above.


<img src="https://github.com/AguaClara/UASB/blob/master/Images/Side%20View%20Holding%20Tank.png?raw=true">
Figure 4. Side view of the holding tank, which leads into the flow dividing tank.

<img src="https://github.com/AguaClara/UASB/blob/master/Images/Bottom%20Dividing%20Tank.png?raw=true">
Figure 5. The dimensions for bottom of the flow dividing tank.  (measurements are in inches)


[Nice figures]

Since the flow dividing bucket is 12” tall, the top of the influent pipes will begin at 46.8” above the ground.

Each inlet pipe will then c~a~rray wastewater to a point on the bottom of the reactor. The team has positioned the four points of influence are as far away from each other as possible on the bottom of the reactor. The bottom of the UASB reactor has a diameter of 3 ft. So, if the center of the reactor is considered to be the origin, then the four points of influence on the bottom of the reactor in polar coordinates will be: (9”, $pi$/4 rad), (.9”, 3$pi$/4 rad), (9”, -$pi$/4 rad), (9”, -3$pi$/4 rad)


<img src="https://github.com/AguaClara/UASB/blob/master/Images/Points%20of%20Influence.png?raw=true">
Figure 6. The points of influence on the bottom of the reactor.

After the team decided on the locations for the points of influence on the bottom of the reactor, it moved on to deciding how to connect each pipe from the flow divider to its respective point of influence. In doing so, the team took effort to reduce head loss of the pipes and make the exiting velocity at each point of influence as equal as possible.

The pipes carrying wastewater away from the flow dividing bucket are vertical. Then, the wastewater needs to be directed to enter the side of the reactor in the horizontal direction (horizontal entry was decided on for ease of fabrication, since it would be difficult to drill ellipses into the UASB reactor to allow for diagonal entry). The team considered using 135 degree elbows instead of 90 degree elbows to minimize horizontal flow, as settling is more likely to occur in horizontal pipes. However, after floating the idea at a technical feedback session, the team realized that such pipes may not be readily available in Honduras, and decided to use 90 degree elbows in the design. https://www.homedepot.com/p/3-in-PVC-DWV-90-Degree-H-x-H-Vent-Elbow-C4807VHD3/205799553


The UASB design team decided that the holding tank should be directly attached to the side of the reactor. This was based on reducing horizontal influent pipe distances, to reduce settling, and to ensure the reactor is compact.[Looks like a run-on sentence..] Since the flow dividing tank be filled with wastewater and hold the tipping bucket system, it will need to be held up by additional supports on the ground. To do so, the team will use 80-20 extrusion bars on opposite sides of the flow dividing bucket.

Next, the team decided where the influent pipes would enter the side of the reactor. The team decided to have the pipes enter the reactor horizontally near the bottom of the reactor to limit the vertical length of influent pipe inside the sludge blanket because during tapioca tests in fall 2018 semester, the team noticed that preferential pathways tended to form around vertical sections of pipe in the sludge blanket. With that in mind, the team decided to have points enter the reactor near the ground to reduce the amount of vertical pipe running through the sludge blanket. The team decided to have pipes enter the reactor at heights of 10 inches and 20 inches above the ground (where the distance is measured from the bottom of the pipe). Then, each pipe will travel horizontally until it is above its respective point of influence, at which point water will be directed down to the bottom of the reactor with a 90 degree elbow. Finally, each pipe will travel vertically until it is 1 inch above the bottom of the reactor. At this point, wastewater will exit into the reactor, hit the bottom, and then begin flowing upwards through the sludge blanket.

![Reactor Influent Design](https://github.com/AguaClara/UASB/blob/master/Images/pipe%20influent%20system.PNG?raw=true)
Figure 7. Influent Design Entering Reactor
[If you have more diagrams to demonstrate where the pipes enter the reactor that would be great. Pictures of the reactor would also help, even if they are subject to future changes]

Based on the height of the flow dividing bucket and the height of the points of entry on the side of the reactor, the team determined the length of influent tube sections. Dimensions are summarized in the sketch below, which is a side view of the UASB. Supports for the flow dividing bucket are not included.


<img src="https://github.com/AguaClara/UASB/blob/master/Images/full%20plant%20-%20design%201.PNG?raw=true">
Figure 7. Full UASB Design 1
[Agree with ananya this pic is a little busy]


The dimensions still need to be slightly altered to account for the size of elbows.


<img src="https://raw.githubusercontent.com/AguaClara/UASB/master/Images/CAD%20Influent%20System.png?raw=true">
Figure 8. Influent bucket system


<img src="https://raw.githubusercontent.com/AguaClara/UASB/master/Images/CAD%20Bucket%20and%20Frame.png?raw=true">
Figure 9. Bucket system without tank

##Future Work
The next step for UASB design is to design the frame using 80 20 extrusions that will support the influent system. The team will also use hydraulic code from previous teams to get an estimate for the exit velocity of water entering the UASB. Upon completing the design for the frame, the team will fabricate the influent system based on its design and begin testing it with water.

We also still need to figure out the optimal height for  the influent pipes will be entering the tank. The research team is currently testing whether the entry of influent pipes above the sludge or the entry of influent pipes close to the bottom will result in less preferential pathways. Once we receive this information, we can finalize on the sections of the length of the pipes that will be vertical and horizontal.

The team’s goal is to have the influent system built by March 11 and begin testing.


##Python Documentation
From the holding tank, wastewater will empty into a flow dividing bucket. The purpose of the flow dividing bucket is to ensure that the four influent pipes receive an equal inflow of wastewater.  The flow dividing bucket is partitioned into four equal sections. Each of the four sections then empties out into a separate inlet pipe. It is imperative that each section in the flow dividing bucket is full of wastewater before the wastewater starts flowing into the influent pipes. It is also desirable for the flow dividing tank to empty out completely between each dump of the tipping bucket as a de-clogging mechanism. These constraints mean that the flow dividing tank should be similar in volume to the tipping bucket, the bottom of the flow dividing tank should be in line with the water line in the reactor, and the diameter of influent pipes should be small enough so that the pipes only start emptying into the larger tank once the flow dividing tank is full.
```python
from aguaclara.core.units import unit_registry as u
from aguaclara.core import physchem as pc
from aguaclara.core import pipes as pipes
from aguaclara.core import utility as ut
from aguaclara.core import constants as con
from aguaclara.research import floc_model as fm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

vol_dump=16.26 * u.L #volume from one dump of the tipping bucket. This will need to be confirmed with testing once we have fabricated altered design for tipping bucket
W_FDT= #width of the flow dividing tank
SA_FDT=width_FDT**2 #surface area of bottom of flow dividing tank

height_FDT= #height of flow dividing tank
W_FDW= #width of flow dividing walls
def head_gain_per_dump(vol_dump, SA_FDT, ):
  ##this is the assumed head gain if flow splits evenly in the flow dividng tank and does not start emptying out until the tip is over


D= #tube diameter, only certain tubing diameters are manufactured (like x16 inch), so an array of available tube diameters is set initially.

#we want flow dividing tank to drain entirely between dumps of tipping bucket
t_drain #is our major constraint. we want time to be slow enough so that  

def t_drain():
  ##time for the flow dividing tank to drain. This time should be slow enough so that in case the bucket initially fills up just one division of flow dividing tank, it will not begin emptying out until overflow reaches other sections BUT fast enough so that the tank completely drains out between successive dumps of the tipping bucket for self cleaning purposes.  




```
