---
title: "Small Step Incremental Verification of Compilers"

authors:
  - Wolf Zimmermann
  - Thomas Kühn 0001
  - Edward Sabinus
  - Mandy Weißbach


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_21.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-031-63790-2_21
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/zimmermannksw24/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/zimmermannksw24/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/zimmermannksw24/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/zimmermannksw24/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Previously, we introduced the idea of agile compiler development, i.e., starting from an initial compiler for the most simple program of a language and extending it in small versions, each introducing a new language concept. Following this idea, in this paper, we propose an approach for incrementally verifying the dynamic semantics specified with abstract state machines (ASMs), such that definitions of previous versions must not be altered in subsequent versions. As a result, the compiler can be verified incrementally without revising the proofs of previous versions. As our first step, in this paper, we formalize and verify the memory mapping of the initial versions with ASMs and discuss their extensibility for the next increments. We plan to demonstrate this approach through the agile implementation and verification of a Sather-K compiler generating MIPS assembly language.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_21.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_21.pdf" >}}

## Reference

```
% BibTex
@inproceedings{ZimmermannKSW24,
  author       = {Wolf Zimmermann and
                  Thomas K{\"{u}}hn and
                  Edward Sabinus and
                  Mandy Wei{\ss}bach},
  editor       = {Silvia Bonfanti and
                  Angelo Gargantini and
                  Michael Leuschel and
                  Elvinia Riccobene and
                  Patrizia Scandurra},
  title        = {Small Step Incremental Verification of Compilers},
  booktitle    = {Rigorous State-Based Methods - 10th International Conference, {ABZ}
                  2024, Bergamo, Italy, June 25-28, 2024, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {14759},
  pages        = {262--269},
  publisher    = {Springer},
  year         = {2024},
  url          = {https://doi.org/10.1007/978-3-031-63790-2\_21},
  doi          = {10.1007/978-3-031-63790-2\_21},
  timestamp    = {Fri, 13 Sep 2024 16:19:49 +0200},
  biburl       = {https://dblp.org/rec/conf/zum/ZimmermannKSW24.bib},
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

