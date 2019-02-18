Introduction

Water pollution is a global issue yet many areas in the world still lack wastewater treatment plants. Water, being a universal solvent, contains dissolved fecal and urine matter, harmful chemicals, and pathogens which makes it harder to separate these compounds.  Leaving wastewater untreated and having it re-enter back into the environment can cause devastating effects on both the environment and human health.

https://water.usgs.gov/edu/wuww.html

Wastewater contains decaying organic matter and nutrients such as phosphorus and nitrogen which can cause algae blooms and eutrophication, reducing the amount of oxygen available in waters and making it harder for aquatic life to survive. These water pollutants are killing marine birds, crustaceans, sea weeds, and many other organisms. Human health is also directly affected by these disease causing pathogens in wastewaters. They destroying crop production, infecting our food supply, and water-borne diseases. Health risk associated with wastewater includes respiratory disease, cancer, diarrheal disease, a neurological disorder, and cardiovascular disease(Mehtab Haseena, 2017).

http://www.alliedacademies.org/articles/water-pollution-and-human-health-7925.html

Some of the biggest issues that wastewater treatment plants face today are energy consumption and environmental footprint. Wastewater facilities have a preliminary treatment, sedimentation, chlorination, and processing sludge which are all electrically and fuel powered (AOS, 2018). There are about 17,000 wastewater treatment plants in the US and they use up about 3% of the nation’s total energy consumption(MGOE, 2019). However, not all countries have access or can afford the same resources, which makes having universal wastewater treatment plants less feasible.

https://aosts.com/how-much-energy-does-wastewater-treatment-plant-use/
https://www.mge.com/saving-energy/business/bea/article_detail.htm?nid=%202431

UASB reactors are used as a preliminary wastewater treatment process to remove suspended solids organic matter in wastewater (Chong et. al, 2012). UASB reactors, instead of using fuel or electricity, rely mainly on gravity and biological processes to remove organic matter and convert it to biogas. They are highly efficient in treating high COD loads, biogas formation, and provides good stabilization of solids(M.K. Daud, 2018).They are less energy intensive than other forms of preliminary wastewater treatment that use aerobic processes. UASB reactors also produce methane as a by-product of anaerobic digestion which can be captured and used for energy production or heating. However, these UASB reactors still rely on electricity.

https://www.hindawi.com/journals/jchem/2018/1596319/

AguaClara, on the other hand, has designed UASB reactor that solely uses gravity. It’s main function was to improve the accessibility of wastewater treatment for smaller communities that didn’t have access to electricity.  In January 2017, this gravity-powered UASB reactor was created  for the EPA People, Prosperity and the Planet (P3) Student Design Competition proposal. The proposed UASB reactor design focused on improving reactor design, making the system cheaper and easier to fabricate so it can be created globally. The team later applied for Phase II funding from the same organization to support the development and implementation of additional reactors for testing and received a grant of $75,000.

In the Spring 2019 semester, the team will focus on building and assembling a UASB pilot-scale reactor to be tested in Ithaca’s Wastewater Treatment Plant by the Summer of 2020.




##Methods

##design for influent system

For the influent system, we have decided to move forward with the Summer 2018 team's plan of a tipping bucket that empties wastewater into a holding tank, which will then empty into a flow dividing bucket, into separate pipes, into the side of the reactor. The Summer 2018 UASB team suggested 2 pipes, but after considering the results of the tapioca tests performed by the Fall 2018 team, the Spring 2019 UASB team has decided to use four influent pipes to promote even distribution of flow through the sludge blanket.

The design for the tipping bucket and holding tank were completed by the 2018 UASB team, and has been incorporated into the current overall UASB design.

The parameters for the holding tank, with a 5-gallon bucket mounted inside, are summarized in the table below:

| Parameter | Value | Justification |
|:-------------- |:-----  |------------- |
|Height|$\geq$ 40 cm| Height of bucket plus 4 cm error|
|Width|35 cm |30 cm for bucket diameter plus 5 cm for both pivot pieces|
|Length|$\geq$ 60 cm|Height of bucket plus extra space to allow free rotation.|


One of the most important characteristics of the influent system is that the four influent pipes receive an equal inflow of wastewater. In order to achieve this, the team has designed a flow dividing bucket. The holding tank will empty wastewater into the flow dividing bucket, which is a smaller tank that is partitioned into four equal sections. Each of the four sections then empties out into a separate inlet pipe. It is imperative that each section in the flow dividing bucket is full of wastewater before the wastewater starts flowing into the influent pipes.

With that in mind, the team calculated height at which the flow dividing bucket will need to be positioned so that it will empty out only once it is full, in order to ensure that each of the four inlet pipes will receive an equal amount of water for each dump of the tipping bucket. In order for that to happen, the water level inside of the reactor must be level with the bottom of the tipping bucket holding tank. According to past team's research, the The reactor will be filled 50% with sludge, which will be 3.5 ft.  Assuming that the tank is about 70% full of liquid, the height of the water in the tank would be roughly 5 ft. The team can set this level during the startup phase by adding water/sludge to the reactor until the desired height is reached. Based on that calculation, the team decided that bottom of the holding tank/top of the flow dividing bucket should be at a height of 58.8 in to ensure the flow dividing bucket is completely filled before wastewater begins flowing into the inlet pipes.


For the flow dividing tank, we chose a 6 gallon 14" by 10" by 10" polethylene tank. We chose this tank so that the four 3 inch diameter pipes could fit the bottom area of the tank in a square while minimizing the horizontal space around them to prevent settling as much as possible. The height of the flow dividing tank will be decided and adjusted accordingly. The bucket will then be divided into four sections by walls of 1.5" thickness.


The team also decided to use 3 inch inner diameter influent pipe design. The team made that decision based on previous teams’ research because clogging is more likely to occur in pipes than 3 inches. According to the AguaClara pipe database, the outer diameter of schedule 40 pipes with a diameter of 3 inches is 3.5 inches. The code used to access that value is shown below.
```python
ND=pipe.ND_SDR_available(3*u.inch, 40)
OD=pipe.OD(ND)
print(OD)
```
That means, that there will need to be four 3.5” diameter holes drilled into the bottom of the flow dividing tank.

A view from above of the flow dividing tank is shown below.

PICTURE!!


Assuming that we are sticking with the 14” height for the flow dividing tank, the top of the influent pipes will begin at 44.8” above the ground.


To make the UASB as compact as possible, reduce the horizontal distance that influent wastewater must travel, and reduce settling, the holding tank will be directly attached to the side of the reactor. Since the holding tank will need to be filled slightly with wastewater and hold the tipping bucket system, it will need to be held up by additional supports on the ground. **material for supports? specific attachment? how many supports?**


```python
```

Each inlet pipe will lead to a point on the bottom of the reactor, so that the four points of influence are as far away from each other as possible. The bottom of the UASB reactor has a diameter of 3 ft. So, if the center of the reactor is considered to be the origin, then the four points of influence on the bottom of the reactor in polar coordinates will be: (.75 ft, $pi$/4 rad), (.75 ft, 3$pi$/4 rad), (.75 ft, -$pi$/4 rad), (.75 ft, -3$pi$/4 rad)

```python
from aguaclara.play import *
(.75*u.ft, math.pi/2)
```
After the team decided on the locations for the points of influence on the bottom of the reactor, it moved on to deciding how to connect each pipe from the tipping bucket to its respective point of influence. In doing so, the team took effort to reduce headloss of the pipes and make the exiting velocity at each point of influence as equal as possible.

![Screen Shot 2019-02-17 at 12.41.38 PM](/assets/Screen%20Shot%202019-02-17%20at%2012.41.38%20PM.png)

The pipes carrying wastewater from the tipping bucket are vertical. Then, the water needs to be directed to enter the side of the reactor in the horizontal direction (horizontal entry was decided on for ease of fabrication, since it would be difficult to drill ellipses into the UASB reactor to allow for diagonal entry). The team considered using 135 degree elbows instead of 90 degree elbows for the change of direction to reduce headloss. The team also considered using diagonal pipes to minimize the amount of horizontal pipes, as settling is more likely to occur in horizontal pipes than diagonal pipes. However, after floating the idea at a technical feedback session, the team realized that such pipes may not be readily available in Honduras, and so it decided to use 90 degree elbows in the design.

After the team made these design decisions, it turned to hydraulic code from previous teams to finalize dimensions of the reactor including height of tipping bucket, height of the canister, diameter of influent pipes. HOLD UP STUFF USING 80 20 extrustion bars
