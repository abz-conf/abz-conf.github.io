---
title: "AMAN Case Study"

authors:
  - Philippe A. Palanque
  - José Creissac Campos


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
#  11 = "pub_short_paper"
#  12 = "pub_long_paper"
#  13 = "pub_invited_talk"
#  14 = "pub_phd_symposium"
publication_types:
  - 9   # default is 1 (conference), adjust as needed

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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_21.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-031-33163-3_21
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/palanquec23/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/palanquec23/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/palanquec23/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/palanquec23/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

This document presents the case study for the ABZ 2023 conference. The case study introduces a safety critical interactive system called AMAN (Arrival MANager), which is a partly-autonomous scheduler of landing sequences of aircraft in airports. This interactive systems interleaves Air Traffic Controllers activities with automation in AMAN. While some AMAN systems are currently deployed in airports, we consider here only a subset of functions which represent a challenge in modelling and verification.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_21.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_21.pdf" >}}

## Reference

```
% BibTex
@inproceedings{PalanqueC23,
  author       = {Philippe A. Palanque and
                  Jos{\'{e}} Creissac Campos},
  editor       = {Uwe Gl{\"{a}}sser and
                  Jos{\'{e}} Creissac Campos and
                  Dominique M{\'{e}}ry and
                  Philippe A. Palanque},
  title        = {{AMAN} Case Study},
  booktitle    = {Rigorous State-Based Methods - 9th International Conference, {ABZ}
                  2023, Nancy, France, May 30 - June 2, 2023, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {14010},
  pages        = {265--283},
  publisher    = {Springer},
  year         = {2023},
  url          = {https://doi.org/10.1007/978-3-031-33163-3\_21},
  doi          = {10.1007/978-3-031-33163-3\_21},
  timestamp    = {Fri, 02 Jun 2023 21:23:52 +0200},
  biburl       = {https://dblp.org/rec/conf/zum/PalanqueC23.bib},
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

