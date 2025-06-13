---
title: "How to Assure Correctness and Safety of Medical Software: The Hemodialysis Machine Case Study"

authors:
  - Paolo Arcaini
  - Silvia Bonfanti
  - Angelo Gargantini
  - Elvinia Riccobene

date: 2016-05-01

# Schedule page publish date (NOT publication's date).
# publishDate: 2020-06-19T16:42:07+02:00

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
  - 10  # default is 1 (conference), adjust as needed

publication: "5th International Conference on ASM, Alloy, B, TLA, VDM, and Z (ABZ'16)"
publication_short: "ABZ'16"

tags:
  - ABZ'16

categories: []

featured: false

projects:
  - abz16

links:
  - name: Digital
    url: https://cs.unibg.it/gargantini/research/papers/abz2016_hemodialysisCaseStudy.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-319-33600-8_30
    icon_pack: fas
    icon: book
  - name: Abstract
    url: "publication/arcaini2016abz/#abstract"
    icon_pack: fas
    icon: file-alt
  - name: View
    url: "publication/arcaini2016abz/#document"
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: "publication/arcaini2016abz/#reference"
    icon_pack: fas
    icon: quote-right
  - name: Source
    url: "publication/arcaini2016abz/#sources"
    icon_pack: fas
    icon: database

slides: ""
---

## Abstract

Medical devices are nowadays more and more software dependent, and software malfunctioning can lead to injuries or death for patients. Several standards have been proposed for the development and the validation of medical devices, but they establish general guidelines on the use of common software engineering activities without any indication regarding methods and techniques to assure safety and reliability. This paper takes advantage of the Hemodialysis machine case study to present a formal development process supporting most of the engineering activities required by the standards, and provides rigorous approaches for system validation and verification. The process is based on the Abstract State Machine formal method and its model refinement principle.

## Document

{{< embed-pdf url="https://cs.unibg.it/gargantini/research/papers/abz2016_hemodialysisCaseStudy.pdf" >}}

## Reference

```
% BibTex
@InProceedings{10.1007/978-3-319-33600-8_30,
author="Arcaini, Paolo
and Bonfanti, Silvia
and Gargantini, Angelo
and Riccobene, Elvinia",
editor="Butler, Michael
and Schewe, Klaus-Dieter
and Mashkoor, Atif
and Biro, Miklos",
title="How to Assure Correctness and Safety of Medical Software: The Hemodialysis Machine Case Study ",
booktitle="Abstract State Machines, Alloy, B, TLA, VDM, and Z",
year="2016",
publisher="Springer International Publishing",
address="Cham",
pages="344--359",
abstract="Medical devices are nowadays more and more software dependent, and software malfunctioning can lead to injuries or death for patients. Several standards have been proposed for the development and the validation of medical devices, but they establish general guidelines on the use of common software engineering activities without any indication regarding methods and techniques to assure safety and reliability.",
isbn="978-3-319-33600-8"
}
```

## Sources

- **Used formal method:**
  [ASM](/method/asm)

  For more information, please contact the <a href ="mailto:arcaini@d3s.mff.cuni.cz;silvia.bonfanti@unibg.it;angelo.gargantini@unibg.it;elvinia.riccobene@unimi.it">authors</a>
