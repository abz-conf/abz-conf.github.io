---
title: "Standalone Event-B Models Analysis Relying on the EB4EB Meta-theory"

authors:
  - Peter Riviere
  - Neeraj Kumar Singh 0001
  - Yamine Aït-Ameur
  - Guillaume Dupont


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_15.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-031-33163-3_15
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/rivieresad23/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/rivieresad23/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/rivieresad23/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/rivieresad23/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Event-B is a state-based correct-by-construction system design formal method relying on proof and refinement where system models are expressed using set theory and First Order Logic (FOL). Through the generation and discharging of proof obligations (POs), Event-B natively supports the establishment of properties such as safety invariant, convergence and refinement. Other properties, relevant to system verification, may be studied as well, but need to be explicitly formalised by the designer, or expressed in another formal method. This process compromises reusability and is error-prone, especially on larger systems. Recently, the reflexive EB4EB framework has been proposed for formalising Event-B concepts as first-class objects. It allows manipulating these concepts using FOL and set theory in Event-B. In this paper, we propose a rigorous methodology for extending the EB4EB framework, to support new system analysis mechanisms associated to properties that are not natively present in core Event-B. Thanks to the reflexive nature of this framework, new generic and reusable system properties and their associated POs are expressed once and for all, and for any refinement level. For specific systems, designers instantiate these properties and the associated POs are automatically generated and submitted to Event-B’s provers. This methodology is used to define three analyses: deadlock-freeness, invariant weakness analysis and reachability, all of which are demonstrated on a case study.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_15.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_15.pdf" >}}

## Reference

```
% BibTex
@inproceedings{RiviereSAD23,
  author       = {Peter Riviere and
                  Neeraj Kumar Singh and
                  Yamine A{\"{\i}}t{-}Ameur and
                  Guillaume Dupont},
  editor       = {Uwe Gl{\"{a}}sser and
                  Jos{\'{e}} Creissac Campos and
                  Dominique M{\'{e}}ry and
                  Philippe A. Palanque},
  title        = {Standalone Event-B Models Analysis Relying on the {EB4EB} Meta-theory},
  booktitle    = {Rigorous State-Based Methods - 9th International Conference, {ABZ}
                  2023, Nancy, France, May 30 - June 2, 2023, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {14010},
  pages        = {193--211},
  publisher    = {Springer},
  year         = {2023},
  url          = {https://doi.org/10.1007/978-3-031-33163-3\_15},
  doi          = {10.1007/978-3-031-33163-3\_15},
  timestamp    = {Tue, 23 May 2023 09:57:42 +0200},
  biburl       = {https://dblp.org/rec/conf/zum/RiviereSAD23.bib},
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

