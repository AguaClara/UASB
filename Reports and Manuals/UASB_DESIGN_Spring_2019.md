## UASB Design, Spring 2019
By Nina Blahut, Shania Fang,  Emily Liu, Kanha Matai
February 22, 2019

## Abstract
Since Spring 2017, the AguaClara Upflow Anaerobic Sludge Blanket (UASB) Team has been working on a detailed design for a pilot-scale, gravity-powered UASB reactor. A UASB reactor treats wastewater anaerobically and produces biogas as a by-product.

Over Spring 2019, the UASB-Design team's main goal has been to finalize the design for the UASB and work on fabrication of the entire system for testing and data collection at the Ithaca Area Wastewater Plant before implementation in Honduras. So far, the team has completed the design dimensions for the influent system and began an onshape CAD design.

##Introduction
The completion of a pilot UASB reactor that will be tested with real wastewater at the Ithaca Area Wastewater Treatment will be a big step for AguaClara’s venture into sustainable wastewater treatment. There is still much that needs to be further discovered and refined, such whether or not the tipping bucket system will be useful in eliminating preferential pathways, the effluent system design, and the gas capture system.

## Literature Review and Previous Work

Water pollution is a global issue yet many areas in the world still lack wastewater treatment plants. Water, being a universal solvent, contains dissolved fecal and urine matter, harmful chemicals, and pathogens which makes it harder to separate these compounds.  Leaving wastewater untreated and releasing it directly back into the environment can cause devastating effects on both the environment and human health.

https://water.usgs.gov/edu/wuww.html

Wastewater contains decaying organic matter and nutrients such as phosphorus and nitrogen which can cause algae blooms and eutrophication, reducing the amount of oxygen available in waters and making it harder for aquatic life to survive. These water pollutants are killing marine birds, crustaceans, sea weeds, and many other organisms. Human health is also directly affected by these disease causing pathogens in wastewaters. They destroying crop production, infecting our food supply, and water-borne diseases. Health risk associated with wastewater includes respiratory disease, cancer, diarrheal disease, a neurological disorder, and cardiovascular disease(Mehtab Haseena, 2017).

http://www.alliedacademies.org/articles/water-pollution-and-human-health-7925.html

Some of the biggest issues that wastewater treatment plants face today are energy consumption and environmental footprint. Wastewater facilities have a preliminary treatment, sedimentation, chlorination, and processing sludge which are all electrically and fuel powered (AOS, 2018). There are about 17,000 wastewater treatment plants in the US and they use up about 3% of the nation’s total energy consumption(MGOE, 2019). However, not all countries have access or can afford the same resources, which makes having universal wastewater treatment plants less feasible.

https://aosts.com/how-much-energy-does-wastewater-treatment-plant-use/
https://www.mge.com/saving-energy/business/bea/article_detail.htm?nid=%202431

UASB reactors are used as a preliminary wastewater treatment process to remove suspended solids organic matter in wastewater (Chong et. al, 2012). UASB reactors, instead of using fuel or electricity, rely mainly on gravity and biological processes to remove organic matter and convert it to biogas. They are highly efficient in treating high COD loads, biogas formation, and provide good stabilization of solids(M.K. Daud, 2018).They are less energy intensive than other forms of preliminary wastewater treatment that use aerobic processes. UASB reactors also produce methane as a byproduct of anaerobic digestion which can be captured and used for energy production or heating. However, these UASB reactors still rely on electricity.

https://www.hindawi.com/journals/jchem/2018/1596319/

AguaClara, on the other hand, has designed a UASB reactor that solely uses gravity. It’s main function is to improve the accessibility of wastewater treatment for smaller communities that don’t have access to electricity.  In January 2017, this gravity-powered UASB reactor was designed  for the EPA People, Prosperity and the Planet (P3) Student Design Competition proposal. The proposed UASB reactor design focused on improving reactor design, making the system cheaper and easier to fabricate so it can be created globally. The team later applied for Phase II funding from the same organization to support the development and implementation of additional reactors for testing and received a grant of $75,000.

Summer 2018
In Summer 2018 the team worked on hydraulic design of the UASB system and created a tipping bucket system which delivered wastwater in large pulses at a high flow rate. The team had two possible designs for the influent system--one option was for influent tubes to enter either at the top of the UASB reactor and the alternative was for influent tubes to enter the UASB reactor. The team also focused on biogas storage and came up with three types of storage: Gas Bag, Fixed Lid, and Floating Lid. They later decided that a gas bag system was both cost effective and transportable for community systems.

Fall 2018
The team researched preferential pathways by doing bench tests. The team fabricated  small scale UASB reactor used chia seeds, marbles, and tapioca to simulate sludge. Preferential pathways occur when incoming wastewater forms a pathway through the sludge blanket; consequently, not all of the wastewater gets in contact with the sludge  and it’s not effectively cleaned. The team concluded that it will likely be necessary to have several influential pipes to promote the even distribution of wastewater flow and decrease preferential pathways.  

In the Spring 2019 semester, the team will focus on building and assembling a UASB pilot-scale reactor to be tested in Ithaca’s Wastewater Treatment Plant by the Summer of 2020.


## Methods

## Design for Influent System

In this section, the team will explain how it made decisions regarding the design for the influent system.

For the influent system, the team has decided to move forward with the Summer 2018 team's design in which a tipping bucket empties wastewater into a holding tank, which will then empty into a flow dividing bucket, into influent separate pipes, into the side of the reactor. The team will also move forward with the Summer 2018 team’s plan to use a 300 gallon reactor tank that has a 36” diameter and 72” height. (https://www.plastic-mart.com/product/17049/300-gallon-plastic-tank-rotoplas-590314-590315)

The Summer 2018 UASB team suggested 2 influent pipes, but after considering the results of the tapioca tests performed by the Fall 2018 team, the Spring 2019 UASB team decided to use four influent pipes to promote even distribution of flow through the sludge blanket. The team also decided to use 3 inch inner diameter pipes for the  influent pipes. The team made that decision based on previous teams’ research, which found that clogging is more likely to occur in pipes smaller than 3 inches. According to the AguaClara pipe database, the outer diameter of schedule 40 pipes with a diameter of 3 inches is 3.5 inches. The code used to access that value is shown below.

```python
ND=pipe.ND_SDR_available(3*u.inch, 40)
OD=pipe.OD(ND)
print(OD)
```

The design for the tipping bucket and holding tank were completed by the 2018 UASB team, and have been incorporated into the current overall UASB design.

The parameters for the holding tank, with a 5-gallon bucket mounted inside, are summarized in the table below:

| Parameter | Value | Justification |
|:-------------- |:-----  |------------- |
|Height|$\geq$ 40 cm| Height of bucket plus 4 cm error|
|Width|35 cm |30 cm for bucket diameter plus 5 cm for both pivot pieces|
|Length|$\geq$ 60 cm|Height of bucket plus extra space to allow free rotation.|

<img src="https://github.com/AguaClara/UASB/blob/master/Images/Timmy_the_Tipping_Bucket.jpg?raw=true">
Figure 1: A picture of the tipping bucket design fabricated by the Summer 2018 Team

From the holding tank, wastewater will empty into a flow dividing bucket. The purpose of the flow dividing bucket is to ensure that the four influent pipes receive an equal inflow of wastewater.  The flow dividing bucket is partitioned into four equal sections. Each of the four sections then empties out into a separate inlet pipe. It is imperative that each section in the flow dividing bucket is full of wastewater before the wastewater starts flowing into the influent pipes.

With that in mind, the team calculated height at which the flow dividing bucket will need to be positioned so that it will empty out only once all of its sections are full of wastewater, in order to ensure that each of the four inlet pipes will receive an equal amount of water for each dump of the tipping bucket. In order for that to happen, the water level inside of the reactor must be just above the bottom of the tipping bucket holding tank. Assuming that the tank is about 80% full of liquid, the height of the water in the tank would be roughly 5 ft. The team can set this level during the startup phase by adding water/sludge to the reactor until the desired height is reached. Based on that calculation, the team decided that the bottom of the holding tank/top of the flow dividing bucket should be at a height of 58.8 in to ensure the flow dividing bucket is completely filled before wastewater begins flowing into the inlet pipes.

For the flow dividing tank, we chose a 6 gallon 12" by 12" by 12" polethylene tank (https://www.usplastic.com/catalog/item.aspx?itemid=124470). The bucket will be divided into four equally sized sections by walls of 1.5" thickness. We chose this tank so that four 3.5” diameter holes (to house influent pipes) and two 1.5” wide dividing walls could fit on the bottom area of the tank while also minimizing the horizontal space around holes because settling could occur there.



Figure 2. A view from above of the holding tank, which leads into the flow dividing tank is shown above

<img src="https://github.com/AguaClara/UASB/blob/master/Images/Top%20View%20Divide.png?raw=true">
Figure 2. A view from above of the holding tank, which leads into the flow dividing tank is shown above




Figure 3. Side view of the holding tank, which leads into the flow dividing tank.
<img src="https://github.com/AguaClara/UASB/blob/master/Images/Side%20View%20Holding%20Tank.png?raw=true">


Figure 4. The dimensions for bottom of the flow dividing tank.  (measurements are in inches)
<img src="https://github.com/AguaClara/UASB/blob/master/Images/Bottom%20Dividing%20Tank.png?raw=true">

Since the flow dividing bucket is 12” tall, the top of the influent pipes will begin at 46.8” above the ground.

Each inlet pipe will then carray wastewater to a point on the bottom of the reactor. The team has positioned the four points of influence are as far away from each other as possible on the bottom of the reactor. The bottom of the UASB reactor has a diameter of 3 ft. So, if the center of the reactor is considered to be the origin, then the four points of influence on the bottom of the reactor in polar coordinates will be: (9”, $pi$/4 rad), (.9”, 3$pi$/4 rad), (9”, -$pi$/4 rad), (9”, -3$pi$/4 rad)

Figure 5. The points of influence on the bottom of the reactor.
<img src="https://github.com/AguaClara/UASB/blob/master/Images/Points%20of%20Influence.png?raw=true">

After the team decided on the locations for the points of influence on the bottom of the reactor, it moved on to deciding how to connect each pipe from the flow divider to its respective point of influence. In doing so, the team took effort to reduce head loss of the pipes and make the exiting velocity at each point of influence as equal as possible.

The pipes carrying wastewater away from the flow dividing bucket are vertical. Then, the wastewater needs to be directed to enter the side of the reactor in the horizontal direction (horizontal entry was decided on for ease of fabrication, since it would be difficult to drill ellipses into the UASB reactor to allow for diagonal entry). The team considered using 135 degree elbows instead of 90 degree elbows to minimize horizontal flow, as settling is more likely to occur in horizontal pipes. However, after floating the idea at a technical feedback session, the team realized that such pipes may not be readily available in Honduras, and decided to use 90 degree elbows in the design. https://www.homedepot.com/p/3-in-PVC-DWV-90-Degree-H-x-H-Vent-Elbow-C4807VHD3/205799553


To make the UASB as compact as possible, reduce the horizontal distance that influent wastewater must travel, and reduce settling, the holding tank will be directly attached to the side of the reactor. Since the flow dividing tank be filled with wastewater and hold the tipping bucket system, it will need to be held up by additional supports on the ground. To do so, the team will use 80-20 extrusion bars on opposite sides of the flow dividing bucket.

Next, the team decided where the influent pipes would enter the side of the reactor. The team decided to have the pipes enter the reactor horizontally near the bottom of the reactor to limit the vertical length of influent pipe inside the sludge blanket because during tapioca tests in fall 2018 semester, the team noticed that preferential pathways tended to form around vertical sections of pipe in the sludge blanket. With that in mind, the team decided to have points enter the reactor near the ground to reduce the amount of vertical pipe running through the sludge blanket. The team decided to have pipes enter the reactor at heights of 10 inches and 15 inches above the ground (where the distance is measured from the center of the pipe). Then, each pipe will travel horizontally until it is above its respective point of influence, at which point water will be directed down to the bottom of the reactor with a 90 degree elbow. Finally, each pipe will travel vertically until it is 1 inch above the bottom of the reactor. At this point, wastewater will exit into the reactor, hit the bottom, and then begin flowing upwards through the sludge blanket.

Based on the height of the flow dividing bucket and the height of the points of entry on the side of the reactor, the team determined the length of influent tube sections. Dimensions are summarized in the sketch below, which is a side view of the UASB. Supports for the flow dividing bucket are not included.

Figure 6. UASB reactor dimensions
<img src="https://github.com/AguaClara/UASB/blob/master/Images/UASB%20Reactor%20Dimensions.png?raw=true">


The dimensions still need to be slightly altered to account for the size of elbows.

Attach CAD MODEL


##Future Work
The next step for UASB design is to design the frame using 80 20 extrusions that will support the influent system. The team will also use hydraulic code from previous teams to get an estimate for the exit velocity of water entering the UASB. Upon completing the design for the frame, the team will fabricate the influent system based on its design and begin testing it with water.

We also still need to figure out the optimal height for  the influent pipes will be entering the tank. The research team is currently testing whether the entry of influent pipes above the sludge or the entry of influent pipes close to the bottom will result in less preferential pathways. Once we receive this information, we can finalize on the sections of the length of the pipes that will be vertical and horizontal.

The team’s goal is to have the influent system built by March 11 and begin testing.
