---
title: "Context-Aware Verification of a Landing Gear System"

authors:
  - Philippe Dhaussy
  - Ciprian Teodorov

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
    url: https://www.ensta-bretagne.fr/dhaussy/Philippe_Dhaussy_fichiers/Dhaussy_Papers/abz_3avril14.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-319-07512-9_4
    icon_pack: fas
    icon: book
  - name: Abstract
    url: "publication/dhaussy2014abz/#abstract"
    icon_pack: fas
    icon: file-alt
  - name: View
    url: "publication/dhaussy2014abz/#document"
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: "publication/dhaussy2014abz/#reference"
    icon_pack: fas
    icon: quote-right
  - name: Source
    url: "publication/dhaussy2014abz/#sources"
    icon_pack: fas
    icon: database

slides: ""
---

## Abstract

Despite the high level of automation, the practicability of formal verification through model-checking of large models is hindered by the combinatorial explosion problem. In this paper we apply a novel context-aware verification technique to the Landing Gear System Case Study (LGS). The idea is to express and verify requirements relative to certain environmental situations. The system environment is decomposed into several independent scenarios (contexts), which are successively composed with the system during reachability analysis. These contexts are specified using a language called CDL (Context Description Language), based on activity and message sequence diagrams. The properties to be verified are specified with observer automata and attached to specific regions in the context. This approach enables an automated context-guided decomposition of the verification into smaller problems, hence effectively reducing the state-space explosion problem. In the case of the LGS this technique enabled the fully-automated decomposition of the verification into 885 smaller model-checking problems.

## Document

{{< embed-pdf url="https://www.ensta-bretagne.fr/dhaussy/Philippe_Dhaussy_fichiers/Dhaussy_Papers/abz_3avril14.pdf" >}}

## Reference

```
% BibTex
@InProceedings{10.1007/978-3-319-07512-9_4,
author="Dhaussy, Philippe
and Teodorov, Ciprian",
editor="Boniol, Fr{\'e}d{\'e}ric
and Wiels, Virginie
and Ait Ameur, Yamine
and Schewe, Klaus-Dieter",
title="Context-Aware Verification of a Landing Gear System",
booktitle="ABZ 2014: The Landing Gear Case Study",
year="2014",
publisher="Springer International Publishing",
address="Cham",
pages="52--65",
abstract="Despite the high level of automation, the practicability of formal verification through model-checking of large models is hindered by the combinatorial explosion problem. In this paper we apply a novel context-aware verification technique to the Landing Gear System Case Study (LGS) [2]. The idea is to express and verify requirements relative to certain environmental situations. The system environment is decomposed into several independent scenarios (contexts), which are successively composed with the system during reachability analysis. These contexts are specified using a language called CDL (Context Description Language), based on activity and message sequence diagrams. The properties to be verified are specified with observer automata and attached to specific regions in the context. This approach enables an automated context-guided decomposition of the verification into smaller problems, hence effectively reducing the state-space explosion problem. In the case of the LGS this technique enabled the fully-automated decomposition of the verification into 885 smaller model-checking problems.",
isbn="978-3-319-07512-9"
}
```

## Sources

- **Used formal method:**
  Context Description Language (CDL)

  For more information, please contact the <a href ="mailto:philippe.dhaussy@ensta-bretagne.fr;ciprian.teodorov@ensta-bretagne.fr">authors</a>
