---
title: "Data Flow Analysis and Testing of Abstract State Machines"

authors:
  - Alessandra Cavarra


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
#  10 = "pub_short_paper"
#  11 = "pub_long_paper"
publication_types:
  - 1   # default is 1 (conference), adjust as needed

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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_8.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-540-87603-8_8
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/cavarra08/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/cavarra08/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/cavarra08/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/cavarra08/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

This paper introduces an approach to apply data flow testing techniques to Abstract State Machines specifications. Since traditional data flow coverage criteria are strictly based on the mapping between a program and its flow graph, they cannot be directly applied to ASMs. In this context we are interested in tracing the flow of data between states in ASM runs as opposed to between nodes in a program’s flow graph. Therefore, we revise the classical concepts in data flow analysis and define them on two levels: the syntactic (rule) level, and the computational (run) level. We also specify a family of ad hoc data flow coverage criteria and introduce a model checking-based approach to generate automatically test cases satisfying a given set of coverage criteria from ASM models.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_8.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_8.pdf" >}}

## Reference

```
% BibTex
@inproceedings{Cavarra08,
  author       = {Alessandra Cavarra},
  editor       = {Egon B{\"{o}}rger and
                  Michael J. Butler and
                  Jonathan P. Bowen and
                  Paul Boca},
  title        = {Data Flow Analysis and Testing of Abstract State Machines},
  booktitle    = {Abstract State Machines, {B} and Z, First International Conference,
                  {ABZ} 2008, London, UK, September 16-18, 2008. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {5238},
  pages        = {85--97},
  publisher    = {Springer},
  year         = {2008},
  url          = {https://doi.org/10.1007/978-3-540-87603-8\_8},
  doi          = {10.1007/978-3-540-87603-8\_8},
  timestamp    = {Tue, 14 May 2019 10:00:50 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/Cavarra08.bib},
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

