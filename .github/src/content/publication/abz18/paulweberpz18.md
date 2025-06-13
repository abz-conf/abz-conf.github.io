---
title: "CASM-IR: Uniform ASM-Based Intermediate Representation for Model Specification, Execution, and Transformation"

authors:
  - Philipp Paulweber
  - Emmanuel Pescosta
  - Uwe Zdun


date: 2018-01-01

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

publication: "6th International Conference on ASM, Alloy, B, TLA, VDM, and Z (ABZ'18)"
publication_short: "ABZ'18"

tags:
  - ABZ'18

categories: []

featured: false

# enable this for case studies
# projects:
#   - abz18

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-319-91271-4_4.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-319-91271-4_4
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/paulweberpz18/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/paulweberpz18/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/paulweberpz18/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/paulweberpz18/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

The Abstract State Machine (ASM) theory is a well-known formal method, which can be used to specify arbitrary algorithms, applications or even whole systems. Over the past years, there have been many approaches to implement concrete ASM-based modeling and specification languages. All of those approaches define their type systems and operator semantics differently in their internal representation, which leads to undesired or unexpected behavior during the modeling, the execution, and code generation of such ASM specifications. In this paper, we present CASM-IR, an Intermediate Representation (IR), designed to aid ASM-based language engineering which is based on a well-formed ASM-based specification format. Moreover, CASM-IR is conceptualized from the ground up to ease the formalization of ASM-based analysis and transformation passes. The feasibility of CASM-IR solving the uniform ASM representation problem is depicted. Based on our CASM-IR implementation, we were able to integrate a front-end of our statically inferred Corinthian Abstract State Machine (CASM) modeling language.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-319-91271-4_4.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-319-91271-4_4.pdf" >}}

## Reference

```
% BibTex
@inproceedings{PaulweberPZ18,
  author       = {Philipp Paulweber and
                  Emmanuel Pescosta and
                  Uwe Zdun},
  editor       = {Michael J. Butler and
                  Alexander Raschke and
                  Thai Son Hoang and
                  Klaus Reichl},
  title        = {{CASM-IR:} Uniform ASM-Based Intermediate Representation for Model
                  Specification, Execution, and Transformation},
  booktitle    = {Abstract State Machines, Alloy, B, TLA, VDM, and {Z} - 6th International
                  Conference, {ABZ} 2018, Southampton, UK, June 5-8, 2018, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {10817},
  pages        = {39--54},
  publisher    = {Springer},
  year         = {2018},
  url          = {https://doi.org/10.1007/978-3-319-91271-4\_4},
  doi          = {10.1007/978-3-319-91271-4\_4},
  timestamp    = {Sat, 09 Apr 2022 12:45:50 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/PaulweberPZ18.bib},
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

