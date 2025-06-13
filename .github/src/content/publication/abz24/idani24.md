---
title: "Transpilation of Petri-nets into B - Shallow and Deep Embeddings"

authors:
  - Akram Idani


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_5.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-031-63790-2_5
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/idani24/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/idani24/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/idani24/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/idani24/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Petri-nets and their variants (Place/Transition nets, High-Level Petri Nets, etc.) are widely used in the development of safety critical-systems. Their success is related to three major aspects: a formal semantics, a graphical syntax and the availability of verification tools. In our previous work we presented a new vision for the semantic definition of Petri-nets applying a Formal Model-Driven Engineering (FMDE) built on the B method. The approach is powered by Meeduse, a language workbench that we developed in order to formally instrument executable Domain-Specific Languages (xDSLs) by applying a deep embedding technique and the B method. However, because of the abstract nature of the underlying formal models, our deep embedding is suitable for the validation and verification activities at the design stage but not sufficient to generate code for target platforms. This paper advances our previous work with a shallow embedding technique taking benefit of the B method tools in order to safely synthesize executable Petri-net controllers that can be embedded in target platforms.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_5.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_5.pdf" >}}

## Reference

```
% BibTex
@inproceedings{Idani24,
  author       = {Akram Idani},
  editor       = {Silvia Bonfanti and
                  Angelo Gargantini and
                  Michael Leuschel and
                  Elvinia Riccobene and
                  Patrizia Scandurra},
  title        = {Transpilation of Petri-nets into {B} - Shallow and Deep Embeddings},
  booktitle    = {Rigorous State-Based Methods - 10th International Conference, {ABZ}
                  2024, Bergamo, Italy, June 25-28, 2024, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {14759},
  pages        = {80--98},
  publisher    = {Springer},
  year         = {2024},
  url          = {https://doi.org/10.1007/978-3-031-63790-2\_5},
  doi          = {10.1007/978-3-031-63790-2\_5},
  timestamp    = {Thu, 04 Jul 2024 22:05:23 +0200},
  biburl       = {https://dblp.org/rec/conf/zum/Idani24.bib},
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

