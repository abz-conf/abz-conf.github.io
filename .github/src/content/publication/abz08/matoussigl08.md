---
title: "A First Attempt to Express KAOS Refinement Patterns with Event B"

authors:
  - Abderrahman Matoussi
  - Frédéric Gervais
  - Régine Laleau


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_27.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-540-87603-8_27
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/matoussigl08/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/matoussigl08/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/matoussigl08/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/matoussigl08/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

It is now recognised that goals play an important role in requirements engineering process, and consequently in systems development process.Whereas specifications allow us to answer the question”WHAT the system does”, goals allow us to address the ”WHY, WHO, WHEN” questions [1]. Up to now, the development process associated with formal methods, including Event B, begins at the specification level. Our objective is to include requirements analysis within this process, and more precisely KAOS[2] which is a methodology to implement goal-based reasoning. Existing work [3,4] that combine KAOS with formal methods generate a formal specification model from a KAOS requirements model.We aim at expressing KAOS goal models with a formal language (Event B), hence staying at the same abstraction level. Our work is based on a constructive approach in which Event B models are built incrementally from KAOS goal models, driven by goal refinement patterns [1]. Since a KAOS goal means that a property must be established, the main idea is to represent each goal as a B event and the property as the post-condition of this B event. Up to now, we consider refinement patterns defined with first-order logic. Patterns with LTL temporal logic will be studied in further work.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_27.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_27.pdf" >}}

## Reference

```
% BibTex
@inproceedings{MatoussiGL08,
  author       = {Abderrahman Matoussi and
                  Fr{\'{e}}d{\'{e}}ric Gervais and
                  R{\'{e}}gine Laleau},
  editor       = {Egon B{\"{o}}rger and
                  Michael J. Butler and
                  Jonathan P. Bowen and
                  Paul Boca},
  title        = {A First Attempt to Express {KAOS} Refinement Patterns with Event {B}},
  booktitle    = {Abstract State Machines, {B} and Z, First International Conference,
                  {ABZ} 2008, London, UK, September 16-18, 2008. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {5238},
  pages        = {338},
  publisher    = {Springer},
  year         = {2008},
  url          = {https://doi.org/10.1007/978-3-540-87603-8\_27},
  doi          = {10.1007/978-3-540-87603-8\_27},
  timestamp    = {Tue, 14 May 2019 10:00:50 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/MatoussiGL08.bib},
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

