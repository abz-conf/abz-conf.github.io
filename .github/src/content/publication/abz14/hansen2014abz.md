---
title: "Validation of the ABZ Landing Gear System Using ProB"

authors:
  - Dominik Hansen
  - Lukas Ladenberger
  - Harald Wiegard
  - Jens Bendisposto
  - Michael Leuschel

date: 2014-05-01

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

publication: "4th International Conference on ASM, Alloy, B, TLA, VDM, and Z (ABZ'14)"
publication_short: "ABZ'14"

tags:
  - ABZ'14

categories: []

featured: false

projects:
  - abz14

links:
  - name: Digital
    url: https://www3.hhu.de/stups/downloads/pdf/abz14casestudy.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-319-07512-9_5
    icon_pack: fas
    icon: book
  - name: Abstract
    url: "publication/hansen2014abz/#abstract"
    icon_pack: fas
    icon: file-alt
  - name: View
    url: "publication/hansen2014abz/#document"
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: "publication/hansen2014abz/#reference"
    icon_pack: fas
    icon: quote-right
  - name: Source
    url: "publication/hansen2014abz/#sources"
    icon_pack: fas
    icon: database

slides: ""
---

## Abstract

In this paper we present our formalisation of the ABZ landing gear case study in Event-B. The development was carried out using the Rodin platform and mainly used superposition refinement to structure the specification. To validate the model we complemented proof with animation and model checking. For the latter, we used the ProB animator and model checker. Graphical representation of the model turned out to be crucial in the development and validation of the model; this was achieved using a new version of BMotion Studio integrated into ProB 2.0.

## Document

{{< embed-pdf url="https://www3.hhu.de/stups/downloads/pdf/abz14casestudy.pdf" >}}

## Reference

```
% BibTex
@InProceedings{10.1007/978-3-319-07512-9_5,
author="Hansen, Dominik
and Ladenberger, Lukas
and Wiegard, Harald
and Bendisposto, Jens
and Leuschel, Michael",
editor="Boniol, Fr{\'e}d{\'e}ric
and Wiels, Virginie
and Ait Ameur, Yamine
and Schewe, Klaus-Dieter",
title="Validation of the ABZ Landing Gear System Using ProB",
booktitle="ABZ 2014: The Landing Gear Case Study",
year="2014",
publisher="Springer International Publishing",
address="Cham",
pages="66--79",
abstract="In this paper we present our formalisation of the ABZ landing gear case study in Event-B. The development was carried out using the Rodin platform and mainly used superposition refinement to structure the specification. To validate the model we complemented proof with animation and model checking. For the latter, we used the ProB animator and model checker. Graphical representation of the model turned out to be crucial in the development and validation of the model; this was achieved using a new version of BMotion Studio integrated into ProB 2.0.",
isbn="978-3-319-07512-9"
}
```

## Sources

- **Used formal method:**
  [Event-B](/method/event-b)
- **Resources and tools:**
  ProB

  For more information, please contact the <a href ="mailto:leuschel@cs.uni-duesseldorf.de">authors</a>
