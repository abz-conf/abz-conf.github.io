---
title: "An Event-B Model of an Automotive Adaptive Exterior Light System"

authors:
  - Amel Mammar
  - Marc Frappier
  - Regine Laleau

date: 2020-06-03

# Schedule page publish date (NOT publication's date).
# publishDate: 2020-06-19T16:42:07+02:00

publication_types:
  - 1 # conference paper

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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-030-48077-6_28.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-030-48077-6_28
    icon_pack: fas
    icon: book
  - name: Abstract
    url: "publication/mammar2020abz/#abstract"
    icon_pack: fas
    icon: file-alt
  - name: View
    url: "publication/mammar2020abz/#document"
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: "publication/mammar2020abz/#reference"
    icon_pack: fas
    icon: quote-right
  - name: Source
    url: "publication/mammar2020abz/#sources"
    icon_pack: fas
    icon: database

slides: ""
---

## Abstract

This paper introduces an Event-B formal model of the adaptive exterior light system for cars, a case study proposed in the context of the ABZ2020 conference. The system describes the different provided lights and the conditions under which they are switched on/off in order to improve the visibility of the driver without dazzling the oncoming ones. The system can be viewed as a lights controller that reads different information form the available sensors (key state, exterior luminosity, etc.) and takes the adequate actions by acting on the actuators of the lights in order to ensure a good visibility for the driver according to the information read. Our model is built using stepwise refinement with the \eventB method. We consider all the features of the case study, all proof obligations have been discharged using the \rodin provers. Our model has been validated using ProB by applying the different provided scenarios. This validation has permitted us to point out and correct some mistakes, ambiguities and oversights in the first versions of the case study.

## Document

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-030-48077-6_28.pdf" >}}

## Reference

```
% BibTex
@inproceedings{mammar2020abz,
  title={{An Event-B Model of an Automotive Adaptive Exterior Light System}},
  author={Mammar, Amel and Frappier, Marc and Laleau, Regine},
  booktitle={7th International Conference on Rigorous State Based Methods (ABZ'20)},
  pages={351--366},
  year={2020},
  organization={Springer}
}
```

## Sources

- **Used formal method:**
  [Event-B](/method/event-b)

  For more information, please contact the <a href ="mailto:amel.mammar@telecom-sudparis.eu;marc.frappier@usherbrooke.ca;laleau@u-pec.fr">authors</a>
