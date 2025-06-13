---
title: "Modelling the mechanical lung ventilation system using TASTD"

authors:
  - Alex Rodrigue Ndouna
  - Marc Frappier

date: 2024-07-03

# Schedule page publish date (NOT publication's date).
# publishDate: 2020-06-19T16:42:07+02:00

# Legend (see /data/publication_types.yaml and e.g. i18n/en.yaml): 
#   0 = "pub_uncat"
#   1 = "pub_conf"
#   2 = "pub_journal"
#   3 = "pub_preprint"
#   4 = "pub_report"
#   5 = "pub_book"
#   6 = "pub_book_section"
#   7 = "pub_thesis"
#   8 = "pub_patent"
#   9 = "pub_case_study_descr"
#  10 = "pub_case_study_contrib"
#  11 = "pub_short_paper"
#  12 = "pub_long_paper"
#  13 = "pub_invited_talk"
#  14 = "pub_phd_symposium"
publication_types:
  - 10  # default is 1 (conference), adjust as needed

publication: "10th International Conference on Rigorous State Based Methods (ABZ'24)"
publication_short: "ABZ'24"

tags:
  - ABZ'24

categories: []

featured: false

projects:
  - abz24

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007/978-3-031-63790-2_26.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-031-63790-2_26
    icon_pack: fas
    icon: book
  - name: Abstract
    url: "publication/frappier2024abz/#abstract"
    icon_pack: fas
    icon: file-alt
  - name: View
    url: "publication/frappier2024abz/#document"
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: "publication/frappier2024abz/#reference"
    icon_pack: fas
    icon: quote-right
  - name: Source
    url: "publication/frappier2024abz/#sources"
    icon_pack: fas
    icon: database

slides: ""
---

## Abstract

For the ABZ2024 conference, the proposed case study consists of modelling the adaptive outdoor mechanical lung ventilation system. The mechanical lung ventilator is intended to provide ventilation support for patients that are in intensive therapy and that require mechanical ventilation. The system under study is made up of two main software components: the graphical user interface (GUI) and the controller, this paper introduces a model for the controller part of the software system using Timed Algebraic State-Transition Diagrams (TASTD). TASTD is an extension of Algebraic State-Transition Diagrams (ASTD) providing timing operators to express timing constraints. The specification makes extensive use of the TASTD modularity capabilities, thanks to its algebraic approach, to model the behaviour of different sensors and actuators separately. We validate our specification using the cASTD compiler, which translates the TASTD specification into a C++ program. This generated program can be executed in simulation mode to manually update the system clock to check timing constraints. The model is executed on the test sequences provided with the case study. The advantages of having modularisation, orthogonality, abstraction, hierarchy, real-time, and graphical representation in one notation are highlighted with the proposed model.

## Document

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_26.pdf" >}}

## Reference

```
% BibTex
@InProceedings{10.1007/978-3-031-63790-2_26,
author="Rodrigue Ndouna, Alex
and Frappier, Marc",
editor="Bonfanti, Silvia
and Gargantini, Angelo
and Leuschel, Michael
and Riccobene, Elvinia
and Scandurra, Patrizia",
title="Modelling a Mechanical Lung Ventilation System Using TASTD",
booktitle="Rigorous State-Based Methods",
year="2024",
publisher="Springer Nature Switzerland",
address="Cham",
pages="324--340",
abstract="For the ABZ2024 conference, the proposed case study consists of modelling an adaptive outdoor mechanical lung ventilation system. The mechanical lung ventilator is intended to provide ventilation support for patients that are in intensive therapy and that require mechanical ventilation. The system under study is made up of two main software components: the graphical user interface (GUI) and the controller, this paper introduces a model for the controller part of the software system using Timed Algebraic State-Transition Diagrams (TASTD). TASTD is an extension of Algebraic State-Transition Diagrams (ASTD) providing timing operators to express timing constraints. The specification makes extensive use of the TASTD modularity capabilities, thanks to its algebraic approach, to model the behaviour of different sensors and actuators separately. We validate our specification using the cASTD compiler, which translates the TASTD specification into a C++ program. This generated program can be executed in simulation mode to manually update the system clock to check timing constraints. The model is executed on the test sequences provided with the case study. The advantages of having modularisation, orthogonality, abstraction, hierarchy, real-time, and graphical representation in one notation are highlighted with the proposed model.",
isbn="978-3-031-63790-2"
}
```

## Sources

- **Model Archive:**
  [GitHub](https://github.com/ndounalex/casestudyABZ2024-tastdmodel)
- **Presentation:**
  [PDF](/data/abz24/frappier2024abz.pdf)
- **Used formal method:**
  [TASTD](/method/TASTD)

  For more information, please contact the <a href ="mailto:Alex.Rodrigue.Ndouna@USherbrooke.ca;Marc.Frappier@USherbrooke.ca">authors</a>
