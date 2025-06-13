---
title: "Automatic Transformation of SysML Model to Event-B Model for Railway CCS Application"

authors:
  - Shubhangi Salunkhe
  - Randolf Berglehner
  - Abdul Rasheeq


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-030-77543-8_14.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-030-77543-8_14
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/salunkhebr21/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/salunkhebr21/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/salunkhebr21/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/salunkhebr21/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Digitalisation and innovation among the railway systems entail effort-demanding challenges, especially when considering how crucial it is to verify safety requirements and proof security levels. The early Verification and Validation (V&V) of railway systems detect critical issues and avoid severe consequences due to software failure. This paper aims to distinguish the subset of SysML language, which can be verified and usable by a systems engineer. As we are interested in proving safety properties expressed using invariants on states, we consider the Event-B method for this purpose. Later the selected SysML subset is used for automatic transformation and finally performing the verification using a formal verification tool. The transformation is applied on a simple point machine case study from DB Netz AG; First, a SysML model is designed using the Windchill modeler, then automatically transformed to Event-B and finally imported into the RODIN platform for formal verification.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-030-77543-8_14.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-030-77543-8_14.pdf" >}}

## Reference

```
% BibTex
@inproceedings{SalunkheBR21,
  author       = {Shubhangi Salunkhe and
                  Randolf Berglehner and
                  Abdul Rasheeq},
  editor       = {Alexander Raschke and
                  Dominique M{\'{e}}ry},
  title        = {Automatic Transformation of SysML Model to Event-B Model for Railway
                  {CCS} Application},
  booktitle    = {Rigorous State-Based Methods - 8th International Conference, {ABZ}
                  2021, Ulm, Germany, June 9-11, 2021, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {12709},
  pages        = {143--149},
  publisher    = {Springer},
  year         = {2021},
  url          = {https://doi.org/10.1007/978-3-030-77543-8\_14},
  doi          = {10.1007/978-3-030-77543-8\_14},
  timestamp    = {Tue, 15 Jun 2021 17:24:03 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/SalunkheBR21.bib},
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

