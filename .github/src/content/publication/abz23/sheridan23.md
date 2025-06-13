---
title: "Exploring a Methodology for Formal Verification of Safety-Critical Systems"

authors:
  - Oisín Sheridan


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_26.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-031-33163-3_26
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/sheridan23/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/sheridan23/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/sheridan23/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/sheridan23/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

As the formal verification of safety-critical software systems often requires the integration of multiple tools and techniques, we propose a three-phase methodology incorporating two complementary workflows to ensure that the system in question fulfills its requirements. We use the Formal Requirements Elicitation Tool (FRET) to structure the requirements so that they can be translated to other formalisms. These translations are then either incorporated directly into an existing model in Simulink, or used to construct a new formal model of the system. Our current use case is a model of a controller for a civilian aircraft engine.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_26.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_26.pdf" >}}

## Reference

```
% BibTex
@inproceedings{Sheridan23,
  author       = {Ois{\'{\i}}n Sheridan},
  editor       = {Uwe Gl{\"{a}}sser and
                  Jos{\'{e}} Creissac Campos and
                  Dominique M{\'{e}}ry and
                  Philippe A. Palanque},
  title        = {Exploring a Methodology for Formal Verification of Safety-Critical
                  Systems},
  booktitle    = {Rigorous State-Based Methods - 9th International Conference, {ABZ}
                  2023, Nancy, France, May 30 - June 2, 2023, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {14010},
  pages        = {361--365},
  publisher    = {Springer},
  year         = {2023},
  url          = {https://doi.org/10.1007/978-3-031-33163-3\_26},
  doi          = {10.1007/978-3-031-33163-3\_26},
  timestamp    = {Fri, 02 Jun 2023 21:23:52 +0200},
  biburl       = {https://dblp.org/rec/conf/zum/Sheridan23.bib},
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

