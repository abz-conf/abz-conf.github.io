---
title: "On Component-Based Reuse for Event-B"

authors:
  - Andrew Edmunds
  - Colin F. Snook
  - Marina Waldén


date: 2016-01-01

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

publication: "5th International Conference on ASM, Alloy, B, TLA, VDM, and Z (ABZ'16)"
publication_short: "ABZ'16"

tags:
  - ABZ'16

categories: []

featured: false

# enable this for case studies
# projects:
#   - abz16

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-319-33600-8_9.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-319-33600-8_9
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/edmundssw16/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/edmundssw16/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/edmundssw16/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/edmundssw16/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Efficient reuse is a goal of many software engineering strategies and is useful in the safety-critical domain where formal development is required. Event-B can be used to develop safety-critical systems, but could be improved by a component-based reuse strategy. In this paper, we outline a component-based reuse methodology for Event-B. It provides a means for bottom-up scalability, and can also be used with the existing top-down approach. We describe the process of creating library components, their composition, and specification of new properties (involving the composed elements). We introduce Event-B component interfaces and propose to use a diagrammatic representation of component instances (based on iUML-B) which can be used to describe the relationships between the composed elements. We also discuss the specification of communication flow across component boundaries and describe the additional proof obligations that are required.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-319-33600-8_9.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-319-33600-8_9.pdf" >}}

## Reference

```
% BibTex
@inproceedings{EdmundsSW16,
  author       = {Andrew Edmunds and
                  Colin F. Snook and
                  Marina Wald{\'{e}}n},
  editor       = {Michael J. Butler and
                  Klaus{-}Dieter Schewe and
                  Atif Mashkoor and
                  Mikl{\'{o}}s Bir{\'{o}}},
  title        = {On Component-Based Reuse for Event-B},
  booktitle    = {Abstract State Machines, Alloy, B, TLA, VDM, and {Z} - 5th International
                  Conference, {ABZ} 2016, Linz, Austria, May 23-27, 2016, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {9675},
  pages        = {151--166},
  publisher    = {Springer},
  year         = {2016},
  url          = {https://doi.org/10.1007/978-3-319-33600-8\_9},
  doi          = {10.1007/978-3-319-33600-8\_9},
  timestamp    = {Mon, 03 Jan 2022 22:35:01 +0100},
  biburl       = {https://dblp.org/rec/conf/asm/EdmundsSW16.bib},
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

