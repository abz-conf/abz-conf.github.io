---
title: "A Structure for Dependability Arguments"

authors:
  - Daniel Jackson 0001
  - Eunsuk Kang


date: 2010-01-01

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
  - 13   # default is 1 (conference), adjust as needed


publication: "2nd International Conference on ASM, Alloy, B, and Z (ABZ'10)"
publication_short: "ABZ'10"

tags:
  - ABZ'10

categories: []

featured: false

# enable this for case studies
# projects:
#   - abz10

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_1.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-642-11811-1_1
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/jacksonk10/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/jacksonk10/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/jacksonk10/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/jacksonk10/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

How should a software system be verified? Much research is currently focused on attempts to show that code modules meet their specifications. This is important, but bugs in code are not the weakest link in the chain. The larger problems are identifying and articulating critical properties, and ensuring that the components of a system - not only software modules, but also hardware peripherals, physical environments, and human operators - together establish them. Another common assumption is that verification must take system design and implementation as given. I’ll explain the rationale for, and elements of, a new approach to verification, in which design is driven by verification goals, and verification arguments are structured in a way that exposes the relationship between critical properties and the components that ensure them.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_1.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_1.pdf" >}}

## Reference

```
% BibTex
@inproceedings{JacksonK10,
  author       = {Daniel Jackson and
                  Eunsuk Kang},
  editor       = {Marc Frappier and
                  Uwe Gl{\"{a}}sser and
                  Sarfraz Khurshid and
                  R{\'{e}}gine Laleau and
                  Steve Reeves},
  title        = {A Structure for Dependability Arguments},
  booktitle    = {Abstract State Machines, Alloy, {B} and Z, Second International Conference,
                  {ABZ} 2010, Orford, QC, Canada, February 22-25, 2010. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {5977},
  pages        = {1},
  publisher    = {Springer},
  year         = {2010},
  url          = {https://doi.org/10.1007/978-3-642-11811-1\_1},
  doi          = {10.1007/978-3-642-11811-1\_1},
  timestamp    = {Tue, 14 May 2019 10:00:50 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/JacksonK10.bib},
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

