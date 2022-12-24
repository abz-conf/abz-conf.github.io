---
title: "Model-Checking Real-Time Properties of an Aircraft Landing Gear System Using Fiacre"

authors:
  - Bernard Berthomieu
  - Silvano Dal Zilio
  - Łukasz Fronc

date: 2014-05-01

# Schedule page publish date (NOT publication's date).
# publishDate: 2020-06-19T16:42:07+02:00

publication_types:
  - 1 # conference paper

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
    url: https://www.archives-ouvertes.fr/hal-00967422/document
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-319-07512-9_8
    icon_pack: fas
    icon: book
  - name: Abstract
    url: "publication/berthomieu2014abz/#abstract"
    icon_pack: fas
    icon: file-alt
  - name: View
    url: "publication/berthomieu2014abz/#document"
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: "publication/berthomieu2014abz/#reference"
    icon_pack: fas
    icon: quote-right
  - name: Source
    url: "publication/berthomieu2014abz/#sources"
    icon_pack: fas
    icon: database

slides: ""
---

## Abstract

We describe our experience with modeling the landing gear system of an aircraft using the formal specification language Fiacre. Our model takes into account the behavior and timing properties of both the physical parts and the control software of this system. We use this formal model to check safety and real-time properties on the system but also to find a safe bound on the maximal time needed for all gears to be down and locked (assuming the absence of failures). Our approach ultimately relies on the model-checking tool Tina, that provides state-space generation and model-checking algorithms for an extension of Time Petri Nets with data and priorities.

## Document

{{< embed-pdf url="https://www.archives-ouvertes.fr/hal-00967422/document" >}}

## Reference

```
% BibTex
@InProceedings{10.1007/978-3-319-07512-9_8,
author="Berthomieu, Bernard
and Dal Zilio, Silvano
and Fronc, {\L}ukasz",
editor="Boniol, Fr{\'e}d{\'e}ric
and Wiels, Virginie
and Ait Ameur, Yamine
and Schewe, Klaus-Dieter",
title="Model-Checking Real-Time Properties of an Aircraft Landing Gear System Using Fiacre",
booktitle="ABZ 2014: The Landing Gear Case Study",
year="2014",
publisher="Springer International Publishing",
address="Cham",
pages="110--125",
abstract="We describe our experience with modeling the landing gear system of an aircraft using the formal specification language Fiacre. Our model takes into account the behavior and timing properties of both the physical parts and the control software of this system. We use this formal model to check safety and real-time properties on the system but also to find a safe bound on the maximal time needed for all gears to be down and locked (assuming the absence of failures). Our approach ultimately relies on the model-checking tool Tina, that provides state-space generation and model-checking algorithms for an extension of Time Petri Nets with data and priorities.",
isbn="978-3-319-07512-9"
}
```

## Sources

- **Used formal method:**
  Time Petri Nets
- **Resources and tools:**
  Tina

  For more information, please contact the <a href ="mailto:bernard.berthomieu@lass.fr;dal.zilio@lass.fr">authors</a>
