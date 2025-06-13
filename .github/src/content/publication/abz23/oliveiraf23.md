---
title: "Modelling an Automotive Software System with TASTD"

authors:
  - Diego de Azevedo Oliveira
  - Marc Frappier


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_10.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-031-33163-3_10
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/oliveiraf23/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/oliveiraf23/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/oliveiraf23/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/oliveiraf23/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

At the ABZ2020 Conference, the case study track proposed to model an Adaptive Exterior Light System and a Speed Control System: the former controls different exterior lights of a vehicle while the latter controls the speed of a vehicle. This paper introduces a model for these two case studies using Timed Algebraic State-Transition Diagrams (TASTD). TASTD is an extension of Algebraic State-Transition Diagrams (ASTD) providing timing operators to express timing constraints. The specification makes extensive use of the TASTD modularity capabilities, thanks to its algebraic approach, to model the behaviour of different sensors and actuators separately. We validate our specification using the cASTD compiler, which translates the TASTD specification into a C++ program. This generated program can be executed in simulation mode to manually update the system clock to check timing constraints. The model is executed on the test sequences provided with the case study. The paper provides a comparison between the TASTD model and other solutions presented at the ABZ2020 Conference. The advantages of having modularisation, orthogonality, abstraction, hierarchy, real-time, and graphical representation in one notation are highlighted with the proposed model.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_10.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_10.pdf" >}}

## Reference

```
% BibTex
@inproceedings{OliveiraF23,
  author       = {Diego de Azevedo Oliveira and
                  Marc Frappier},
  editor       = {Uwe Gl{\"{a}}sser and
                  Jos{\'{e}} Creissac Campos and
                  Dominique M{\'{e}}ry and
                  Philippe A. Palanque},
  title        = {Modelling an Automotive Software System with {TASTD}},
  booktitle    = {Rigorous State-Based Methods - 9th International Conference, {ABZ}
                  2023, Nancy, France, May 30 - June 2, 2023, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {14010},
  pages        = {124--141},
  publisher    = {Springer},
  year         = {2023},
  url          = {https://doi.org/10.1007/978-3-031-33163-3\_10},
  doi          = {10.1007/978-3-031-33163-3\_10},
  timestamp    = {Fri, 02 Jun 2023 21:23:53 +0200},
  biburl       = {https://dblp.org/rec/conf/zum/OliveiraF23.bib},
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

