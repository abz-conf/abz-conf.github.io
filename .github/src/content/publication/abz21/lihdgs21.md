---
title: "Unbounded Barrier-Synchronized Concurrent ASMs for Effective MapReduce Processing on Streams"

authors:
  - Zilinghan Li
  - Shilan He
  - Yiqing Du
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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-030-77543-8_1.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-030-77543-8_1
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/lihdgs21/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/lihdgs21/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/lihdgs21/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/lihdgs21/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

MapReduce supports the processing of large data sets in parallel. It has been shown that MapReduce is an example for the use of the bulk synchronous parallel (BSP) bridging model, a model for parallel computation on a fixed set of processors comprising alternating computation and communication phases. In this article we extend the normal execution of MapReduce from processing large finite data sets to processing stream queries with input data stream assumed to continue indefinitely. We classify stream queries into three classes, memoryless, semi-memoryless and memorable, and provide the model for each class using MapReduce based on BSP. In addition, as some stream queries require large amounts of computing sources, the BSP computation model is extended to a model with unbounded many agents, but preserving the barrier synchronization. A behavioral theory is developed for this model extending the behavioral theory of the BSP model. This comprises an axiomatization, the definition of Infinite-Agent BSP abstract state machines (Inf-Ag-BSP-ASM) and the proof that such ASMs capture the unbounded synchronized computations. Finally, we show how MapReduce processing can be further improved on grounds of the unbounded extension.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-030-77543-8_1.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-030-77543-8_1.pdf" >}}

## Reference

```
% BibTex
@inproceedings{LiHDGS21,
  author       = {Zilinghan Li and
                  Shilan He and
                  Yiqing Du and
                  Sen{\'{e}}n Gonz{\'{a}}lez and
                  Klaus{-}Dieter Schewe},
  editor       = {Alexander Raschke and
                  Dominique M{\'{e}}ry},
  title        = {Unbounded Barrier-Synchronized Concurrent ASMs for Effective MapReduce
                  Processing on Streams},
  booktitle    = {Rigorous State-Based Methods - 8th International Conference, {ABZ}
                  2021, Ulm, Germany, June 9-11, 2021, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {12709},
  pages        = {3--16},
  publisher    = {Springer},
  year         = {2021},
  url          = {https://doi.org/10.1007/978-3-030-77543-8\_1},
  doi          = {10.1007/978-3-030-77543-8\_1},
  timestamp    = {Wed, 09 Jun 2021 12:14:31 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/LiHDGS21.bib},
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

