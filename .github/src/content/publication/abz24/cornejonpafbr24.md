---
title: "An Analysis of the Impact of Field-Value Instance Navigation in Alloy&apos;s Model Finding"

authors:
  - César Cornejo
  - María Marta Novaira
  - Sonia Permigiani
  - Nazareno Aguirre
  - Marcelo F. Frias
  - Simón Gutiérrez Brida
  - Germán Regis


date: 2024-01-01

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

publication: "10th International Conference on Rigorous State Based Methods (ABZ'24)"
publication_short: "ABZ'24"

tags:
  - ABZ'24

categories: []

featured: false

# enable this for case studies
# projects:
#   - abz24

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_9.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-031-63790-2_9
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/cornejonpafbr24/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/cornejonpafbr24/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/cornejonpafbr24/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/cornejonpafbr24/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

The use of SAT-based model finding for specification analysis is a crucial characteristic of Alloy, and a main reason of its success as a language for software specification. When a property of a specification is analyzed and deemed satisfiable, the user usually explores instances of the corresponding satisfiability, in order to understand the analysis outcome. The order in which instances are obtained during exploration can impact the efficiency and effectiveness with which specification analysis is carried out. This has been observed by various researchers, and different instance exploration strategies have been proposed, besides the standard SAT-solver driven strategy implemented with the Alloy Analyzer. In this paper, we concentrate on a strategy recently proposed in the literature, that we refer to as “field-value” driven, and has been implemented in the tool HawkEye. The tool allows the user to interactively guide instance exploration, by enforcing constraints requiring fields to contain (resp., do not contain) specific values. We design an experiment involving faulty Alloy specifications featuring combinations of over constraints and under constraints, and perform a user study to analyze the impact of this instance exploration strategy, in comparison with the standard SAT-solver driven exploration. The study focuses on HawkEye’s facility of interactive instance querying and how it may favor users, in its current realization, during Alloy model analysis and debugging. We perform an assessment of the evaluation, and summarize some of the reasons that may diminish the impact of field-value exploration in model finding.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_9.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_9.pdf" >}}

## Reference

```
% BibTex
@inproceedings{CornejoNPAFBR24,
  author       = {C{\'{e}}sar Cornejo and
                  Mar{\'{\i}}a Marta Novaira and
                  Sonia Permigiani and
                  Nazareno Aguirre and
                  Marcelo F. Frias and
                  Sim{\'{o}}n Guti{\'{e}}rrez Brida and
                  Germ{\'{a}}n Regis},
  editor       = {Silvia Bonfanti and
                  Angelo Gargantini and
                  Michael Leuschel and
                  Elvinia Riccobene and
                  Patrizia Scandurra},
  title        = {An Analysis of the Impact of Field-Value Instance Navigation in Alloy's
                  Model Finding},
  booktitle    = {Rigorous State-Based Methods - 10th International Conference, {ABZ}
                  2024, Bergamo, Italy, June 25-28, 2024, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {14759},
  pages        = {141--159},
  publisher    = {Springer},
  year         = {2024},
  url          = {https://doi.org/10.1007/978-3-031-63790-2\_9},
  doi          = {10.1007/978-3-031-63790-2\_9},
  timestamp    = {Mon, 03 Mar 2025 21:25:08 +0100},
  biburl       = {https://dblp.org/rec/conf/zum/CornejoNPAFBR24.bib},
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

