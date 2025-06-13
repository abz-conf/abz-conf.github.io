---
title: "Introducing Specification-Based Data Structure Repair Using Alloy"

authors:
  - Razieh Nokhbeh Zaeem
  - Sarfraz Khurshid


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
  - 11   # default is 1 (conference), adjust as needed


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_34.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-642-11811-1_34
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/zaeemk10/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/zaeemk10/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/zaeemk10/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/zaeemk10/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

While several different techniques utilize specifications to check correctness of programs before they are deployed, the use of specifications in deployed software is more limited, largely taking the form of runtime checking where assertions form a basis for detecting erroneous program states and terminating erroneous executions in failures. Recent approaches [1] proposed constraint-based repair where data structure constraints are used to repair erroneous states. However, data structure constraints are too weak a form of specification for error recovery in general. We have developed a specification-based approach for data structure repair, which allows repairing erroneous executions in deployed software by repairing erroneous states. The key novelty is our support for rich behavioral specifications, such as those that relate pre-states with post-states to accurately specify expected behavior and hence to enable precise repair.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_34.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_34.pdf" >}}

## Reference

```
% BibTex
@inproceedings{ZaeemK10,
  author       = {Razieh Nokhbeh Zaeem and
                  Sarfraz Khurshid},
  editor       = {Marc Frappier and
                  Uwe Gl{\"{a}}sser and
                  Sarfraz Khurshid and
                  R{\'{e}}gine Laleau and
                  Steve Reeves},
  title        = {Introducing Specification-Based Data Structure Repair Using Alloy},
  booktitle    = {Abstract State Machines, Alloy, {B} and Z, Second International Conference,
                  {ABZ} 2010, Orford, QC, Canada, February 22-25, 2010. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {5977},
  pages        = {398--399},
  publisher    = {Springer},
  year         = {2010},
  url          = {https://doi.org/10.1007/978-3-642-11811-1\_34},
  doi          = {10.1007/978-3-642-11811-1\_34},
  timestamp    = {Tue, 14 May 2019 10:00:50 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/ZaeemK10.bib},
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

