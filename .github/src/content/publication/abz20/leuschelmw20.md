---
title: "Modelling and Validating an Automotive System in Classical B and Event-B"

authors:
  - Michael Leuschel
  - Mareike Mutz
  - Michelle Werth

date: 2020-06-03

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
  - 10   # default is 1 (conference), adjust as needed

publication: "7th International Conference on Rigorous State Based Methods (ABZ'20)"
publication_short: "ABZ'20"

tags:
  - ABZ'20

categories: []

featured: false

projects:
  - abz20

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-030-48077-6_27.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-030-48077-6_27
    icon_pack: fas
    icon: book
  - name: Abstract
    url: "publication/leuschel2020abz/#abstract"
    icon_pack: fas
    icon: file-alt
  - name: View
    url: "publication/leuschel2020abz/#document"
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: "publication/leuschel2020abz/#reference"
    icon_pack: fas
    icon: quote-right
  - name: Source
    url: "publication/leuschel2020abz/#sources"
    icon_pack: fas
    icon: database

slides: ""
---

## Abstract

We have modelled parts of the ABZ automotive case study using the B-method. For the early phases of modelling we have used the classical B for software, while for proof we have used Event-B and Rodin. It is maybe surprising that classical B's machine inclusion mechanism along with operation calls can be used for modular system modelling. Moreover, for one particular style of modelling, the result can then be translated to superposition refinement with event extension in Event-B. Before conducting the proof, we have validated our models using model checking and animation with visualizations. The graphical visualizations were constructed using a new plugin (VisB) which helped uncover errors and transforms our model into an executable, interactive reference specification which can be examined by users without formal background.

## Document

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-030-48077-6_27.pdf" >}}

## Reference

```
% BibTex
@inproceedings{leuschel2020abz,
  title={{Modelling and Validating an Automotive System in Classical B and Event-B}},
  author={Leuschel, Michael and Mutz, Mareike and Werth, Michelle},
  booktitle={7th International Conference on Rigorous State Based Methods (ABZ'20)},
  pages={335--350},
  year={2020},
  organization={Springer}
}
```

## Sources

- **Used formal method:**
  [Classical B](/method/b)
  [Event-B](/method/event-b)
- **Resources and tools:**
  VisB

  For more information, please contact the <a href ="mailto:michael.leuschel@hhu.de">authors</a>
