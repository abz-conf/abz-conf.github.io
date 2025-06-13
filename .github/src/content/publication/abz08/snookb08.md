---
title: "UML-B: A Plug-in for the Event-B Tool Set"

authors:
  - Colin F. Snook
  - Michael J. Butler


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_32.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-540-87603-8_32
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/snookb08/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/snookb08/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/snookb08/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/snookb08/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

UML-B is a graphical formal modelling notation that relies on Event-B for its underlying semantics and is closely integrated with the ‘Rodin’, Event-B verification tools. UML-B is similar to UML but has its own meta-model. UML-B provides tool support, including drawing tools and a translator to generate Event-B models. When a UML-B drawing is saved the translator automatically generates the corresponding Event-B model. The Event-B verification tools (syntax checker and prover) then run automatically providing an immediate display of problems which are indicated on the relevant UML-B diagram.The UML-B modelling environment consists of a UML-B project containing a UML-B model. Four interlinked diagram types (package, context, class and statemachine) are available. Package Diagrams are used to describe the ‘refines’ and ‘sees’ relationships between top level components (machines and contexts) of a UML-B project. UML-B mirrors the Event-B approach where static data (sets and constants) are modelled in a separate package called a ‘context’. The context diagram is similar to a class diagram but has only constant data represented by ClassTypes, Attributes and Associations. ClassTypes define ‘carrier’ sets or constant subsets of other ClassTypes.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_32.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_32.pdf" >}}

## Reference

```
% BibTex
@inproceedings{SnookB08,
  author       = {Colin F. Snook and
                  Michael J. Butler},
  editor       = {Egon B{\"{o}}rger and
                  Michael J. Butler and
                  Jonathan P. Bowen and
                  Paul Boca},
  title        = {{UML-B:} {A} Plug-in for the Event-B Tool Set},
  booktitle    = {Abstract State Machines, {B} and Z, First International Conference,
                  {ABZ} 2008, London, UK, September 16-18, 2008. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {5238},
  pages        = {344},
  publisher    = {Springer},
  year         = {2008},
  url          = {https://doi.org/10.1007/978-3-540-87603-8\_32},
  doi          = {10.1007/978-3-540-87603-8\_32},
  timestamp    = {Mon, 03 Jan 2022 22:35:01 +0100},
  biburl       = {https://dblp.org/rec/conf/asm/SnookB08.bib},
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

