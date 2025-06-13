---
title: "Validating the Hybrid ERTMS/ETCS Level 3 Concept with Electrum"

authors:
  - Alcino Cunha
  - Nuno Macedo

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
    url: https://repositorium.sdum.uminho.pt/bitstream/1822/68520/1/abz18.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-319-91271-4_21
    icon_pack: fas
    icon: book
  - name: Abstract
    url: "publication/cunha2018abz/#abstract"
    icon_pack: fas
    icon: file-alt
  - name: View
    url: "publication/cunha2018abz/#document"
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: "publication/cunha2018abz/#reference"
    icon_pack: fas
    icon: quote-right
  - name: Source
    url: "publication/cunha2018abz/#sources"
    icon_pack: fas
    icon: database

slides: ""
---

## Abstract

This paper reports on the development of a formal model for the Hybrid ERTMS/ETCS Level 3 concept in Electrum, a lightweight formal specification language that extends Alloy with mutable relations and temporal logic operators. We show how Electrum and its Analyzer can be used to perform scenario exploration to validate this model, namely to check that all the example operational scenarios described in the reference document are admissible, and to reason about expected safety properties, which can be easily specified and model checked for arbitrary track configurations. The Analyzer depicts scenarios (and counter-examples) in a graphical notation that is logic-agnostic, making them understandable for stakeholders without expertise in formal specification.

## Document

{{< embed-pdf url="https://repositorium.sdum.uminho.pt/bitstream/1822/68520/1/abz18.pdf" >}}

## Reference

```
% BibTex
@inproceedings{cunha2018validating,
  title={Validating the hybrid ERTMS/ETCS level 3 concept with electrum},
  author={Cunha, Alcino and Macedo, Nuno},
  booktitle={International Conference on Abstract State Machines, Alloy, B, TLA, VDM, and Z},
  pages={307--321},
  year={2018},
  organization={Springer}
}
```

## Sources

- **Used formal method:**
  Electrum
- **Resources and tools:**
  Electrum

  For more information, please contact the <a href ="mailto:nfmmacedo@di.uminho.pt">authors</a>
