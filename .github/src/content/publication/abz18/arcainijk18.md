---
title: "Modelling the Hybrid ERTMS/ETCS Level 3 Case Study in Spin"

authors:
  - Paolo Arcaini
  - Pavel Jezek
  - Jan Kofron

date: 2018-05-01

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

publication: "6th International Conference on ASM, Alloy, B, TLA, VDM, and Z (ABZ'18)"
publication_short: "ABZ'18"

tags:
  - ABZ'18

categories: []

featured: false

projects:
  - abz18

links:
  - name: Digital
    url: https://www.irit.fr/ABZ-CS/html_files/files/2018/PDF/AJK_ABZ2018.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-319-91271-4_19
    icon_pack: fas
    icon: book
  - name: Abstract
    url: "publication/arcaini2018abz/#abstract"
    icon_pack: fas
    icon: file-alt
  - name: View
    url: "publication/arcaini2018abz/#document"
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: "publication/arcaini2018abz/#reference"
    icon_pack: fas
    icon: quote-right
  - name: Source
    url: "publication/arcaini2018abz/#sources"
    icon_pack: fas
    icon: database

slides: ""
---

## Abstract

The Spin model checker has been successfully applied to the modelling, validation, and verification of different safety-critical systems. In this paper, we model and validate the Hybrid ERTMS/ETCS Level 3 Case Study using Spin; in particular, we show the assumptions we made to keep the state space limited, and present the problems and ambiguities that arose during the modelling. Although Spin offers several advantages in terms of validation and verification facilities, its modelling language Promela is limited if compared to higher level notations of other formal methods. Therefore, we discuss the advantages and disadvantages of using the tool, and how it could be improved in terms of modelling facilities.

## Document

{{< embed-pdf url="https://www.irit.fr/ABZ-CS/html_files/files/2018/PDF/AJK_ABZ2018.pdf" >}}

## Reference

```
% BibTex
@InProceedings{caseStudyABZ2018,
author={Arcaini, Paolo and Je{\v{z}}ek, Pavel and Kofro{\v{n}}, Jan},
editor={Butler, Michael and Raschke, Alexander and Hoang, Thai Son and Reichl, Klaus},
title={Modelling the {Hybrid ERTMS/ETCS Level 3 Case Study in Spin}},
booktitle={Abstract State Machines, Alloy, B, TLA, VDM, and Z},
year={2018},
publisher={Springer International Publishing},
address={Cham},
pages={277--291},
isbn={978-3-319-91271-4},
doi={https://doi.org/10.1007/978-3-319-91271-4_19}
}
```

## Sources

- **Used formal method:**
  Spin
- **Resources and tools:**
  Spin
- **Website:**
  http://d3s.mff.cuni.cz/~kofron/abz18casestudy.html
- **Model Archive:**
  [ZIP](/data/abz18/arcaini2018abz.zip)

For more information, please contact the <a href ="mailto:arcaini@d3s.mff.cuni.cz">authors</a>
