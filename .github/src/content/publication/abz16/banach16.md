---
title: "Hemodialysis Machine in Hybrid Event-B"

authors:
  - Richard Banach

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
    url: https://www.research.manchester.ac.uk/portal/files/31402126/FULL_TEXT.PDF
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-319-33600-8_32
    icon_pack: fas
    icon: book
  - name: Abstract
    url: "publication/banach2016abz/#abstract"
    icon_pack: fas
    icon: file-alt
  - name: View
    url: "publication/banach2016abz/#document"
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: "publication/banach2016abz/#reference"
    icon_pack: fas
    icon: quote-right
  - name: Source
    url: "publication/banach2016abz/#sources"
    icon_pack: fas
    icon: database

slides: ""
---

## Abstract

The hemodialysis machine case study is examined in Hybrid Event-B (an extension of Event-B that includes provision for continuously varying behaviour as well as the usual discrete changes of state). A broadly component based strategy is adopted, using the multi-machine and coordination facilities of Hybrid Event-B. Since, like most medical procedures, hemodialysis is under overall human control, it is largely a sequential process, with some branching to deal with exceptional circumstances. This makes for a relatively uncomplicated modelling framework, provided a model of the operator is included in order to capture the handling of exceptions.

## Document

{{< embed-pdf url="https://www.research.manchester.ac.uk/portal/files/31402126/FULL_TEXT.PDF" >}}

## Reference

```
% BibTex
@InProceedings{10.1007/978-3-319-33600-8_32,
author="Banach, Richard",
editor="Butler, Michael
and Schewe, Klaus-Dieter
and Mashkoor, Atif
and Biro, Miklos",
title="Hemodialysis Machine in Hybrid Event-B",
booktitle="Abstract State Machines, Alloy, B, TLA, VDM, and Z",
year="2016",
publisher="Springer International Publishing",
address="Cham",
pages="376--393",
isbn="978-3-319-33600-8"
}
```

## Sources

- **Used formal method:**
  Hybrid [Event-B](/method/event-b)

  For more information, please contact the <a href ="mailto:banach@cs.man.ac.uk">authors</a>
