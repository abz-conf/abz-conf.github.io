---
title: "Formal System Modelling Using Abstract Data Types in Event-B"

authors:
  - Andreas Fürst
  - Thai Son Hoang
  - David A. Basin
  - Naoto Sato
  - Kunihiko Miyazaki


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
#  10 = "pub_short_paper"
#  11 = "pub_long_paper"
publication_types:
  - 1   # default is 1 (conference), adjust as needed

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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-662-43652-3_20.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-662-43652-3_20
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/fursthbsm14/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/fursthbsm14/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/fursthbsm14/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/fursthbsm14/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

We present a formal modelling approach using Abstract Data Types (ADTs) for developing large-scale systems in Event-B. The novelty of our approach is the combination of refinement and instantiation techniques to manage the complexity of systems under development. With ADTs, we model system components on an abstract level, specifying only the necessary properties of the components. At the same time, we postpone the introduction of their concrete definitions to later development steps. We evaluate our approach using a largescale case study in train control systems. The results show that our approach helps reduce system details during early development stages and leads to simpler and more automated proofs.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-662-43652-3_20.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-662-43652-3_20.pdf" >}}

## Reference

```
% BibTex
@inproceedings{FurstHBSM14,
  author       = {Andreas F{\"{u}}rst and
                  Thai Son Hoang and
                  David A. Basin and
                  Naoto Sato and
                  Kunihiko Miyazaki},
  editor       = {Yamine A{\"{\i}}t Ameur and
                  Klaus{-}Dieter Schewe},
  title        = {Formal System Modelling Using Abstract Data Types in Event-B},
  booktitle    = {Abstract State Machines, Alloy, B, TLA, VDM, and {Z} - 4th International
                  Conference, {ABZ} 2014, Toulouse, France, June 2-6, 2014. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {8477},
  pages        = {222--237},
  publisher    = {Springer},
  year         = {2014},
  url          = {https://doi.org/10.1007/978-3-662-43652-3\_20},
  doi          = {10.1007/978-3-662-43652-3\_20},
  timestamp    = {Tue, 14 May 2019 10:00:50 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/FurstHBSM14.bib},
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

