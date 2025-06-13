---
title: "Event-B as DSL in Isabelle and HOL Experiences from a Prototype"

authors:
  - Benoît Ballenghien
  - Burkhart Wolff


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
#  11 = "pub_short_paper"
#  12 = "pub_long_paper"
#  13 = "pub_invited_talk"
#  14 = "pub_phd_symposium"
publication_types:
  - 10  # default is 1 (conference), adjust as needed

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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_18.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-031-63790-2_18
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/ballenghienw24/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/ballenghienw24/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/ballenghienw24/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/ballenghienw24/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

The proof assistant Isabelle/HOL is made available inside a flexible system framework allowing for logically safe extensions, which comprise both theories as well as implementations for code-generation, documentation, and specific support for a variety of formal methods. Following the techniques in [9] and the theoretical groundwork in [4], we show the major milestones for the implementation of a B-Tool and the resulting refinement method inside the Isabelle/HOL platform. The prototype HOL-B provides IDE support, documentation support, a theory for the Z-Mathematical Toolkit underlying the B-Method, and a generated denotational semantics for a B MACHINE specification implemented as a specification construct in Isabelle/HOL. Extended by more automated proof machinery geared to refinements, HOL-B can serve as a more portable, flexible and extensible tool for Event-B that may profit from the large Isabelle/HOL libraries providing Algebra and Analysis theories.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_18.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_18.pdf" >}}

## Reference

```
% BibTex
@inproceedings{BallenghienW24,
  author       = {Beno{\^{\i}}t Ballenghien and
                  Burkhart Wolff},
  editor       = {Silvia Bonfanti and
                  Angelo Gargantini and
                  Michael Leuschel and
                  Elvinia Riccobene and
                  Patrizia Scandurra},
  title        = {Event-B as {DSL} in Isabelle and {HOL} Experiences from a Prototype},
  booktitle    = {Rigorous State-Based Methods - 10th International Conference, {ABZ}
                  2024, Bergamo, Italy, June 25-28, 2024, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {14759},
  pages        = {241--247},
  publisher    = {Springer},
  year         = {2024},
  url          = {https://doi.org/10.1007/978-3-031-63790-2\_18},
  doi          = {10.1007/978-3-031-63790-2\_18},
  timestamp    = {Fri, 19 Jul 2024 23:15:46 +0200},
  biburl       = {https://dblp.org/rec/conf/zum/BallenghienW24.bib},
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

