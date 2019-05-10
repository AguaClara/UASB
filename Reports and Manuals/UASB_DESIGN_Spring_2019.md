## UASB Design, Spring 2019
By Nina Blahut, Shania Fang,  Emily Liu, Kanha Matai
March 15, 2019

[What's this achieve## thing here?"-Addressed EL"]

**[Felix: Hey I'm going to be making comments in these square brackets. After addressing any comments please write within the brackets "-Addressed __" with the individual's initials in the __ space. They will be deleted in the next report.]**

## Abstract
Since Spring 2017, the AguaClara Upflow Anaerobic Sludge Blanket (UASB) Team has been working on a detailed design for a pilot-scale, gravity-powered UASB reactor. A UASB reactor treats wastewater anaerobically and produces biogas as a by-product.

During Spring 2019, the UASB-Design team's main goal was to finalize the design for the UASB and support the design with substantial Python code and CAD designs. So far, the team has completed a general CAD design on Onshape for the entire UASB reactor and used python coding to predict how the geometry of the UASB design will influence the up flow velocity of wastewater through the reactor.

## Introduction
In the past, AguaClara has focused on creating sustainable and inexpensive drinking water treatment, and has recently expanded to wastewater treatment. Previously, AguaClara has struggled to find demand for wastewater treatment plants in Nicaragua or Honduras because people were reluctant to invest in a **[a "-Addressed EL"]** system that would not directly affect the health of community members. Fortunately, a growth in awareness in regards to the importance of wastewater treatment as well as funding from EPA for the development of wastewater treatment technologies allowed AguaClara to move forward with its venture into sustainable wastewater treatment. One project AguaClara established for its undertaking in wastewater treatment that of designing and fabricating pilot scale UASB reactor. Upon completion, the pilot UASB reactor will be tested with wastewater at the Ithaca Area Wastewater Treatment Facility (IAWWTF).


 In a UASB reactor, wastewater flows through a sludge blanket. The sludge blanket contains millions of methane-producing bacteria which consume many of the organic pollutants in the wastewater. As a result, effluent from the UASB can be returned to the environment safely. There is still much that needs to be further discovered and refined, such as whether or not the tipping bucket system will be useful in eliminating preferential pathways, the effluent system design, and the methane gas capture system.

## Literature Review and Previous Work

According to [US Geological Survey](https://water.usgs.gov/edu/wuww.html) (USGS), wastewater **[wastewater "-Addressed EL"]** is any kind of water used by humans. This used water may include dissolved fecal and urine matter, harmful chemicals, pathogens, and many more pollutants. Because it is full of contaminants, **[,"-Addressed EL"]** it's not longer safe for use. Because water is a universal solvent, it becomes difficult to separate the water from these harmful compounds. These compounds come from a variety of sources such as household wastes from toilets, sinks, baths, and drains or from factories, farming, schools, and urban runoff. As a result, billions of gallons of wastewater are [are "-Addressed EL"] produced and yet many areas in the world still lack access to wastewater treatment plants, thus making wastewater a global issue. Leaving wastewater untreated and releasing it directly back into the environment can produce devastating effects on both the environment and human health.

Wastewater can also contain decaying organic matter and nutrients such as phosphorus and nitrogen which can cause eutrophication, a term for excess nutrients. Eutrophication then causes algae blooms, leading to oxygen-deprived conditions once the large amount of algae dies off and begins to decompose. This negatively impacts the ecosystem because the lack of oxygen makes it harder for aquatic life to survive. At high concentrations, these water pollutants and organic matter are killing marine birds, crustaceans, sea weeds, and many other organisms. Having too much nitrogen in water can also be dangerous for humans because it can cause methemoglobinemia (blue baby syndrome) by preventing normal uptake of oxygen in the blood.

Human health is also directly affected by a lack of wastewater treatment. Much of untreated wastewater eventually ends up in our rivers, streams, and sometimes ground water. It is often assumed that groundwater is pure and clean; however, it is possible for groundwater to be contaminated by wastewater seeping into the ground. ([Catherine Taylor & Joseph Yahner, 1996](https://engineering.purdue.edu/~frankenb/NU-prowd/disease.htm)). When wastewater reaches drinking water sources, it can pose significant health risks for the community. Pathogens in wastewater destroy crop production, infecting the food supply, and cause water-borne diseases. Some of the many bacteria, viruses, and parasites present in wastewater include: cholera, typhoid, giardiasis and  cryptosporidiosis. ([Catherine Taylor & Joseph Yahner, 1996](https://engineering.purdue.edu/~frankenb/NU-prowd/disease.htm)). Health risks associated with wastewater includes respiratory disease, cancer, diarrheal disease, a neurological disorder, and cardiovascular disease ([Mehtab Haseena, 2017](http://www.alliedacademies.org/articles/water-pollution-and-human-health-7925.html)).

Some of the biggest issues that wastewater treatment plants face today are energy consumption and environmental footprints. Wastewater facilities typically have treatment processes that include preliminary treatment, sedimentation, chlorination, and processing sludge which are all electrically and fuel powered ([AOS, 2018](https://aosts.com/how-much-energy-does-wastewater-treatment-plant-use/)). In 2018, there were about 14,748 wastewater treatment plants in the US and electricity accounts for 90-95% of the total energy consumed at these facilities while the rest is accounted by fuels such as oil or natural gas. ([University of Michigan, 2019](http://css.umich.edu/factsheets/us-wastewater-treatment-factsheet)). Wastewater Treatment plants end up using up about 3% of the nation’s total energy consumption ([MGOe, 2019](https://www.mge.com/saving-energy/business/bea/article_detail.htm?nid=%202431)). However, not all countries have access or can afford the same resources such as money, infrastructure, materials, and technology, which makes having universal wastewater treatment plants not feasible in many parts of the world, especially more rural and less developed areas.

Traditional UASB reactors are used as a preliminary wastewater treatment process to remove suspended solids organic matter in wastewater (Chong et. al, 2012). UASB reactors, instead of using fuel or electricity, rely mainly on gravity and biological processes to remove organic matter and convert it to biogas. UASB stands for Upflow Anaerobic Sludge Blanket and a UASB reactor is a single tank process where wastewater enters the reactor and flows upward through a suspended sludge blanket. This suspended sludge blanket is made up of cultures of anaerobic microorganisms that filters and cleans wastewater by removing organic contaminants and pathogens. UASB reactors are highly efficient in treating high COD loads, biogas formation, and provide good stabilization of solids ([M.K. Daud, 2018](https://www.hindawi.com/journals/jchem/2018/1596319/)).They are less energy intensive than other forms of preliminary wastewater treatment that use aerobic processes. UASB reactors also produce methane as a byproduct of anaerobic digestion which can be captured and used for energy production or heating. However, these UASB reactors still rely on electricity.

AguaClara, on the other hand, has designed a UASB reactor that solely relies on gravity. It’s main function is to improve the accessibility and affordability of wastewater treatment for smaller communities that don’t have access to electricity. In January 2017, this gravity-powered UASB reactor was designed for the EPA People, Prosperity and the Planet (P3) Student Design Competition proposal. The proposed UASB reactor design focused on improving reactor design, making the system cheaper and easier to fabricate so that it could be created globally. The team later applied for Phase II funding from the same organization to support the development and implementation of additional reactors for testing and received a grant of $75,000.

**Summer 2018**
In Summer 2018 the team worked on the hydraulic design of the UASB system and created a tipping bucket system which delivered wastewater in large pulses at a high flow rate. The team had two possible designs for the influent system--one option was for influent tubes to enter either at the top of the UASB reactor, and the alternative was for influent tubes to enter the UASB reactor at the bottom. The team also focused on biogas storage and decided that a gas bag system was the best option. In a gas bag system, gas will flow out of a pipe in the lid of the UASB into a gas bag. Pros of the gas bag system are that it is inexpensive and allows for the easy transport of biogas to communities for use.

**Fall 2018**
Preferential pathways in wastewater treatment occur when incoming wastewater forms a tunnel through the sludge blanket instead of flowing evenly through the blanket; consequently, not all of the wastewater gets in contact with sludge granules, and thus not effectively treated. In Fall 2018, the UASB team researched preferential pathways in UASB by doing bench tests. The team fabricated a small scale UASB reactor used chia seeds, marbles, and tapioca to simulate sludge. The Fall 2018 UASB team found that preferential flow patterns were likely to occur. The team concluded that it will likely be necessary to have several influential pipes to promote the even distribution of wastewater flow and decrease preferential pathways. The figure below shows a tapioca test from the Fall 2018 semester. The uneven distribution of red dye through the tapioca layer indicates that preferential pathways are forming.

![Red Dye Test](https://github.com/AguaClara/UASB/blob/master/Images/UASB_Red_Dye_Tapioca_Test.PNG?raw=true)

**Fig. 1: Preliminary dye tests with tapioca showing preferential pathways<p>**

**Spring 2019**
In the Spring 2019 semester, the team focused on finalizing the UASB pilot-scale reactor design which would be fabricated and tested in Ithaca’s Wastewater Treatment Plant in the Summer of 2020.

## Methods

### Design for Influent System

This section explains how the Spring 2019 team made decisions regarding the design for the influent system.

For the influent system, the team decided to move forward with the Summer 2018 team's design in which a tipping bucket empties wastewater into a holding tank, which will then empty into a flow dividing bucket connected to influent pipes that lead into the side of the reactor. The Summer 2018 team's tipping bucket design is included below in Figure 2.

A design for the tipping bucket was completed by the summer 2018 team.

![Summer 2018 tipping bucket design](https://github.com/AguaClara/UASB/blob/master/Images/Influent_Tank_Tipping_Bucket.png?raw=true)
**Figure 2. Summer 2018 Final Tipping Bucket design**

The team also chose move forward with the Summer 2018 team’s plan to use a [300 gallon reactor tank](https://www.plastic-mart.com/product/17049/300-gallon-plastic-tank-rotoplas-590314-590315) that has a 36” diameter and 72” height.

The team decided to use high density polyethylene (HDPE) for the majority of the plastic parts of the UASB, such as the influent pipes and the 300 gallon reactor tank, would need to be welded together. HDPE was chosen because it is durable and corrosion resistant, and large tanks made of HDPE, unlike PVC, are available. HDPE can be welded together with other HDPE materials whereas welding it with PVC or LDPE is not be feasible.

This semester, the team realized an issue with the previous team's tipping bucket design: the frame for the tipping bucket is metal. This would cause issues as the metal frame would get wet from splashing water and hence rust. To combat this issue, the team altered the design of the tipping bucket to exclude metal parts.

Certain elements from the previous team's tipping bucket design, including the volume of the tipping bucket and the locations of the pivots with respect to the bucket's center will remain the same. The previous team determined the optimal location of pivots by performing tests with pivots in various positions and selecting the locations in which the tipping bucket filled the most while still emptying completely.

**Table 1. Summer 2018 Tipping Bucket Trial Results**
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
Trial 7 of the tipping bucket yielded the most successful results in that the bucket filled the most, while still emptying out all the way. Trials where the bucket did not empty completely were voided because water left in the bucket would cause a build-up of organic matter.

Based on the Summer 2018 team's results, the pivots will likely be positioned 5 cm horizontal from the center of the tipping bucket and 15.5 cm above the base of the bucket (both measurements are made from the center of the pivot). The volume of one tip from the tipping bucket is expected to be 16.26 liters. However, further testing will need to be done once a final design has been decided because the distribution of weight for the tipping bucket has changed since the frame of the tipping bucket is now plastic instead of metal.

**[Wondering why these constraints were used Summer 2018's results. As in why not go to 1 cm in the Horizontal Pivot Position or lower than 15.5 for Vertical Position? If there is a clear explanation as to the limits I would include that here. "-Addressed EL"]**

## Redesigning the Tipping Bucket
The 2019 spring team decided to remake the original metal frame from an HDPE sheet. The team ordered HDPE sheet and cut it into rods to replicate the geometry of the original frame that was constructed from 80/20 extrusions. The team determined that a 1 inch thick 48" by 24" sheet would be sufficient material and strength of 1 inch would be sufficient to hold up the bucket.

## Flow Dividing Tank
Wastewater from the tipping bucket is dumped into a flow dividing tank. The purpose of the flow dividing tank is to ensure that the four influent pipes receive an equal inflow of wastewater.  The flow dividing tank is partitioned into four equal sections. Figure 3 shows a top view of these sections. Each of the four sections drains into a separate inlet pipe. The figures below illustrate the flow dividing tank.
<img src="https://github.com/AguaClara/UASB/blob/master/Images/Top%20View%20Divide.png?raw=true">

**Figure 3. Top view of the holding tank, which leads into the flow dividing tank.**

<img src="https://github.com/AguaClara/UASB/blob/master/Images/Side%20View%20Holding%20Tank.png?raw=true">

**Figure 4. Side view of the holding tank, which leads into the flow dividing tank.**

<img src="https://github.com/AguaClara/UASB/blob/master/Images/Bottom%20Dividing%20Tank.png?raw=true">

**Figure 5. The dimensions for bottom of the flow dividing tank. (In inches)**

It would be imperative that each section in the flow dividing tank fills with wastewater before the wastewater starts flowing into the influent pipes so that each pipe will distribute the same amount of water inside the reactor. It is also desirable for the flow dividing tank to empty out completely between each dump of the tipping bucket as a de-clogging mechanism. These constraints mean that the flow dividing tank should be similar in volume to the tipping bucket, the bottom of the flow dividing tank should be at the same elevation **[in line like at same elevation? "-Addressed EL"]** as the water level in the reactor, and the diameter of influent pipes should be small enough so that the pipes drain slowly enough to allow for wastewater to overflow into all sections of the flow dividing case, in case the wastewater from the tipping bucket fills up only one section first. All of these constraints  are further described and investigated in the Python Documentation section.

In order for the de-clogging mechanism to occur, the water level inside the reactor's canister must be in line with the bottom of the flow dividing tank. Assuming that the reactor is about 80% full of liquid, the height of the water in the reactor would be roughly 5 ft. The team can set this level during the startup phase by adding water/sludge to the reactor until the desired height is reached. With that in mind, the bottom of the flow dividing tank should also be located at a height of roughly 5 ft.

## Influent Pipes
The Summer 2018 UASB team suggested 2 influent pipes, but after considering the results of the tapioca tests performed by the Fall 2018 team, the Spring 2019 UASB team decided to use four influent pipes to promote distribution of flow more evenly **[more evenly "-Addressed EL"]** through the sludge blanket. The Summer 2018 UASB team also suggested that the influent pipe diameter range from 2.95-3.94 inches to reduce clogging. However, the current team decided to decrease the diameter of the influent pipe to range from 1-2 inches **[Is there a reason you guys didn't consistently use imperial vs metric pipe diameters? Would keep it consistent unless it's unavoidable "-Addressed EL"]**. The team made that decision based on two constraints: a diameter much smaller than one inch would be more likely to cause clogging and result in too slow of an **[too slow of an "-Adressed EL"]** upflow velocity of wastewater through the reactor, and a diameter much larger than one inch would be less effective in promoting even flow through influent tubes.


Each inlet pipe will then carry wastewater to a point on the bottom of the reactor. The team has positioned the four points of influence are as far away from each other as possible on the bottom of the reactor. The bottom of the UASB reactor has a diameter of 3 ft. So, if the center of the reactor is considered to be the origin, then the four points of influence on the bottom of the reactor in polar coordinates will be: (9”, $pi$/4 rad), (.9”, 3$pi$/4 rad), (9”, -$pi$/4 rad), (9”, -3$pi$/4 rad). Figure four illustrates the locations of the points of influence to the bottom of the reactor.


<img src="https://github.com/AguaClara/UASB/blob/master/Images/Points%20of%20Influence.png?raw=true">

**Figure 6. The points of influence on the bottom of the reactor.**

After deciding on the locations for the points of influence on the bottom of the reactor, the team discussed how to minimize the amount of horizontal piping because settling of wastewater is more likely to occur in horizontal pipe **[part after "ways to" sounds off. If this is misworded please address "-Addressed EL"]**. The team decided to attach the holding tank to the side of the reactor to reduce settling and to ensure the reactor is compact.

Wastewater flow from the flow dividing bucket drains into vertical pipes. The wastewater needs to be directed to enter the side of the reactor through horizontal pipes. Horizontal entry was decided for ease of fabrication, since it would be difficult to drill ellipses into the UASB reactor to allow for diagonal entry. The team considered using 135 degree elbows instead of 90 degree elbows to minimize horizontal flow, as settling is more likely to occur in horizontal pipes. However, after floating the idea at a technical feedback session, the team realized that such pipes may not be readily available in Honduras, and decided to use [90 degree](https://www.homedepot.com/p/3-in-PVC-DWV-90-Degree-H-x-H-Vent-Elbow-C4807VHD3/205799553) elbows in the design.

Next, the team decided where the influent pipes enter the reactor. During tapioca tests in fall 2018 semester, the team noticed that preferential pathways tended to form around vertical sections of pipe in the sludge blanket. With that in mind, the team decided to have pipes enter the reactor near the ground to reduce the amount of vertical pipe running through the sludge blanket. The team decided to have pipes enter the reactor at heights of 10 inches and 20 inches above the ground (where the distance is measured from the bottom of the pipe). Then, each pipe extends horizontally until it is above its respective point of influence, at which point the pipe is directed down to the bottom of the reactor with a 90 degree elbow. Finally, each pipe will travel vertically until it is 1 inch above the bottom of the reactor. At this point, wastewater will exit into the reactor, hit the bottom, and then begin flowing upwards through the sludge blanket.

![Reactor Influent Design](https://github.com/AguaClara/UASB/blob/master/Images/pipe%20influent%20system.PNG?raw=true)
**Figure 7. Influent Design Entering Reactor**

<img src="https://github.com/AguaClara/UASB/blob/master/Images/full%20plant%20-%20design%201.PNG?raw=true">

**Figure 8. Full UASB Design 1**



<img src="https://raw.githubusercontent.com/AguaClara/UASB/master/Images/CAD%20Influent%20System.png?raw=true">

**Figure 9. Influent bucket system**


<img src="https://raw.githubusercontent.com/AguaClara/UASB/master/Images/CAD%20Bucket%20and%20Frame.png?raw=true">

**Figure 10. Bucket system without tank**

## Future Work
In order to reach the goal of fabrication, UASB Design must also complete the design for the effluent system, gas collection, and support system while considering materials for the entire reactor.

After deciding that the majority of the UASB reactor will be made up of HDPE, research has to be done in finding pipes and reactor tank made up of this material. For the biogas, instead of using a balloon ballo[o "-Addressed EL"]n contraption to collect methane gas, a bubble counter meter will be used to see how much biogas is being created. Once the design is finished, the methane gas will be burned off by a mechanism in the Ithaca's Waste Water Treatment Facility.

For the effluent system a valve needs to be added at the end to ensure there will be consistent effluent flow and make maintenance accessibility easier. Since the effluent pipe will begin extruding out from the UASB reactor upwards at 60 degrees to make sure the sludge granules settle back into the reactor, the team also has to figure out a way to add a pipe going vertically upwards through the effluent pipe to make sure atmospheric pressure is the same throughout. If atmospheric pressure can be maintained through the fabrication of the vertical pipe, the effluent pipe will ideally bend at the middle from upwards 60 degrees to a downwards vertical pipe that empties the effluent. Unfortunately, finding 30 degree connections are rather difficult to find in Honduras, so the team has yet to settle on a design of the effluent pipe.

Initially to support the influent system and pipes, the team had decided to use 80/20 extrusions; however, upon further consideration of the environment in which the reactor will be tested, the team will prioritize materials that can support heavy objects while being [that can support heavy objects while being "-Addressed EL"] [both "-Addressed EL"] both resistant to rusting and maintained easily **[maintained easily "-Addressed EL"]** ~~easily maintained but also able to support heavy objects~~.

Upon completing the design for the frame, the team will fabricate the influent system based on its design and begin testing it with water.

The optimal height and cross-sectional area for the influent pipes to be entering the tank still needs to be determined so that the flow of wastewater passing through the sludge will be between .0069 m/s - .02778 m/s . It is desirable for the upflow velocity to be faster than the velocity of the sludge granules settling to keep the bed fluidized but not so fast that the granules washout because of inadequate residence time. The research team is currently testing whether the entry of influent pipes above the sludge or the entry of influent pipes close to the bottom will result in less preferential pathways. Once UASB design receive this information, the team can finalize on the sections of the length of the pipes that will be vertical and horizontal.

[Beautiful CAD drawings uWu]
## Python Documentation
This python documentation is used to determine the relationship between drain time from the flow tank, diameter of the influent pipes, geometry of the flow dividing tank, and resulting up flow velocity, so that the team can make better informed design decisions. The code is below, and comments have been added for clarity.

The time it takes for the flow dividing tank to drain should be slow enough so that in case the bucket initially fills up just one division of flow dividing tank, it will not begin emptying out until overflow reaches other sections, but fast enough so that the tank completely drains out between successive dumps of the tipping bucket for self cleaning purposes and so that up flow velocity of influent water is fast enough to lift settling sludge particles. This drain time is determined by the diameter of the influent pipes and the head gain per dump of the tipping bucket, and the ensuing code will be used to determine the optimal combination of influent pipe diameter and flow dividing tank geometry to achieve said drain time.

```python
import aguaclara.core.head_loss as minorloss
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

"""UASB design.
This module aims to provide constants and functions to define both hydraulic
(head loss, retention time, drain time etc.) and geometric (influent pipe diameter, flow dividing tank geometry, UASB canister dimensions,
etc.) values that specify a UASB design.,"""
class UASB:
  def __init__(
          self,
          #Q = 8 * u.L/u.s, #NOTE: this refers to the instantaneous Q during a dump from the tipping bucket, assuming that the tipping bucket is ~16 L and takes two seconds to dump
          temp = 25 * u.degC, #average temperature in Honduras
          cannister_diam = 3 * u.ft,
          effluent_H = 5 * u.ft, #based on estimate that the 7ft tall canister is ~70% full of water  
          vol_dump = 16.26 * u.L, #NOTE: dump vol from previous team's design--subject to change once current team tests new tipping bucket design
          W_FDT = 9.937 * u.inch, #https://www.usplastic.com/catalog/item.aspx?itemid=66355&catid=
          FDT_H = 16.8125 * u.inch, #this was selected as bucket for flow dividing tank because it is similar in volume to volume of dump from tipping bucket, square, and HDPE (and not many other buckets fit all of these criteria)
          FDT_walls_t = .25 * u.inch,
          overflow_H = 1 * u.inch, #NOTE: come up with justification for this
          pipe_diam = 1 * u.inch,
          n_elbows = 3,
          pipe_roughness = .000003 * u.m,
          time_dump = 2* u.s,
          UASB_diameter = 3 * u.ft,
          HRT = 4 * u.hr #minimum HRT of wastewater in reactor for adequate treatment
  ):
      """Instantiate a UASB object, representing a real UASB component.
      :param Q: Flow rate of water water through the UASB.
      :type Q: float * u.L/u.s
      :param temp: Water temperature of the UASB
      :type temp: float * u.degC
      :param cannister_diam: diameter of the UASB canister
      :type cannister_diam: float * u.ft
      :param effluent_H: height of effluent line in UASB
      :type effluent_H: float * u.ft
      :param vol_dump: volume of one complete dump from tipping bucket
      :type vol_dump: float * u.L
      :param W_FDT: width of the inside of flow dividing tank
      :type W_FDT: float* u.inch
      :param FDT_H: height of the flow dividing tank
      :type FDT_H: float * u.inch
      :param FDT_walls_t: thickness of the walls of the flow dividing tank
      :type FDT_walls_t: float * u.inch
      :param overflow_H: desired height that wastewater from one dump of the tipping bucket overflows the flow dividing walls
      :type overflow_H: float * u.inch
      :param pipe_diam: ID of the influent pipes
      :type pipe_diam: float * u.inch
      :param n_elbows: number of 90 degree elbows per influent pipe
      :type n_elbows: float * dimensionless
      :param pipe_roughness: roughness of influent pipes
      :type pipe_roughness: float * u.m
      :returns: object
      :rtype: UASB
      """

      self.temp = temp
      self.cannister_diam = cannister_diam
      self.effluent_H = effluent_H
      self.vol_dump = vol_dump
      self.W_FDT = W_FDT
      self.FDT_H = FDT_H
      self.FDT_walls_t = FDT_walls_t
      self.overflow_H = overflow_H
      self.pipe_diam = pipe_diam
      self.n_elbows = n_elbows
      self.pipe_roughness = pipe_roughness
      self.time_dump = time_dump
      self.UASB_diameter = UASB_diameter
      self.HRT = 4 * u.hr

  @property
  def H_walls(self):
      """Calculates the height of the flow dividing walls, so that if a complete tip were to fill the flow dividing tank before it started draining out, the height of water would overflow the flow dividing walls by the desired height"""
      H_walls=(self.vol_dump-self.overflow_H*self.W_FDT**2)/(self.W_FDT**2-self.FDT_walls_t*self.W_FDT-self.FDT_walls_t*(self.W_FDT-self.FDT_walls_t)) #calculate H_walls by setting vol_dump equal to volume inside flow dividing system accounting for the volume that the flow dividing walls occupy
      H_walls=H_walls.to(u.inch)
      return H_walls

  @property
  def head_gain_per_dump(self):
      """Calculates head gain if flow splits evenly in the flow dividing tank and does not start emptying out until the tip is over."""
      HG=self.H_walls+self.overflow_H
      HG=HG.to(u.inch)
      return HG

  @property
  def vol_cannister(self):
      """Calculates the volume of wastewater in the reactor assuming that the water level inside the canister does not exceed that of the effluent line"""
      vol=(pc.area_circle(self.cannister_diam)*self.effluent_H).to(u.L)
      return vol

  @property
  def Qmax(self):
      """Calculates the max flow rate for wastewater entering the influent system to meet minimum retention time of wastewater inside the UASB reactor """
      return self.vol_cannister/self.HRT


  @property
  def FDT_section_area(self):
      """calculates the area of one section of the flow dividing tank"""
      return (self.W_FDT/2-1/2*self.FDT_walls_t)**2

  @property
  def FDT_area(self):
    """calculates the area the flow dividing tank"""
    return self.W_FDT**2

  @property
  def equivPipeRadiusFDT(self):
    """calculates the equivalent hydraulic radius of one section of the flow dividing tank"""
    radius=4*self.FDT_section_area/(4*(self.W_FDT/2-1/2*self.FDT_walls_t))
    return radius

  @property
  def pulseQSec(self):
    """calcultes flow rate during pulse in one section of influent system"""
    Q=self.vol_dump/self.time_dump/4
    return Q

  @property
  def influent_K(self):
      """this function calculates the minor loss coefficient of one of the influent pipes into the overall reactor. n_90elbows=number of 90 elbows in an influent pipe, D_pipe is the diameter of an influent pipe. Chose to calculate for minor loss because in the UASB design, minor losses are much more significant than major losses."""
      #k_val_FDT_ent_reduction=minorloss.k_value_reduction(self.W_FDT, self.W_FDT/2-1/2*self.FDT_walls_t,self.Q,fitting_angle=180,rounded=False,nu=pc.viscosity_kinematic(self.temp),pipe_rough=self.pipe_roughness) #calculates k value as water goes from overflow area into one section of the flow dividing tank #QUESTION: does it make sense to use the total area of FDT/area of section instead of diameters instead of diameters? since calculation is just a ratio of the two/how much does square vs round pipeshaspe affect the k minor coefficient
      #k_val_FDT_exit_reduction=minorloss.k_value_reduction(self.equivPipeRadiusFDT, self.pipe_diam, self.pulseQsec, fitting_angle=180, rounded=False,nu=pc.viscosity_kinematic(self.temp),pipe_rough=self.pipe_roughness)
       #calculates k value as water goes from flow dividing tank to influent pipe
      influent_K=self.n_elbows*minorloss.EL90_K_MINOR+minorloss.PIPE_EXIT_K_MINOR+minorloss.PIPE_ENTRANCE_K_MINOR #QUESTION: should this include a term for entrance k val?
      return influent_K

  @property
  def t_drain(self):
        """This function returns the estimated drain time from the FDT in the case that water from the tipping bucket fills up the sections evenly and quickly, so that water doesn't start draining until each section is full of water/there is water overflowing the dividing walls. headgain=headgain per dump """
        t_drain=8*self.FDT_section_area/(np.pi*self.pipe_diam**2)*(self.head_gain_per_dump*self.influent_K/(2*pc.gravity))**.5 #from equation (97) in FCM_derivations section in AguaClara textbook
        return t_drain.to(u.s)

  @property
  def upflow_vel(self):
      """this function calculates an estimate for upflow velocity in the UASB reactor assuming that water from the dump is divided evenly into sections and does not start draining until dump is complete. Ideally, this velocity will be as fast settling velocity of sludge particles, which is approximately .007 m/s, to make a fluidized sludge blanket. """
      UASB_Q_dump=self.vol_dump/self.t_drain ##calculate flow rate through UASB as water from a dump of tipping bucket flows through the system
      UASB_CA=pc.area_circle(self.UASB_diameter)
      up_vel=UASB_Q_dump/UASB_CA
      return up_vel.to(u.m/u.s)

D_avail= ([ .75, 1.0, 1.25, 1.5, 2, 2.5, 3])*u.inch

myUASB=UASB()
print(myUASB.time_dump)

print('The height of walls in the flow dividing tank should be', myUASB.H_walls)
print('The maximum flow of wastewater this UASB can handle is', (myUASB.Qmax).to(u.L/u.s))

drain_times=np.zeros(len(D_avail))*u.s
upflow_vels=np.zeros(len(D_avail))*u.m/u.s
for i in range(0,len(D_avail)):
  myUASB=UASB(pipe_diam=D_avail[i])
  drain_times[i]=myUASB.t_drain
  upflow_vels[i]=myUASB.upflow_vel

plt.scatter(D_avail, drain_times)
plt.title('Pipe Diameter vs Drain Time')
plt.xlabel('Pipe Diameter (Inches)')
plt.ylabel('Drain time (Seconds)')

plt.scatter(D_avail, upflow_vels)
plt.title('Pipe Diameter vs Upflow Velocity')
plt.xlabel('Pipe Diameter (Inches)')
plt.ylabel('Upflow Velocity (Meters/second)')
plt.ylim(0, .01)
```

## Analysis of Python Documentation
A major restriction on the influent system for the UASB was ensuring the ability to suspend the sludge particles in the reactor. This was dictated by the settling velocity for sludge particles. After conducting research into finding the settling velocity, the UASB team found that the velocity varies with density of sludge particles, ranging from 0.0009 m/s to 0.0167 m/s ((Miranda, Borges, & Monteggia 2017). As the 0.0167 cm/s up-flow occurs are exceptionally high densities of sludge, UASB Design would be requiring up-flow velocities closer the mean settling velocity of 0.0004m/s. Below are figures showing the calculated correlation between the pipe diameter and the drain time of the flow dividing tank, from which the up-flow velocity in the reactor was deduced.


![Pipe Diameter vs Drain Time](https://github.com/AguaClara/UASB/blob/master/Images/Pipe%20Diamter%20vs%20Drain%20Time.png?raw=true)

**Fig. 11: Pipe Diameter vs Drain Time**

![Pipe Diameter vs Upflow Velocity](https://github.com/AguaClara/UASB/blob/master/Images/Pipe%20Diameter%20vs%20Upflow%20Velocity.png?raw=true)

**Fig. 12: Pipe Diameter vs Upflow Velocity**

From the restriction from the settling velocity and the corresponding up-flow velocities from pipe diameters, the UASB design team decided to utilize an influent pipe with 1.5 inch diameter.

Other takeaways from the python are that the height of walls in the flow dividing tank should be 9.522 inch and the maximum flow of wastewater this UASB can handle is 0.0695 liter / second.

All of these calculations were based on the parameters that were initialized in the UASB object. Temperature is 25 degree celsius, the canister diameter is 3 ft. The height of the effluent pipe is 5 feet. The volume of one dump from the tipping bucket is 16.26 L. The width of the flow dividing tank is 9.937 inches, the height of the flow dividing tank is 16.8125 inches, the thickness of the flow dividing walls are 1/4 inch, there are 3 elbows per influent pipe, and HRT is 4 hours.




**Table 1. Design Parameters for Old UASB Reactor**

| UASB element      | Measurement |
| ----------------- | ----------- |
| Diameter Canister | 3 feet      |
| Height Canister  | 7 feet       |
| Diameter of Influent Pipe         | 1.5 inch            |
| Number of Elbows                  | 12                  |
| Average Up Flow Velocity          | 0.0695 liter/second |
| Tipping Bucket Dump Volume        | 16.26 liters        |
| Width of Flow Dividing Tank       | 9.9375 inches       |
| Number of Influent Pipes          | 4                   |
| Height of the Flow Dividing Walls |9.522 inches         |
| Thickness of the Flow Dividing Walls  | 0.25 inch       |
| Hydraulic Retention Time          | 4 hours             |








## New Smaller/Clear Reactors for Testing at IAWTTF
The UASB design team went over details of implementing the reactor at the IAWWTF with Ed Gottlieb, who is the contact at the IAWWTF, Ruth Richardson, and Monroe Weber-Shirk.

The plan moving forward consists of having six, ten inch diameter and seven feet tall reactors instead of one three feet diameter and seven feet tall reactor. Having six reactors will help substantiate results, test whether or not pulsated flow of the tipping bucket is making the reactor more effective in cleaning wastewater, and serve as a basis for future improvements such as how changing flow rates can affect reactor efficiency. In addition, the smaller diameter allows for the reactors to be constructed from clear PVC pipe, so that the team can observe what is going on inside of the reactor; namely, whether or not pulsated flow is fluidizing the sludge blanket.

There are some protocols and expectations for working in the IAWWTF facility. The gates are normally locked on weekdays from 5:30 PM-6:30 AM and opened on weekends 8:00 AM-2:00 PM. To get in and out of IAWWTF, sign-in/sign-out sheets must be signed in the administrative building. When taking samples from the wastewater treatment, release forms must be filled out. The grant given to IAWWTF was originally ten thousand dollars and now it is five thousand. An additional portion of grant can be given for supplies and construction if needed. There is an email that lists out all the lab testing costs. Lab tests will be done at IAWWTF and will focus mainly on chemical oxygen demand (COD) and biogas production (methane). Graduate Student Egidio, part of Professor Ruth Richardson’s research group, might work at the lab in IAWWTF because he has experience with wastewater sample and analysis. Students can also participate and lab tests but will need to be trained by Jose, the lead in the IAWWTF lab. In addition, UASB Design needs the lab's schedule so that the team does not interfere with IAWWTF's lab time. There is not an official subcontractor form yet for Cornell to fill out, but the IAWWTF’s contact in the legal department for the city, Corrine, will come up with something.

At the IAWWTF, there are two spaces available for testing the reactors. The first space has piping with wastewater at least six feet above the ground. Wastewater flow can be split evenly by filling a reservoir with wastewater and splitting the water with six peristaltic pumps. There is a gutter in the room for effluent, and a sump pump can lift the wastewater back up to the pipe it came from. However there is uncertainty as to how long the space can be reserved for. There are other companies that might bid for the space and use it for their own research. There is also a question of whether there is enough ventilation to get rid of the methane.

The second space is the current space that AguaClara UASB has reserved for a longer period of time. The space is also a newly renovated building. However it is a no-explosion zone, so regular pumps cannot be placed inside. The regular pumps can only be placed outside and have electrical wires run around the outside space. If pumps are placed inside the space, it must be ensured that the pumps and pipeline are explosion proof, which is expensive. Solids would also need to be specially screened so that pumps do not clog from something like an extremely thin wire. The space can fit six reactors with a cross-sectional area of two feet by two feet, but the reactors would need to be placed carefully. It is also difficult to access the wastewater because it is roughly thirty feet below ground level; therefore, explosion proof peristaltic pumps would be needed to lift the water. However, thirty feet is the limit to how high water can be pumped up on Earth, so multiple explosion proof pumps may be needed.

Various ideas for implementation of the reactors at the IAWWTF and maintenence were discussed. To ensure the stability of the reactors, it was proposed that an attachment would be put on top of all six reactors and linked together on a rope or cord. A hole would be drilled through the wall, and an anchor attached to the rope would be put through the hole and sealed to stabilize all of the reactors in a row. Straps would be put around each of the reactors and hooked onto the anchor in the wall. Triangular pieces were also considered to support the round bottom cap of the reactor and keep the reactor from tipping over. However, since the team has decided to use flanges on the top and bottom of the reactor, large, flat bolts can be attached to the flanges to stabilize the reactor, which are shown below in Figure 17. The reactor can be manually/physically cleaned in the inside by a magnetic scraper, similar to cleaners for fish tanks. For it to work, the magnet must be strong enough to go through the walls of the reactor.

## Design Process for the Smaller, Clear Reactors

The team used design decisions from the previous iteration of the UASB to inform its decisions on the smaller scaled design.

Major changes from the larger UASB design to the smaller UASBs include scaling the main reactor from three feet in diameter to ten inches in diameter, replacing four influent pipes with just one influent pipe, replacing the flow dividing tank with a drain pipe, and placing the tipping bucket design on top of the UASB canister.

![Drawing of New UASB Design](https://github.com/AguaClara/UASB/blob/master/Images/Screen%20Shot%202019-05-09%20at%207.19.19%20PM.png?raw=true)

**Fig. 12: Sketch of New UASB Design**

![CAD Model of New UASB Design](https://github.com/AguaClara/UASB/blob/master/Images/Screen%20Shot%202019-05-09%20at%207.21.21%20PM.png?raw=true)

**Fig. 13: CAD Model of New UASB Design**

As shown in Figure 12 and 13, the new UASB design directs wastewater through an influent system such as a tipping bucket to the drain pipe, to the influent pipe, into the UASB canister, and then out of the effluent pipe. Since the purpose of having six reactors is to test as many unknowns as possible, 

The previous design for the UASB used a 36" diameter canister. The smaller design will use a 10" clear PVC pipe instead. The 10" PVC clear pipe was chosen so that multiple reactors could fit in the available space at the IAWWTF. In addition, PVC pipes can more readily be bought clear, which can give the team more information as to what occurs within the reactor. The height of the UASB will be 8ft, since clear PVC pipes are sold in lengths of 8 ft.

To clean the reactor, it might be manually/physically cleaned in the inside or magnetic scraper might be used. For it to work, the magnet must be strong enough to go through the walls of the reactor.

![CAD Model of Drain Pipe(Highlighted in Orange) ](https://github.com/AguaClara/UASB/blob/master/Images/Screen%20Shot%202019-05-09%20at%207.24.38%20PM.png?raw=true)

**Fig. 14: Drain Pipe is Highlighted in Orange**


The drain pipe connects the holding tank, which houses the tipping bucket, to the influent pipe. Its purpose is to slow down incoming wastewater, to allow gas bubbles to escape. It is the same volume as one dump from the tipping bucket.  Its bottom is in line with the water level inside the canister, which means that the head gain per dump is the volume of one dump of the tipping bucket divided by the cross sectional area of the drain pipe.

Another important element of the design is the effluent system.

![Effluent System ](https://github.com/AguaClara/UASB/blob/master/Images/Screen%20Shot%202019-05-09%20at%207.27.39%20PM.png?raw=true)

**Fig. 15: Effluent System**

At first, the team thought that the effluent tube would need to be at a 60 degree angle to prevent sludge granule washout, similar to a tube settler; however, the team realized that the washout will not be a concern, since the average up flow velocity in the UASB canister is so slow. Since washout is not a concern, the design will use a horizontal effluent pipe to maximize the allowable height of the sludge blanket in the UASB reactor. The upside down T shape (indicated by green arrow) will be at a height of approximately 7 feet because the desired the water level because it maximizes the usage of space, but prevents overflow in the case of an accident. The actual effluent line will be about 10 cm below the water line in the canister to prevent biogas from entering the effluent in case the water level dips abnormally low. In addition, water will enter the effluent pipe through holes on the top of the pipe, as indicated by the teal arrows, so that rising biogas bubbles do not enter the effluent. Lastly, the upwards pointing pipe, as indicated by the red arrow, will maintain atmospheric pressure inside the reactor, so that the effluent doesn’t suck biogas out from inside the reactor.

![CAD Model of Flange](https://github.com/AguaClara/UASB/blob/master/Images/Screen%20Shot%202019-05-09%20at%207.31.19%20PM.png?raw=true)

**Fig. 16: CAD Model of Flange**


![Image of Flange and Gasket Being Used](https://github.com/AguaClara/UASB/blob/master/Images/Screen%20Shot%202019-05-09%20at%207.31.13%20PM.png?raw=true)

**Fig. 17: Image of Flange and Gasket Being Used**

The team decided to use flanges and blind flanges as end caps for the top and bottom of the reactor. That way, large, flat bolts can be used to the stabilize the reactor from the bottom, and the tipping bucket can be placed on top of the reactor, so that additional support is not required for the tipping bucket.

![Image of Flange and Gasket Being Used](https://github.com/AguaClara/UASB/blob/master/Images/Screen%20Shot%202019-05-09%20at%207.34.10%20PM.png?raw=true)

**Fig. 18: Sketch of FOG Removal**


A FOG removal system was also incorporated into the UASB design to prevent excess FOG from accumulating. A sketch of the FOG removal system is pictured above. The way it works is that the bottom of a funnel will be about in line with that the water level in the canister, and then attached to a pipe that leads down and has a valve on it. That way, as FOG collect on the surface, they will be pushed up into the funnel, since they are less dense than water. Then, the valve can be opened to empty out those FOG. The half circle hanging below the funnel is the gas bubble deflector, which will block methane gas bubbles from escaping out of the FOG removal system.


The major constraint for the UASB reactor is that the up flow velocity during pulsated flow be high enough to fluidize the sludge blanket. According to our literature review, this corresponds to an up flow velocity of about 16.7 mm/s (Miranda, Borges, & Monteggia 2017). The team used that constraint as a guide to determine design specifications for the UASB reactors.

The code below relates the geometry of the UASB reactor, the change in the water level during a pulse, and the average pulse up flow velocity. It's current state shows the final dimensions that have been decided on for the fabrication of the UASB pilot scale reactors. These dimensions are chosen, so that the up flow velocity during a pulse from the tipping bucket is fast enough to fluidize of the sludge blanket. If the code is run, it will display a table of important dimensions of the UASB reactor.

## Python for New Smaller/Clear Reactors for Testing at IAWTTF

```python
import aguaclara.core.head_loss as minorloss
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


class UASBtest:
  def __init__(
          self,
          temp = 10 * u.degC, #estimated temp at IAAWTF
          pipe_diam = 1.5 * u.inch, #diameter of the influent pipe
          n_elbows = 2, #the number of elbows in the influent pipe
          pipe_roughness = .0015 * u.mm, # PVC pipe roughness
          time_dump = 2* u.s, #NOTE: get better value with actual testing, this is a rough estimate
          UASB_diameter = 10 * u.inch,
          UASB_height = 8 * u.ft, #this height refers to the height of the pipe that is used to make the UASB canister, NOT the water level in the UASB.
          HRT = 4 * u.hr, #minimum HRT of wastewater in reactor for adequate treatment NOTE: some studies have shown 6 hrs is optimal
          target_upflow_vel= 16.7 * u.mm/u.s, #target up flow velocity to fluidize sludge blanket
          diameter_drain_pipe= 3 * u.inch, #diameter of the pipe that connects the holding tank to influent pipe ( 3 inches was chosen so that the area was similar to that of one section in drain tank in previous design.)
          descending_sewage_vel= .2 * u.m/u.s, #Maximum velocity that will allow air bubbles to rise out of reactor. Must only be achieved in beginning of influent pipe systems, not throughout.
          ww_gen_rate = 10.8 * u.L/u.hr, #Wastewater Generation per Person
          angle_sludge_weir=60*u.degrees, #angle of sludge weir
          percent_sludge= .7, #based on summer 2018 team research
          diam_sludge_granules = .5 * u.mm, #this is the lower end of range of diameters for sludge, goes up to 3 mm https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6070658/ so this would correspond to a slower setting particle
          rho_sludge= 1383 * u.g/u.L, #density of sludge granules. source:https://www.ijsr.net/archive/v4i4/SUB153022.pdf
          rho_water=1 *u.g/u.mL,
          lift= 5*u.cm, #5 cm
          effluent_pipe_diameter=1*u.inch

):
      """Instantiate a UASB object, representing a real UASB component.
      :param Q: Flow rate of water water through the UASB.
      :type Q: float * u.L/u.s
      :param temp: Water temperature of the UASB
      :type temp: float * u.degC
      :param cannister_diam: diameter of the UASB canister
      :type cannister_diam: float * u.ft
      :param effluent_H: height of effluent line in UASB
      :type effluent_H: float * u.ft
      :param vol_dump: volume of one complete dump from tipping bucket
      :type vol_dump: float * u.L
      :param pipe_diam: ID of the influent pipes
      :type pipe_diam: float * u.inch
      :param n_elbows: number of 90 degree elbows per influent pipe
      :type n_elbows: float * dimensionless
      :param pipe_roughness: roughness of influent pipes
      :type pipe_roughness: float * u.m
      :returns: object
      :rtype: UASB
      """
      self.temp = temp
      self.pipe_diam = pipe_diam
      self.n_elbows = n_elbows
      self.pipe_roughness = pipe_roughness
      self.time_dump = time_dump
      self.UASB_diameter = UASB_diameter
      self.HRT = HRT
      self.target_upflow_vel=target_upflow_vel
      self.diameter_drain_pipe=diameter_drain_pipe
      self.descending_sewage_vel=descending_sewage_vel
      self.percent_sluge=percent_sludge
      self.UASB_height=UASB_height
      self.effluent_pipe_diameter=effluent_pipe_diameter
      self.ww_gen_rate=ww_gen_rate
      self.lift=lift


  @property
  def UASB_area(self):
    """This function calculates the surface area of the UASB canister """
    area= pc.area_circle(self.UASB_diameter)
    return area

  @property
  def vol_dump(self):
    vol=self.lift*self.UASB_area
    return vol

  @property
  def area_drain_pipe(self):
    area=pc.area_circle(self.diameter_drain_pipe)
    return area

  @property
  def HG_per_dump(self):
    """This function calculates the head gain per dump, assuming that the water level in the canister is in line with the bottom of the "drain pipe" that connects the holding tank to the 1 inch influent pipe """
    HG=self.vol_dump/self.area_drain_pipe
    return HG

  @property
  def length_drain_pipe(self):
    """This function calculates the length of the drain pipe necessary so that the volume of 1 dump from the tipping bucket fills the drain pipe""" #NOTE: this adds an extra 1/2 inch of length to the drain pipe, could consider removing that
    h=(self.HG_per_dump+1/2*u.inch).to(u.inch)
    return h  

  @property
  def water_level_height(self):
    """This function determines the height of the water level in the reactor. The water level is supposed to be in line with the bottom of the drain pipe and the drain pipe is attached directly to the holding tank, so the water level is equal to the length of the drain pipe subtracted from the total height of the clear PVC pipe that serves as the UASB reactor"""   
    return self.UASB_height-self.length_drain_pipe

  @property
  def volume_UASB(self):
    """this function calculates volume of liquid inside UASB reactor, not including influent pipes"""
    vol=self.UASB_area*self.water_level_height
    return vol

  @property
  def flow_rate_avg(self):
    """this function estimates the max flow rate, given min HRT and volume of fluid inside canister, that the UASB can handle"""
    Qmax=(self.volume_UASB)/self.HRT
    return Qmax

  @property
  def upflow_vel_avg(self):
    """this function calculates the average up flow velocity of in the UASB canister"""
    up_v=self.flow_rate_avg/self.UASB_area
    return up_v

  @property
  def aggregate_k(self):
    """This function calculates  the aggregate minor loss coefficient of the drain system from the holding tank into the 'canister' aka the 10 inch clear PVC pipe"""
    influent_K=self.n_elbows*minorloss.EL90_K_MINOR+minorloss.PIPE_EXIT_K_MINOR+minorloss.PIPE_ENTRANCE_K_MINOR
    return influent_K

  @property
  def drain_time(self):
    """This function calculates how long it takes for a dump from the tipping bucket to drain into the tank, assuming that the bottom of the drain pipe (which connects the 1.5 inch pipe to the holding tank) is in line with the water level in the canister and does not begin draining out until the dump is complete. Note that this time should be approximately the same as the time it takes for the tipping bucket to fill up/fast enough to produce desired up flow velocity in the tank"""
    #NOTE: should we include minor loss from holding tank to drain tank, or assume water just starts from drain tank
    #NOTE: drain time also might drastically underestimate actual drain time, since all the water from the tipping bucket won't necessarily go straight into the drain pipe from the tipping bucket, but could linger around the bottom of the holding tank.  
    time = 8*self.area_drain_pipe/(np.pi*(self.pipe_diam)**2)*(self.HG_per_dump*self.aggregate_k/(2*pc.gravity))**(1/2)
    return time    


  @property
  def upflow_velocity_pulse_average(self):
    """this function estimates the average upflow velocity in the canister during a pulse by dividing the time it takes for a dump from the tipping bucket to drain into the system to get a "pulse flow rate" and then dividing that by the cross sectional area of the UASB to get an estimate for "pulse up flow velocity"""
    UASB_Q_dump=self.vol_dump/self.drain_time ##calculate flow rate through UASB as water from a dump of tipping bucket flows through the system
    up_vel=UASB_Q_dump/self.UASB_area
    return up_vel.to(u.m/u.s)

  @property
  def bucket_fill_time(self):
    """This function determines the estimated time it will take the tipping bucket to fill, using the estimated volume of one dump from the new, smaller tipping bucket size and the flow rate of water entering the UASB, according to the function flow_rate_max"""
    UASB_Q_dump=self.vol_dump/self.drain_time #calculate flow rate through UASB as water from a dump of tipping bucket flows through the system
    up_vel=UASB_Q_dump/self.UASB_area
    return up_vel.to(u.m/u.s)

  @property
  def num_people_served(self):
    """This function estimates the number of people that could be served by a UASB reactor of this size"""
    num=self.ww_gen_rate/self.flow_rate_avg
    num=num.to(u.dimensionless)
    return num

test=UASBtest()

(test.num_people_served)
data ={'UASB element':['Diameter Canister', 'Diameter Influent Pipe', 'Number of Elbows in Influent', 'Average Up flow Pulse Velocity', 'Tipping Bucket Dump Volume', 'Length Drain Pipe', 'Diameter Drain Pipe', 'Water Level Height'],
       'Measurement': [test.UASB_diameter, test.pipe_diam, test.n_elbows, test.upflow_velocity_pulse_average, test.vol_dump.to(u.gal), test.length_drain_pipe, test.diameter_drain_pipe, test.water_level_height]}


df=pd.DataFrame(data)
print(df)

```

## Analysis

<<<<<<< HEAD

**Table 2. Design Parameters for New UASB Reactor**

| UASB element                   | Measurement          |
| ------------------------------ | -------------------- |
| Diameter of Canister           | 10 inches            |
| Diameter of Influent Pipe      | 1.5 inches           |
| Number of Elbows in Influent   | 2                    |
| Average Up Flow Pulse Velocity | 0.02044 meter/second |
| Tipping Bucket Dump Volume     | 0.2534 centimeter    |
| Length Drain Pipe              | 22.37 inches         |
| Diameter Drain Pipe            | 3 inches             |



=======
UASB element             Measurement
0               Diameter Canister                 10 inch
1          Diameter Influent Pipe                1.5 inch
2    Number of Elbows in Influent                       2
3  Average Up flow Pulse Velocity  0.01752 meter / second
4      Tipping Bucket Dump Volume           0.6693 gallon
5               Length Drain Pipe              16.57 inch
6             Diameter Drain Pipe                3.5 inch
7              Water Level Height              6.619 foot
>>>>>>> 5a906a95e0a5f167b18f14f9bdf82fbf627ce192


The combination of design specifications, as shown above, results in an estimated average pulse up flow velocity of 17.52 mm/s. The estimated up flow is probably faster than what it actually will be, since it will take water additional time to make its way from the holding pipe to the drain pipe, and because major losses within the piping system are not addressed in the model. Since that is the case, it is good that the estimated average pulse up flow velocity is a bit higher than the target of 16.4 mm/s. The has team decided to use these specification in its fabrication of the UASB reactors, which will be tested at the IAWWTP.

The list of materials can be accessed at this link:
**add link that Kanha and I complete today**


```

@property
"""Got BiogasFlow code from Spring 2018"""
def BiogasFlow(Q, COD_Load, T):
    """Calculates the biogas production rate from the flow rate through the reactor, the COD concentration of the influent, and the temperature of the reactor

    For the doctest to pass, one must initialize the flow from UASB_design using UASB_Size(3 * u.ft, 7 * u.ft)

    >>> from aide_design.play import*
    >>> import math
    >>> BiogasFlow(UASB_design[2], 274.6 * (u.mg / u.L), 25 * u.degC)
    >>> 25 * u.degC <--- Vlaue for Temp
    >>> 274.6 * (u.mg / u.L) <--- value for COD_Load
    The volumetric methane production per second is 0.0013 liter / second <-- will be value for Q
    The volumetric methane production per second is 112.3 liter / day
    [<Quantity(0.0012996707807037425, 'liter / second')>, <Quantity(112.29155545280335, 'liter / day')>]
    """
    # Calculating methane production by mass
    COD_Load= 274.6* (u.mg / u.L)
    Q=0.0013 * (u.L / u.s)
    COD_Load = COD_Load.to(u.g / u.L)
    COD_eff = 0.7 # Assuming 70% efficency of COD removal and conversion in reactor
    COD_rem = COD_Load * COD_eff
    Y_obs = 0.23 # Upper limit of sludge production
    COD_CH4 = (Q * COD_rem) - (Y_obs * Q * COD_Load)
    # Calculating correction factor for operational temperature of the reactor
    T = T.to(u.degK)
    P = 1 * u.atm
    K_COD = 64 * (u.g / u.mol)
    R = 0.08206 * ((u.atm * u.L) / (u.mol * u.degK))
    K = (P * K_COD) / (R * T)
    #Calculate the volumetric flow rate of methane production
    Q_CH4 = COD_CH4 / K # per second
    Q_day = Q_CH4 * 86400 * (u.s / u.day) # per day

    print("The volumetric methane production per second is", Q_CH4, "\n" "The volumetric methane production per second is", Q_day)
    return [Q_CH4, Q_day]

doctest.testmod(verbose=True)


# Flow rate through UASB reactor
Flow_design = 0.0013*(u.g/u.s)
Temp = 25 * u.degC  # Assuming mesophilic conditions
COD_removal_eff = 0.7 # 70% removal efficiency

#Approximate loading rates for domestic wastewater
COD_Load_min = 100 * (u.mg / u.L)
COD_Load_mid = 200 * (u.mg / u.L)
COD_Load_max = 300 * (u.mg / u.L)
COD_ITHACA= 274.6* (u.mg / u.L) # Avg from Table 2
COD_Load= 274.6* (u.mg / u.L)
Q_Biogas = BiogasFlow(Flow_design, COD_ITHACA, Temp, 0.7)
#Calculating size of storage device
print(Q_Biogas.to(u.L/u.day))

print((3.6*u.m).to(u.feet))

(0.0009 *u.m/u.s).to(u.m/u.hr)

(0.0167 *u.m/u.s).to(u.m/u.hr)
```








## Bibliography

- AOS Treatment Solutions. “How Much Energy Does a Wastewater Treatment Plant Use?” AOS Treatment Solutions, AOS Treatment Solutions, LLC, March 1 2018, https://aosts.com/how-much-energy-does-wastewater-treatment-plant-use/

- Catherine Taylor & Joseph Yahner. “Wastewater Treatment Protects Small Community Life, Health.” On-Site Wastewater Disposal and Public Health, Purdue University, Summer 1996, https://engineering.purdue.edu/~frankenb/NU-prowd/disease.htm

- Center for Sustainable Systems, University of Michigan. 2018. "U.S. Wastewater Treatment Factsheet." Pub. No. CSS04-14, http://css.umich.edu/factsheets/us-wastewater-treatment-factsheet

- Cho, S.h., et al. “Settling Velocity Model of Activated Sludge.” Water Research, vol. 27, no. 7, 1993, pp. 1237–1242., doi:10.1016/0043-1354(93)90016-b.

- M. K. Daud, Hina Rizvi, Muhammad FarhanAkram, Shafaqat Ali, Muhammad Rizwan,Muhammad Nafees, and Zhu Shui Jin. “Review of Upflow Anaerobic Sludge Blanket Reactor Technology: Effect of Different Parameters and Developments for Domestic Wastewater Treatment.” Journal of Chemistry, Hindawi, 2018, https://www.hindawi.com/journals/jchem/2018/1596319/

- Mehtab Haseena*, Muhammad Faheem Malik, Asma Javed, Sidra Arshad, Nayab Asif, Sharon Zulfiqar and Jaweria Hanif. “Water pollution and human health.” Environmental Risk Assessment and Remediation,Allied Academies, July 13 2017, http://www.alliedacademies.org/articles/water-pollution-and-human-health-7925.html

- Miranda, L. A. S., et al. “Use Of A Griffith Tube To Evaluate The Anaerobic Sludge Sedimentation In A Uasb Reactor Treating An Effluent With Long-Chain Fatty Acids.” Brazilian Journal of Chemical Engineering, vol. 34, no. 1, 2017, pp. 131–141., doi:10.1590/0104-6632.20170341s20150427.
-
- MGOe. “Wastewater Treatment Plants.”Your Community Energy C
ompany, Madison Gas and Electric Company, 2019, https://www.mge.com/saving-energy/business/bea/article_detail.htm?nid=%202431


- Perlman, Howard. “Wastewater Treatment Water Use.” The USGS Water Science School, US Geological Survey, Dec. 2 2016, https://water.usgs.gov/edu/wuww.html



According to 3 sources, BOD:COD ratio for untreated waste water is around 0.6.
([Anil Kumar, Purnima Dhall, Rita Khumar, 2010](https://www.sciencedirect.com/science/article/pii/S0964830510000107))
([Ilias 3, 2010](https://cgi.tu-harburg.de/~awwweb/wbt/emwater/lessons/lesson_a1/lm_pg_1068.html))
([Liyang Yang, Hyun-Sang Shin, jin Hur, 2014](https://cgi.tu-harburg.de/~awwweb/wbt/emwater/lessons/lesson_a1/lm_pg_1068.html))

Data of average BOD concentration from the last week of each month from 8/18/19- 3/18/19 from Ithaca's Wastewater Treatment Plant will be averaged altogether. Average overall BOD concentration was 164.75 mg/L. When converted to COD, taking into account that BOD:COD ratio is 0.6, the COD concentration was 274.6 mg/L.

**Table 2. BOD Concentration from last week of each month from 8/18/19 to 3/18/19**
| Month                         | BOD Concentration Data 1 (mg/L) | BOD Concentration Data 2 (mg/L)| Average (mg/L) |
| ----------------------------- | ------------------------ | ------------------------ | ------- |
| September                     | 138                      | 140                      | 139     |
| October                       | 164                      | 169                      | 166.5   |
| November                      | 183                      | N/A                      | 183     |
| December                      | 170                      | 239                      | 204.5   |
| January                       | 174                      | 98                       | 136     |
| February                      | 164                      | 155                      | 159.5   |
| Avg overall BOD Conc (mg/L) |                          |                          |164.75  |
| Avg overall COD Conc (mg/L) |                          |                          |274.6   |


**Table 3. Design Parameters for biogas (from Summer 2018 Final Report)**
| Parameters                    | Values       | Basis of Design|
| ----------------------------- | --------| ------------------------ |
| COD Removal Efficiency  | 70%     | 140                      |Based on [Van Lier Report](https://courses.edx.org/c4x/DelftX/CTB3365STx/asset/Chap_4_Van_Lier_et_al.pdf)|
| Percent of COD directed to Sludge Production Y_obs | 23%     | Based on [Anaerobic Reactors](https://www.iwapublishing.com/sites/default/files/ebooks/9781780402116.pdf) Chose highest value of removal to get minimum production value|
| Pressure(P)   | 1 atm     | Biogas produced will expand against a bag and be at very low pressures  |
| Temperature (T)  | 25 celcius   | Assuming optimal biological conditions |
| COD_Load | 274.6  (mg/L)   | Average COD load from Ithaca's wastewater Treatment Plant 8/18/19 to 3/18/19 |


```python
from aide_design.play import*
from aguaclara.core.units import unit_registry as u
import doctest
"""Got BiogasFlow code from Spring 2018"""
def BiogasFlow(Q, COD_Load, T):
    """Calculates the biogas production rate from the flow rate through the reactor, the COD concentration of the influent, and the temperature of the reactor

    For the doctest to pass, one must initialize the flow from UASB_design using UASB_Size(3 * u.ft, 7 * u.ft)

    >>> from aide_design.play import*
    >>> import math
    >>> BiogasFlow(UASB_design[2], 274.6 * (u.mg / u.L), 25 * u.degC)
    >>> 25 * u.degC <--- Vlaue for Temp
    >>> 274.6 * (u.mg / u.L) <--- value for COD_Load
    The volumetric methane production per second is 0.0013 liter / second <-- will be value for Q
    The volumetric methane production per second is 112.3 liter / day
    [<Quantity(0.0012996707807037425, 'liter / second')>, <Quantity(112.29155545280335, 'liter / day')>]
    """
    # Calculating methane production by mass
    COD_Load= 274.6* (u.mg / u.L)
    Q=0.0013 * (u.L / u.s)
    COD_Load = COD_Load.to(u.g / u.L)
    COD_eff = 0.7 # Assuming 70% efficency of COD removal and conversion in reactor
    COD_rem = COD_Load * COD_eff
    Y_obs = 0.23 # Upper limit of sludge production
    COD_CH4 = (Q * COD_rem) - (Y_obs * Q * COD_Load)
    # Calculating correction factor for operational temperature of the reactor
    T = T.to(u.degK)
    P = 1 * u.atm
    K_COD = 64 * (u.g / u.mol)
    R = 0.08206 * ((u.atm * u.L) / (u.mol * u.degK))
    K = (P * K_COD) / (R * T)
    #Calculate the volumetric flow rate of methane production
    Q_CH4 = COD_CH4 / K # per second
    Q_day = Q_CH4 * 86400 * (u.s / u.day) # per day

    print("The volumetric methane production per second is", Q_CH4, "\n" "The volumetric methane production per second is", Q_day)
    return [Q_CH4, Q_day]

doctest.testmod(verbose=True)


# Flow rate through UASB reactor
Flow_design = UASB_design[1]
print(Flow_design)

Temp = 25 * u.degC  # Assuming mesophilic conditions
COD_removal_eff = 0.7 # 70% removal efficiency

#Approximate loading rates for domestic wastewater
COD_Load_min = 100 * (u.mg / u.L)
COD_Load_mid = 200 * (u.mg / u.L)
COD_Load_max = 300 * (u.mg / u.L)
COD_ITHACA= 274.6* (u.mg / u.L) # Avg from Table 2
COD_Load= 274.6* (u.mg / u.L)
Q_Biogas = BiogasFlow(Flow_design, COD_ITHACA, Temp, 0.7)
#Calculating size of storage device
print(Q_Biogas.to(u.L/u.day))
```
