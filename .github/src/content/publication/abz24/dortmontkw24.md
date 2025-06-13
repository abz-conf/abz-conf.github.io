---
title: "Modelling and Analysing a Mechanical Lung Ventilator in mCRL2"

authors:
  - Danny van Dortmont
  - Tim Willemse
  - Jeroen Keiren

date: 2024-07-03

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
#  14 = "pub_phd_symposium"
publication_types:
  - 10  # default is 1 (conference), adjust as needed

publication: "10th International Conference on Rigorous State Based Methods (ABZ'24)"
publication_short: "ABZ'24"

tags:
  - ABZ'24

categories: []

featured: false

projects:
  - abz24

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_27.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-031-63790-2_27
    icon_pack: fas
    icon: book
  - name: Abstract
    url: "publication/keiren2024abz/#abstract"
    icon_pack: fas
    icon: file-alt
  - name: View
    url: "publication/keiren2024abz/#document"
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: "publication/keiren2024abz/#reference"
    icon_pack: fas
    icon: quote-right
  - name: Source
    url: "publication/keiren2024abz/#sources"
    icon_pack: fas
    icon: database

slides: ""
---

## Abstract

We model the Mechanical Lung Ventilator (MLV) in the process algebra mCRL2. The functional requirements of the MLV are formalised in the modal mu-calculus, and we use model checking to analyse whether these requirements hold true of our model. Our formalisation of the MLV and its requirements reveal a few subtle imprecisions and unclarities in the informal document and we analyse their impact.

## Document

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_27.pdf" >}}

## Reference

```
% BibTex
@InProceedings{10.1007/978-3-031-63790-2_27,
author="van Dortmont, Danny
and Keiren, Jeroen J. A.
and Willemse, Tim A. C.",
editor="Bonfanti, Silvia
and Gargantini, Angelo
and Leuschel, Michael
and Riccobene, Elvinia
and Scandurra, Patrizia",
title="Modelling and Analysing a Mechanical Lung Ventilator in mCRL2",
booktitle="Rigorous State-Based Methods",
year="2024",
publisher="Springer Nature Switzerland",
address="Cham",
pages="341--359",
abstract="We model the Mechanical Lung Ventilator (MLV) in the process algebra mCRL2. The functional requirements of the MLV are formalised in the modal {\$}{\$}{\backslash}mu {\$}{\$}$\mu$-calculus, and we use model checking to analyse whether these requirements hold true of our model. Our formalisation of the MLV and its requirements reveal a few subtle imprecisions and unclarities in the informal document and we analyse their impact.",
isbn="978-3-031-63790-2"
}
```

## Sources

- **Model Archive:**
  [GitHub](https://doi.org/10.5281/zenodo.10978852)
- **Presentation:**
  [PDF](/data/abz24/keiren2024abz.pdf)
- **Used formal method:**
  [mCRL2](/method/mCRL2)

  For more information, please contact the <a href ="mailto:d.f.m.v.dortmont@student.tue.nl;j.j.a.keiren@tue.nl;t.a.c.willemse@tue.nl">authors</a>
