---
title: "Modelling Hybrid Programs with Event-B"

authors:
  - Meryem Afendi
  - Régine Laleau
  - Amel Mammar


date: 2020-01-01

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
#  10 = "pub_short_paper"
#  11 = "pub_long_paper"
publication_types:
  - 1   # default is 1 (conference), adjust as needed

publication: "7th International Conference on Rigorous State Based Methods (ABZ'20)"
publication_short: "ABZ'20"

tags:
  - ABZ'20

categories: []

featured: false

# enable this for case studies
# projects:
#   - abz20

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-030-48077-6_10.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-030-48077-6_10
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/afendilm20/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/afendilm20/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/afendilm20/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/afendilm20/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Hybrid systems are one of the most common mathematical models for Cyber-Physical Systems (CPSs). They combine discrete dynamics represented by state machines or finite automata with continuous behaviors represented by differential equations. The measurement of continuous behaviors is performed by sensors. When these sensors have a continuous access to these measurements, we call such model an Event-Triggered model. The properties of this model are easier to prove, while its implementation is difficult in practice. Therefore, it is preferable to introduce a more realistic model, called Time-Triggered model, where the sensors take periodic measurements. Contrary to Event-Triggered models, Time-Triggered models are much easier to implement, but much more difficult to verify. Based on the differential refinement logic (dR\(\mathcal {L}\)), a dynamic logic for refinement relations on hybrid systems, it is possible to prove that a Time-Triggered model refines an Event-Triggered model. The major limitation of such logic is that it is not supported by any prover. In this paper, we propose a correct-by-construction approach that implements the reasoning on hybrid programs particularly the reasoning of dR\(\mathcal {L}\) in Event-B to take advantage of its associated tools.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-030-48077-6_10.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-030-48077-6_10.pdf" >}}

## Reference

```
% BibTex
@inproceedings{AfendiLM20,
  author       = {Meryem Afendi and
                  R{\'{e}}gine Laleau and
                  Amel Mammar},
  editor       = {Alexander Raschke and
                  Dominique M{\'{e}}ry and
                  Frank Houdek},
  title        = {Modelling Hybrid Programs with Event-B},
  booktitle    = {Rigorous State-Based Methods - 7th International Conference, {ABZ}
                  2020, Ulm, Germany, May 27-29, 2020, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {12071},
  pages        = {139--154},
  publisher    = {Springer},
  year         = {2020},
  url          = {https://doi.org/10.1007/978-3-030-48077-6\_10},
  doi          = {10.1007/978-3-030-48077-6\_10},
  timestamp    = {Tue, 16 Jun 2020 17:18:07 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/AfendiLM20.bib},
  bibsource    = {dblp computer science bibliography, https://dblp.org}
}


```

<!-- # add information for case study papers (if available)
## Sources

- **Used formal method:**
  [ASM](/method/asm)
- **Resources and tools:**
  Asmeta

For more information, please contact the <a href ="mailto:silvia.bonfanti@unibg.it;arcaini@nii.ac.jp;angelo.gargantini@unibg.it;scandurra@unibg.it;elvinia.riccobene@unimi.it">authors</a>-->

