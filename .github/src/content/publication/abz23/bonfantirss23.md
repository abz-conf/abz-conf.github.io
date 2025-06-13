---
title: "Modeling the MVM-Adapt System by Compositional I/O Abstract State Machines"

authors:
  - Silvia Bonfanti
  - Elvinia Riccobene
  - Davide Santandrea
  - Patrizia Scandurra


date: 2023-01-01

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
#  10 = "pub_short_paper"
#  11 = "pub_long_paper"
publication_types:
  - 1   # default is 1 (conference), adjust as needed

publication: "9th International Conference on Rigorous State Based Methods (ABZ'23)"
publication_short: "ABZ'23"

tags:
  - ABZ'23

categories: []

featured: false

# enable this for case studies
# projects:
#   - abz23

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_8.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-031-33163-3_8
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/bonfantirss23/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/bonfantirss23/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/bonfantirss23/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/bonfantirss23/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

With the increasing complexity and scale of software-intensive systems, model-based system development requires composable system models and composition operators. In line with such a vision, this paper describes our experience in modeling the behavior of the MVM-Adapt, an adaptive version of the Mechanical Ventilator Milano that has been designed, certified, and deployed during the COVID-19 pandemic for treating pneumonia. To keep the complexity of the requirements and models under control, we exploited a compositional modeling technique for discrete-event systems based on Abstract State Machines (ASMs). Essentially, separate ASMs represent the behavior of interacting subsystems of the MVM with their new adaptive functionalities; they can communicate with each other through I/O events, and co-operate by a precise orchestration schema.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_8.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_8.pdf" >}}

## Reference

```
% BibTex
@inproceedings{BonfantiRSS23,
  author       = {Silvia Bonfanti and
                  Elvinia Riccobene and
                  Davide Santandrea and
                  Patrizia Scandurra},
  editor       = {Uwe Gl{\"{a}}sser and
                  Jos{\'{e}} Creissac Campos and
                  Dominique M{\'{e}}ry and
                  Philippe A. Palanque},
  title        = {Modeling the MVM-Adapt System by Compositional {I/O} Abstract State
                  Machines},
  booktitle    = {Rigorous State-Based Methods - 9th International Conference, {ABZ}
                  2023, Nancy, France, May 30 - June 2, 2023, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {14010},
  pages        = {107--115},
  publisher    = {Springer},
  year         = {2023},
  url          = {https://doi.org/10.1007/978-3-031-33163-3\_8},
  doi          = {10.1007/978-3-031-33163-3\_8},
  timestamp    = {Fri, 02 Jun 2023 21:23:53 +0200},
  biburl       = {https://dblp.org/rec/conf/zum/BonfantiRSS23.bib},
  bibsource    = {dblp computer science bibliography, https://dblp.org}
}


```

<!-- # add information for case study papers (if available)
## Sources

- **Used formal method:**
  [ASM](/method/asm)
- **Resources and tools:**
  Asmeta

For more information, please contact the <a href ="mailto:silvia.bonfanti@unibg.it;arcaini@nii.ac.jp;angelo.gargantini@unibg.it;scandurra@unibg.it;elvinia.riccobene@unimi.it">authors</a>-->

