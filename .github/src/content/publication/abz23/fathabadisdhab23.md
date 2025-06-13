---
title: "Designing Critical Systems Using Hierarchical STPA and Event-B"

authors:
  - Asieh Salehi Fathabadi
  - Colin F. Snook
  - Dana Dghaym
  - Thai Son Hoang
  - Fahad Alotaibi
  - Michael J. Butler


date: 2023-01-01

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

publication: "9th International Conference on Rigorous State Based Methods (ABZ'23)"
publication_short: "ABZ'23"

tags:
  - ABZ'23

categories: []

featured: false

# enable this for case studies
# projects:
#   - abz23

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_17.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-031-33163-3_17
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/fathabadisdhab23/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/fathabadisdhab23/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/fathabadisdhab23/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/fathabadisdhab23/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

In the design of critical systems, it is important to ensure a degree of formality so that we reason about safety and security at early stages of analysis and design, rather than detect problems later. Influenced by ideas from STPA we present a hierarchical analysis process that aims to justify the design and flow-down of derived critical requirements arising from safety hazards and security vulnerabilities identified at the system level. At each level, we verify that the design achieves the safety/security requirements by backing the analysis with formal modelling and proof using Event-B refinement. The formal model helps to identify hazards/vulnerabilities arising from the design and how they relate to the safety accidents/security losses being considered at this level. We then re-apply the same process to each component of the design in a hierarchical manner. Thus we use ideas from STPA, backed by Event-B models, to drive the design, replacing the system level requirements with component requirements. In doing so, we decompose critical requirements down to components, transforming them from abstract system level requirements, towards concrete solutions that we can implement correctly so that the hazards/vulnerabilities are eliminated.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_17.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_17.pdf" >}}

## Reference

```
% BibTex
@inproceedings{FathabadiSDHAB23,
  author       = {Asieh Salehi Fathabadi and
                  Colin F. Snook and
                  Dana Dghaym and
                  Thai Son Hoang and
                  Fahad Alotaibi and
                  Michael J. Butler},
  editor       = {Uwe Gl{\"{a}}sser and
                  Jos{\'{e}} Creissac Campos and
                  Dominique M{\'{e}}ry and
                  Philippe A. Palanque},
  title        = {Designing Critical Systems Using Hierarchical {STPA} and Event-B},
  booktitle    = {Rigorous State-Based Methods - 9th International Conference, {ABZ}
                  2023, Nancy, France, May 30 - June 2, 2023, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {14010},
  pages        = {220--237},
  publisher    = {Springer},
  year         = {2023},
  url          = {https://doi.org/10.1007/978-3-031-33163-3\_17},
  doi          = {10.1007/978-3-031-33163-3\_17},
  timestamp    = {Fri, 02 Jun 2023 21:23:52 +0200},
  biburl       = {https://dblp.org/rec/conf/zum/FathabadiSDHAB23.bib},
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

