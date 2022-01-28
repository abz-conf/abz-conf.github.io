---
title: "Modeling of a Speed Control System using Event-B"

authors:
- Amel Mammar
- Marc Frappier

date: 2020-06-03

# Schedule page publish date (NOT publication's date).
# publishDate: 2020-06-19T16:42:07+02:00

publication_types:
-  1 # conference paper

publication: "7th International Conference on Rigorous State Based Methods (ABZ'20)"
publication_short: "ABZ'20"

tags:
- ABZ'20

categories: []

featured: false

projects:
- abz20

links:
- name: Digital
  url: https://link.springer.com/content/pdf/10.1007%2F978-3-030-48077-6_29.pdf
  icon_pack: fas
  icon: file-pdf
- name: Printed
  url: https://doi.org/10.1007/978-3-030-48077-6_29
  icon_pack: fas
  icon: book
- name: Abstract
  url: "publication/mammar2020abz_/#abstract"
  icon_pack: fas
  icon: file-alt
- name: View
  url: "publication/mammar2020abz_/#document"
  icon_pack: fas
  icon: glasses
- name: Cite
  url: "publication/mammar2020abz_/#reference"
  icon_pack: fas
  icon: quote-right
- name: Source
  url: "publication/mammar2020abz_/#sources"
  icon_pack: fas
  icon: database

slides: ""
---

## Abstract

The present paper presents our proposal of an \eventB model of a speed control system, a part of the case study provided in the ABZ2020 conference. The case study describes how the system regulates the current speed of a car according to a set criteria like the speed desired by the driver, the position of a possible preceding vehicle but also a given speed limit that the driver must not exceed. For that purpose, this controller reads different information form the available sensors (key state, desired speed, etc.) and takes the adequate actions by acting on the actuators of the car's speed according to the read information. To formally model this system, we adopt a stepwise refinement approach with the Event-B method. We consider most features of the case study, all proof obligations have been discharged using the Rodin provers. Our model has been validated using ProB by applying the different provided scenarios. This validation has permitted us to point out and correct some mistakes, ambiguities and oversights contained in the first versions of the case study.

## Document

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-030-48077-6_29.pdf" >}}

## Reference

~~~
% BibTex
@inproceedings{mammar2020modeling,
  title={{Modeling of a Speed Control System using Event-B}},
  author={Mammar, Amel and Frappier, Marc},
  booktitle={7th International Conference on Rigorous State Based Methods (ABZ'20)},
  pages={367--381},
  year={2020},
  organization={Springer}
}
~~~

## Sources

- **Model Archive:**
  Not available
- **Presentation:**
  Not available
- **Used formal method:**
  [Event-B](/method/event-b)
- **Resources and tools:**
  Not available
- **Required OS:**
  Not available
- **Website:**
  Not available
- **Remarks and recommendation:**
  Not available
