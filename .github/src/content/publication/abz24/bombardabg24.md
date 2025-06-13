---
title: "From Concept to Code: Unveiling a Tool for Translating Abstract State Machines into Java Code"

authors:
  - Andrea Bombarda
  - Silvia Bonfanti
  - Angelo Gargantini


date: 2024-01-01

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

publication: "10th International Conference on Rigorous State Based Methods (ABZ'24)"
publication_short: "ABZ'24"

tags:
  - ABZ'24

categories: []

featured: false

# enable this for case studies
# projects:
#   - abz24

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_10.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-031-63790-2_10
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/bombardabg24/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/bombardabg24/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/bombardabg24/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/bombardabg24/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Formal methods play a crucial role in modeling and quality assurance, but to be deployed on real systems, formal specifications need to be translated into implementation. Manually converting formal models into code poses challenges such as increased costs, limitations in specification reuse, and the potential for introducing errors. To overcome these limitations, Model-Driven Engineering (MDE) approaches enable developers to generate software code automatically. This paper proposes the Asmeta2Java tool for the automatic translation of formal Asmeta specifications into executable Java code. The designers start at an abstract level and perform refinement steps and verification activities. At the end, they automatically generates the code by applying the model-to-code transformation. Moreover, a process to validate and evaluate the transformation is presented.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_10.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_10.pdf" >}}

## Reference

```
% BibTex
@inproceedings{BombardaBG24,
  author       = {Andrea Bombarda and
                  Silvia Bonfanti and
                  Angelo Gargantini},
  editor       = {Silvia Bonfanti and
                  Angelo Gargantini and
                  Michael Leuschel and
                  Elvinia Riccobene and
                  Patrizia Scandurra},
  title        = {From Concept to Code: Unveiling a Tool for Translating Abstract State
                  Machines into Java Code},
  booktitle    = {Rigorous State-Based Methods - 10th International Conference, {ABZ}
                  2024, Bergamo, Italy, June 25-28, 2024, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {14759},
  pages        = {160--178},
  publisher    = {Springer},
  year         = {2024},
  url          = {https://doi.org/10.1007/978-3-031-63790-2\_10},
  doi          = {10.1007/978-3-031-63790-2\_10},
  timestamp    = {Thu, 04 Jul 2024 22:05:23 +0200},
  biburl       = {https://dblp.org/rec/conf/zum/BombardaBG24.bib},
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

