# UASB Research: Spring 2019 Research Report

###  Cara Smith, Rafael Heryapriadi, and Jahin Aishee
#### February 21, 2019

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
- [EPA Funding Assurance](#epa-funding-assurance)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->




## Abstract

  For the past two years, the AguaClara Upflow Anaerobic Sludge Blanket Team, also known has UASB, has been in the works of designing and fabricating a pilot-scale Upflow Anaerboic Sludge Blanket reactor, a system which treats wastewater via anaerobic digestion, producing biogas in the process. UASB's design is completely gravity-powered and is a low cost solution to treating wastewater in rural communities that cannot afford typical wastewater treatment plants.

  This semester, the UASB Team divided into the two sister teams of UASB Research (UASB-R) and UASB Design (UASB-D). UASB Research is focused on benchtop testing of a model UASB, researching ways to increase the reactor's efficiency, and test out designs in lab before being implemented by UASB Design.

## Introduction
  
## Literature Review and Previous Work

  A paper published by Tamil Nadu Agricultural University did a study in 2013 on a Upflow Anaerobic Sludge Blanket Reactor that was designed to handle 8,800 liters per day of influent wastewater where they found that the most effective volume of the reactor was 8.84 m^3 and that the optimum organic loading rate was observed to be 2.67 COD  m^-3 per day. When the reactor operated at 3 days HRT the efficiency of the reactor was 70%. The reactor was also designed to collect gas to use for energy. This study done at a papaya fruit processing factory, where the reactor cost   Rs. 80,000, showed that the gas utilized had a payback period of 3 to 4 years . It also proved that the UASB provides onsite solutions to waste management problems.

 https://www.sciencedirect.com/science/article/pii/S0960852411013964
  The experiment of the effect of the temperature on low-strength wastewater treatment by UASB reactor using poly(vinyl alcohol)-gel carrie by Dophuong Khanh and team that published in 2011 shows that Hydraulic Retention Time (HDR) was reduced as the temperature was decreased. The research also shows that the COD (Chemical Oxygen Demand) removal rate was reduced by half when the temperature is decreased by 10’C. The key of the UASB process that allows higher volume of  COD loadings than in other anaerobic processes is the development of dense granulated sludge which require months to develop. 


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

#### Fall 2018
   The result shows that the layer of tapioca did not lift entirely off the bottom of the reactor, but instead it stretched as influent wastewater travelled through it. The team added red dye to the influent to follow the path of the flow of water, and found that the formation of preferential pathways through the tapioca layer which lead to inefficient treatment. The team then came out idea of spreading the inlet flow by drilling four holes near the bottom to decrease the preferential paths. 
  Using the photometer, the team wanted to test how water is flowing through the sludge blanket by measuring whether or not the red dye concentration in the effluent tube is changing as expected. However, the tapioca was not a suitable material because it was too cloudy for the photometer to measure the red dye concentration. 
  The team then tried to used chia seeds instead of tapioca, and resulted in a worse scenario because chia seed was too buoyant in water and prone to flowing out of the effluent. Ultimately the team used glass marble as the sludge blanket due to the time constrained. As predicted, this material was too heavy for the influent water to lift them. 

## Spring 2019 Goals

  There are a few goals UASB Research wants to accomplish this semester. The first is the inlet system of the UASB. The UASB team was dissatisfied with the model inlet design used during the fall; the single inlet tube, whose goal was to deliver wastewater to the bottom of the reactor, was not spreading out the water evenly throughout the model sludge blanket. When the water is not evenly distributed, the reactor is less efficient; some sludge granules are not getting into contact with the wastewater, and therefore they cannot degrade the organic material in the wastewater.  

  The team has sketched out a few designs - all with four openings in the inlet - to better distribute the flow. An idea to put in a manifold was shut down over concerns of clogging. UASB-R has already got the parts in order to create one of the designs, and the contruction and testing of that design will be accomplished after UASB-R

The inlet tube has to be inserted in the side of the UASB tank, so the February goal of 


