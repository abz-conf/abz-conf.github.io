---
title: "Using a Formal B Model at Runtime in a Demonstration of the ETCS Hybrid Level 3 Concept with Real Trains"

authors:
  - Dominik Hansen
  - Michael Leuschel
  - David Schneider
  - Sebastian Krings
  - Philipp Körner
  - Thomas Naulin
  - Nader Nayeri
  - Frank Skowron

date: 2018-05-01

# Schedule page publish date (NOT publication's date).
# publishDate: 2020-06-19T16:42:07+02:00

publication_types:
  - 1 # conference paper

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
    url: https://www3.hhu.de/stups/downloads/pdf/etcsHL3.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-319-91271-4_20
    icon_pack: fas
    icon: book
  - name: Abstract
    url: "publication/hansen2018abz/#abstract"
    icon_pack: fas
    icon: file-alt
  - name: View
    url: "publication/hansen2018abz/#document"
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: "publication/hansen2018abz/#reference"
    icon_pack: fas
    icon: quote-right
  - name: Source
    url: "publication/hansen2018abz/#sources"
    icon_pack: fas
    icon: database

slides: ""
---

## Abstract

In this article, we present a concrete realisation of the ETCS Hybrid Level 3 concept, whose practical viability was evaluated in a field demonstration in 2017. Hybrid Level 3 (HL3) introduces Virtual SubSections (VSS) as sub-divisions of classical track sections with Trackside Train Detection (TTD). Our approach introduces an add-on for the Radio Block Centre (RBC) of Thales, called Virtual Block Function (VBF), which computes the occupation states of the VSSs according to the HL3 concept using the train position reports, train integrity information, and the TTD occupation states. From the perspective of the RBC, the VBF behaves as an Interlocking (IXL) that transmits all signal aspects for virtual signals introduced for each VSS to the RBC. We report on the development of the VBF, implemented as a formal B model executed at runtime using ProB and successfully used in a field demonstration to control real trains.

## Document

{{< embed-pdf url="https://www3.hhu.de/stups/downloads/pdf/etcsHL3.pdf" >}}

## Reference

```
% BibTex
@inproceedings{hansen2018using,
  title={Using a formal B model at runtime in a demonstration of the ETCS hybrid level 3 concept with real trains},
  author={Hansen, Dominik and Leuschel, Michael and Schneider, David and Krings, Sebastian and K{\"o}rner, Philipp and Naulin, Thomas and Nayeri, Nader and Skowron, Frank},
  booktitle={International Conference on Abstract State Machines, Alloy, B, TLA, VDM, and Z},
  pages={292--306},
  year={2018},
  organization={Springer}
}
```

## Sources

- **Used formal method:**
  [Classical B](/method/b)
- **Resources and tools:**
  ProB

  For more information, please contact the <a href ="mailto:hansen@cs.uni-duesseldorf.de;leuschel@cs.uni-duesseldorf.de">authors</a>
