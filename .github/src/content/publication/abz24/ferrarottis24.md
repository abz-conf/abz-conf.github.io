---
title: "Modal Extensions of the Logic of Abstract State Machines"

authors:
  - Flavio Ferrarotti
  - Klaus-Dieter Schewe


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_8.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-031-63790-2_8
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/ferrarottis24/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/ferrarottis24/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/ferrarottis24/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/ferrarottis24/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Based on the logic of non-deterministic Abstract State Machines (ASMs) we define a modal extension \(\mathcal{M}\mathcal{L}_{\text {ASM}}\)  by first introducing multi-step predicates and then adding quantification over the number of steps. We show that liveness conditions such as invariance, conditional and unconditional progress, and persistence on all or some runs of an ASM can be expressed in this logic. We show the existence of a complete fragment of \(\mathcal{M}\mathcal{L}_{\text {ASM}}\), which still contains the interesting liveness conditions, and demonstrate the usefulness of this complete fragment by an example concerning mutual exclusion.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_8.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_8.pdf" >}}

## Reference

```
% BibTex
@inproceedings{FerrarottiS24,
  author       = {Flavio Ferrarotti and
                  Klaus{-}Dieter Schewe},
  editor       = {Silvia Bonfanti and
                  Angelo Gargantini and
                  Michael Leuschel and
                  Elvinia Riccobene and
                  Patrizia Scandurra},
  title        = {Modal Extensions of the Logic of Abstract State Machines},
  booktitle    = {Rigorous State-Based Methods - 10th International Conference, {ABZ}
                  2024, Bergamo, Italy, June 25-28, 2024, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {14759},
  pages        = {123--140},
  publisher    = {Springer},
  year         = {2024},
  url          = {https://doi.org/10.1007/978-3-031-63790-2\_8},
  doi          = {10.1007/978-3-031-63790-2\_8},
  timestamp    = {Thu, 04 Jul 2024 22:05:23 +0200},
  biburl       = {https://dblp.org/rec/conf/zum/FerrarottiS24.bib},
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

