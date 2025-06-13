---
title: "A Model-Based Transformation Approach to Reuse and Retarget CASM Specifications"

authors:
  - Philipp Paulweber
  - Uwe Zdun


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
#  11 = "pub_short_paper"
#  12 = "pub_long_paper"
#  13 = "pub_invited_talk"
publication_types:
  - 11  # default is 1 (conference), adjust as needed

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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-319-33600-8_17.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-319-33600-8_17
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/paulweberz16/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/paulweberz16/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/paulweberz16/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/paulweberz16/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

The Abstract State Machine (ASM) theory is a way to specify algorithms, applications and systems in a formal model. Recent ASM languages and tools address either the translation of ASM specifications to a specific target programming language or aim at the execution in a specific environment. In this work-in-progress paper we outline a model-based transformation approach supporting (1) the specification of applications or systems using the Corinthian Abstract State Machine (CASM) modeling language and (2) retargeting those applications to different programming language and hardware target domains. An intermediate model is introduced, which not only captures software-based implementations, but also the generation of hardware-related code in the same model. This approach offers a new formal modeling perspective onto modular, reusable and retargetable software and hardware designs for the development of embedded systems. We provide a short overview of our CASM compiler design as well as the retargetable model-based approach to generate code for different target domains.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-319-33600-8_17.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-319-33600-8_17.pdf" >}}

## Reference

```
% BibTex
@inproceedings{PaulweberZ16,
  author       = {Philipp Paulweber and
                  Uwe Zdun},
  editor       = {Michael J. Butler and
                  Klaus{-}Dieter Schewe and
                  Atif Mashkoor and
                  Mikl{\'{o}}s Bir{\'{o}}},
  title        = {A Model-Based Transformation Approach to Reuse and Retarget {CASM}
                  Specifications},
  booktitle    = {Abstract State Machines, Alloy, B, TLA, VDM, and {Z} - 5th International
                  Conference, {ABZ} 2016, Linz, Austria, May 23-27, 2016, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {9675},
  pages        = {250--255},
  publisher    = {Springer},
  year         = {2016},
  url          = {https://doi.org/10.1007/978-3-319-33600-8\_17},
  doi          = {10.1007/978-3-319-33600-8\_17},
  timestamp    = {Sat, 09 Apr 2022 12:45:50 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/PaulweberZ16.bib},
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

