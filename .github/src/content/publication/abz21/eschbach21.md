---
title: "Formalizing and Analyzing System Requirements of Automatic Train Operation over ETCS Using Event-B"

authors:
  - Robert Eschbach


date: 2021-01-01

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
  - 11   # default is 1 (conference), adjust as needed

publication: "8th International Conference on Rigorous State Based Methods (ABZ'21)"
publication_short: "ABZ'21"

tags:
  - ABZ'21

categories: []

featured: false

# enable this for case studies
# projects:
#   - abz21

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-030-77543-8_13.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-030-77543-8_13
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/eschbach21/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/eschbach21/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/eschbach21/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/eschbach21/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

The European Railway Traffic Management System (ERTMS) aims at the replacement of incompatible national railway traffic management systems in Europe. A part of ERTMS is the European Train Control System (ETCS). ETCS is an automatic train protection system and can collaborate with an automatic train operation system (ATO). ATO can control and monitor the braking, traction and door system of a train. This collaboration is called ATO over ETCS. In this paper we describe the experiences gained in the formalization and the formal analysis of system requirements related to the modes of the ATO onboard unit and its interfaces to train, ATO trackside unit, and ETCS onboard unit. A primary goal to achieve was the stepwise and systematic construction of an Event-B specification tightly coupled with the requirements based on a bidirectional traceability concept. Another goal was the formal verification of important safety properties related to the mode transitions and transition conditions of the ATO onboard unit.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-030-77543-8_13.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-030-77543-8_13.pdf" >}}

## Reference

```
% BibTex
@inproceedings{Eschbach21,
  author       = {Robert Eschbach},
  editor       = {Alexander Raschke and
                  Dominique M{\'{e}}ry},
  title        = {Formalizing and Analyzing System Requirements of Automatic Train Operation
                  over {ETCS} Using Event-B},
  booktitle    = {Rigorous State-Based Methods - 8th International Conference, {ABZ}
                  2021, Ulm, Germany, June 9-11, 2021, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {12709},
  pages        = {137--142},
  publisher    = {Springer},
  year         = {2021},
  url          = {https://doi.org/10.1007/978-3-030-77543-8\_13},
  doi          = {10.1007/978-3-030-77543-8\_13},
  timestamp    = {Tue, 15 Jun 2021 17:24:03 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/Eschbach21.bib},
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

