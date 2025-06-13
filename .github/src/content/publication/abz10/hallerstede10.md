---
title: "Structured Event-B Models and Proofs"

authors:
  - Stefan Hallerstede


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
#  10 = "pub_short_paper"
#  11 = "pub_long_paper"
publication_types:
  - 1   # default is 1 (conference), adjust as needed

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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_21.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-642-11811-1_21
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/hallerstede10/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/hallerstede10/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/hallerstede10/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/hallerstede10/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Event-B does not provide specific support for the modelling of problems that require some structuring, such as, local variables or sequential ordering of events. All variables need to be declared globally and sequential ordering of events can only be achieved by abstract program counters. This has two unfortunate consequences: such models become less comprehensible — we have to infer sequential ordering from the use of program counters; proof obligation generation does not consider ordering — generating too many proof obligations (although these are usually trivially discharged). In this article we propose a method for specifying structured models avoiding, in particular, the use of abstract program counters. It uses a notation that mainly serves to drive proof obligation generation. However, the notation also describes the structure of a model explicitly. A corresponding graphical notation is introduced that visualises the structure of a model.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_21.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_21.pdf" >}}

## Reference

```
% BibTex
@inproceedings{Hallerstede10,
  author       = {Stefan Hallerstede},
  editor       = {Marc Frappier and
                  Uwe Gl{\"{a}}sser and
                  Sarfraz Khurshid and
                  R{\'{e}}gine Laleau and
                  Steve Reeves},
  title        = {Structured Event-B Models and Proofs},
  booktitle    = {Abstract State Machines, Alloy, {B} and Z, Second International Conference,
                  {ABZ} 2010, Orford, QC, Canada, February 22-25, 2010. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {5977},
  pages        = {273--286},
  publisher    = {Springer},
  year         = {2010},
  url          = {https://doi.org/10.1007/978-3-642-11811-1\_21},
  doi          = {10.1007/978-3-642-11811-1\_21},
  timestamp    = {Tue, 14 May 2019 10:00:50 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/Hallerstede10.bib},
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

