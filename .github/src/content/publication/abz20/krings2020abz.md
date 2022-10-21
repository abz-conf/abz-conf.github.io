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

publication_types:
  - 1 # conference paper

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

- **Model Archive:**
  Please contact <a href ="mailto:sebastian@krin.gs;p.koerner@hhu.de;jannik.dunkelau@hhu.de;chris.rutenkolk@hhu.de">authors</a>
- **Presentation:**
  Not available
- **Used formal method:**
  MISRA C
- **Resources and tools:**
  Not available
- **Required OS:**
  Not available
- **Website:**
  Not available
- **Remarks and recommendation:**
  Not available
