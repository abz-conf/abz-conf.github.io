---
title: "A Verified Low-Level Implementation of the Adaptive Exterior Light and Speed Control System"

authors:
  - Sebastian Krings
  - Philipp Koerner
  - Jannik Dunkelau
  - Chris Rutenkolk

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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-030-48077-6_30.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-030-48077-6_30
    icon_pack: fas
    icon: book
  - name: Abstract
    url: "publication/krings2020abz/#abstract"
    icon_pack: fas
    icon: file-alt
  - name: View
    url: "publication/krings2020abz/#document"
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: "publication/krings2020abz/#reference"
    icon_pack: fas
    icon: quote-right
  - name: Source
    url: "publication/krings2020abz/#sources"
    icon_pack: fas
    icon: database

slides: ""
---

## Abstract

In this article, we present an approach to the ABZ 2020 case study, that differs from the ones usually presented at ABZ: Rather than using a (correct-by-construction) approach following a formal method, we use MISRA C for a low-level implementation instead. We strictly adhere to test-driven development for validation, and only afterwards apply model checking using CBMC for verification. In consequence, our realization of the ABZ case study can serve as a baseline reference for comparison, allowing to assess the benefit provided by the various formal modeling languages, methods and tools.

## Document

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-030-48077-6_30.pdf" >}}

## Reference

```
% BibTex
@inproceedings{krings2020abz,
  title={{A Verified Low-Level Implementation of the Adaptive Exterior Light and Speed Control System}},
  author={Krings, Sebastian and Koerner, Philipp and Dunkelau, Jannik and Rutenkolk, Chris},
  booktitle={7th International Conference on Rigorous State Based Methods (ABZ'20)},
  pages={382--397},
  year={2020},
  organization={Springer}
}
```

## Sources

- **Used formal method:**
  MISRA C

  For more information, please contact the <a href ="mailto:sebastian@krin.gs;p.koerner@hhu.de;jannik.dunkelau@hhu.de;chris.rutenkolk@hhu.de">authors</a>
