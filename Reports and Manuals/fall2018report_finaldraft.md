# UASB, Fall 2018
### Ian Cullings, Ananya Gangadhar, Cara Smith, Nina Blahut
#### December 8, 2018


[**CEO: This is a very good report. Great job adjusting the format where it makes sense. The only thing that seems out of place is the Gates Grant description...but I'm not sure where else you would put that..so it is fine how it is. Requires only minor edits.**]

[Resolved-AG **ZC: All or most figures are missing a figure caption. Figure captions should be stand-alone i.e. I should be able to understand what the figure it showing without having to search through the report for its reference. Each figure should also be referenced in-text.**]

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
  - [Fall 2018 Goals](#fall-2018-goals)
- [Lab Experiments](#lab-experiments)
  - [Tapioca Tests](#tapioca-tests)
    - [Experimental Apparatus](#experimental-apparatus)
    - [Set Up](#set-up)
    - [Experimental Procedure](#experimental-procedure)
    - [Cleaning Procedure](#cleaning-procedure)
  - [ProCoDa Method File](#procoda-method-file)
  - [Results](#results)
  - [Analysis](#analysis)
  - [Design Modifications](#design-modifications)
- [Gates Grant](#gates-grant)
- [Future Work](#future-work)
- [EPA Funding Assurance](#epa-funding-assurance)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Abstract
Since Spring 2017, the AguaClara Upflow Anaerobic Sludge Blanket (UASB) Team has been working on a detailed design of a pilot-scale UASB reactor. A UASB reactor treats wastewater anaerobically and produces biogas as a byproduct. Working towards that goal, the team has created Python code to record the design process and calculations for this AguaClara UASB.

During Fall 2018, the team continued design work on the UASB with the goal of completing a full design. The team also began researching flow patterns through the UASB to optimize treatment and prevent short-circuiting.

[**ZC: Make sure to use past tense throughout the report once you finalize**-Adressed NB]

## Introduction

Many countries in the world lack proper access to wastewater treatment and release their wastewater directly into the environment untreated. The organic and fecal matter present in domestic water can cause harmful effects to the environment and on human health.

Organic matter in wastewater is broken down by bacteria that feed on it, consuming oxygen in the process. Depletion of dissolved oxygen levels in water can threaten and kill aquatic life.  Additionally, nutrients such as nitrogen and phosphorus present in high concentrations in wastewater can lead to explosive algal growth in waterways, which depletes oxygen levels and can create dead zones through a process known as [eutrophication](https://oceanservice.noaa.gov/facts/eutrophication.html). Fecal matter in wastewater can also cause the spread of infectious waterborne diseases like cholera, salmonella, and diarrhea, making it a huge threat to public health.

The current technology in the United States for treating municipal wastewater requires long retention times, large land areas and high monetary and energy costs. The large infrastructure and associated costs make conventional wastewater treatment unfeasible for small communities, who then resort to directly discharging their wastewater into streams. This problem can be addressed with the use of Upflow Anaerobic Sludge Blanket (UASB) reactors.

UASB reactors are used for primary treatment and clarify wastewater by removing suspended solids organic matter ([Chong et. al, 2012](https://www.sciencedirect.com/science/article/pii/S0043135412002400?via%3Dihub)). Organic carbon in the wastewater flowing up through the sludge blanket is consumed by the microbes residing within the sludge through the process of anaerobic digestion, which is when bacteria break down biodegradable material without needing oxygen to do so. The paticular bacteria in the sludge blanket produce methane as a by-product of anaerobic digestion. This methane can be captured and burned for energy production or heating.
[**ZC: Bacteria and archaea make up a microbial community in each sludge granule i.e. the microbes are the sludge. Also define anaerobic digestion -Fixed CJMS**]

UASB reactors are already less energy intensive than many other forms of preliminary wastewater treatment, but they still require an electrical energy input. However, the UASB reactor designed by AguaClara is completely gravity-powered.[**ZC: This is a mischaracterization of what a UASB is. Utilizing gravity to power a UASB hydraulically was first proposed in the EPA Phase I proposal. It has never been implemented in literature. Typical UASB reactors still require a constant energy input for pumping like other wastewater treatment systems. Note that the energy input is lower than more conventional primary clarification methods such as activated sludge.-Fixed CJMS**] In January 2017, a novel gravity-powered UASB reactor was designed by AguaClara for the EPA People, Prosperity and the Planet (P3) [Student Design Competition proposal](https://docs.google.com/document/d/1geug1EyFjCRLQgO79vTOXUUFia3RBw3bhaIHPUiqu44/edit?usp=sharing). This reactor was designed to improve the accessibility of wastewater treatment for small communities. The proposed UASB reactor design identified areas to improve conventional reactor design, making the system cheaper and easier to fabricate and implement globally. The team later applied for Phase II funding from the same organization to support development and implementation of additional reactors for testing.

In the Fall 2018 semester, the team will focus on benchtop testing of the various components of the UASB reactor, and simulate the movement of water through the sludge blanket in order to better understand flow patterns within the reactor and possible failure modes.

[**CEO: The intro is very well written!**]

## Literature Review and Previous Work

UASB reactors are currently being used for wastewater treatment to varying degrees of success. In 2005, Sato et. al performed a case study done on 16 full-scale UASBs in the Yamuna River Basin in India [(Sato, 2005)](https://www.sciencedirect.com/science/article/pii/S0301479705002860). The study found that the concentration of pollutants in effluent from these UASBs usually did not meet the effluent standards of most developing countries (Sato, 2005). Despite the failings of UASB reactors, the study is significant in showing that these reactors are an affordable option for wastewater treatment.   The study also emphasizes the importance of redesigning a UASB reactor to produce acceptable discharge standards.

One of the main drawbacks of UASB reactors is that there is a long initial start-up period before steady-state conditions are achieved; this time is usually in the range of several months [(Wang, 2018)](https://link.springer.com/article/10.1007%2Fs11356-017-0457-5
). Methods to decrease startup time include increasing load, optimizing temperature for anaerobic digestion, using a sufficient amount of sludge, and adding metal or an inert carrier. Wang et al. concluded that the addition of $FeCl_3$ [**ZC: The formatting here doesn't show up on GitHub**]during the initial stage of the UASB reactor start-up to promote granulation combined with the addition of Zero Valence Ions (ZVI) during the middle stage of reactor start-up is highly effective in reducing the initial start-up period (Wang, 2018). Once the team fabricates the pilot UASB, studies similar to this one will be useful in strategizing how to speed up the start-up period to test UASB quicker.

In typical UASB reactors, studies have found that removal of total suspended solids (TSS) is inversely proportional to upflow velocity within the reactor.  This parameter is difficult to minimize since decreasing upflow velocity requires decreasing flow rate, which reduces the total amount of wastewater treated, reducing reactor efficiency. *Seghezzo et al.* compared efficiency of reactors at various upflow velocities and various sludge blanket heights. At lower upflow velocities, the height of the sludge blanket did not impact efficiency significantly, provided the height was roughly 2/5 the height of the tank. At higher upflow velocities, it was found that a sludge blanket height of 0.92m in a 2.5m tall reactor provided optimal conditions compared to higher sludge blanket heights.  [(Seghezzo, 2018)](https://www.researchgate.net/publication/266880587_The_effect_of_sludge_discharges_and_upflow_velocity_on_the_removal_of_suspended_solids_in_a_UASB_reactor_treating_settled_sewage_at_moderate_temperatures). The model reactor at these dimensions removed 80% of the TSS and 90% of the volatile suspended solids (VSS).  The overall findings of the paper suggested lower upflow velocities and taller sludge blankets are optimal for UASB efficiency.

[MAYBE RESOLVED?-AG-Show the units and chemical formulas in appropriate format. You may find something useful here: https://confluence.cornell.edu/display/AGUACLARA/Style+Guide+for+Figures%2C+Tables%2C+and+Equations]

Additionally, [Lettinga et. al. (1993)](https://ac.els-cdn.com/096085249390038D/1-s2.0-096085249390038D-main.pdf?_tid=c83c2cd0-507e-4bba-a527-852fb5b2d0ed&acdnat=1537204715_6f79df9120ffd2cb0883ce08f1828336) [**ZC: Lettinga** Addressed IC]highlights how the process of granulation within the UASB reactor is positively impacted by high upflow velocities within the UASB reactor and low hydraulic retention times. Both of these studies will be important when designing for UASB efficiency.  

[**CEO:Do these studies contradict each other? How will you optimize both in your desgin?**]


## Timeline of UASB
#### Summer 2016
The UASB team was formed in the Summer of 2016. At that point, the objective of the team was to design and implement a functional lab-scale UASB reactor to treat synthetic blackwater. Blackwater is wastewater from toilets. In the summer of 2016, the UASB team constructed four small-scale UASB reactors and found that those small-scale reactors could successfully treat synthetic wastewater. The team also found that increased wastewater concentration and higher residence times resulted in higher biogas removal and increased Chemical Oxygen Demand (COD) removal.


#### Fall 2016
In the fall of 2016, the UASB team underwent several changes. First, the team altered the design of the small-scale UASB reactors by implementing shorter and narrower influent lines. The team also changed the synthetic wastewater recipe. More specifically, the team substituted glucose with insoluble carbon compounds. The team also researched retention time in the reactors with fluoride tracer tests, and found a HRT of 3.22 hours in one of the reactors (close to the target of 4 hours).

#### Spring 2017
During the spring of 2017, the team worked on assessing the efficiency of two modifications to the UASB reactor: plate settlers and the submerged gas collection lid. After conducting granule settling tests, the team was unable to conclude whether or not plate settlers significantly improve solid retention time. The team also conducted a Submerged Gas Capture Lid Test and concluded that a check valve would be useful to allow for continuous collection into a gas tank without loss of biogas.

#### Summer 2017
In the summer of 2017, the UASB team continued with similar research and testing to that of the Spring 2017 semester. This time, the team determined that plate settlers were not required for a full scale reactor. Instead, a smaller settling apparatus, such as a sloped exit weir, can achieve similar sludge retention time (SRT).

#### Fall 2017
During the fall of 2017, the UASB team made several strides. Firstly, the team settled on the critical design assumptions for the fabrication of a UASB reactor at the IAWWTF . The critical design assumptions were as follows: a reactor diameter of 3 feet, a reactor height of 7 feet, a 4 hour hydraulic residence time, a flow rate of .036 L/s. The  team also designed a biogas capture lid. In this system, as biogas is produced in the reactor, it displaces water out from under the lid. Gas is then stored there until it is manually removed.

The team also wrote Python calculations in Jupyter notebook (available on GitHub) to estimate biogas production based on COD input.

Next, the team decided to add plate settlers back to the effluent tube. Plate settlers are intended to prevent dislodged granules from escaping the reactor. The fall 2017 team also worked on designing a sludge weir for the UASB reactor.

#### Spring 2018
UASB continued efforts to improve the design of the pilot-scale UASB reactor in Spring 2018. A major area of focus was the influent flow system. After extensive research, the team chose top influent flow instead of bottom influent flow to prevent clogs. Next, the team decided to incorporate pulse flow into the reactor to achieve the desired flow of .03 L/s. The team proposed two methods to produce pulse flow: a tipping bucket design and a siphon.

UASB also worked on biogas production. The team wrote code to estimate biogas production rate based on the flow rate through the reactor, the COD concentration of influent, and the temperature of the reactor. The team decided on a gas bag system to store biogas as it is flexible, easy to connect to the reactor, affordable, and easily transported. The team also wrote code to determine the required volume and dimensions for the lid of the biogas system. The team also looked into a fats, oils and greases (FOG) removal system. The concluded that manual skimming of FOG could always be used as a backup option.

Next, the team developed the design for the pilot UASB reactor's sludge sampling and removal system. For the sludge weir, the team chose a tube with a 6 inch diameter jutting out of the reactor at the predicted height of the sludge blanket at a downwards angle with two valves.

Lastly, the team wrote code to calculate the optimal size of the pilot UASB reactor's tube settler, the number of plates required, and the overall height of the settling arm.

#### Summer 2018
The summer team continued work on the hydraulic design of the UASB system.  The major design project was creating the tipping bucket system to deliver wastewater in pulses.  The system consists of a pivoting bucket which fills with wastewater before tipping and delivering the wastewater in a large pulse at a high flow rate.  After brainstorming the idea, the team designed and tested models to determine optimal design and flow rates for the system.  The team also continued developing code for the entire system, and made a Computer Aided Design (CAD) [model of the UASB reactor](https://cornell47.autodesk360.com/g/shares/SH7f1edQT22b515c761e1224485004ae7e44?viewState=NoIgbgDAdAjCA0IDeAdEAXAngBwKZoC40ARXAZwEsBzAOzXjQEMyzd1C0IBOAEx4GYeAFgBsAWgBMjAGY8xQgKwTxjLl3H8A7KoBGEABwQd-IZrQBfEAF0gA) using Fusion 360.

## Fall 2018 Goals

[**ZC: Again, update sentence structure to past tense once the report is finalized** ADDRESSED NB]

In the fall semester of 2018, the team aimed to finalize the UASB reactor design before fabrication. While the team did not accomplish this goal, the team began to address this goal with bench top tests to study the flow patterns through sludge.  Tapioca was chosen to use for a model of a sludge blanket because tapioca has material properties similar to that of sludge. The goal of these tests was to inform the team on failure conditions in the model UASB reactor.

Another goal for the Fall 2018 semester was to write code to model designs of the reactor.  Since the UASB reactor can have many design approaches, it is important to create flexible code that can test different positions and determine the required parameters. This semester, the team started writing the code to determine the dimensions of the effluent tube of the model reactor. Once this goal has been completed, the final dimensions of the reactor, upflow velocity, thickness of the sludge blanket and number of influent pipes can be determined.

Because AguaClara has moved from Fusion 360 to Onshape, UASB also aimed to create an updated CAD model of the UASB reactor on OnShape. This goal was not accomplished the semester, but the team will consult with AIDE to see if there is a simple way to move the design from Fusion.

The final goal for the team in the fall 2018 semester was to begin prepping for fabrication. This includes locating and ordering materials, making fabrication and safety plans, and learning fabrication techniques such as plastic welding. While the team did not locate nor order materials, members got fabrication experience during bench top tests as well as safety training.
Our full task map is included below:
<div style = “text-align:center”>

<p align="center">
  <img src="https://github.com/AguaClara/UASB/blob/master/Images/task_map_F18.jpg?raw=true" width="800px" /></p>
<p align="center">Fig. x: Lab scale model UASB reactor<p>

[The task map above looks good, but using a flowchart instead of a photo might be better. Addressed IC]
# Lab Experiments

## Tapioca Tests
The major research focus the fall semester of 2018 was running a series of “tapioca tests” to get a better idea on how influent wastewater will travel through a sludge blanket in the current design for the UASB reactor. Because it would be costly and wasteful to use an actual sludge blanket during the early testing stages, the team first chose to use tapioca to model a sludge blanket. Tapioca has similar material properties to sludge, is inexpensive, and readily available.

### Experimental Apparatus

To run model experiments, a scaled-down UASB reactor (Figure 2) was fabricated over the summer.  The reactor was created using a clear 3 inch diameter clear PVC pipe, which was welded to a PVC sheet.  A 2 inch hole was then drilled and tapped at 70% of the height of the reactor, and a half inch push to connect was connected.  

 [**ZC: Please use professional/academic language when referring to objects by alternative names. Recall that this information is published online and represents AguaClara.**  Addressed IDC]


<p align="center">
  <img src="https://github.com/AguaClara/UASB/blob/master/Images/UASB_prototype.png?raw=true" width="400px" /></p>
<p align="center">Fig. x: Lab scale model UASB reactor<p>

Figure Two: Model UASB Reactor with tapioca set up for experiments.  

The influent tube was created using rigid plastic tubing, that was attached through connectors to flexible tubing running through the pumps.  This was attached to the back of our lab bench using 80-20 bars and brackets so that it could be simply loosened and removed from the reactor for adjustments.  This allowed the influent tube to be easily removed and changed with different modifications throughout the semester.

### Set Up

Place the small-scale UASB reactor on the lab bench. Use brackets to secure a 5/8 inch pipe so that it is positioned perpendicular to the bottom of the reactor and it extends to about .5 cm above the bottom of the small-scale reactor. Attach the influent pipe to a 600 RMP. Attach a red dye pump to the influent line of water.

### Experimental Procedure

1. Prepare tapioca by mixing equal parts tapioca and water.
2. Wait ten minutes for tapioca pearls to expand in water.
3. Pour tapioca into Bethany until it is ¾ full.
4. Use leveler to ensure that the influent pipe is perpendicular to the bottom of the reactor.
6. Inject a plug of red dye to the influent water.  
7. Use ProCoda to pump water into Bethany through the influent pipe.
8. Observe the flow of red dye through the tapioca layer and the movement of the tapioca blanket.
9. Repeat steps 1 through 8 using different flow rates and length of flow rate pulse.
10. Clean up.

### Cleaning Procedure
1. Use strainer to separate water and tapioca.
2. Refrigerate leftover tapioca.
3. Dump water down the drain.
4. Rinse out the small-scale UASB reactor.

## ProCoDa Method File

The ProCoDa file used for the Tapioca tests has three states:

<p align="center">
  <img src="https://github.com/AguaClara/UASB/blob/master/Images/statel.PNG?raw=true" width="300px" /></p>
<p align="center">Fig. x: State list for Tapioca Test<p align="center">

* Off: Full system off, shuts down both pumps
* On: Pump runs at set flowrate in pulses separated by pulses at the set time
* Pause: System turns off during set time and then turns on

The set points are listed below:
<p align="center">
  <img src="https://github.com/AguaClara/UASB/blob/master/Images/setp.PNG?raw=true" width="300px" /></p>
<p align="center">Fig. x: ProCoDa Setup for experiments<p align="center">

* ON: Turns system on
* OFF: Turns system off
* Flow rate: Desired flow rate of system, in $ml/s$
* Tubing size: Integer corresponding to tubing size, found on [AguaClara Confluence](https://confluence.cornell.edu/display/AGUACLARA/Auto+Tutorial+for+Peristaltic+Pumps)
* Pump speed: calculates desired pump speed (in rpm) using ProCoDa function
* Run time: The time the pump should run at the calculated speed.  For the experiments this was 3 seconds.
* Pause time: The time the system remains in the pause state before running.  For the experiments, this was 30 seconds.

For our the initial experiments, red dye was loaded into the system manually by running the pump until a set amount of dye was visible in the tubing, then injected through running the water pump.  In future quantitative tests this will be controlled through ProCoDa as well using the second pump.

## Results

During tests, the team uses ProCoDa to pump water through an influent pipe down the center of the small-scale reactor. The influent pipe extends to about a half of a centimeter above the reactor’s bottom. Once influent water hits the bottom of the reactor, it travels upwards through the layer of tapioca. Then, when the water level in the reactor reaches the height of the effluent tube, water exits the reactor

The behavior of the mini-reactor during tapioca tests has been somewhat on par with that of a functional UASB reactor. In the team’s initial tests with a 100 RPM pump, there was no observable fluidization of the tapioca blanket; however, the transition to a 600 RPM pump and subsequent increase of influent flow rate resulted in the partial fluidization of the tapioca. The layer of tapioca did not lift entirely off the bottom of the reactor, but there was noticeable stretching of the tapioca layer as influent wastewater traveled through it, and the sludge blanket did indeed stretch uniformly.



[**ZC: This image appears rotated on GitHub. Also include a standalone figure caption and reference the figure in the text.**]

## Analysis
In a properly functioning UASB reactor, the wastewater will spread out evenly as it travels through the sludge blanket, so that it has the maximal possible surface contact with the granules in the sludge blanket. This has not happened in the tests yet. The team added red dye to influent water in order to follow the path of water through the model reactor.

<p align="center">
  <img src="https://github.com/AguaClara/UASB/blob/master/Images/UASB_Red_Dye_Tapioca_Test.PNG?raw=true=50x" width="250px" /></p>
<p align="center">Fig. x: Preliminary dye tests with tapioca showing preferential pathways<p>

[**ZC: There is a formatting problem here**]
In figure x, the tapioca is not an even shade of pink because the dye has not evenly distributed itself due to preferential pathways
The reactor has been slightly lifted off the lab bench so a camera can be placed below and record the water movement at the opening of the influent tube. In doing so, the team observed the formation of preferential pathways through the tapioca layer. Preferential pathways occur when incoming wastewater forms a tunnel through the sludge blanket and shoots through the tunnel instead of distributing evenly throughout the sludge blanket. As a result of preferential pathways, wastewater only gets contact with a very small portion of the surface area of the sludge blanket and hydraulic retention time is decreased, so the wastewater is not adequately cleaned. The testing showed the formation of preferential pathways along the walls of the reactor and along the influent tube, which can be seen in the tapioca — only portions of which made contact with the dye.

## Design Modifications
Firstly, modifications were made to the influent system. Instead of one large opening for wastewater to flow out the influent pipe, the team has capped this opening and drilled 4 holes near the bottom of the point, guessing that influent wastewater will now be forced to spread out, thereby decreasing the likelihood of preferential paths from forming.

<p align="center">
  <img src="https://github.com/AguaClara/UASB/blob/master/Images/Modified_Influent_Pipe_Drawing.JPG?raw=true" width="250px" /></p>
<p align="center">Fig. x: Schematic for modified influent pipe<p>

In order to begin collecting quantitative data, the team set up a photometer. The photometer will be used in testing to determine how water is flowing through the sludge blanket. A plug of red dye will be injected to the influent pipe in the UASB. Then, the photometer will measure the concentration of red dye coming out of the model UASB reactor in the effluent tube. If the reactor is functioning properly, the red dye will flow evenly through the model sludge blanket, so all the dye will come out of the effluent tube at the same time, which will be indicated by a spike of red dye concentration coming out of the effluent tube. The photometer will be used to measure whether or not the red dye concentration in the effluent tube is changing as expected for a functional UASB.  
[**ZC: A figure with the experimental apparatus (whether photo or diagram) would help explain this better and assist future teams replicate your work if needed**]

The decision to use a photometer to collect quantitative data made tapioca an unsuitable sludge blanket because tapioca gives off a residue in water, which makes it too cloudy for the photometer to measure red dye concentration. Chia seeds were chosen as a replacement to model the sludge blanket since they do not degrade as quickly as tapioca does.

In order to prepare the model sludge blanket from chia seeds, the team placed the chia seeds in water and waited approximately 20 minutes for the seeds to expand. The chia seeds were somewhat buoyant in water. Some of the chia seeds sank to the bottom of the container and others stuck together on the water's surface. When the team placed the expanded chia seeds inside the model UASB reactor and began to run water through the model UASB reactor, it became clear that chia seeds are not an effective model for the sludge blanket. Firstly, chia seeds are to sticky; the seeds stick to each other, which prevents water from flowing through them, and they stick to the walls and sides of the reactor. Secondly, the chia seeds were prone to flowing out of the effluent tube, which caused frequent clogging and would render photometer readings meaningless.

<p align="center">
  <img src="https://github.com/AguaClara/UASB/blob/master/Images/The%20UASB%20Apocalypse.jpg?raw=true" width="300px" /></p>
<p align="center">Fig. x: Chia seeds forming uneven clumps within the lab UASB reactor<p>

Upon realizing that chia seeds were not usable for modeling the sludge blanket, the team decided that glass beads would be a possible alternative. Due to time constraints, the team was unable to order new materials for the sludge blanket model, but there were glass marbles in the lab, which the team decided to test as a model sludge blanket.

<p align="center">
  <img src="https://github.com/AguaClara/UASB/blob/master/Images/rightside.jpeg?raw=true" width="300px" /></p>
<p align="center">Fig. x: Dye tests in the lab UASB reactor filled with marbles<p>

The glass marbles were about 1 cm in diameter. The glass marbles did not work as a model for sludge granules because they were too heavy for the influent water to lift them. While the glass marbles were not useful for modeling the sludge blanket, they did give the team the opportunity to use the photometer to measure the read dye concentration of water in the model UASB effluent.

Next semester, the team plans to purchase glass beads that share a similar size and density to that of sludge granules. The team also plans to run tests with actual sludge from a local brewery.


## Gates Grant
UASB has written and submitted a grant proposal for the Gates Grand Challenges Round 22 for Innovation for WASH in Urban Settings. In the proposal, the team suggested a system for wastewater treatment in developing urban settings by initially separating domestic wastewater into its two components: blackwater (water from flush toilets) and greywater (water from sinks, laundry, etc.). Then the blackwater would be treated via our UASB reactor.

An eighteen-month plan for the implementation of an UASB reactor in Honduras was developed, along with an estimated budget. If chosen, UASB would receive $100,000 for Phase I and up to one million dollars if also selected for Phase II.
The schematic below summarizes the idea proposed in the Gates Proposal.

<p align="center">
  <img src="https://github.com/AguaClara/UASB/blob/master/Images/gates%20grant%20schematic.png?raw=true" width="800px" /></p>
<p align="center">Fig. x: Flow chart used in the Gates Grant proposal<p>

The proposal can be read [here](https://github.com/AguaClara/UASB/blob/master/README.md).

# Future Work

While quite a lot was accomplished this semester, UASB discovered that there are still a lot of elements of the UASB reactor that need to be researched and finalized within a short amount of time; therefore, the team structure will be changing next semester. In final discussions, the team decided that the main priority for next semester is the design and fabrication team, and not the fluids research.  While this research was still valuable for increasing the teams knowledge of how upflow reactors work, the main focus of the team should be creating a working prototype to test in the wastewater treatment plant.  As such, the team recommends that the main UASB team completely focus on design, and if there is room for another team created, we will recruit a full research team to continue the research work done this semester.

### Design Team Goals

The main task for the fabrication team will be to finish design of the UASB system, create a CAD model in OnShape, and begin fabrication so the system can be implemented.  This will primarily involve writing flexible design code that incorporates many parts of the UASB system together and runs calculations for all of them.  As such, it would be desirable to recruit students with design experience, fluids experience, and fabrication experience to this team.  

### Research Team Goals

The main task for the research team is to continue the testing done this semester. This includes reducing preferential pathways, working on influent design, and integrating the tipping bucket system worked on during the summer into the design. This would also involve helping the fabrication team with elements they think should be tested out in lab before being implemented fully into the actual reactor.

### Key Contacts

Due to a shift in leadership, the team decided to list some key contacts for the UASB project so all members will know who to reach out to.  They are summarized in the table below.

| Name                | Role                                                              | Email                             |
| ------------------- | ----------------------------------------------------------------- | --------------------------------- |
| Dr. Ruth Richardson | Faculty Advisor                                                   | water.ruth@gmail.com              |
| Ed Gottlieb         | Wastewater plant operator, primary contact at Wastewater facility | EGottlieb@cityofithaca.org        |
| Robert Cleeton      | Contact at Anheuser-Bush, source for anaerobic granules           | robert.cleeton@anheuser-busch.com |



# EPA Funding Assurance
This publication [article] was developed under Assistance Agreement No. SU-83926801 awarded by the U.S. Environmental Protection Agency to Cornell University. It has not been formally reviewed by EPA. The views expressed in this document are solely those of [name of recipient or names of authors] and do not necessarily reflect those of the Agency. EPA does not endorse any products or commercial services mentioned in this publication.
