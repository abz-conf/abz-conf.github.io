---
title: "A Concept-Driven Construction of the Mondex Protocol Using Three Refinements"

authors:
  - Gerhard Schellhorn
  - Richard Banach


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_6.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-540-87603-8_6
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/schellhornb08/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/schellhornb08/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/schellhornb08/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/schellhornb08/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

The Mondex case study concerns the formal development and verification of an electronic purse protocol. Several groups have worked on its specification and mechanical verification, their solutions being (as were ours previously), either one big step or several steps motivated by the task’s complexity. A new solution is presented that is structured into three refinements, motivated by the three concepts underlying Mondex: a message protocol to transfer money over a lossy medium, protection against replay attacks, and uniqueness of transfers using sequence numbers. We also give an improved proof technique based on our theoretical results on verifying interleaved systems.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_6.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_6.pdf" >}}

## Reference

```
% BibTex
@inproceedings{SchellhornB08,
  author       = {Gerhard Schellhorn and
                  Richard Banach},
  editor       = {Egon B{\"{o}}rger and
                  Michael J. Butler and
                  Jonathan P. Bowen and
                  Paul Boca},
  title        = {A Concept-Driven Construction of the Mondex Protocol Using Three Refinements},
  booktitle    = {Abstract State Machines, {B} and Z, First International Conference,
                  {ABZ} 2008, London, UK, September 16-18, 2008. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {5238},
  pages        = {57--70},
  publisher    = {Springer},
  year         = {2008},
  url          = {https://doi.org/10.1007/978-3-540-87603-8\_6},
  doi          = {10.1007/978-3-540-87603-8\_6},
  timestamp    = {Mon, 03 Mar 2025 20:58:01 +0100},
  biburl       = {https://dblp.org/rec/conf/asm/SchellhornB08.bib},
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

