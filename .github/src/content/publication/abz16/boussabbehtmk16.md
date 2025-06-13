---
title: "Formal Proofs of Termination Detection for Local Computations by Refinement-Based Compositions"

authors:
  - Maha Boussabbeh
  - Mohamed Tounsi 0001
  - Mohamed Mosbah 0001
  - Ahmed Hadj Kacem


date: 2016-01-01

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

publication: "5th International Conference on ASM, Alloy, B, TLA, VDM, and Z (ABZ'16)"
publication_short: "ABZ'16"

tags:
  - ABZ'16

categories: []

featured: false

# enable this for case studies
# projects:
#   - abz16

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-319-33600-8_12.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-319-33600-8_12
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/boussabbehtmk16/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/boussabbehtmk16/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/boussabbehtmk16/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/boussabbehtmk16/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

In this paper, we propose a formal framework enhancing the termination detection property of distributed algorithms and reusing their specifications as well as their proofs. By relying on refinement and composition, we show that an algorithm specified with local termination detection, can be reused in order to compute the same algorithm with global termination detection. The main idea relies upon the development of distributed algorithms following a top/down approach and the integration of additional computation steps developed in a pre-defined module. This module is specified in a generic and scalable way in order to be composed with particular developments. Once the composition link is proven, the global termination emerges automatically.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-319-33600-8_12.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-319-33600-8_12.pdf" >}}

## Reference

```
% BibTex
@inproceedings{BoussabbehTMK16,
  author       = {Maha Boussabbeh and
                  Mohamed Tounsi and
                  Mohamed Mosbah and
                  Ahmed Hadj Kacem},
  editor       = {Michael J. Butler and
                  Klaus{-}Dieter Schewe and
                  Atif Mashkoor and
                  Mikl{\'{o}}s Bir{\'{o}}},
  title        = {Formal Proofs of Termination Detection for Local Computations by Refinement-Based
                  Compositions},
  booktitle    = {Abstract State Machines, Alloy, B, TLA, VDM, and {Z} - 5th International
                  Conference, {ABZ} 2016, Linz, Austria, May 23-27, 2016, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {9675},
  pages        = {198--212},
  publisher    = {Springer},
  year         = {2016},
  url          = {https://doi.org/10.1007/978-3-319-33600-8\_12},
  doi          = {10.1007/978-3-319-33600-8\_12},
  timestamp    = {Tue, 11 Oct 2022 14:59:07 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/BoussabbehTMK16.bib},
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

