## UASB Design, Spring 2019
By Nina Blahut, Shania Fang,  Emily Liu, Kanha Matai
March 15, 2019

## Abstract
Since Spring 2017, the AguaClara Upflow Anaerobic Sludge Blanket (UASB) Team has been working on a detailed design for a pilot-scale, gravity-powered UASB reactor. A UASB reactor treats wastewater anaerobically and produces biogas as a by-product.

During [Perhaps during instead of over. This is just a stylistic preference] Spring 2019, the UASB-Design team's main goal will be [want to use future tense] to  finalize the design for the UASB and support the design with substantial Python code and CAD designs. So far, the team has completed a general CAD design on Onshape for the entire UASB reactor.

##Introduction
In the past, AguaClara has focused on creating sustainable and inexpensive drinking water treatment; however, it is currently expanding to wastewater treatment. The completion of a pilot UASB reactor that will be tested with influent [influent] wastewater entering [entering] Ithaca Area Wastewater Treatment Facility [Plant] (IAWWTF) will be a big step for AguaClara’s venture into sustainable wastewater treatment. [I suggest that you briefly explain that AguaClara only has experience in drinking water treatment since this intro is BEFORE literature review where that is explained. The assumed audience is not me, but someone who is unfamiliar with AguaClara] There is still much that needs to be further discovered and refined, such as whether or not the tipping bucket system will be useful in eliminating preferential pathways, the effluent system design, and the gas capture system.
In the past, AguaClara has focused on creating sustainable and inexpensive drinking water treatment; however, it is currently expanding to wastewater treatment. The completion of a pilot UASB reactor that will be tested with influent [influent] wastewater entering [entering] Ithaca Area Wastewater Treatment Facility [Plant] (IAWWTF) will be a big step for AguaClara’s venture into sustainable wastewater treatment. [I suggest that you briefly explain that AguaClara only has experience in drinking water treatment since this intro is BEFORE literature review where that is explained. The assumed audience is not me, but someone who is unfamiliar with AguaClara] In an UASB reactor, wastewater will flow through a sludge blanket, composed of millions of methane-producing bacteria which will consume many of the organic pollutants in the water. As a result, wastewater can now be recycled for recreational activities and put back into the environment safely. There is still much that needs to be further discovered and refined, such as whether or not the tipping bucket system will be useful in eliminating preferential pathways, the effluent system design, and the methane gas capture system.

## Literature Review and Previous Work

According to [US Geological Survey](https://water.usgs.gov/edu/wuww.html) (USGS), Wastewater is any kind of water used by humans. This used water may include dissolved fecal and urine matter, harmful chemicals, pathogens, and many more pollutants. Because it is full of contaminants it's not longer safe for use. [where does all this stuff come from? ie mention sewage, industry, etc.] Because water is a universal solvent, it becomes difficult to separate the water from these harmful compounds. These compounds come from a variety of sources such as household wastes from toilets, sinks, baths, and drains or from factories, farming, schools, and urban runoff. As a result, billions of gallons of wastewater is produced and yet many areas in the world still lack access to wastewater treatment plants, thus making waster water a global issue.[What's wastewater?] Leaving wastewater untreated and releasing it directly back into the environment can produce devastating effects on both the environment and human health. [last sentence of the paragraph would probably work better as the 2nd to explain where the contaminants come from]

Wastewater can also contain decaying organic matter and nutrients such as phosphorus and nitrogen which can cause algae blooms and thus eutrophication. [to be specific... eutrophication (excess nutrients) causes algae blooms, which only create anoxic conditions when large amounts of algae die off and require lots of oxygen to decompose] To be specific, eutrophication is the process where excess nutrients, specifically phosphorus or nitrogen, can cause algae to bloom quickly and in large amounts thus creating anoxic conditions because when large amounts of algae die off, they require lots of oxygen to decompose. This negatively impacts the ecosystem because the lack of oxygen makes it harder for aquatic life to survive. At high concentrations,[at high concentrations, organic matter and nutrients are naturally found in low concentrations] these water pollutants are killing marine birds, crustaceans, sea weeds, and many other organisms. Having too much nitrogen in water can also be dangerous for humans because it can cause methemoglobinemia(blue baby syndrome)by preventing normal uptake of oxygen in the blood.

Human health is also directly affected by a lack of wastewater treatment. Much of untreated wastewater eventually ends up in our rivers, streams, and sometimes ground water. It is often assumed that groundwater is pure and clean; however, it is possible for groundwater to get contaminated by have wastewater seep into the ground. ([Catherine Taylor & Joseph Yahner, 1996](https://engineering.purdue.edu/~frankenb/NU-prowd/disease.htm)). When wastewater reaches drinking water sources, it can pose significant health risks for the community. Pathogens in wastewater are [are] destroying crop production, infecting our food supply, and [causing] causing water-borne diseases. Some of the many bacteria, viruses, and parasites present in wastewater include: cholera, typhoid, giardiasis and  cryptosporidiosis. ([Catherine Taylor & Joseph Yahner, 1996](https://engineering.purdue.edu/~frankenb/NU-prowd/disease.htm)). Health risks associated with wastewater includes respiratory disease, cancer, diarrheal disease, a neurological disorder, and cardiovascular disease ([Mehtab Haseena, 2017](http://www.alliedacademies.org/articles/water-pollution-and-human-health-7925.html)).
[I think you can hyperlink these instead of just slapping them here. No links in the middle of paragraphs!]

Some of the biggest issues that wastewater treatment plants face today are energy consumption and environmental footprints. Wastewater facilities [typically] typically have [treatment processes that include] treatment processes that include preliminary treatment, sedimentation, chlorination, and processing sludge which are all electrically and fuel powered ([AOS, 2018](https://aosts.com/how-much-energy-does-wastewater-treatment-plant-use/)). In 2018[what year?], there are about 14,748 wastewater treatment plants in the US and electricity accounts for 90-95% of the total energy consumed at these facilities while the rest is accounted by fuels such as oil or natural gas. ([University of Michigan, 2019](http://css.umich.edu/factsheets/us-wastewater-treatment-factsheet)). Wastewater Treatment plants end up using up about 3% of the nation’s total energy consumption([MGOe, 2019](https://www.mge.com/saving-energy/business/bea/article_detail.htm?nid=%202431)). However, not all countries have access or can afford [to what?] the same resources such as money, infrastructure, materials, and [infrastructure(or technology, etc)] technology, which makes having universal wastewater treatment plants not feasible in many parts of the world, especially more rural and less developed areas.

[Traditional] Traditional UASB reactors are used as a preliminary wastewater treatment process to remove suspended solids organic matter in wastewater (Chong et. al, 2012). UASB reactors, instead of using fuel or electricity, rely mainly on gravity and biological processes to remove organic matter and convert it to biogas. UASB stands for upflow anaerobic sludge blanket and a UASB reactor is a single tank process where wastewater enters the reactor and flows upward through a suspended sludge blanket. This suspended sludge blanket is made up of cultures of anaerobic microorganisms that filters and cleans wastewater by removing organic contaminants and pathogens. UASB reactors are highly efficient in treating high COD loads, biogas formation, and provide good stabilization of solids([M.K. Daud, 2018](https://www.hindawi.com/journals/jchem/2018/1596319/)).They are less energy intensive than other forms of preliminary wastewater treatment that use aerobic processes. UASB reactors also produce methane as a byproduct of anaerobic digestion which can be captured and used for energy production or heating. However, these UASB reactors still rely on electricity.

AguaClara, on the other hand, has designed a UASB reactor that solely relies on gravity. It’s main function is to improve the accessibility [and affordability?] and affordability of wastewater treatment for smaller communities that don’t have access to electricity. In January 2017, this gravity-powered UASB reactor was designed for the EPA People, Prosperity and the Planet (P3) Student Design Competition proposal. The proposed UASB reactor design focused on improving reactor design, making the system cheaper and easier to fabricate so [that] that it [could] could be created globally. The team later applied for Phase II funding from the same organization to support the development and implementation of additional reactors for testing and received a grant of $75,000.

**Summer 2018**
In Summer 2018 the team worked on [the] the hydraulic design of the UASB system and created a tipping bucket system which delivered wastewater [come on guys how did you miss this one? it's red on my atom] in large pulses at a high flow rate. The team had two possible designs for the influent system--one option was for influent tubes to enter either at the top of the UASB reactor, and the alternative was for influent tubes to enter the UASB reactor at the bottom [where? at the bottom?]. The team also focused on biogas storage and came up with three types of storage: Gas Bag, Fixed Lid, and Floating Lid. They later decided that a gas bag system was both cost effective and transportable for community systems.

**Fall 2018**
Preferential pathways in wastewater treatment when occur when incoming wastewater forms a tunnel through the sludge blanket instead of flowing evenly through the blanket; consequently, not all of the wastewater gets in contact with sludge granules, and it’s not effectively cleaned. [What did the team find? before you conclude anything... All you've done is say that they researched preferential pathways and explain what pref pathways are. I assume that pref pathways were a problem since it can be a problem in WW treatment in general but it is not explicitly said that Fall2018 UASB found pref flow to be a problem] In Fall 2018, the UASB team researched preferential pathways in UASBS by doing bench tests. The team fabricated a small scale UASB reactor used chia seeds, marbles, and tapioca to simulate sludge. UASB team found that preferential flow patterns were likely to occur. The team concluded that it will likely be necessary to have several influential pipes to promote the even distribution of wastewater flow and decrease preferential pathways.
[maybe a diagram/picture would help with this explanation] [ADD PICTURE FROM PREVIOUS RED DYE TESTS SHOWING PREFERENTIAL FLOW]
<p align="center">
  <img src="https://github.com/AguaClara/UASB/blob/master/Images/UASB_Red_Dye_Tapioca_Test.PNG?raw=true=50x" width="250px" /></p>
<p align="center">Fig. 1: Preliminary dye tests with tapioca showing preferential pathways<p>


In the Spring 2019 semester, the team will focus on finalizing the UASB pilot-scale reactor design which will be tested in Ithaca’s Wastewater Treatment Plant by the Summer of 2020.


## Methods

### Design for Influent System

In this section, the team will explain how it made decisions regarding the design for the influent system.

For the influent system, the team has decided to move forward with the Summer 2018 team's design in which a tipping bucket empties wastewater into a holding tank, which will then empty into a flow dividing bucket connected to influent pipes that lead into the side of the reactor. The team will also move forward with the Summer 2018 team’s plan to use a [300 gallon reactor tank](https://www.plastic-mart.com/product/17049/300-gallon-plastic-tank-rotoplas-590314-590315) that has a 36” diameter and 72” height.

The team has decided to use high density polyethylene (HDPE) for the majority of the plastic parts of the UASB, such as the influent pipes and the 300 gallon reactor tank, will need to be welded together. HDPE was chosen because it is durable and corrosion resistant, and large tanks made of HDPE, unlike PVC, are available. HDPE can mainly be welded together with other HDPE materials whereas welding it with PVC or LDPE wouldn't be feasible.

A design for the tipping bucket was completed by the summer 2018 team.
![Summer 2018 tipping bucket design](https://github.com/AguaClara/UASB/blob/master/Images/Influent_Tank_Tipping_Bucket.png?raw=true)

Figure 2. Summer 2018 Final Tipping Bucket design

This semester, the team realized an issue with the previous team's tipping bucket design: the frame for the tipping bucket is metal. This is an issue because the metal frame would get wet from splashing water and then rust. To combat this issue, the team will alter the design of the tipping bucket, so that there are no metal parts. The revised tipping bucket will be made by welding HDPE plates to the sides of a 5 gallon HDPE bucket, then welding HDPE rods onto those plates, which will be used to mount the tipping bucket in the holding tank.


Certain elements from the previous team's tipping bucket design, including the volume of the tipping bucket and the locations of the pivots with respect to the bucket's center will remain the same. The previous team determined the optimal location of pivots by performing tests with pivots in various positions and selecting the locations in which the tipping bucket filled the most while still emptying completely.

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

From the holding tank, wastewater will empty into a flow dividing tank. The purpose of the flow dividing tank is to ensure that the four influent pipes receive an equal inflow of wastewater.  The flow dividing tank is partitioned into four equal sections. Each of the four sections then empties out into a separate inlet pipe. It is imperative that each section in the flow dividing tank is full of wastewater before the wastewater starts flowing into the influent pipes so that each pipe will distribute the same amount of water inside the reactor. It is also desirable for the flow dividing tank to empty out completely between each dump of the tipping bucket as a de-clogging mechanism. These constraints mean that the flow dividing tank should be similar in volume to the tipping bucket, the bottom of the flow dividing tank should be in line with the water line in the reactor, and the diameter of influent pipes should be small enough so that the pipes only start emptying into the larger tank once the flow dividing tank is full. All of these constrains are delved in

In order for the de-clogging mechanism to happen, the water level inside of the reactor must be just above the bottom of the flow dividing tank. Assuming that the reactor is about 80% full of liquid, the height of the water in the reactor would be roughly 5 ft[diagram showing the heights of water in both flow dividing tank and reactor would be helpful]. The team can set this level during the startup phase by adding water/sludge to the reactor until the desired height is reached. Based on the previous calculation, the team decided that the bottom of the flow dividing tank should be at a height of 58.8 inches to ensure the flow dividing tank completely empties.

The Summer 2018 UASB team suggested 2 influent pipes, but after considering the results of the tapioca tests performed by the Fall 2018 team, the Spring 2019 UASB team decided to use four influent pipes to promote more even distribution of flow through the sludge blanket. The Summer 2018 UASB team also suggested that the influent pipe diameter range from 75-100mm to reduce clogging. However, the current team has decided to decrease the diameter of the influent pipe to range from 1-2 inches. The team made that decision based on two constraints: a diameter much smaller than one inch would be more likely to cause clogging and a diameter much larger than one inch would be less effective in promoting even flow through influent tubes. Larger pipes will not restrict water flow as well as smaller pipes; thus, if the tipping bucket unevenly distributes the water into the flow dividing tank and leads to larger pipes, more water can enter certain pipes than others, which would result in more of an uneven flow in comparison to a flow dividing tank that leads to smaller pipes. These constraints will be explained in more depth in the python documentation. [GO BACK AND REPHRASE THIS ONCE WE HAVE WORKED OUT THE CODE MORE]

Figure 3. Top view of the holding tank, which leads into the flow dividing tank.
<img src="https://github.com/AguaClara/UASB/blob/master/Images/Top%20View%20Divide.png?raw=true">

Figure 4. Side view of the holding tank, which leads into the flow dividing tank.
<img src="https://github.com/AguaClara/UASB/blob/master/Images/Side%20View%20Holding%20Tank.png?raw=true">


[Nice figures]
Figure 5. The dimensions for bottom of the flow dividing tank.  (measurements are in inches)
<img src="https://github.com/AguaClara/UASB/blob/master/Images/Bottom%20Dividing%20Tank.png?raw=true">

Each inlet pipe will then carry wastewater to a point on the bottom of the reactor. The team has positioned the four points of influence are as far away from each other as possible on the bottom of the reactor. The bottom of the UASB reactor has a diameter of 3 ft. So, if the center of the reactor is considered to be the origin, then the four points of influence on the bottom of the reactor in polar coordinates will be: (9”, $pi$/4 rad), (.9”, 3$pi$/4 rad), (9”, -$pi$/4 rad), (9”, -3$pi$/4 rad)

Figure 6. The points of influence on the bottom of the reactor.
<img src="https://github.com/AguaClara/UASB/blob/master/Images/Points%20of%20Influence.png?raw=true">

After deciding on the locations for the points of influence on the bottom of the reactor, the team discussed ways to reduce head loss from horizontal piping. Thus, the holding tank will be attached to the side of the reactor to reduce head loss but to also reduce settling and to ensure the reactor is compact. In addition, the team discussed how to connect each pipe from the flow divider to its respective point of influence. In doing so, the team attempted to reduce head loss of the pipes and make the exiting velocity at each point of influence as equal as possible. [Looks like a run-on sentence..]

The pipes carrying wastewater away from the flow dividing bucket are vertical. Then, the wastewater needs to be directed to enter the side of the reactor in the horizontal direction (horizontal entry was decided for ease of fabrication, since it would be difficult to drill ellipses into the UASB reactor to allow for diagonal entry). The team considered using 135 degree elbows instead of 90 degree elbows to minimize horizontal flow, as settling is more likely to occur in horizontal pipes. However, after floating the idea at a technical feedback session, the team realized that such pipes may not be readily available in Honduras, and decided to use [90 degree](https://www.homedepot.com/p/3-in-PVC-DWV-90-Degree-H-x-H-Vent-Elbow-C4807VHD3/205799553) elbows in the design.

Next, the team decided the influent pipes would enter the same side of the reactor. The pipes will enter the reactor horizontally near the bottom of the reactor to limit the vertical length of influent pipe inside the sludge blanket because during tapioca tests in fall 2018 semester, the team noticed that preferential pathways tended to form around vertical sections of pipe in the sludge blanket. With that in mind, the team decided to have points enter the reactor near the ground to reduce the amount of vertical pipe running through the sludge blanket. The team decided to have pipes enter the reactor at heights of 10 inches and 20 inches above the ground (where the distance is measured from the bottom of the pipe). Then, each pipe will travel horizontally until it is above its respective point of influence, at which point water will be directed down to the bottom of the reactor with a 90 degree elbow. Finally, each pipe will travel vertically until it is 1 inch above the bottom of the reactor. At this point, wastewater will exit into the reactor, hit the bottom, and then begin flowing upwards through the sludge blanket.

![Reactor Influent Design](https://github.com/AguaClara/UASB/blob/master/Images/pipe%20influent%20system.PNG?raw=true)
Figure 7. Influent Design Entering Reactor
[If you have more diagrams to demonstrate where the pipes enter the reactor that would be great. Pictures of the reactor would also help, even if they are subject to future changes]


<img src="https://github.com/AguaClara/UASB/blob/master/Images/full%20plant%20-%20design%201.PNG?raw=true">
Figure 8. Full UASB Design 1
[Agree with ananya this pic is a little busy]
>>>>>>> ec3335e45361f88836d4df03bc14ad0458cb1952


The dimensions still need to be slightly altered to account for the size of elbows.


<img src="https://raw.githubusercontent.com/AguaClara/UASB/master/Images/CAD%20Influent%20System.png?raw=true">
Figure 9. Influent bucket system


<img src="https://raw.githubusercontent.com/AguaClara/UASB/master/Images/CAD%20Bucket%20and%20Frame.png?raw=true">
Figure 10. Bucket system without tank

## Future Work
In order to reach the goal of fabrication, UASB Design must also complete the design for the effluent system, gas collection, and support system while considering materials for the entire reactor.

After deciding that the majority of the UASB reactor will be made up of HDPE, more research has to be done in finding pipes and reactor tank made up of this material. For the biogas, instead of using a ballon contraption to collect methane gas, a bubble counter meter will be used to see how much biogas is being created. Once the design is finished, the methane gas will be burned off by a mechanism in the Ithaca's Waste Water Treatment Facility.

For the effluent system a valve needs to be added at the end to ensure there will be consistent effluent flow and make maintenance accessibility easier. Since the effluent pipe will begin extruding out from the UASB reactor upwards at 60 degrees to make sure the sludge granules settle back into the reactor, the team also has to figure out a way to add a pipe going vertically upwards through the effluent pipe to make sure atmospheric pressure is the same throughout. If atmospheric pressure can be maintained through the fabrication of the vertical pipe, the effluent pipe will ideally bend at the middle from upwards 60 degrees to a downwards vertical pipe that empties the effluent. Unfortunately, finding 30 degree connections are rather difficult to find in Honduras, so the team has yet to settle on a design of the effluent pipe.

Initially to support the influent system and pipes, the team had decided to use 80/20 extrusions; however, upon further consideration of the environment in which the reactor will be tested, the team will prioritize materials that are resistant to rusting and easily maintained but also able to support heavy objects.

The team will also rely on hydraulic code from previous teams to get an estimate for the exit velocity of water entering the UASB. Upon completing the design for the frame, the team will fabricate the influent system based on its design and begin testing it with water.

The optimal height and cross-sectional area for the influent pipes to be entering the tank still needs to be determined so that the flow of wastewater passing through the sludge will be around .0069 m/s - .02778 m/s . It is desirable for the upflow velocity to be faster than the velocity of the sludge granules settling to keep the bed fluidized but not too fast where the granules will washout because of inadequate residence time. The research team is currently testing whether the entry of influent pipes above the sludge or the entry of influent pipes close to the bottom will result in less preferential pathways. Once UASB design receive this information, the team can finalize on the sections of the length of the pipes that will be vertical and horizontal.



## Python Documentation
From the holding tank, wastewater will empty into a flow dividing bucket. The purpose of the flow dividing bucket is to ensure that the four influent pipes receive an equal inflow of wastewater.  The flow dividing bucket is partitioned into four equal sections. Each of the four sections drains into a separate inlet pipe. It is desired that each section in the flow dividing bucket is full of wastewater before the wastewater starts flowing into the influent pipes, to ensure even flow. It is also desirable for the flow dividing tank to empty out completely between each dump of the tipping bucket as a de-clogging mechanism. These constraints mean that the flow dividing tank should be similar in volume to the tipping bucket and the bottom of the flow dividing tank should be in line with the water line in the reactor.  Lastly, the time it takes for the flow dividing tank to drain should be slow enough so that in case the bucket initially fills up just one division of flow dividing tank, it will not begin emptying out until overflow reaches other sections, but fast enough so that the tank completely drains out between successive dumps of the tipping bucket for self cleaning purposes and so that up flow velocity of influent water is fast enough to lift settling sludge particles. This drain time is determined by the diameter of the influent pipes and the head gain per dump of the tipping bucket, and the ensuing code will be used to determine the optimal combination of influent pipe diameter and flow dividing tank geometry to achieve said drain time.

Important note is that the water level of the reactor is set at the same height as the bottom of the flow dividing tank.
```python
from aguaclara.core.units import unit_registry as u
from aguaclara.core import physchem as pc
from aguaclara.core import pipes as pipes
from aguaclara.core import head_loss as HL
from aguaclara.core import utility as ut
from aguaclara.core import constants as con
from aguaclara.research import floc_model as fm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

vol_d=16.26 * u.L #volume from one dump of the tipping bucket. This will need to be confirmed with testing once we have fabricated altered design for tipping bucket

def max_t_drain(vol_dump, Q):
  """time between dumps of tipping bucket, this should be maximum drain time so that the bucket will empty out between each dump, for cleaning and clog identification."""
  t=vol_dump/Q
  return t.to(u.s)

def H_walls(vol_dump, W_FDT, t_walls,overflow_H):
  """this function calculates the height of the flow dividing walls, so that if a complete tip were to fill the flow dividing tank before it started draining out, the water level would be an inch above the top of the flow dividing tank. vol_dump=volume from one dump from tipping bucket; W_FDT=width of flow dividing tank; t_walls=thickness of the flow dividing walls; overflow_H=desired height of overflow over walls"""
  H_walls=(vol_dump-overflow_H*W_FDT**2)/(W_FDT**2-t_walls*W_FDT-t_walls*(W_FDT-t_walls)) #calculate H_walls by setting vol_dump equal to volume inside flow dividing system accounting for the volume that the flow dividing walls occupy
  H_walls=H_walls.to(u.inch)
  return H_walls


W_FDT_test= 12*u.inch #width of flow dividing walls
t_walls_test=1.5*u.inch
vol_dump_test=17 *u.L
overflow_test=1*u.inch  

H_walls_test=H_walls(vol_dump_test, W_FDT_test, t_walls_test, overflow_test)
print(H_walls_test)

def min_H_FDT(H_walls, overflow_H):
  """This function returns the minimum height of flow dividing tank."""
  min_H=head_gain_per_dump(H_walls, overflow_H)

def head_gain_per_dump(H_walls, overflow_H):
  """this is the assumed head gain if flow splits evenly in the flow dividing tank and does not start emptying out until the tip is over."""
  HG=H_walls+overflow_H
  HG=HG.to(u.inch)
  return HG

HG_per_dump_test=head_gain_per_dump(H_walls_test, overflow_test)
print(HG_per_dump_test)

def influent_K(n_90el):
  """this function calculates the minor loss coefficient of one of the influent pipes into the overall reactor. n_90elbows=number of 90 elbows in an influent pipe, D_pipe is the diameter of an influent pipe. Chose to calculate for minor loss because in the UASB design, minor losses are much more significant than major lossess."""
  influent_K=n_90el*HL.EL90_K_MINOR+HL.PIPE_EXIT_K_MINOR+HL.PIPE_ENTRANCE_K_MINOR
  return influent_K

def t_drain_fail_case(D_pipe, W_FDT, H_walls, n_90el):
  """ this function is meant to test fail case, to see how long it will take a section to drain in the case that all of the water from a tipping bucket dump goes into only one section of the flow dividing tank """
  A_FDT=W_FDT**2 #calculate the area of the flow dividing tank
  K_tot=influent_K(n_90el)
  t_drain=8*A_FDT/(np.pi*D_pipe**2)*(H_walls*K_tot/(2*pc.gravity))**.5 #from equation (97) in FCM_derivations section in AguaClara textbook
  return t_drain.to(u.s)

##Testing the function  t_fail_case
D_pipe_test=1*u.inch
n_90el_test=3
t_drain_fail_case_test=t_drain_fail_case(D_pipe_test, W_FDT_test, H_walls_test, n_90el_test)
print('If the influent pipes have a diameter of', D_pipe_test, 'and the width of the flow dividing tank is', W_FDT_test, 'then if all of the water went into only one section of of the flow dividing tank, that sections would take', t_drain_fail_case_test, ' to drain.')

def t_drain_even(D_pipe, W_FDT, H_walls, overflow_H, n_90el):
  """This function returns the estimated drain time from the FDT in the case that water from the tipping bucket fills up the sections evenly and quickly, so that water doesn't start draining until each section is full of water/there is water overflowing the dividing walls. headgain=headgain per dump """
  A_FDT=W_FDT**2 #calculate the area of the flow dividing tank
  K_tot=influent_K(n_90el)
  HG= head_gain_per_dump(H_walls, overflow_H)
  t_drain=8*A_FDT/(np.pi*D_pipe**2)*(HG*K_tot/(2*pc.gravity))**.5 #from equation (97) in FCM_derivations section in AguaClara textbook
  return t_drain.to(u.s)


t_drain_even_test=t_drain_even(D_pipe_test, W_FDT_test, H_walls_test,overflow_test, n_90el_test)  
print('If the influent pipes have a diameter of', D_pipe_test, 'and the width of the flow dividing tank is', W_FDT_test, 'then if all of the water went into only one section of of the flow dividing tank, that sections would take', t_drain_even_test, ' to drain.')



def D_pipe(W_FDT, t_drain, n_90el, H_walls, overflow_H):
  """This function returns the best diameter pipe to get the desired t_drain, given a flow dividing tank and goal drain time for the flow dividing tank. This is calculated based on case where flow divides evenly between sections and does not start draining until dump is complete."""
  A_FDT=W_FDT**2
  H=head_gain_per_dump(H_walls, overflow_H)
  K_tot=influent_K(n_90el)
  D=((8*W_FDT**2)/(np.pi*t_drain))**1/2*((H*K_tot)/(2*pc.gravity))**(1/4) #From equation 96 in AC textbook.
  return D.to(u.inch)

##Testing D_pipe function
Q_test= .08 * (u.L/u.s)#flow rate entering the UASB from Summer 2018 report
t_drain_test=max_t_drain(vol_d, Q_test)
print(t_drain_test)
print(overflow_test)
D=D_pipe(W_FDT_test, t_drain_test, n_90el_test, H_walls_test, overflow_test)

def upflow_vel(t_drain_even, UASB_diameter, vol_dump):
  """this function calculates an estimate for upflow velocity in the UASB reactor assuming that water from the dump is divided evenly into sections and does not start draining until dump is complete. Ideally, this velocity will be as fast settling velocity of sludge particles, which is approximately .007 m/s, to make a fluidized sludge blanket. """
  UASB_Q_dump=vol_dump/t_drain_even ##calculate flow rate through UASB as water from a dump of tipping bucket flows through the system
  UASB_CA=pc.area_circle(UASB_diameter)
  up_vel=UASB_Q_dump/UASB_CA
  return up_vel.to(u.m/u.s)

##Testing upflow_vel function
UASB_diameter_test=3*u.ft
upflow_vel_test=upflow_vel(t_drain_even_test, UASB_diameter_test, vol_d)
print(upflow_vel_test)


##NOW USING HYDRAULIC CODE TO TEST DIFFERENT DESIGN OPTIONS

##will graph drain times versus different pipe sizes with other parameters preset for reasons which are explained in the comment next to each variable assignment.
D_avail= ([.75, 1.0, 1.25, 1.5])*u.inch#array of available HPDE pipes ranging in size from
n_90el= 3 #set n_90el to 3 because there are 3 elbows in each influent pipe in the current design
W_FDT= (9+15/16)*u.inch  #this was selected as the width for the flow dividing tank because a bucket, which similar in volume to that of a tipping bucket dump,with a square bottom and made of HDPE is readily available online
overflow= 1 *u.inch #set overflow as 1 inch--this could be modified to increase driving head if necessary
t_even_drains=(np.zeros(len(D_avail)))*u.s #this array will store the estimated drain time for input UASB design with severable possible diameters
UASB_diameter=3*u.ft
vol_dump = 16.26 *u.L


for i in range(0,len(D_avail)): #populate t_even_drains
  t_even_drains[i]= t_drain_even(D_avail[i], W_FDT, H_walls_test,overflow_test, n_90el_test)

#graph drain times vs diameter
plt.scatter(D_avail, t_even_drains)
plt.xlabel('Influent Pipe Diameter (inch)')
plt.ylabel('Flow Dividing Tank Drain Time (sec)')
plt.title('Estimated Flow Dividing Tank versus Pipe Diameter for Even Flow Division Case')

#now, graphing upflow velocity vs pipe diameter
upflow_vels=(np.zeros(len(D_avail)))*(u.m/u.s) #this array will store the upflow velocities for input UASB design with severable possible diameters

 for i in range(0,len(D_avail)):
  t_even_drains[i]= t_drain_even(D_avail[i], W_FDT, H_walls_test,overflow_test, n_90el_test)
  upflow_vels[i]=upflow_vel(t_even_drains[i], UASB_diameter,vol_dump)

plt.scatter(D_avail,upflow_vels)
plt.xlabel('Influent Pipe Diameter (inch)')
plt.ylabel('Estimated Upflow Velocity (m/s)')
plt.title('Estimated Upflow Velocity if UASB Operates Properly')
plt.ylim((0, .001))   # set the ylim to bottom, top





xArray = u.Quantity(np.arange(5,21), u.inch) #width of tank
section_FDT = plt.plot(xArray, t_drain_fail_case(1*u.inch, xArray, H_walls(vol_d, xArray, t_walls_test, overflow_test), n_90el_test), label='One Section of FDT')
entire_FDT = plt.plot(xArray, t_drain_even(1*u.inch, xArray, H_walls(vol_d, xArray, t_walls_test, overflow_test), overflow_test, n_90el_test), label='Entire FDT')

plt.xlabel('Width of FDT (in.)')
plt.ylabel('Time taken to Drain (sec.)')
plt.title('Time Taken for One Section of the Flow Dividing to Drain vs. Width of Flow Dividing Tank')
plt.minorticks_on()
plt.grid(which = 'major')
plt.grid(which = 'minor')
plt.legend(loc = 'upper right', ncol = 2)
plt.tight_layout()
plt.show()

```

### Future Work for Python Documentation
In the future, the team plants to instantiate a UASB object to represent a real UASB. The team will also do additional research to import more available HDPE tank dimensions and HDPE pipe sizing, so that it can test the available combinations with ease to determine the optimal design for the UASB influent system, and then use that to update the onShape model. The team also needs to do testing with the tipping bucket to make a more informed decision about optimal drain time.

## Bibliography


- AOS Treatment Solutions. “How Much Energy Does a Wastewater Treatment Plant Use?” AOS Treatment Solutions, AOS Treatment Solutions, LLC, March 1 2018, https://aosts.com/how-much-energy-does-wastewater-treatment-plant-use/

- Catherine Taylor & Joseph Yahner. “Wastewater Treatment Protects Small Community Life, Health.” On-Site Wastewater Disposal and Public Health, Purdue University, Summer 1996, https://engineering.purdue.edu/~frankenb/NU-prowd/disease.htm

- Center for Sustainable Systems, University of Michigan. 2018. "U.S. Wastewater Treatment Factsheet." Pub. No. CSS04-14, http://css.umich.edu/factsheets/us-wastewater-treatment-factsheet

- M. K. Daud, Hina Rizvi, Muhammad FarhanAkram, Shafaqat Ali, Muhammad Rizwan,Muhammad Nafees, and Zhu Shui Jin. “Review of Upflow Anaerobic Sludge Blanket Reactor Technology: Effect of Different Parameters and Developments for Domestic Wastewater Treatment.” Journal of Chemistry, Hindawi, 2018, https://www.hindawi.com/journals/jchem/2018/1596319/

- Mehtab Haseena*, Muhammad Faheem Malik, Asma Javed, Sidra Arshad, Nayab Asif, Sharon Zulfiqar and Jaweria Hanif. “Water pollution and human health.” Environmental Risk Assessment and Remediation,Allied Academies, July 13 2017, http://www.alliedacademies.org/articles/water-pollution-and-human-health-7925.html


- MGOe. “Wastewater Treatment Plants.”Your Community Energy Company, Madison Gas and Electric Company, 2019, https://www.mge.com/saving-energy/business/bea/article_detail.htm?nid=%202431


- Perlman, Howard. “Wastewater Treatment Water Use.” The USGS Water Science School, US Geological Survey, Dec. 2 2016, https://water.usgs.gov/edu/wuww.html
