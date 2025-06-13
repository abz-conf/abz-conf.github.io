---
title: "Generating Tests from B Specifications and Test Purposes"

authors:
  - Jacques Julliand
  - Pierre-Alain Masson
  - Régis Tissot


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_12.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-540-87603-8_12
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/julliandmt08/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/julliandmt08/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/julliandmt08/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/julliandmt08/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

This paper is about generating tests from test purposes, in addition to structural tests. We present a method that re-uses a behavioural model and an abstract test concretization layer developed for structural testing, and relies on additional test purposes. We propose, in the B framework, a process of test generation that uses the symbolic animation mechanisms of LTG (Leirios Test Generator) based on constraint solving, and guided by the test purposes. We build for that a B animable model that is the synchronized product of a behavioural B abstract model and a test purpose described as a labelled transition system. We prove the correctness of this method, and illustrate it by means of the IAS case study. IAS is a smart-card application dedicated to the operations of Identification, Authentication and electronic Signature.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_12.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_12.pdf" >}}

## Reference

```
% BibTex
@inproceedings{JulliandMT08,
  author       = {Jacques Julliand and
                  Pierre{-}Alain Masson and
                  R{\'{e}}gis Tissot},
  editor       = {Egon B{\"{o}}rger and
                  Michael J. Butler and
                  Jonathan P. Bowen and
                  Paul Boca},
  title        = {Generating Tests from {B} Specifications and Test Purposes},
  booktitle    = {Abstract State Machines, {B} and Z, First International Conference,
                  {ABZ} 2008, London, UK, September 16-18, 2008. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {5238},
  pages        = {139--152},
  publisher    = {Springer},
  year         = {2008},
  url          = {https://doi.org/10.1007/978-3-540-87603-8\_12},
  doi          = {10.1007/978-3-540-87603-8\_12},
  timestamp    = {Tue, 14 May 2019 10:00:50 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/JulliandMT08.bib},
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

