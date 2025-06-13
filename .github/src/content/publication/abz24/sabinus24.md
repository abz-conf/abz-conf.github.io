---
title: "Proof Construction and Checking on Evolving Abstract State Machines"

authors:
  - Edward Sabinus


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_30.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-031-63790-2_30
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/sabinus24/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/sabinus24/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/sabinus24/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/sabinus24/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Abstract State Machines (ASMs) are widely used in the formalization and verification of the semantics of software or hardware. However, tools for assisting this process for evolving specifications are still lacking. With evolving we denote adding extensions without refactoring. We want to create a tool assisting in the verification of evolving specifications. Our approach is to translate ASM specifications into the language of an existing proof checker, construct the proofs as far as possible automatically, and check the proofs with the proof checker. Further, we want proofs of evolvable specifications also to be evolvable. This paper gives a brief overview of the approach and discusses the first step of this work, namely the translation of ASM specifications into the language of an existing proof checker, with consideration of automation possibilities.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_30.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_30.pdf" >}}

## Reference

```
% BibTex
@inproceedings{Sabinus24,
  author       = {Edward Sabinus},
  editor       = {Silvia Bonfanti and
                  Angelo Gargantini and
                  Michael Leuschel and
                  Elvinia Riccobene and
                  Patrizia Scandurra},
  title        = {Proof Construction and Checking on Evolving Abstract State Machines},
  booktitle    = {Rigorous State-Based Methods - 10th International Conference, {ABZ}
                  2024, Bergamo, Italy, June 25-28, 2024, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {14759},
  pages        = {392--396},
  publisher    = {Springer},
  year         = {2024},
  url          = {https://doi.org/10.1007/978-3-031-63790-2\_30},
  doi          = {10.1007/978-3-031-63790-2\_30},
  timestamp    = {Thu, 04 Jul 2024 22:05:23 +0200},
  biburl       = {https://dblp.org/rec/conf/zum/Sabinus24.bib},
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

