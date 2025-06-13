---
title: "Designing Exception Handling Using Event-B"

authors:
  - Asieh Salehi Fathabadi
  - Colin F. Snook
  - Thai Son Hoang
  - Robert Thorburn
  - Michael J. Butler
  - Leonardo Aniello
  - Vladimiro Sassone


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

# enable this for case studies
# projects:
#   - abz24

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_22.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-031-63790-2_22
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/fathabadishtbas24/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/fathabadishtbas24/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/fathabadishtbas24/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/fathabadishtbas24/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

The design of exception handling is a complex task requiring insight and domain expertise to ensure that potential abnormal conditions are identified and a recovery process is designed to return the system to a safe state. Formal methods can address this complexity, by supporting the analysis of exception handling at the abstract design stages utilising mathematical modelling and proofs. Event-B is a state-based formal method for modelling and verifying the consistency of discrete systems. However it lacks explicit support for analysing the handling of exceptions. In this paper, we use UML-B state machines to support the modelling of normal behaviour assisting the identification and handling of exceptions. This is followed by verification of exception handler recovery mechanisms using the built-in model checker and provers of the Event-B tool-set.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_22.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_22.pdf" >}}

## Reference

```
% BibTex
@inproceedings{FathabadiSHTBAS24,
  author       = {Asieh Salehi Fathabadi and
                  Colin F. Snook and
                  Thai Son Hoang and
                  Robert Thorburn and
                  Michael J. Butler and
                  Leonardo Aniello and
                  Vladimiro Sassone},
  editor       = {Silvia Bonfanti and
                  Angelo Gargantini and
                  Michael Leuschel and
                  Elvinia Riccobene and
                  Patrizia Scandurra},
  title        = {Designing Exception Handling Using Event-B},
  booktitle    = {Rigorous State-Based Methods - 10th International Conference, {ABZ}
                  2024, Bergamo, Italy, June 25-28, 2024, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {14759},
  pages        = {270--277},
  publisher    = {Springer},
  year         = {2024},
  url          = {https://doi.org/10.1007/978-3-031-63790-2\_22},
  doi          = {10.1007/978-3-031-63790-2\_22},
  timestamp    = {Thu, 04 Jul 2024 22:05:23 +0200},
  biburl       = {https://dblp.org/rec/conf/zum/FathabadiSHTBAS24.bib},
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

