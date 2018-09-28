# AguaClara Research Report & Manual Template
#### Natalie Mottl, William Pennock, Janak Shah, and Jillian Whiting
#### February 20, 2018

# Template Description
This template will lay out all possible sections that could be used for a research report and manual. All research reports and manuals should strive to comply with this template, but every team will use different parts. In order to use this template, copy this file from the AguaClara team resources repository to your team's repository, and rename it for your team in a format similar to  "[Team Name] [Semester]". An example would be "Filter and Treatment Train Flow Control Spring 2017." For additional information on all the possibilities in markdown files, refer to the AguaClara Interactive Tutorial and the AguaClara Tutorial training pages. After you complete that step, please delete this description and everything above this.

# UASB, Fall 2018
#### Ian Cullings, Ananya Gangadhar, Cara Smith, Nina Blahut
#### September 27, 2018

## Abstract
Briefly summarize your previous work, goals and objectives, what you have accomplished, and future work. (100 words max)

## Introduction
Explain how the completion of your challenge will affect AguaClara and the mission of providing safe drinking water (or sustainable wastewater treatment!). If this is a continuing team, how will your contribution build upon previous research? What needs to be further discovered or defined? If this is a new team, what prompted the inclusion of this team?

## Literature Review and Previous Work
Discuss what is already known about your research area based on both external work and that of past AguaClara Teams. Connect your objectives with what is already known and explain what additional contribution you intend to make. Make sure to add APA formatted in-text citations. If you mention the author(s) in your sentence, you can simply give the year of publication.[(Logan et. al. 1987)](http://www.jstor.org/stable/pdf/25043431.pdf?acceptTC=true)

UASBs are currently being used for wastewater treatment in the real world to varying degrees of success. In 2005, there was a case study done on 16 full-scale UASBs in the Yamuna River Basin in India (Sato, 2005). The study found that the concentration of pollutants in effluent from these UASBs usually did not meet the effluent standards of most developing countries (Sato, 2005). Despite the failure of the aforementioned UASB reactors to bring wastewater to effluent standards, the study is significant in showing that UASBs are an affordable option for wastewater treatment and underscores the importance of designing a UASB reactor that produces effluent, which meets discharge standards. 

One of the main drawbacks of UASB digesters is that there is long initial start-up period before steady-state conditions are achieved; this time is usually in the range of several months (Wang, 2018). There are methods to decrease startup time such as increasing load, optimizing temperature for anaerobic digestion, using a sufficient amount of sludge, and adding metal or an inert carrier. A 2018 study concluded that the addition of FeCl3 during the initial stage of the UASB start-up to promote granulation combined with the addition of ZVI during the middle stage of reactor start-up is highly effective in reducing the initial start-up period (Wang, 2018). Once the team fabricates the pilot UASB, studies similar to this one will be useful in strategizing how to speed up the start-up period to test UASB quicklier. 

The effect of sludge discharges and upflow velocity on the removal of suspended solids in a UASB reactor treating settled sewage at moderate temperatures. 

Solid removal is inversely proportionally to upflow velcoity. But of course, we can't run of reactor super slow, or else it would be time-consuming and ineffiencient. Sludge still has to be discharged at minimum frequency. A study was done in Argentina comparing effiency of reactors at various uplflow velocities and various sludge blanket heights. At lower upflow velocities, the height of the sludge blanket didn't matter as much as long as its around 2/5 the height of the tank (over 0.9m for a tank of 2.5m in height) . But at higher velocities, a height of 0.92m ends up winning out over higher sludge blanket heights (The effect of sludge discharges and upflow velocity on the removal of suspended solids in a UASB reactor treating settled sewage at moderate temperatures. (Seghezzo, 2018)

At this height, TSS removal remains above 90% and VSS removal above 80% when the upflow velocity was between 0.30-0.7m/hr, but the best was at 0.48m/hr (TSS removal of 95%, VSS of 90%) An efficient operation could be around 0.5m/hr and height of sludge blanket= 1-2m
If you wanted to go higher, at .85m/hr -wash out won’t occur, but might not be quite as efficient
Overall low upflow velocities and taller sludge blankets tend to be the way to go. Another paper recommends an upflow velocity between 0.25m/hr and 0.8m/hr, corroborating these claims (Ghangrekar, 2012)

## UASB's work
The UASB team was formed in the Summer of 2016. At that point, the objective of the team was to design and implement a functional lab-scale UASB system to treat synthetic black water. In summer of 2016, the UASB team constructed four small-scale UASB reactors and found that those small-scale reactors could successfully treat synthetic wastewater. The team also found that increased wastewater concentration and higher residence times resulted in higher biogas removal  and increased COD removal. 

Then, in the fall of 2016 the UASB team made several changes. First, the team altered the design of the small-scale UASBs by implementing shorter and narrower influent lines. The team also changed the synthetic wastewater recipe; more specifically, the team substituted glucose with insoluble carbon compounds. The team also researched retention time in the reactors with fluoride tracer tests, and found a HRT of 3.22 hours in one of the reactors,  which was not too far off from the target of 4 hours. 

Moving on, during the Spring of 2017, the team worked on assessing the efficiency of two modifications to the UASB system: plate settlers and the submerged gas collection lid. After conducting a granule settling tests, the team was unable to conclude whether or not plate settlers significantly improve solid retention time. The team also conducted a Submerged Gas Capture Lid Test and concluded that a check valve would be useful to allow for continuous collection into a gas tank without loss of biogas. 

Then, in the Summer 2017, the UASB continued with similar research and testing to that of the Spring 2017 semester. This time, the team determined that plate settlers were not required for a full scale reactor; instead, a smaller settling apparatus, such as a sloped exit weir, can achieve similar SRT. 

During the Fall of 2017, the UASB team made several strides. Firstly, the team made critical design assumptions for the fabrication of a a UASB treatment system at the IAWWTF . The critical design assumptions were as follows: a reactor diameter of 3 feet, a reactor height of 7 feet, a 4 hour hydraulic residence time, a flow rate of .036 L/s. The  team also designed a biogas capture lid. In this system, as biogas is produced in the reactor, it displaces water out from under the lid. Then, gas is stored there until it is manually removed. Also related to biogas, the team wrote calculations in Jupyter to estimate biogas production based on COD input. Next, the team added an effluent tube settler to the design, which is intended to prevent dislodged granules from escaping the reactor. The Fall of 2017 team also worked on designing a sludge weir for the UASB reactor. The team found that it was difficult to predict the growth rate of sludge cells, so it decided to set an initial size for the pilot scale reactor and then collect data from the pilot for future designs. 

The UASB continued efforts to improve the design of the pilot-scale UASB during the Spring of 2018. A major area of focus was the influent flow system. After extensive research the team chose top influent flow instead of bottom influent flow to prevent clogs. Next, the team decided to incorporate pulse flow into the reactor to achieve the desired flow of .03 L/s. The team proposed two methods to produce pulse flow: a tipping bucket design and a siphon. The next area of research during the Spring of 2018 was on biogas production. The team wrote code to estimate biogas production rate based on flow rate through the reactor, the COD concentration of influent, and the temperature of the reactor. Also related to biogas, the team decided that a gas bag would be used to store the biogas released from the reactor, since it is flexible, easy to connect to the reactor, affordable, and easily transported. Furthermore, the team wrote code for the biogas capture design, which intakes the daily volume of biogas produced, the desired number of days for storage, and time required before critical lid failure and then returns the required volume for the temporary storage system and required dimensions for the lid to retain a set amount of biogas before failing. The team also looked into a FOG removal system and came up with the idea of an outflow pipe or siphon coming out of the removable lid with a valve to allow for the discharge of water containing fats. The team also concluded that manual skimming of FOGs could always be used as a backup option. Next, the team developed the design for the pilot UASB’s sludge sampling and removal system. For the sludge weird, the team decided on a tube with a 6 inch diameter jutting out of the reactor at the predicted height of the sludge blanket at a downwards angle with two valves. Lastly, the team wrote code to calculate the optimal size of the pilot UASB’s tube settler, the number of plates required, and the overall height of the settling arm. 

Summer 2018 (to be written 9/28 I'm currently too dead :) -Cara

Fall 2018
This semester, our team has been finalizing our designs for our UASB system. We are on track, so far, to begin to expand from our model into a full-fledged UASB system before the semester ends. But first, we will be performing tests of the effectiveness of our reactor by modeling the sludge blanket with tapioca. This will allow us the get a feel for the reactor and tweak our design as we go, without having to worry about live bacteria just yet. We may also make a CAD model of our design, but that has yet to be decided. Also, we have been consulting with Dr. Monroe and Prof. Edwin Cowen, as well as researching similar UASB experiments done both at home and abroad, for how to make our system as efficient as possible and determining final qualities of the reactor, such as the dimensions of the tank, upflow velocity, thickness of sludge blanket, number of pipes flowing in and out of the reactor, etc. Trial-and-error through our tapioca tests, however, will be the final determination. Once we feel we have modeled the optimum system, we will build our reactor at the Ithaca Wastewater Plant, which has graciously offered us a lead-free room in their building. This may possibly be done by first building sections of the reactor at the lab and then moving them to the Plant for final construction.




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

# Add/Delete/Change this Template as you see Fit
When using this template keep in mind that this serves three purposes. The first is to provide your team feedback on your progress, assumptions, and conclusions. The second is to keep your team focused on what you are learning and doing for AguaClara. Another is to educate future teams on what you've learned and done. This document should be comprehensive, consistent, and well-written. With that in mind, add, subtract, or move sections. Reach out to the RAs and graders for help with figuring out what should or shouldn't include. Focus on how wonderful a reference you are making through this and work hard on communicating amongst yourselves and with future teammates. (Delete this section before submitting)

```python
# To convert the document from markdown to pdf
pandoc Name_of_this_file.md -o TeamName_Research_Report.pdf
```
