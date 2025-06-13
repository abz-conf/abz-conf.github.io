---
title: "Introducing Aspect-Oriented Specification for Abstract State Machines"

authors:
  - Marcel Dausend
  - Alexander Raschke


date: 2014-01-01

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

publication: "4th International Conference on ASM, Alloy, B, TLA, VDM, and Z (ABZ'14)"
publication_short: "ABZ'14"

tags:
  - ABZ'14

categories: []

featured: false

# enable this for case studies
# projects:
#   - abz14

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-662-43652-3_15.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-662-43652-3_15
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/dausendr14/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/dausendr14/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/dausendr14/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/dausendr14/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

With the paradigm of aspect orientation, a developer is able to separate the code of so-called cross-cutting concerns from the rest of the program logic. This possibility is useful for formal specifications, too. For example, security aspects can be separated from the rest of the specification. Another use case for aspect orientation in specifications is the extension of specifications without touching the original ones. The definition of formal semantics for UML profiles without changing the original UML specification is an example for this application. This paper describes the implementation of the aspect oriented approach in Abstract State Machines. We introduce an aspect language with its syntax and formal semantics. It allows for specifying pointcuts where an original specification is augmented with aspect specification. Besides the general overview of this language extension, some ASM specific features of the realization are depicted in detail.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-662-43652-3_15.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-662-43652-3_15.pdf" >}}

## Reference

```
% BibTex
@inproceedings{DausendR14,
  author       = {Marcel Dausend and
                  Alexander Raschke},
  editor       = {Yamine A{\"{\i}}t Ameur and
                  Klaus{-}Dieter Schewe},
  title        = {Introducing Aspect-Oriented Specification for Abstract State Machines},
  booktitle    = {Abstract State Machines, Alloy, B, TLA, VDM, and {Z} - 4th International
                  Conference, {ABZ} 2014, Toulouse, France, June 2-6, 2014. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {8477},
  pages        = {174--187},
  publisher    = {Springer},
  year         = {2014},
  url          = {https://doi.org/10.1007/978-3-662-43652-3\_15},
  doi          = {10.1007/978-3-662-43652-3\_15},
  timestamp    = {Tue, 14 May 2019 10:00:50 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/DausendR14.bib},
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

