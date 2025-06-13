---
title: "Modelling an automotive software-intensive system with adaptive features using ASMETA"

authors:
  - Paolo Arcaini
  - Silvia Bonfanti
  - Angelo Gargantini
  - Elvinia Riccobene
  - Patrizia Scandurra

date: 2020-06-03

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
publication_types:
  - 10   # default is 1 (conference), adjust as needed

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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-030-48077-6_25.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-030-48077-6_25
    icon_pack: fas
    icon: book
  - name: Abstract
    url: "publication/arcaini2020abz/#abstract"
    icon_pack: fas
    icon: file-alt
  - name: View
    url: "publication/arcaini2020abz/#document"
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: "publication/arcaini2020abz/#reference"
    icon_pack: fas
    icon: quote-right
  - name: Source
    url: "publication/arcaini2020abz/#sources"
    icon_pack: fas
    icon: database

slides: ""
---

## Abstract

In the context of automotive domain, modern control systems are software-intensive and have adaptive features to provide safety and comfort. These software-based features demand software engineering approaches and formal methods that are able to guarantee correct operation, since malfunctions may cause harm/damage. Adaptive Exterior Light and the Speed Control Systems are examples of software-intensive systems that equip modern cars. We have used the Abstract State Machines to model the behaviour of both control systems. Each model has been developed through model refinement, following the incremental way in which functional requirements are given. We used the asmeta tool-set to support the simulation of the abstract models, their validation against the informal requirements, and the verification of behavioural properties. In this paper, we discuss our modelling, validation and verification strategies, and the results (in terms of features addressed and not) of our activities. In particular, we provide insights on how we addressed the adaptive features (the adaptive high beam headlights and the adaptive cruise control) by explicitly modelling their software control loops according to the MAPE-K (Monitor-Analyse-Plan-Execute over a shared Knowledge) reference control model for self-adaptive systems.

## Document

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-030-48077-6_25.pdf" >}}

## Reference

```
% BibTex
@inproceedings{arcaini2020abz,
  title={{Modelling an automotive software-intensive system with adaptive features using ASMETA}},
  author={Arcaini, Paolo and Bonfanti, Silvia and Gargantini, Angelo and Riccobene, Elvinia and Scandurra, Patrizia},
  booktitle={7th International Conference on Rigorous State Based Methods (ABZ'20)},
  pages={302--317},
  year={2020},
  organization={Springer}
}
```

## Sources

- **Used formal method:**
  [ASM](/method/asm)
- **Resources and tools:**
  Asmeta

  For more information, please contact the <a href ="mailto:silvia.bonfanti@unibg.it;arcaini@nii.ac.jp;angelo.gargantini@unibg.it;scandurra@unibg.it;elvinia.riccobene@unimi.it">authors</a>
