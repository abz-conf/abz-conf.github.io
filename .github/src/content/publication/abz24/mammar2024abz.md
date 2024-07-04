---
title: "An Event-B Model of a Mechanical Lung Ventilator"

authors:
  - Amel Mammar

date: 2024-07-03

# Schedule page publish date (NOT publication's date).
# publishDate: 2020-06-19T16:42:07+02:00

publication_types:
  - 1 # conference paper

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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_25.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-031-63790-2_25
    icon_pack: fas
    icon: book
  - name: Abstract
    url: "publication/mammar2024abz/#abstract"
    icon_pack: fas
    icon: file-alt
  - name: View
    url: "publication/mammar2024abz/#document"
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: "publication/mammar2024abz/#reference"
    icon_pack: fas
    icon: quote-right
  - name: Source
    url: "publication/mammar2024abz/#sources"
    icon_pack: fas
    icon: database

slides: ""
---

## Abstract

In this paper, we present a formal Event-B model of the Mechanical Lung Ventilator (MLV), the case study provided by the ABZ’24 conference. This system aims at helping patients maintain good breathing by providing mechanical ventilation. For this purpose, two modes are possible: Pressure Controlled Ventilation (PCV) and Pressure Support Ventilation (PSV). In the former mode, respiratory cycles are completely defined by the patient that is able to start breathing on its own. In the latter mode, the respiratory cycle is constant and controlled by the ventilator. Let us note that it is possible to move from a given mode to the other depending on the breathing capabilities of the patient under ventilation. In this paper, we illustrate the use of a correct-by-construction approach, the Event-B formal method and its refinement process, for the formal modeling and the verification of such a complex and critical system. The development of the formal models has been achieved under the Rodin platform that provides us with automatic and interactive provers used to verify the correctness of the models. We have also validated the built Event-B models using the ProB animator/model checker.

## Document

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_25.pdf" >}}

## Reference

```
% BibTex
@InProceedings{Mammar2024abz,
author="Mammar, Amel",
editor="Bonfanti, Silvia
and Gargantini, Angelo
and Leuschel, Michael
and Riccobene, Elvinia
and Scandurra, Patrizia",
title="An Event-B Model of a Mechanical Lung Ventilator",
booktitle="Rigorous State-Based Methods",
year="2024",
publisher="Springer Nature Switzerland",
address="Cham",
pages="307--323",
abstract="In this paper, we present a formal Event-B model of the Mechanical Lung Ventilator (MLV), the case study provided by the ABZ'24 conference. This system aims at helping patients maintain good breathing by providing mechanical ventilation. For this purpose, two modes are possible: Pressure Controlled Ventilation (PCV) and Pressure Support Ventilation (PSV). In the former mode, respiratory cycles are completely defined by the patient that is able to start breathing on its own. In the latter mode, the respiratory cycle is constant and controlled by the ventilator. Let us note that it is possible to move from a given mode to the other depending on the breathing capabilities of the patient under ventilation. In this paper, we illustrate the use of a correct-by-construction approach, the Event-B formal method and its refinement process, for the formal modeling and the verification of such a complex and critical system. The development of the formal models has been achieved under the Rodin platform that provides us with automatic and interactive provers used to verify the correctness of the models. We have also validated the built Event-B models using the ProB animator/model checker.",
isbn="978-3-031-63790-2"
}
```

## Sources

- **Model Archive:**
  [GitHub](https://github.com/AmelMammar/MechanicalLungVentilator)
- **Presentation:**
  [PDF](/data/abz24/mammar2024abz.pdf)
- **Used formal method:**
  [Event-B](/method/event-b)

  For more information, please contact the <a href ="mailto:amel.mammar@telecom-sudparis.eu">authors</a>
