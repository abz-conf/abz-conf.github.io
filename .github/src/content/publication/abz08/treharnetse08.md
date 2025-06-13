---
title: "Object Modelling in the SystemB Industrial Project"

authors:
  - Helen Treharne
  - Edward Turner
  - Steve A. Schneider
  - Neil Evans


date: 2008-01-01

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
  - 11   # default is 1 (conference), adjust as needed

publication: "1st International Conference on ASM, B, and Z (ABZ'08)"
publication_short: "ABZ'08"

tags:
  - ABZ'08

categories: []

featured: false

# enable this for case studies
# projects:
#   - abz08

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_46.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-540-87603-8_46
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/treharnetse08/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/treharnetse08/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/treharnetse08/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/treharnetse08/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

The SystemB project is a two year project at the University of Surrey, funded by AWE plc, and is concerned with bridging the areas of formal methods and object modelling. The project is focused on the CSP ∥ B integrated formal method and increasing its level of tool support so that CSP ∥ B models of Executable UML (xUML) systems can be constructed automatically. The CSP ∥ B models will subject the xUML model to formal analysis prior to generating executable code. We are currently developing a CSP ∥ B model generator within the xUML toolsuite provided by Kennedy Carter Ltd. xUML is used within AWE and we will initially focus on reasoning about xUML state machines. Actions within xUML state machines are defined using the Action Specification Language (ASL). ASL is more low level than the Object Constraint Language; they can execute concurrently, and can also be used in operation definitions. Hence it is a challenge to model formally. In the extended abstract we provide an overview of one ASL to AMN translation pattern being developed and highlight the role of B in the project.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_46.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_46.pdf" >}}

## Reference

```
% BibTex
@inproceedings{TreharneTSE08,
  author       = {Helen Treharne and
                  Edward Turner and
                  Steve A. Schneider and
                  Neil Evans},
  editor       = {Egon B{\"{o}}rger and
                  Michael J. Butler and
                  Jonathan P. Bowen and
                  Paul Boca},
  title        = {Object Modelling in the SystemB Industrial Project},
  booktitle    = {Abstract State Machines, {B} and Z, First International Conference,
                  {ABZ} 2008, London, UK, September 16-18, 2008. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {5238},
  pages        = {359},
  publisher    = {Springer},
  year         = {2008},
  url          = {https://doi.org/10.1007/978-3-540-87603-8\_46},
  doi          = {10.1007/978-3-540-87603-8\_46},
  timestamp    = {Fri, 07 Aug 2020 17:57:33 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/TreharneTSE08.bib},
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

