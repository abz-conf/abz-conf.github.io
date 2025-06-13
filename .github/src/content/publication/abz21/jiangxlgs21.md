---
title: "Towards Refinement of Unbounded Parallelism in ASMs Using Concurrency and Reflection"

authors:
  - Fengqing Jiang
  - Neng Xiong
  - Xinyu Lian
  - Senén González
  - Klaus-Dieter Schewe


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
#  11 = "pub_short_paper"
#  12 = "pub_long_paper"
#  13 = "pub_invited_talk"
publication_types:
  - 11   # default is 1 (conference), adjust as needed

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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-030-77543-8_10.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-030-77543-8_10
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/jiangxlgs21/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/jiangxlgs21/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/jiangxlgs21/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/jiangxlgs21/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

The BSP bridging model can be exploited to support MapReduce processing. This article describes how this can be realised using a work-stealing approach, where an idle processor can autonomously grab a thread from a partially ordered pool of open threads and execute it. It is further outlined that this can be generalised for the refinement of an unboundedly parallel ASM by a concurrent, reflective BSP-ASM, i.e. the individual agents are associated with reflective ASMs, i.e. they can adapt their own program.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-030-77543-8_10.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-030-77543-8_10.pdf" >}}

## Reference

```
% BibTex
@inproceedings{JiangXLGS21,
  author       = {Fengqing Jiang and
                  Neng Xiong and
                  Xinyu Lian and
                  Sen{\'{e}}n Gonz{\'{a}}lez and
                  Klaus{-}Dieter Schewe},
  editor       = {Alexander Raschke and
                  Dominique M{\'{e}}ry},
  title        = {Towards Refinement of Unbounded Parallelism in ASMs Using Concurrency
                  and Reflection},
  booktitle    = {Rigorous State-Based Methods - 8th International Conference, {ABZ}
                  2021, Ulm, Germany, June 9-11, 2021, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {12709},
  pages        = {118--123},
  publisher    = {Springer},
  year         = {2021},
  url          = {https://doi.org/10.1007/978-3-030-77543-8\_10},
  doi          = {10.1007/978-3-030-77543-8\_10},
  timestamp    = {Wed, 09 Jun 2021 12:14:31 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/JiangXLGS21.bib},
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

