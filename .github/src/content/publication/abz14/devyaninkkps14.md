---
title: "Formal Verification of OS Security Model with Alloy and Event-B"

authors:
  - Petr N. Devyanin
  - Alexey V. Khoroshilov
  - Victor V. Kuliamin
  - Alexander K. Petrenko
  - Ilya V. Shchepetkov


date: 2014-01-01

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
  - 11  # default is 1 (conference), adjust as needed

publication: "4th International Conference on ASM, Alloy, B, TLA, VDM, and Z (ABZ'14)"
publication_short: "ABZ'14"

tags:
  - ABZ'14

categories: []

featured: false

# enable this for case studies
# projects:
#   - abz14

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-662-43652-3_30.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-662-43652-3_30
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/devyaninkkps14/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/devyaninkkps14/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/devyaninkkps14/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/devyaninkkps14/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

The paper presents a work-in-progress on formal verification of operating system security model, which integrates control of confidentiality and integrity levels with role-based access control. The main goal is to formalize completely the security model and to prove its consistency and conformance to basic correctness requirements concerning keeping levels of integrity and confidentiality. Additional goal is to perform data flow analysis of the model to check whether it can preserve security in the face of certain attacks. Alloy and Event-B were used for formalization and verification of the model. Alloy was applied to provide quick constraint-based checking and uncover various issues concerning inconsistency or incompleteness of the model. Event-B was applied for full-scale deductive verification. Both tools worked well on first steps of model development, while after certain complexity was reached Alloy began to demonstrate some scalability issues.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-662-43652-3_30.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-662-43652-3_30.pdf" >}}

## Reference

```
% BibTex
@inproceedings{DevyaninKKPS14,
  author       = {Petr N. Devyanin and
                  Alexey V. Khoroshilov and
                  Victor V. Kuliamin and
                  Alexander K. Petrenko and
                  Ilya V. Shchepetkov},
  editor       = {Yamine A{\"{\i}}t Ameur and
                  Klaus{-}Dieter Schewe},
  title        = {Formal Verification of {OS} Security Model with Alloy and Event-B},
  booktitle    = {Abstract State Machines, Alloy, B, TLA, VDM, and {Z} - 4th International
                  Conference, {ABZ} 2014, Toulouse, France, June 2-6, 2014. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {8477},
  pages        = {309--313},
  publisher    = {Springer},
  year         = {2014},
  url          = {https://doi.org/10.1007/978-3-662-43652-3\_30},
  doi          = {10.1007/978-3-662-43652-3\_30},
  timestamp    = {Sun, 02 Jun 2019 21:23:59 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/DevyaninKKPS14.bib},
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

