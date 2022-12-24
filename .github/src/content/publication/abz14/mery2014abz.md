---
title: "Modeling an Aircraft Landing System in Event-B"

authors:
  - Dominique Méry
  - Neeraj Kumar Singh

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
    url: https://eb2all.loria.fr/html_files/files/landingsystem.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-319-07512-9_12
    icon_pack: fas
    icon: book
  - name: Abstract
    url: "publication/mery2014abz/#abstract"
    icon_pack: fas
    icon: file-alt
  - name: View
    url: "publication/mery2014abz/#document"
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: "publication/mery2014abz/#reference"
    icon_pack: fas
    icon: quote-right
  - name: Source
    url: "publication/mery2014abz/#sources"
    icon_pack: fas
    icon: database

slides: ""
---

## Abstract

This paper presents a stepwise formal development of the landing system of an aircraft. The formal models include the complex behaviour, temporal behaviour and sequence of operations of the landing gear system. The models are formalized in Event-B modeling language, and then the ProB model checker is used to verify the deadlock freedom and to validate the behaviour requirements by animating the formalized models. This case study is considered as a benchmark for techniques and tools dedicated to the verification of behavioural properties of the complex critical systems.

## Document

{{< embed-pdf url="https://eb2all.loria.fr/html_files/files/landingsystem.pdf" >}}

## Reference

```
% BibTex
@InProceedings{10.1007/978-3-319-07512-9_12,
author="M{\'e}ry, Dominique
and Singh, Neeraj Kumar",
editor="Boniol, Fr{\'e}d{\'e}ric
and Wiels, Virginie
and Ait Ameur, Yamine
and Schewe, Klaus-Dieter",
title="Modeling an Aircraft Landing System in Event-B",
booktitle="ABZ 2014: The Landing Gear Case Study",
year="2014",
publisher="Springer International Publishing",
address="Cham",
pages="154--159",
abstract="This paper presents a stepwise formal development of the landing system of an aircraft. The formal models include the complex behaviour, temporal behaviour and sequence of operations of the landing gear system. The models are formalized in Event-B modeling language, and then the ProB model checker is used to verify the deadlock freedom and to validate the behaviour requirements by animating the formalized models. This case study is considered as a benchmark for techniques and tools dedicated to the verification of behavioural properties of the complex critical systems.",
isbn="978-3-319-07512-9"
}
```

## Sources

- **Used formal method:**
  [Event-B](/method/event-b)
- **Resources and tools:**
  Rodin, ProB

  For more information, please contact the <a href ="mailto:dominique.mery@loria.fr;neeraj.singh@toulouse-inp.fr">authors</a>
