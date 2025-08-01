---
title: "Refinement of Timing Constraints for Concurrent Tasks with Scheduling"

authors:
  - Chenyang Zhu 0001
  - Michael J. Butler
  - Corina Cîrstea


date: 2018-01-01

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

publication: "6th International Conference on ASM, Alloy, B, TLA, VDM, and Z (ABZ'18)"
publication_short: "ABZ'18"

tags:
  - ABZ'18

categories: []

featured: false

# enable this for case studies
# projects:
#   - abz18

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-319-91271-4_15.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-319-91271-4_15
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/zhubc18/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/zhubc18/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/zhubc18/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/zhubc18/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Event-B is a refinement-based formal method that is used for system-level modeling and analysis of concurrent and distributed systems. Work has been done to extend Event-B with discrete time constraints. However the previous work does not capture the communication and competition between concurrent processes. In this paper, we distinguish task-based timing properties with scheduler-based timing properties from the perspective of different system design phases. To refine task-based timing properties with scheduler-based timing properties based on existing trigger-response patterns, we introduce a nondeterministic queue based scheduling framework to schedule processes under concurrent circumstances, which addresses the problems of refining deadline constraint under concurrent situations. Additional gluing invariants are provided to this refinement. To demonstrate the usability of the framework, we provide approaches to refine this framework with FIFO scheduling policy as well as deferrable priority based scheduling policy with aging technique. We demonstrate our framework and refinement with a timed mutual exclusion case study. The model is proved using the Rodin tool.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-319-91271-4_15.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-319-91271-4_15.pdf" >}}

## Reference

```
% BibTex
@inproceedings{ZhuBC18,
  author       = {Chenyang Zhu and
                  Michael J. Butler and
                  Corina C{\^{\i}}rstea},
  editor       = {Michael J. Butler and
                  Alexander Raschke and
                  Thai Son Hoang and
                  Klaus Reichl},
  title        = {Refinement of Timing Constraints for Concurrent Tasks with Scheduling},
  booktitle    = {Abstract State Machines, Alloy, B, TLA, VDM, and {Z} - 6th International
                  Conference, {ABZ} 2018, Southampton, UK, June 5-8, 2018, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {10817},
  pages        = {219--233},
  publisher    = {Springer},
  year         = {2018},
  url          = {https://doi.org/10.1007/978-3-319-91271-4\_15},
  doi          = {10.1007/978-3-319-91271-4\_15},
  timestamp    = {Wed, 14 Aug 2019 12:01:55 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/ZhuBC18.bib},
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

