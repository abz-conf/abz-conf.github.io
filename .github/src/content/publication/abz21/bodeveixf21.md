---
title: "Event-B Formalization of Event-B Contexts"

authors:
  - Jean-Paul Bodeveix
  - Mamoun Filali


date: 2021-01-01

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

publication: "8th International Conference on Rigorous State Based Methods (ABZ'21)"
publication_short: "ABZ'21"

tags:
  - ABZ'21

categories: []

featured: false

# enable this for case studies
# projects:
#   - abz21

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-030-77543-8_5.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-030-77543-8_5
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/bodeveixf21/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/bodeveixf21/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/bodeveixf21/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/bodeveixf21/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

This paper presents an Event-B meta-modelisation of an Event-B project restricted to its context hierarchy which introduces the functional part of a development through sets, constants, axioms and theorems. We study the proposal of a new mechanism for Event-B. It consists in allowing to instantiate in a new context an already proved theorem in a given context. We investigate the validation of the instantiation mechanism in order to prove the validity of imported theorems. We also compare the proposal with similar mechanisms available within some existing theorem provers.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-030-77543-8_5.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-030-77543-8_5.pdf" >}}

## Reference

```
% BibTex
@inproceedings{BodeveixF21,
  author       = {Jean{-}Paul Bodeveix and
                  Mamoun Filali},
  editor       = {Alexander Raschke and
                  Dominique M{\'{e}}ry},
  title        = {Event-B Formalization of Event-B Contexts},
  booktitle    = {Rigorous State-Based Methods - 8th International Conference, {ABZ}
                  2021, Ulm, Germany, June 9-11, 2021, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {12709},
  pages        = {66--80},
  publisher    = {Springer},
  year         = {2021},
  url          = {https://doi.org/10.1007/978-3-030-77543-8\_5},
  doi          = {10.1007/978-3-030-77543-8\_5},
  timestamp    = {Tue, 15 Jun 2021 17:24:03 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/BodeveixF21.bib},
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

