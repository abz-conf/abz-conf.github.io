---
title: ABZ 2025 – 11th International Conference on Rigorous State Based Methods
date:  "2024-09-17T00:00:00+01:00"
draft: false
share: false
contacts: true
commentable: false
editable: false

# Optional header image (relative to `static/img/` folder).
header:
  caption: ""
  image: ""

skyline: 
  image: "DuesseldorfSkyline_alternative_small.svg"
  url: "https://de.wikipedia.org/wiki/Düsseldorf"
---
## Workshops

ABZ 2025 will host the following workshops (to be completed).

### Rodin Workshop

Event-B is a formal method for system-level modeling and analysis. The Rodin Platform is an Eclipse-based toolset for Event-B that provides effective support for modeling and automated proof. The platform is open source and is further extendable with plug-ins. A range of plug-ins have already been developed.

The purpose of this workshop is to bring together existing and potential users and developers of the Rodin toolset and to foster a broader community of Rodin users and developers.

For Rodin users, the workshop will provide an opportunity to share tool experiences and gain an understanding of ongoing tool developments. For plug-in developers, the workshop will provide an opportunity to showcase their tools and to achieve better coordination of tool development efforts. 

Participants may attend or present both in person or remotely. 
If you are willing to participate remotely, please contact the organizers.

#### Format and Date

The workshop will host presentations, with ample time for discussions.

The Rodin workshop will be held on June 10, 2025.

#### Submission

If you are interested in giving a presentation at the Rodin workshop or have a plug-in to demonstrate, send a short abstract (1 or 2 pages PDF) to rodin@ecs.soton.ac.uk by 10th May.
We will endeavour to accommodate all submissions that are clearly relevant to Rodin and Event-B.
The proceedings of the workshop will be available as a technical report at the University of Southampton.

Additional details can be found at [https://wiki.event-b.org/index.php/Rodin_Workshop_2025](https://wiki.event-b.org/index.php/Rodin_Workshop_2025)

#### Exclusive Opportunity: Special Issue Publication

This year, we are excited to announce that a special issue is in the planning stages, and the selected high-quality submissions will be invited to contribute to a Special Issue.
(Note: The finalisation of the special issue is currently underway.)

#### Organisers

- Asieh Salehi Fathabadi, University of Southampton
- Laurent Voisin, Systerel
- Neeraj Kumar Singh,  INPT-ENSEEIHT / IRIT, University of Toulouse
- Michael Leuschel, Heinrich-Heine-Universität, Germany
- Son Hoang,  University of Southampton


### Tutorial and Workshop: Exploring Formal Methods for Unmanned Aerial Vehicles

<img src="/img/prob_drone.jpeg" style="width: 100%; height: auto; display: block;">

Unmanned aerial vehicle, including drones and electric flying taxis, will be essential in the future, supporting areas like logistics, transportation, infrastructure monitoring, disaster response, defense, and surveillance.
Accidents involving unmanned aerial vehicle could lead to serious threats to human lives, the environment, or cause significant financial damages. Therefore, ensuring the safety of unmanned aerial vehicle is crucial. 
This event focuses on using formal methods as a key approach to improve and ensure the safety of unmanned aerial vehicles.



This event will consist of two parts:
- a presentation and tutorial on using B and ProB in the classroom to enable students to write formal B models for high-level control of drones
- additional contributions by participants

#### Part I. Tutorial 

In an educational setting, we assigned students the task of selecting a drone-related problem (collision avoidance, exploring the environment, chasing another drone, etc.), modeling it with Classical B and Event-B, and formulating, validating, and verifying safety properties using ProB and Rodin.
The formal models were then connected to Crazyflie drones for real-life demonstration.
On the technical side, we [enhanced ProB to enable communication with the drones](https://prob.hhu.de/w/index.php?title=JSON_and_Sockets), allowing us to read sensor data and control them.
In the first part of the workshop, we present a tutorial on writing formal B models to control drones and present our experiences on teaching and getting the high-level control for drones to work.

#### Part 2. Workshop

In the second part, we invite other participants to give a presentation.
Our goal is to provide a platform for discussing challenges, issues and solutions in using formal methods for unmanned aerial vehicles and robotic systems, and explore new research and teaching directions together.

Relevant topics include, but are not limited to:

- Formal modeling, validation, and verification of aerial vehicles or robotic systems, including multi-agent systems
- Validation and verification of AI-driven systems
- Formal methods tool support: simulation, co-simulation, runtime monitoring, runtime verification, ...
- High-level control for aerial vehicles or robotic systems
- Application of formal methods to real-world aerial vehicles or robotic systems
- Teaching resources for formal models and aerial vehicles or robotic systems


If you are interested in giving a presentation at the workshop, we encourage you to send a short abstract (1 or 2 pages of PDF) to Fabian.Vu@hhu.de by <b>May 10th 2025</b> (but ideally as soon as possible).

We already have the following invited talks confirmed:

Marie Farrell. Sharper Specs for Smarter Drones: Formalising Requirements with FRET.
- Abstract: In this talk I will summarise our recent work on formalising requirements for an autonomous tilt-rotor drone in the ProVANT Emergentia research project. I will describe the process of formalising the natural-language requirements using NASA's Formal Requirements Elicitation Tool (FRET). I will present the progress made in each of the four sequential iterations of the requirements set as new information was elicited and incorporated. 

Thierry Lecomte. Introducing Feasible Safety to Autonomous Firefighting Drone.
- Abstract: We are presenting the formalization of the safety function of an autonomous aerial firefighting drone, from its system level RoboSim modelling to its implementation in B on a safety computer. The safety function implies a return to the base in case of power shortage or loss of communication with the base. The presentation provides a bird view on the overall experiment with a focus on the technical analyses and low-level formal modeling. 



