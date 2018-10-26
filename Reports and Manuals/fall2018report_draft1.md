# UASB, Fall 2018
### Ian Cullings, Ananya Gangadhar, Cara Smith, Nina Blahut
#### September 27, 2018


## Table of Contents
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [Abstract](#abstract)
- [Introduction](#introduction)
- [Literature Review and Previous Work](#literature-review-and-previous-work)
- [Timeline of UASB](#timeline-of-uasb)
    - [Summer 2016](#summer-2016)
    - [Fall 2016](#fall-2016)
    - [Spring 2017](#spring-2017)
    - [Summer 2017](#summer-2017)
    - [Fall 2017](#fall-2017)
    - [Spring 2018](#spring-2018)
    - [Summer 2018](#summer-2018)
- [Fall 2018 Goals](#fall-2018-goals)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

[EM: Hello, UASB team! For context, my comments will be underneath the paragraph in which I am referring to. Any questions, as always, contact aguaclaragraders@gmail.com!]

## Abstract
Since Spring 2017, the AguaClara Upflow Anaerobic Sludge Blanket (UASB) Team has been working on a detailed design of modified, pilot-scale UASB reactor.. A UASB reactor treats wastewater anaerobically and produces biogas as a by-product. Working towards that goal, the team has created Python code to record the design process and calculations for this AguaClara UASB.

For Fall 2018, the team will continue design work on the UASB with the goal of completing a full design.  Once this is done, the team will begin preparations for fabrication and implementation of the UASB at the Ithaca Area Wastewater Treatment Plant (IAWWTF).  Another goal for the semester is to begin researching flow patterns through the UASB to optimize treatment and prevent short-circuiting.

[EM: Great start - very clear and easy to understand. I would take out the part about the EPA proposal, it's not relevant.  Addressed -IC]

## Introduction

Many countries in the world lack proper access to wastewater treatment and release their wastewater directly into the environment untreated. The organic and fecal matter present in domestic water can cause harmful effects to the environment and on human health.

Organic matter in wastewater is broken down by bacteria that feed on it, consuming oxygen in the process. Depletion of dissolved oxygen levels in water can threaten and kill aquatic life.  Additionally, nutrients such as nitrogen and phosphorus present in high concentrations in wastewater can lead to explosive algal growth in waterways, which depletes oxygen levels and can create dead zones through a process known as [eutrophication](https://oceanservice.noaa.gov/facts/eutrophication.html). Fecal matter in wastewater can also cause the spread of infectious waterborne diseases like cholera, salmonella, and diarrhea, making it a huge threat to public health.

The current technology in the United States for treating municipal wastewater requires long retention times, large land areas and high monetary and energy costs. The large infrastructure and associated costs make conventional wastewater treatment unfeasible for small communities, who then resort to directly discharging their wastewater into streams. This problem can be addressed with the use of Upflow Anaerobic Sludge Blanket (UASB) reactors.

UASB reactors are used for primary treatment and clarify wastewater by removing suspended solids organic matter ([Chong et. al, 2012](https://www.sciencedirect.com/science/article/pii/S0043135412002400?via%3Dihub)). Organic carbon in the wastewater flowing up through the sludge blanket is consumed by the microbes residing within the sludge.  UASB reactors also produce methane as a by-product of anaerobic digestion.  This methane can be captured and burned for energy production or heating.

UASB reactors rely on gravity to clarify wastewater and biological processes to remove organic matter and convert it to biogas. They are less energy intensive than other forms of preliminary wastewater treatment that use aerobic processes.

In January 2017, a novel pilot scale UASB reactor design was created by AguaClara for the EPA People, Prosperity and the Planet (P3) [Student Design Competition proposal](https://docs.google.com/document/d/1geug1EyFjCRLQgO79vTOXUUFia3RBw3bhaIHPUiqu44/edit?usp=sharing). This reactor was designed to improve the accessibility of wastewater treatment for small communities. The proposed UASB reactor design identified areas to improve conventional reactor design, making the system cheaper and easier to fabricate and implement globally.  The team later applied for Phase II funding from the same organization to support development and implementation of additional reactors for testing.

## Literature Review and Previous Work

[EM: ^^^ Resolved - AG]

UASB reactors are currently being used for wastewater treatment to varying degrees of success. In 2005, Sato et. al performed a case study done on 16 full-scale UASBs in the Yamuna River Basin in India [(Sato, 2005)](https://www.sciencedirect.com/science/article/pii/S0301479705002860). The study found that the concentration of pollutants in effluent from these UASBs usually did not meet the effluent standards of most developing countries (Sato, 2005). Despite the failings of UASB reactors, the study is significant in showing that these reactors are an affordable option for wastewater treatment.   The study also emphasizes the importance of redesigning a UASB reactor to produce acceptable discharge standards.

[EM: Last sentence is awkward. Addressed -IC]

One of the main drawbacks of UASB reactors is that there is long initial start-up period before steady-state conditions are achieved; this time is usually in the range of several months [(Wang, 2018)](https://link.springer.com/article/10.1007%2Fs11356-017-0457-5
). Methods to decrease startup time include increasing load, optimizing temperature for anaerobic digestion, using a sufficient amount of sludge, and adding metal or an inert carrier. Wang et al. concluded that the addition of $FeCl_3$ during the initial stage of the UASB reactor start-up to promote granulation combined with the addition of Zero Valence Ions (ZVI) during the middle stage of reactor start-up is highly effective in reducing the initial start-up period (Wang, 2018). Once the team fabricates the pilot UASB, studies similar to this one will be useful in strategizing how to speed up the start-up period to test UASB quicker.

[EM: Be consistent with the way you refer to the reactor; will it be 'UASBs' or 'UASB digester?' Also, the sentence "A 2018 study concluded..." is long and a bit confusing. Is the start-up period in which the FeCl3 is added different than the start-up period that is looking to be shortened?]

In typical UASB reactors, removal of total suspended solids (TSS) is inversely proportional to upflow velocity within the reactor. This parameter is difficult to minimize since decreasing upflow velocity requires decreasing flow rate, which reduces the total amount of wastewater treated, reducing reactor efficiency. *Seghezzo et al.* compared efficiency of reactors at various upflow velocities and various sludge blanket heights. At lower upflow velocities, the height of the sludge blanket didn't impact efficiency significantly provided the height was roughly 2/5 the height of the tank. At higher upflow velocities, it was found that a sludge blanket height of 0.92 $m$ in a 2.5 $m$ tall reactor provided optimal conditions compared to higher sludge blanket heights.  [(Seghezzo, 2018)](https://www.researchgate.net/publication/266880587_The_effect_of_sludge_discharges_and_upflow_velocity_on_the_removal_of_suspended_solids_in_a_UASB_reactor_treating_settled_sewage_at_moderate_temperatures).

At this height, total suspended solids (TSS) removal remains above 90% and volatile suspended solids (VSS) removal above 80% when the upflow velocity was between 0.30-0.7 $m/hr$, but the best upflow velocity was at 0.48 $m/hr$ (TSS removal of 95%, VSS of 90%) An efficient operation could be around 0.5 $m/hr$ and height of sludge blanket= 1-2 $m$.
At  an upflow velocity of .85m/hr -wash out won’t occur, but might not be quite as efficient.
Overall low upflow velocities and taller sludge blankets tend to be optimal. Another paper recommends an upflow velocity between 0.25m/hr and 0.8m/hr, corroborating these claims [(Ghangrekar, 2012)](https://nptel.ac.in/courses/105105048/M21L35.pdf)

[EM: Provide the whole word of an acronym before just using the acronym (e.g. VSS). Above paragraph is messy; it is too wordy, lacking correct punctuation, and a bit informal.]

A paper published in the Netherlands ([Lattinga et. al, 1993](https://ac.els-cdn.com/096085249390038D/1-s2.0-096085249390038D-main.pdf?_tid=c83c2cd0-507e-4bba-a527-852fb5b2d0ed&acdnat=1537204715_6f79df9120ffd2cb0883ce08f1828336)) highlights how the process of granulation within the UASB reactor is positively impacted by high upflow velocities within the UASB reactor and low hydraulic retention times. This is an important parameter to keep in mind while designing the UASB reactor.

## Timeline of UASB
#### Summer 2016
The UASB team was formed in the Summer of 2016. At that point, the objective of the team was to design and implement a functional lab-scale UASB reactor to treat synthetic black water. Blackwater is wastewater from toilets. In the summer of 2016, the UASB team constructed four small-scale UASB reactors and found that those small-scale reactors could successfully treat synthetic wastewater. The team also found that increased wastewater concentration and higher residence times resulted in higher biogas removal and increased COD removal.

[EM: Define blackwater if not mentioned earlier in report. Adressed-NB]

#### Fall 2016
In the fall of 2016, the UASB team underwent several changes. First, the team altered the design of the small-scale UASB reactors by implementing shorter and narrower influent lines. The team also changed the synthetic wastewater recipe; more specifically, the team substituted glucose with insoluble carbon compounds. The team also researched retention time in the reactors with fluoride tracer tests, and found a HRT of 3.22 hours in one of the reactors,  which was not too far off from the target of 4 hours.

#### Spring 2017
During the Spring of 2017, the team worked on assessing the efficiency of two modifications to the UASB reactor: plate settlers and the submerged gas collection lid. After conducting granule settling tests, the team was unable to conclude whether or not plate settlers significantly improve solid retention time. The team also conducted a Submerged Gas Capture Lid Test and concluded that a check valve would be useful to allow for continuous collection into a gas tank without loss of biogas.

#### Summer 2017
In the summer of 2017, the UASB team continued with similar research and testing to that of the Spring 2017 semester. This time, the team determined that plate settlers were not required for a full scale reactor; instead, a smaller settling apparatus, such as a sloped exit weir, can achieve similar sludge retention time (SRT).

#### Fall 2017
During the Fall of 2017, the UASB team made several strides. Firstly, the team made critical design assumptions for the fabrication of a a UASB reactor at the IAWWTF . The critical design assumptions were as follows: a reactor diameter of 3 feet, a reactor height of 7 feet, a 4 hour hydraulic residence time, a flow rate of .036 L/s. The  team also designed a biogas capture lid. In this system, as biogas is produced in the reactor, it displaces water out from under the lid. Then, gas is stored there until it is manually removed. The team also wrote calculations in Jupyter to estimate biogas production based on COD input. Next, the team added an effluent tube settler to the design, which is intended to prevent dislodged granules from escaping the reactor. The Fall 2017 team also worked on designing a sludge weir for the UASB reactor.

[EM: Fix grammar and spelling errors.]

#### Spring 2018
UASB continued efforts to improve the design of the pilot-scale UASB reactor in Spring 2018. A major area of focus was the influent flow system. After extensive research, the team chose top influent flow instead of bottom influent flow to prevent clogs. Next, the team decided to incorporate pulse flow into the reactor to achieve the desired flow of .03 L/s. The team proposed two methods to produce pulse flow: a tipping bucket design and a siphon.

[EM: Fix grammar and spelling errors (the UASB.. team? reactor?)Adressed]

UASB also worked on biogas production. The team wrote code to estimate biogas production rate based on flow rate through the reactor, the COD concentration of influent, and the temperature of the reactor. The team decided that a gas bag would be used to store the biogas because it is flexible, easy to connect to the reactor, affordable, and easily transported. The team also wrote code to determine the required volume and dimensions for the lid of the biogas system. The team also looked into a fats, oils and greases (FOG) removal system. The concluded that manual skimming of FOG could always be used as a backup option.

[EM: The sentences in this paragraph are long and busy. Consider revising and making it a bit simpler.Adressed -NB]

Next, the team developed the design for the pilot UASB reactor's sludge sampling and removal system. For the sludge weir, the team chose a tube with a 6 inch diameter jutting out of the reactor at the predicted height of the sludge blanket at a downwards angle with two valves.

Lastly, the team wrote code to calculate the optimal size of the pilot UASB reactor's tube settler, the number of plates required, and the overall height of the settling arm.

[EM: When was it decided that plate settlers are actually required in a full-scale reactor (assuming conclusions from the Summer 2017 team was correct)?]

#### Summer 2018
In summer 2018, a Computer Aided Design (CAD) [model of the UASB reactor](https://cornell47.autodesk360.com/g/shares/SH7f1edQT22b515c761e1224485004ae7e44?viewState=NoIgbgDAdAjCA0IDeAdEAXAngBwKZoC40ARXAZwEsBzAOzXjQEMyzd1C0IBOAEx4GYeAFgBsAWgBMjAGY8xQgKwTxjLl3H8A7KoBGEABwQd-IZrQBfEAF0gA) was made using Fusion 360. The team decided that the best way to deliver wastewater to the UASB reactor was to use a tipping bucket system, because it is easy to manufacture, and uses parts that are both easy to obtain and inexpensive. The summer team determined hydraulic parameters, created code for the influent system parameters, and weighed the different methods of collecting the biogas produced. A tipping bucket influent system design was finalized after testing prototypes. Preliminary bench top tests were also performed to record the flow patterns in the tank.

[EM: What is a tipping bucket system?]

## Fall 2018 Goals

This semester, the team will finalize the UASB reactor design before fabrication. First, benchtop tests will be performed to study the flow patterns through the sludge (which will be simulated using tapioca). This will allow us to test various reactor and influent conditions and check for failure. The UASB reactor design can be modified based on the results of the tapioca tests. The plan is to consult Dr. Monroe Weber-Shirk and Dr. Todd Cowen for the details of the hydraulic design of the reactor, and also conduct literature searches for reactor designs. With this, the final dimensions of the reactor, upflow velocity, thickness of the sludge blanket and number of influent pipes can be determined.

[EM: How was it decided to use tapioca.. and are there drawbacks to using it? The answer to this is not necessarily relevant in the goals section, but it is something to keep in mind while writing the rest of the future report. Also, fix for grammar and punctuation mistakes.]

One major part of the design process will be writing design code for the reactor.  Since the UASB reactor can have many design approaches, it is important to create flexible code that can test different positions and determine the required parameters.  The team will be writing this code within the design manual and testing it rigorously to get the best design solution.

The team also plans to create an updated CAD model of the UASB reactor on OnShape (since AguaClara Cornell plans to move away from using Fusion 360 and use OnShape instead). If this cannot be accomplished the semester, it will be higher priority goal in the spring semester.

[EM: Fix grammar and spelling mistakes.]

The final goal of the team this semester is to begin prepping for fabrication.  This includes locating and ordering materials, making fabrication and safety plans, and learning fabrication techniques such as plastic welding.  With this groundwork laid, the team can begin fabrication easily and have a full plan on how to proceed.

Our full task map is included below:

![Task Map](https://github.com/AguaClara/UASB/blob/master/Images/taskmap_fall2018.JPG?raw=true)

## Lab Experiments

### Tapioca Tests
In the past few weeks, the UASB team has started a series of “tapioca tests” to get a better idea on how influent wastewater will travel through a sludge blanket in the current design for the UASB reactor. Because it would be costly and wasteful to use an actual sludge blanket during the early testing stages, the team has chosen tapioca to model a sludge blanket due to its similar material properties as well as due to its lower cost and widespread availability.

Pictured below is the small-scale model of the UASB reactor, which the team has been using for tapioca tests. So far, the tests have been in the preliminary, qualitative stages to get a better idea for how influent wastewater will travel through a sludge blanket in the UASB reactor, and whether or not a pulsed flow is effective.

**Photo of Small Scale Reactor**


####Conclusions Drawn from Experiment
So, moving forward, the team needs to rethink the design for the UASB reactor’s influent system. It must be altered to force wastewater to flow more evenly through the sludge blanket to eliminate preferential pathways.

The team has a few ideas on how to combat this problem. One idea is changing the number of influent pipes. While the majority of tests have been done with a single influent pipe, two pipes could lead to the wastewater being distributed more evenly among the sludge blanket instead of concentrating itself in the middle of the reactor. This will be a key focal area for the team’s tests in the upcoming month. So far, the team has only run an experiment with two tubes once, and very little could be concluded from that experiment due to significant leakage at the connection where the influent tube split off into two separate tubes. Once the connection is corrected, the team will resume tapioca tests.

Another idea is to change the geometry of the influent pipe, perhaps to something resembling a sprinkler. Again, the team needs to keep in mind that making pipes too small will cause clogging, and then no wastewater will flow through any part of the bed. If this were to be tested, this component would need to be designed and then fabricated.

Overall, the tapioca tests are still in the early stages, and a lot more tests will need to be run before an optimal flow rate and influent design is established. There are still several options that need to be explored before a definite one is chosen, and that will take time.

#### Methods
During tests, the team uses ProCoda to pump water through an influent pipe down the center of the small-scale reactor. The influent pipe extends to about a half of a centimeter above the reactor’s bottom. Once influent water hits the bottom of the reactor, it travels upwards through the layer of tapioca. Then, when the the water level in the reactor reaches the height of the effluent tube, water exits the reactor

The behavior of the mini-reactor during tapioca tests has been somewhat on par with that of a functional UASB reactor. In the team’s initial tests with a 100 RPM pump, there was no observable fluidization of the the tapioca blanket; however, the transition to a 600 RPM pump and subsequent increase of influent flow rate resulted in the partial fluidization of the tapioca. The layer of tapioca did not lift entirely off the bottom of the mini-reactor, but there was noticeable elongation of the tapioca layer as influent wastewater traveled through it, and the sludge blanket was indeed elongated uniformly

But in a properly functioning UASB reactor, the wastewater will then spread out evenly as it travels through the sludge blanket, so that it has the maximal possible surface contact with the granules in the sludge blanket. This has not happened in our tests. The team added red dye to influent water in order to follow the path of water through the model reactor. As shown, the reactor has been slightly lifted off the lab bench so a camera can be placed below and record the water movement at the opening of the influent tube. In doing so, the team observed the formation of preferential pathways through the tapioca layer. Preferential pathways are what happens when when incoming wastewater forms a tunnel through the sludge blanket and shoots through that tunnel instead of distributing itself evenly throughout the sludge blanket. As a result of preferential pathways, wastewater only gets contact with a very small portion of the surface area of the sludge blanket and hydraulic retention time is decreased, so the wastewater is not adequately cleaned. The testing showed the formation of preferential pathways along the walls of the reactor and along the influent tube.

<!--

#### Experimental Procedure

#### Results

## Methods
Explain the techniques you have used to acquire additional data and insights. Reserve fine detail for the Manual at the end of the report, but use this section to give an overview with enough detail for the reader to understand your Results and Analysis. Describe your apparatus, and have a justification for every decision you made and every parameter you chose in the design of the apparatus. Be especially careful to detail the conditions your experiments were conducted under, as this information is especially important for interpreting your results

Below, some example sections are given. Sectioning the report is meant to keep similar information together.  Continue making sections as necessary, or delete sections if you do not need them. Feel free to add subsubsections to further delineate the information. For example, under the Experimental Apparatus section below, the EStaRS team might consider having sections such as "Filter Design" and "Filter Fabrication".

### Experimental Apparatus
Explain your apparatus setup using enough detail such that future teams can recreate your apparatus. Make sure to explain why you built it this way. Create a schematic drawing of the apparatus (not a photo) that has clearly labeled components, flow paths, sensors, and reactor geometry.
* Design (calculations, constraints)

  $\frac{-b\pm\sqrt{b^2-4ac}}{2a}$
* Schematic (label parts)

  <img src="https://github.com/jillianwhiting/Jillian-Whiting/blob/master/Images/IMG_0009.jpg?raw=true" height=250 width=200>

* Image (from lab; label parts)
* Materials (dimensions, materials)
* Complications in construction
* If already constructed: write a brief summary of important constraints, include any revisions to apparatus, also reference the prior report where construction is described

### Procedure
Discuss your experimental procedure. How did you run your experiment? What were you testing? What were the values of relevant parameters?

## Results and Analysis
Present an observation (results), then explain what happened (analysis).  Each paragraph should focus on one aspect of your results. In that same paragraph, you should interpret that result.  
In other words, there should not be two distinct paragraphs, but instead one paragraph containing one result and the interpretation and analysis of this result. Here are some guiding questions for results and analysis:

When describing your results, present your data, using the guidelines below:
* What happened? What did you find?
* Show your experimental data in a professional way.
```python
from aide_design.play import*
x = np.array([1,2,3,4,5])
y = np.array([1,2,3,4,5])
plt.figure('ax',(10,8))
plt.plot(x,y,'*')
plt.savefig('/Users/jillianwhiting/github/Jillian-Whiting/Images/linear')
plt.show()
```
![linear](https://github.com/jillianwhiting/Jillian-Whiting/blob/master/Images/linear.png?raw=true)
Figure 1: Captions are very important for figures. Captions go below figures.

### Figure requirements
 - Create the graph using python (not Excel)
 - If the x axis is time then make zero time reflect the beginning of the test.
 - Use a white background for all graphs.
 - Most data will have both x and y values and thus should be presented using an xy scatter plot.
 - Label all axes and include units where appropriate.
 - Axis scale labels should be in the margin of the graph and not inside the graph border.
 - Eliminate parts of the range in both x and y axis that aren't used or that aren't meaningful.
 - Place a caption with a brief description below the graph. Add this caption using the wiki formatting, not in your graphing software.
 - Use data symbols to show data points unless there is so much data that the symbols overlap. If the data symbols overlap it is better to connect the data points with a line and not show the data symbols.
 - When presenting multiple plots on a single graph make sure that it is easy to distinguish the plots using the legend.
 - If curve fitting is used explain why and include the equation (elsewhere in the report).
 - If a model or theoretical curve is presented it should be a smooth curve without data points.
 - Use the same font in the graphs as you use in the text of the report.
 - Insert the graph in your report after the first reference to it in the text. Inserted the graph after the next paragraph break
 - Scale the size of the graph so it is large enough to see the data and read the text without having to follow a link to see a larger image. Avoid using hyperlinks on images because that causes the export to Microsoft Word option to not include the image.

After describing a particular result, within a paragraph, go on to connect your work to fundamental physics/chemistry/statics/fluid mechanics, or whatever field is appropriate. Analyze your results and compare with theoretical expectations; or, if you have not yet done the experiments, describe your expectations based on established knowledge. Include implications of your results. How will your results influence the design of AguaClara plants? If possible provide clear recommendations for design changes that should be adopted. Show your experimental data in a professional way using the following guidelines:
* Why did you get those results/data?
* Did these results line up with expectations?
* What went wrong?
* If the data do not support your hypothesis, is there another hypothesis that describes your new data?

## Conclusions
Explain what you have learned and how that influences your next steps. Why does what you discovered matter to AguaClara?

Make sure that you defend your conclusions with facts and results.

## Future Work
Describe your plan of action for the next several weeks of research. Detail the next steps for this team. How can AguaClara use what you discovered for future projects? Your suggestions for challenges for future teams are most welcome. Should research in this area continue?

## Bibliography
Logan, B. E., Hermanowicz, S. W., & Parker,A. S. (1987). A Fundamental Model for Trickling Filter Process Design. Journal (Water Pollution Control Federation), 59(12), 1029–1042.

# Manual
The goal of this section is to provide all of the guidance that would be necessary for a future team to pick up your work where you left off. Please try to be thorough and put yourselves in the shoes of a newcomer to the project. Below are some recommended sections, but the manual will likely take a slightly different form for each team.

## Fabrication Details
Include any information related to the fabrication of equipment, experimental apparatuses, or technologies. Include the purpose of each step and the fabrication methods used. Reference appropriate safety precautions.

## Special Components
If your subteam uses a particular part that is unique and you could foresee a future subteam needing to order it or learn more about it, please include basic information like the vendor where it was purchased, catalog/item number, and a link to any documentation.

## Experimental Methods
### Set-up
Step 1.
* Put tasks in a sequential order.
* It is okay to have sub-lists.
  - Like this.

### Experiment
Step 1.

### Cleaning Procedure
Step 1.

## Experimental Checklist
Another potential section could include a list of things that you need to check before running an experiment.

## ProCoDA Method File
Use this section to explain your method file. This could be broken up into several components as shown below:

### States
Here, you should describe the function of each state in your method file, both in terms of its overall purpose and also in terms of the details that make it distinct from other states. For example:
\begin{itemize}
\item \underline{OFF} - Resting state of ProCoDA. All sensors, relays, and pumps are turned off.
\end{itemize}

### Set Points
Here, you should list the set points used in your method file and explain their use as well as how each was calculated.

## Python Code

### Variables
$g$: gravity
$\sigma$: dispersion
$a$: amplitude
$h$: water depth
$H$: distance from wave crest to trough (2$a$)
$T$: wave period
$\lambda$: wavelength
$k$: wavenumber
$c_p$: celerity (wave phase speed)
$P$: pressure
$F$: force
$u$, $w$: x-velocity, z-velocity components

```python
# Comment
```


### EPA Funding Assurance
This publication [article] was developed under Assistance Agreement No. SU-83926801 awarded by the U.S. Environmental Protection Agency to Cornell University. It has not been formally reviewed by EPA. The views expressed in this document are solely those of [name of recipient or names of authors] and do not necessarily reflect those of the Agency. EPA does not endorse any products or commercial services mentioned in this publication.

# Add/Delete/Change this Template as you see Fit
When using this template keep in mind that this serves three purposes. The first is to provide your team feedback on your progress, assumptions, and conclusions. The second is to keep your team focused on what you are learning and doing for AguaClara. Another is to educate future teams on what you've learned and done. This document should be comprehensive, consistent, and well-written. With that in mind, add, subtract, or move sections. Reach out to the RAs and graders for help with figuring out what should or shouldn't include. Focus on how wonderful a reference you are making through this and work hard on communicating amongst yourselves and with future teammates. (Delete this section before submitting)

```python
# To convert the document from markdown to pdf
pandoc Name_of_this_file.md -o TeamName_Research_Report.pdf
```
-->
