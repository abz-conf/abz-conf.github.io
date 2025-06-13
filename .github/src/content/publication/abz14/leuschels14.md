---
title: "Towards B as a High-Level Constraint Modelling Language - Solving the Jobs Puzzle Challenge"

authors:
  - Michael Leuschel
  - David Schneider 0001


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-662-43652-3_8.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-662-43652-3_8
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/leuschels14/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/leuschels14/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/leuschels14/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/leuschels14/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

We argue that B is a good language to conveniently express a wide range of constraint satisfaction problems. We also show that some problems can be solved quite effectively by the ProB tool. We illustrate our claim on several examples, such as the jobs puzzle - for which we solve the challenge set out by Shapiro. Here we show that the B formalization is both very close to the natural language specification and can still be solved efficiently by ProB. Our approach is particularly interesting when a high assurance of correctness is required. Indeed, compared to other existing approaches and tools, validation and double checking of solutions is available for ProB and formal proof can be applied to establish important properties or provide an unambiguous semantics to the problem specification.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-662-43652-3_8.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-662-43652-3_8.pdf" >}}

## Reference

```
% BibTex
@inproceedings{LeuschelS14,
  author       = {Michael Leuschel and
                  David Schneider},
  editor       = {Yamine A{\"{\i}}t Ameur and
                  Klaus{-}Dieter Schewe},
  title        = {Towards {B} as a High-Level Constraint Modelling Language - Solving
                  the Jobs Puzzle Challenge},
  booktitle    = {Abstract State Machines, Alloy, B, TLA, VDM, and {Z} - 4th International
                  Conference, {ABZ} 2014, Toulouse, France, June 2-6, 2014. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {8477},
  pages        = {101--116},
  publisher    = {Springer},
  year         = {2014},
  url          = {https://doi.org/10.1007/978-3-662-43652-3\_8},
  doi          = {10.1007/978-3-662-43652-3\_8},
  timestamp    = {Tue, 14 May 2019 10:00:50 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/LeuschelS14.bib},
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

