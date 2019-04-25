# UASB Research: Spring 2019 Research Report

###  Cara Smith, Rafael Heryapriadi, and Jahin Aishee
#### March 14th, 2019

**[Felix: Hey I'm going to be making comments in these square brackets. After addressing any comments please write within the brackets "-Addressed __" with the individual's initials in the __ space. They will be deleted in the next report.]**


## Table of Contents
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


  - [Abstract](#abstract)
  - [Introduction](#introduction)
  - [Literature Review and Previous Work](#literature-review-and-previous-work)
  - [Timeline of UASB](#timeline-of-uasb)
      - [Summer 2016](#summer-2016)
      - [2016](#fall-2016)
      - [Spring 2017](#spring-2017)
      - [Summer 2017](#summer-2017)
      - [Fall 2017](#fall-2017)
      - [Spring 2018](#spring-2018)
      - [Summer 2018](#summer-2018)
      - [Fall 2018](#fall-2018)
  - [Spring 2019 Goals](#spring-2019-goals)
  - [Lab Experiments](#lab-experiments)
      - [Methods](#methods)
      - [Methods - Part II](#methods-part-II)
      - [Results and Analysis](#results-and-analysis)
  - [Conclusion: Future Work](#future-work)
      - [Fabricating a Model Tipping Bucket System](#fabricating-a-model-tipping-bucket-system)
- [EPA Funding Assurance](#epa-funding-assurance)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


## Abstract

  For the past two years, the AguaClara Upflow Anaerobic Sludge Blanket Team, also known has UASB, has been in the works of designing and fabricating a pilot-scale Upflow Anaerboic Sludge Blanket reactor, a system which treats wastewater via anaerobic digestion, producing biogas in the process. UASB's design is completely gravity-powered and is a low cost solution to treating wastewater in rural communities that cannot afford typical wastewater treatment plants.

  This semester, the UASB Team divided into the two sister teams of UASB Research (UASB-R) and UASB Design (UASB-D). UASB-R is focused on benchtop testing of a model UASB, researching ways to increase the reactor's efficiency, and test out designs in lab before being implemented by UASB Design.

## Introduction

   When communities do not have access to wastewater treatment, they are forced to dump untreated wastewater directly to the environment. It eventually ends up in our rivers, streams, lakes, and oceans, and underground water sources tapped for well water [(Yahner and Taylor, 2018)](https://engineering.purdue.edu/~frankenb/NU-prowd/disease.htm). Wastewater contains organic and fecal matter, which can have harmful effects on the environment. Nutrients, such as nitrogen and phosphorus, can invade water sources causing algae blooms, and heavy metals and other inorganic material can **[also]** pollute bodies of water [(Gao, 2017)](http://isoilonline.com/2017/06/impacts-releasing-untreated-inadequately-treated-wastewater/).

  Untreated wastewater also is a significant public health risk, since wastewater can carry hundreds of different pathogens that can make a human very ill. Pathogens may be transmitted by direct contact with sewage, by eating food or drinking water contaminated with sewage, or through contact with human, animal, or insect carriers. Typhoid fever, cholera and especially diarrhea are common waterborne diseases that are often found in areas with improper wastewater treatment.

  It is difficult for many communities to find technology that can offer a reasonable, inexpensive way of treating wastewater. The United States treats its wastewater with technology that involves **[try using the word "requires"]** large retention times and ~~take up~~ significant amounts of land. American wastewater treatment plants also require a large energy input ~~,~~ because they are usually designed for densely populated urban areas, and are therefore expensive to set up and run.

  UASB’s reactor seeks **[A little weird to say that the reactor is seeking to do so and so... since reactor doesn't have hopes and dreams. Try something like "The purpose of UASB's reactor..." or the "UASB's reactor is designed to..."]** to reduce the challenges of setting up wastewater treatment systems in developing countries. An UASB reactor works by pumping wastewater into the bottom of a large tank filled with colonies of methane-producing, anaerobic bacteria, that form a structure called a sludge blanket. As the wastewater works its way up through the sludge blanket, the bacteria break down the organic and fecal matter and produce methane as a by-product. This has two benefits: one, this removes harmful particles in wastewater, and two, the methane automatically bubbles up to the top of the tank, where it can be collected and be burned as an energy source or heating. The water will then exit out the effluent pipe, where it can then go through a secondary treatment such as chlorination. UASB’s design, unlike other UASB reactors, is also completely gravity-powered and therefore requires zero electrical energy input. However, similar to an AguaClara plant, it requires an elevation difference to ~~flow~~ **[drive the flow of]** the wastewater through the UASB tank. This will be taken care of as long as the reactor is placed downhill from the wastewater source (e.g. a village).

  A depiction of the design is shown below:
<p align="center">
<img src="https://github.com/AguaClara/UASB/blob/master/Images/AC_FrontView.PNG?raw=true" width="200px"
/></p> <p align="center">
 <p align="center">
<img src="https://github.com/AguaClara/UASB/blob/master/Images/AC_SideView.PNG?raw=true" width="250px"
/></p>
<p align="center">Fig. 1a and 1b: Diagram of a traditional UASB Reactor (front and side views)

A recent, updated model in OnShape has also been created by UASB-Design [UASB model](https://cad.onshape.com/documents/9ad827a5eca9b7988dc2f6a0/w/b0be5680611b

0cca297e07f2/e/01184b12f18fae4acc6559c3) as UASB-Design.

**[A bit of an error on the caption here I think? Seems that the link got severed. But your figures are great. If they could be a bit bigger that would be perfect. If that's not possible it's okay. ]**
## Literature Review and Previous Work

  Tamil Nadu Agricultural University did a study in 2013 on an Upflow Anaerobic Sludge Blanket Reactor that was designed to handle 8,800 liters per day of influent wastewater where they found that the most effective volume of the reactor was 8.84 $m^3$ and that the optimum organic loading rate or the amount of water per unit of water was observed to have a chemical oxygen demand (COD) of 2.67$m^{-3}$ per day **[Correct me if I'm wrong but isn't COD measured in units of mass/volume?]** . This is the amount of oxygen needed to break down the wastewater's organic contents (so a high COD value is an indicator of a high amount of organic pollution). When the reactor operated at 3 days hydraulic retention time, or the length of time water has to sit in the reactor, the efficiency of the reactor was 70%. The reactor was also designed to collect gas that could be utilized for energy. This study done at a papaya fruit processing factory, where the reactor cost only Rs. 80,000 ($1160), showed that the gas used as energy had a payback period of 3 to 4 years, which is a fast payback period compared to solar panels. It also proved that the UASB provides onsite solutions to waste management problems [(Jeyapandiyan, 2014).](https://www.worldscientific.com/doi/abs/10.1142/9781848165434_0004)

  From the article “Anearobic Treatment Using UASB Reactors: Engineering and Operational Aspects” (Jules B. Van Lier et al.) it's apparent that the UASB reactor consists of 4 functional units: Primary Clarifier to remove the non biodegradable solids, Biological Reactor (secondary treatment) to remove organic compounds, Secondary Clarifier to treat effluent in the settler zone, and Sludge Digester to stabilize and improve dewatering characteristics. The article also discusses the importance of a pre-treatment and post treatment units, and gave examples of how developing countries like India do not have the support from academic institutions for researching this process when ~~they~~ compared ~~it~~ to Brazil, a country that has invested in fundamental and applied research in the subject matter. What Brazil has done, resulted in a large variety of STP (Sewage Treatment Plant)  in which the anaerobic technology is combined with adequate post treatment that offering cost-effective solution. Therefore**[,]** to point out the importance of the pre-treatment process, Lier mentioned that “without an efficient pretreatment treatment, the design, operation and maintenance of UASB reactors become an impossible job”. The site visit of full-scale STP~~’~~s revealed that there are many factors that are as important as a good design: [most importantly,] the operation and maintenance of the treatment plants [(Lier, 2010).](https://www.researchgate.net/publication/308072163_Design_of_Upflow_Anaerobic_Sludge_Blanket_UASB_reactor_for_Jam_Industry_Wastes)


## Timeline of UASB
#### Summer 2016
The UASB team was formed in the Summer of 2016. At that point, the objective of the team was to design and implement a functional lab-scale UASB reactor to treat synthetic blackwater **[Seems to be first time that you've mentioned synthetic wastewater/blackwater. You explain what blackwater is but what does "synthetic" mean?]**. Blackwater is wastewater from toilets. In the summer of 2016, the UASB team constructed four small-scale UASB reactors and found that those small-scale reactors could successfully treat synthetic wastewater. The team also found that increased wastewater concentration and higher residence times resulted in higher biogas removal and increased Chemical Oxygen Demand (COD) removal.

#### Fall 2016
In the fall of 2016, the UASB team underwent several changes. First, the team altered the design of the small-scale UASB reactors by implementing shorter and narrower influent lines. The team also changed the synthetic wastewater recipe. More specifically, the team substituted glucose with insoluble carbon compounds. The team also researched retention time in the reactors with fluoride tracer tests, and found a HRT of 3.22 hours in one of the reactors (close to the target of 4 hours).

#### Spring 2017
During the spring of 2017, the team worked on assessing the efficiency of two modifications to the UASB reactor: plate settlers and the submerged gas collection lid. After conducting granule settling tests, the team was unable to conclude whether or not plate settlers significantly improve solid retention time. The team also conducted a Submerged Gas Capture Lid Test and concluded that a check valve would be useful to allow for continuous collection into a gas tank without loss of biogas.

#### Summer 2017
In the summer of 2017, the UASB team continued with similar research and testing to that of the Spring 2017 semester. This time, the team determined that plate settlers were not required for a full scale reactor. Instead, a smaller settling apparatus, such as a sloped exit weir, can achieve similar sludge retention time (SRT). **[What is the implication of not requiring plate settlers? Does this save space in the UASB design?]**

#### Fall 2017
During the fall of 2017, the UASB team made several strides. Firstly, the team settled on the critical design assumptions for the fabrication of a UASB reactor at the Ithaca Area Wastewater Treatment Facility (IAWWTF). The critical design assumptions were as follows: a reactor diameter of 3 feet, a reactor height of 7 feet, a 4 hour hydraulic residence time, **[and]** a flow rate of .036 L/s. The  team also designed a biogas capture lid. In this system, as biogas is produced in the reactor, it displaces water out from under the lid. Gas is then stored there until it is manually removed.

The team also wrote Python calculations in Jupyter notebook (available on GitHub) to estimate biogas production based on COD input.

Next, the team decided to add plate settlers back to the effluent tube. Plate settlers are intended to prevent dislodged granules from escaping the reactor. The fall 2017 team also worked on designing a sludge weir for the UASB reactor.

#### Spring 2018
UASB continued efforts to improve the design of the pilot-scale UASB reactor in Spring 2018. A major area of focus was the influent flow system. After extensive research, the team chose top influent flow instead of bottom influent flow to prevent clogs **[Top influent flow like water is flowing from top to bottom? If so rewording it to clarify may help]**. Next, the team decided to incorporate pulse flow into the reactor to achieve the desired flow of .03 L/s. The team proposed two methods to produce pulse flow: a tipping bucket design and a siphon.

UASB also worked on biogas production. The team wrote code to estimate biogas production rate based on the flow rate through the reactor, the COD concentration of influent, and the temperature of the reactor **[this is just a peeve but I would move the first part of the list to the end. Saving the longest/heaviest for last typically makes something more readable]**. The team decided on a gas bag system to store biogas as it is flexible, easy to connect to the reactor, affordable, and easily transported. The team also wrote code to determine the required volume and dimensions for the lid of the biogas system. The team also looked into a fats, oils and greases (FOG) removal system. The ~~concluded~~ **[conclusion was]** that manual skimming of FOG could always be used as a backup option.

Next, the team developed the design for the pilot UASB reactor's sludge sampling and removal system. For the sludge weir, the team chose a tube with a 6 inch diameter jutting out of the reactor at the predicted height of the sludge blanket at a downwards angle with two valves.

Lastly, the team wrote code to calculate the optimal size of the pilot UASB reactor's tube settler, the number of plates required, and the overall height of the settling arm.

#### Summer 2018
The summer team continued work on the hydraulic design of the UASB system.  The major design project was creating the tipping bucket system to deliver wastewater in pulses.  The system consists of a pivoting bucket which fills with wastewater before tipping and delivering the wastewater in a large pulse at a high flow rate. After brainstorming the idea, the team designed and tested models to determine optimal design and flow rates for the system. The team also continued developing code for the entire system, and made a Computer Aided Design (CAD) [model of the UASB reactor](https://cornell47.autodesk360.com/g/shares/SH7f1edQT22b515c761e1224485004ae7e44?viewState=NoIgbgDAdAjCA0IDeAdEAXAngBwKZoC40ARXAZwEsBzAOzXjQEMyzd1C0IBOAEx4GYeAFgBsAWgBMjAGY8xQgKwTxjLl3H8A7KoBGEABwQd-IZrQBfEAF0gA) using Fusion 360.

#### Fall 2018

  During the fall of 2018, the team tested a benchtop UASB model in the lab. Because actual sludge granules ~~for~~ **[were]** not readily available, and the team considered ~~it~~ **[using them]** to be wasteful for early testing stages, the team decided to use tapioca to model the sludge blanket. Tapioca has similar material properties as sludge, inexpensive and readily available made it a suitable alternate material. Tapioca was used to identify preferential paths in the UASB reactor **[Define prefential paths]**. Preferential pathways cause an uneven distribution of wastewater flow throughout the reactor, making the UASB reactor less efficient.

  The benchtop model was a scaled down version of a real UASB reactor, made using Polyvinyl Chloride (PVC). The influent was set on top perpendicular to the bottom plate and a hole was drilled at the top of the model connected with a pipe as the effluent. The team used ProCoDa software to pump the water through the influent pipe. They also added red dye to the initial pulse of water to manually to look for preferential paths. It was suggested to use a second pump for inputting the dye in the future for more accurate testing.

**[A picture of benchtop model would be nice here]**

  The result of the testing shows that the layer of tapioca did not lift entirely off the bottom of the reactor, but instead it stretched as influent “wastewater” traveled through it. The red dye in the influent revealed the formation of preferential pathways through the tapioca layer. The team then came up with the idea of spreading the inlet flow by drilling four holes on the inlet tube near the bottom to decrease the preferential paths, but it was not completed by the end of 2018.

  So then a photometer was used to more accurately depict how the water was flowing through the sludge blanket by measuring whether or not the red dye concentration in the effluent tube was changing as expected. However, the tapioca was not a suitable material because it was too cloudy for the photometer to measure the red dye concentration.

The team then tried to use chia seeds instead of tapioca, which resulted in a worse scenario;  the chia seeds was too buoyant in water and prone to flowing out of the effluent. Ultimately the team used glass marbles  as the sludge blanket due to the time constrains. As predicted, this material was too heavy for the influent water to lift them and it was back to the drawing board.



## Spring 2019 Goals

  The goal of this semester was to redefine the inlet system to allow even distribution of influent water and biogas capture.  The model inlet design used during the fall, the single inlet tube whose goal was to deliver wastewater to the bottom of the reactor, was not spreading out the water evenly throughout the model sludge blanket leading to an inefficient reactor, thus less water purification **[Run on sentence here. Would split into two]**. That is due to some sludge granules not getting into contact with the wastewater, and therefore not degrading the organic matter in the wastewater. Another significant problem with the previous inlet design was that the inlet tube was inserted directly above the UASB reactor, but this is where the biogas capturing system must be.

  With the aforementioned problems, and the fact that UASB's old model was lost, creating a new model-scale inlet was a necessity. The team first sketched a few inlet designs with four openings to better distribute water flow. An idea of utilizing a manifold was shut down over concerns of clogging. ~~With finalized~~ **[After finalizing,]** designs UASB-R got the parts to construct a new model and started fabrication. Shown in Figure 3 is Design #1 excluding the attachment with the four openings.

<p align="center">
<img src="https://github.com/AguaClara/UASB/blob/master/Images/R%20Prototype.jpeg?raw=true" width="250px" /></p>
<p align="center">Fig. 3: Beginnings of the first inlet design of 2019

 As one can see, the inlet tube **[horizontally]** enters on the right side of the tank ~~with a horizontal component~~. UASB-R also thought of inserting the inlet tube at a lower height to see if the water velocity ~~be the~~ could be higher or cause less head loss. The two designs are shown in Figure 4.

 <p align="center">
<img src="https://github.com/AguaClara/UASB/blob/master/Images/Sketch%20UASB-R.jpeg?raw=true" width="250px" /></p>
<p align="center">Fig. 4: Two competing designs; sketch does not include effluent design or the biogas capture system.

The list below ~~was~~ **[contains]** the more detailed goals of UASB-R this semester:

- Construct and test the four inlet tube attachment using sludge granules.
- Test to see whether pulse flow vs continuous is flow more efficient using sludge granules*
    (Orginally, UASB was under the impression pulse flow would increase efficiency in the UASB reactor by increasing upflow velocity,       but new research has been pointing toward continuous flow.)
- Keep with UASB Design for any bench testing - specifically working on a design to evenly distribute wastewater flow through the inlet when the tipping bucket releases the wastewater.

## Lab Experiments

### Methods

The UASB-R team created an experiment that examined the exit velocity of the water from the effluent tube. Inlet systems that come in at two different heights of the benchtop model as shown in Figure 4 were designed and created.

**[Is there any experimental data on exit velocity recorded that you can show? Or are these experiments just based on observation?]**

UASB-R started to test the first design (the sketch on the right in Fig. 4 and shown in Fig. 5) using only tap water (no sludge). There were several leaks coming from the two elbows because the parts were old. These were replaced. Also, the team discovered leaks between the drilled hole and the 0.5" inlet pipe, so the team drilled a larger hole and attached seal tape to the threaded fitting to prevent leaks, as shown in Fig. 6.


<p align="center">
<img src="https://github.com/AguaClara/UASB/blob/master/Images/0625E55A-A03A-4D96-8646-0B8E1F3820A9.jpeg?raw=true" width="250px"
/></p>
<p align="center">Fig. 5: The old faulty connection

<p align="center">x`
<img src="https://github.com/AguaClara/UASB/blob/master/Images/New%20UASB.jpeg?raw=true" width="250px"/></p>
<p align="center">Fig. 6: the fixed connection

The UASB-R was able to start performing experiments with old sludge. NOTE: While sludge can stay alive in a suspended state in a fridge for up to one year, with only a small amount of sludge left, the team planned to get more sludge in early March. Unfortunately, due to AguaClara's contact for sludge granules at the Aanheuser-Busch Plant in Syracuse, NY retiring, both Prof. Ruth Richardson of the CEE department and UASB-R ~~have been unable to find a new~~ [did not have a] contact as of mid-April, and plans to get more sludge granules have stalled. Thankfully, the small amount was enough to finish this semester's testing.

UASB_R started pumping water through the UASB inlet at different flow rates and calculating the exit velocity. However, after consulting with a research advisor, it ~~was~~ **[became]** apparent that an inlet tube at a lower height would not be beneficial as the different heights would not make a significant difference to the efficiency of the reactor. Also, the lower inlet would make the system harder to clean and fix if anything **[were to break]** ~~broke~~. Thus, the remainder of the testing and some data initially collected was scrapped, but this initial testing helped the team learn more about ProCoDa ~~--~~ (the software used to run the pump), and the design fabricated was reused in the next task of the semester. [This last part of sentence is a bit odd. Don't know what you mean by the "design fabricated".. Did you mean the reactor shown in Fig 6?]

[I would recommend placing some of the math that you had done to determine that the lower height would not be beneficial in this section. It is also unclear why you haven't included any of the data that you had collected.]
### Methods - Part II

The four inlet system is shown below. The goal was less about fabricating an model that would perfectly emulate the inlet system and more about ~~getting~~ **[fabricating]** a simple design ~~fabricating~~ quickly ~~,~~ with materials already in the lab ~~,~~ that would provide four openings for the water to flow into the reactor tank ~~,~~ **[. This was done]** so **[that]** the team could test the hypothesis: that a greater number of inlets would reduce preferential pathways through the sludge blanket. There is would be no use using this more complicated design if it were to give the same results as the initial one-inlet design from last semester.

<p align="center">
<img src="https://github.com/AguaClara/UASB/blob/master/Images/IMG_0681%20(1).JPG?raw=true" width="250px"/></p>
<p align="center">Fig. 7 - The inlet system with four openings


The reactor tank was filled with tapioca and a bit of water, as shown in Fig. 8. A small amount of 20.0 g/ml solution of red dye was added to the tube that connects the pump and inlet, and water was pumped through the reactor, using ProCoDa at a flow rate of 1.0 ml/s. This one done four times. After each test, the tapioca was taken out of the reactor and rinsed with water to remove any leftover dye that would affect the team's results. Pictures and ~~vidoe~~ **[video]** recordings were taken to compare the results of each tests with each other and the tapioca tests with the one-inlet design from last semester.

 <p align="center">
<img src= "https://github.com/AguaClara/UASB/blob/master/Images/IMG_0815%20(1).JPG?raw=true" width="250px"/></p>
<p align="center"> Fig. 8 - The tapioca-filled UASB reacotor, pre-testing.

**[You guys should have a materials list to recreate both apparatuses that you have created, or at least make a note to refer to your sister team's report for materials. From the rubric "Clearly explain your apparatus and experiments. Provide enough detail for future team members and people unconnected to AguaClara to reproduce your experiments and apparatus"]**
 ###  Results and Analysis

As water moved through the reactor, the initial burst of dye spread throughout the lower part of the reactor, however the dyed water did not reach the sludge blanket uniformly for the first 10-20s (Fig. 9 and 10), which could lead to delay in wastewater treatment on a bigger scale.

<p align="center">
<img src="https://github.com/AguaClara/UASB/blob/master/Images/IMG_0806%20(1).JPG?raw=true" width="250px"/></p>
<p align="center">Fig. 9 - Front view of the reactor

<p align="center">
<img src="https://github.com/AguaClara/UASB/blob/master/Images/IMG_0808%20(1).JPG?raw=true" width="250px"/></p>
<p align="center">Fig. 10 - Back view of the reactor

But we found that preferential pathways (which would look like a long, mostly vertical stripe of white tapioca) were not indeed forming. **[Eventually]** The water was ~~eventually~~ reaching each part of the tapioca and not selectively choosing certain pathways, as shown in Fig. 11 after running the water for about 40 seconds during one of the tests.

<p align="center">
<img src="https://github.com/AguaClara/UASB/blob/master/Images/IMG_0844.JPG?raw=true" width="250px"/></p>
<p align="center">Fig. 11 - Reactor after dye has spread further

As the solution wasn't deemed perfect since during a meeting with Professor Weber-Shirk, Professor Richardson and the rest of the wastewater teams, there was a debate on ~~coming up with a way~~ **[how]** to check if the sludge blanket itself [and] not just ~~a~~ **[the]** tapioca model is being evenly fluidized in an UASB reactor. **[This sentence doesn't read quite smoothly. I would reorganizethis sentence]** However, this idea would have to researched further before it can be implemented.

Video recordings of some of the testing can be found [here](https://drive.google.com/open?id=1_VGCU7eiPV4JmfQAUlWmPip_AhztPh2U) and [here](https://drive.google.com/open?id=1ANP1-9QebNSnVUzGvlk4KH14PmZ7Fq4a).


## Future Work

### Fabricating a Model Tipping Bucket System

To test out the pulse inlet flow thoroughly, the team continued the idea of using the tipping bucket from 2018. Based on that tipping bucket, this year's UASB-R fabricated an inlet system using four pipes, where the tipping bucket pours the waste water, as shown in Figure 12.

Based on the sketch in Figure 12, the red section represents a wastewater tank that holds wastewater before **[entering?]** the tipping bucket, and the black box located on the bottom are the four pipe outlet system that deliver the waste water evenly to the sludge blanket reactor.

A transparent material was used to fabricate this system, so the team could observe what happens inside the tank. The tank was fabricated using the plastic containers, and the four pipe outlet system was fabricated using .5" thick plastic sheet. The plastic sheet was cut into squares with a perimeter of 3" and with a total of five sides. The four sides were for the wall, and the other side was used to enclose the bottom of the box. The four pieces of cut plastic then were glued together using PVC glue.

<p align="center">
<img src="https://github.com/AguaClara/UASB/blob/master/Images/BC6EE48D-AAA1-43AC-A45D-0C40D29D7809.jpeg?raw=true" width="250px"/></p>
<p align="center">Fig. 12 - Sketch of the tipping bucket system. Inlet tubes not included

The fabrication recently begun. The team has looked into testing the model of the tipping bucket system itself to see if ~~the~~ the flow is being evenly distributed into the four pipe inlet system. If not, UASB-R and UASB-D planned to work on new ideas to fix the problem. This process may be postponed to next semester depending on how long fabrication and testing takes.

## Key Contacts

The team has listed some key contacts for the UASB project so all members will know who to reach out to. They are summarized in the table below.

| Name                | Role                                                              | Email                             |
| ------------------- | ----------------------------------------------------------------- | --------------------------------- |
| Dr. Ruth Richardson | Faculty Advisor                                                   | water.ruth@gmail.com              |
| Ed Gottlieb         | Wastewater plant operator, primary contact at Wastewater facility | EGottlieb@cityofithaca.org        |
| N/A      | Contact at Anheuser-Bush, source for anaerobic granules           | N/A|



## EPA Funding Assurance
This article was developed under Assistance Agreement No. SU-83926801 awarded by the U.S. Environmental Protection Agency to Cornell University. It has not been formally reviewed by EPA. The views expressed in this document are solely those of [name of recipient or names of authors] and do not necessarily reflect those of the Agency. EPA does not endorse any products or commercial services mentioned in this publication.
