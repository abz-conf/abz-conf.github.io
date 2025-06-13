---
title: "Development of a Verified Flash File System"

authors:
  - Gerhard Schellhorn
  - Gidon Ernst
  - Jörg Pfähler
  - Dominik Haneberg
  - Wolfgang Reif


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
  - 13   # default is 1 (conference), adjust as needed

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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-662-43652-3_2.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-662-43652-3_2
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/schellhornephr14/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/schellhornephr14/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/schellhornephr14/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/schellhornephr14/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

This paper gives an overview over the development of a formally verified file system for flash memory. We describe our approach that is based on Abstract State Machines and incremental modular refinement. Some of the important intermediate levels and the features they introduce are given. We report on the verification challenges addressed so far, and point to open problems and future work. We furthermore draw preliminary conclusions on the methodology and the required tool support.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-662-43652-3_2.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-662-43652-3_2.pdf" >}}

## Reference

```
% BibTex
@inproceedings{SchellhornEPHR14,
  author       = {Gerhard Schellhorn and
                  Gidon Ernst and
                  J{\"{o}}rg Pf{\"{a}}hler and
                  Dominik Haneberg and
                  Wolfgang Reif},
  editor       = {Yamine A{\"{\i}}t Ameur and
                  Klaus{-}Dieter Schewe},
  title        = {Development of a Verified Flash File System},
  booktitle    = {Abstract State Machines, Alloy, B, TLA, VDM, and {Z} - 4th International
                  Conference, {ABZ} 2014, Toulouse, France, June 2-6, 2014. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {8477},
  pages        = {9--24},
  publisher    = {Springer},
  year         = {2014},
  url          = {https://doi.org/10.1007/978-3-662-43652-3\_2},
  doi          = {10.1007/978-3-662-43652-3\_2},
  timestamp    = {Tue, 07 May 2024 20:13:31 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/SchellhornEPHR14.bib},
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

