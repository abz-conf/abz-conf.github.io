---
title: "Extensible Record Structures in Event-B"

authors:
  - Asieh Salehi Fathabadi
  - Colin F. Snook
  - Thai Son Hoang
  - Dana Dghaym
  - Michael J. Butler


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-030-77543-8_12.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-030-77543-8_12
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/fathabadishdb21/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/fathabadishdb21/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/fathabadishdb21/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/fathabadishdb21/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Event-B is a state-based formal method for system development. The Event-B mathematical language does not support a syntax for the direct definition of structured types such as records. This paper proposes extending the Event-B language with direct record definitions. A key feature is the ability to extend records with new fields in refinement steps. The XEvent-B tool, which supports a textual representation of Event-B models, is extended to provide support for direct record definition and automatic transformation of record structures into standard Event-B elements. We demonstrate this work by modelling of the Tokeneer case study.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-030-77543-8_12.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-030-77543-8_12.pdf" >}}

## Reference

```
% BibTex
@inproceedings{FathabadiSHDB21,
  author       = {Asieh Salehi Fathabadi and
                  Colin F. Snook and
                  Thai Son Hoang and
                  Dana Dghaym and
                  Michael J. Butler},
  editor       = {Alexander Raschke and
                  Dominique M{\'{e}}ry},
  title        = {Extensible Record Structures in Event-B},
  booktitle    = {Rigorous State-Based Methods - 8th International Conference, {ABZ}
                  2021, Ulm, Germany, June 9-11, 2021, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {12709},
  pages        = {130--136},
  publisher    = {Springer},
  year         = {2021},
  url          = {https://doi.org/10.1007/978-3-030-77543-8\_12},
  doi          = {10.1007/978-3-030-77543-8\_12},
  timestamp    = {Tue, 15 Jun 2021 17:24:03 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/FathabadiSHDB21.bib},
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

