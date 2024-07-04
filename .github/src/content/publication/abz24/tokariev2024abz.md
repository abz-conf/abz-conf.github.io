---
title: "Real-Time CCSL: Application to the Mechanical Lung Ventilator"

authors:
  - Pavlo Tokariev
  - Fredric Mallet

date: 2024-07-03

# Schedule page publish date (NOT publication's date).
# publishDate: 2020-06-19T16:42:07+02:00

publication_types:
  - 1 # conference paper

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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_24.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-031-63790-2_24
    icon_pack: fas
    icon: book
  - name: Abstract
    url: "publication/tokariev2024abz/#abstract"
    icon_pack: fas
    icon: file-alt
  - name: View
    url: "publication/tokariev2024abz/#document"
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: "publication/tokariev2024abz/#reference"
    icon_pack: fas
    icon: quote-right
  - name: Source
    url: "publication/tokariev2024abz/#sources"
    icon_pack: fas
    icon: database

slides: ""
---

## Abstract

This case-study paper reports on our experience in modelling the mechanical lung ventilator using the Clock Constraint Specification Language (CCSL). CCSL captures the causal and temporal behaviour of a system by specifying constraints on logical clocks. Logical clocks are integer counters where the occurrence of an event, a tick, advances the counter and marks the advance in time. In this framework, chronometric clocks become logical clocks just with a special external meaning. Encoding chronometric clocks as counters may result in verification inefficiency and hard-to-read specifications. The paper introduces in the language some real-time constructs to directly encode phenomena like clock drift, skew and jitter. This makes patterns explicit in turn enabling optimizations. To realize these optimizations, we alter the internal symbolic representation of clock constraints. We also introduce an explicit notion of parameters and intervals. While for some constraints it mainly consists of adding syntactic sugar and pre-processing facilities, we believe it improves the readability. We illustrate the new constructs on the mechanical lung ventilator system. We start with a purely logical specification, we point at the sources of inefficiencies and then we discuss the benefits of the extensions on specific parts.

## Document

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_24.pdf" >}}

## Reference

```
% BibTex
@InProceedings{10.1007/978-3-031-63790-2_24,
author="Tokariev, Pavlo
and Mallet, Fr{\'e}d{\'e}ric",
editor="Bonfanti, Silvia
and Gargantini, Angelo
and Leuschel, Michael
and Riccobene, Elvinia
and Scandurra, Patrizia",
title="Real-Time CCSL: Application to the Mechanical Lung Ventilator",
booktitle="Rigorous State-Based Methods",
year="2024",
publisher="Springer Nature Switzerland",
address="Cham",
pages="289--306",
abstract="This case-study paper reports on our experience in modelling the mechanical lung ventilator using the Clock Constraint Specification Language (CCSL). CCSL captures the causal and temporal behaviour of a system by specifying constraints on logical clocks. Logical clocks are integer counters where the occurrence of an event, a tick, advances the counter and marks the advance in time. In this framework, chronometric clocks become logical clocks just with a special external meaning. Encoding chronometric clocks as counters may result in verification inefficiency and hard-to-read specifications.",
isbn="978-3-031-63790-2"
}
```

## Sources

- **Model Archive:**
  [GitHub](https://github.com/PaulRaUnite/mlv_spec/releases/tag/v0.1)
- **Presentation:**
  [PDF](/data/abz24/tokariev2024abz.pdf)
- **Used formal method:**
  [CCSL](/method/CCSL)

  For more information, please contact the <a href ="mailto:Pavlo.Tokariev@inria.fr;Frederic.Mallet@univ-cotedazur.fr">authors</a>
