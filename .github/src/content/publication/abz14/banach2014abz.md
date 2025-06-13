---
title: "The Landing Gear Case Study in Hybrid Event-B"

authors:
  - Richard Banach

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
    url: http://www.cs.man.ac.uk/~banach/some.pubs/CEvB.LanGear.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-319-07512-9_9
    icon_pack: fas
    icon: book
  - name: Abstract
    url: "publication/banach2014abz/#abstract"
    icon_pack: fas
    icon: file-alt
  - name: View
    url: "publication/banach2014abz/#document"
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: "publication/banach2014abz/#reference"
    icon_pack: fas
    icon: quote-right
  - name: Source
    url: "publication/banach2014abz/#sources"
    icon_pack: fas
    icon: database

slides: ""
---

## Abstract

A case study problem based on a set of aircraft landing gear is examined in Hybrid Event-B (an extension of Event-B that includes provision for continuously varying behaviour as well as the usual discrete changes of state). Although tool support for Hybrid Event-B is currently lacking, the complexity of the case study provides a valuable challenge for the expressivity and modelling capabilities of the formalism. The size of the case study, and in particular, the number of overtly independent subcomponents that the problem domain contains, both significantly exercise the multi-machine and coordination capabilities of Hybrid Event-B, requiring the use of novel coordination mechanisms.

## Document

{{< embed-pdf url="http://www.cs.man.ac.uk/~banach/some.pubs/CEvB.LanGear.pdf" >}}

## Reference

```
% BibTex
@InProceedings{10.1007/978-3-319-07512-9_9,
author="Banach, Richard",
editor="Boniol, Fr{\'e}d{\'e}ric
and Wiels, Virginie
and Ait Ameur, Yamine
and Schewe, Klaus-Dieter",
title="The Landing Gear Case Study in Hybrid Event-B",
booktitle="ABZ 2014: The Landing Gear Case Study",
year="2014",
publisher="Springer International Publishing",
address="Cham",
pages="126--141",
abstract="A case study problem based on a set of aircraft landing gear is examined in Hybrid Event-B (an extension of Event-B that includes provision for continuously varying behaviour as well as the usual discrete changes of state). Although tool support for Hybrid Event-B is currently lacking, the complexity of the case study provides a valuable challenge for the expressivity and modelling capabilities of the formalism. The size of the case study, and in particular, the number of overtly independent subcomponents that the problem domain contains, both significantly exercise the multi-machine and coordination capabilities of Hybrid Event-B, requiring the use of novel coordination mechanisms.",
isbn="978-3-319-07512-9"
}
```

## Sources

- **Used formal method:**
  Hybrid [Event-B](/method/event-b)

  For more information, please contact the <a href ="mailto:banach@cs.man.ac.uk">authors</a>
