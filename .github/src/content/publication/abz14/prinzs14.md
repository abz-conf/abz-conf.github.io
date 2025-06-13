---
title: "Distributed ASM - Pitfalls and Solutions"

authors:
  - Andreas Prinz 0001
  - Edel Sherratt


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
#  11 = "pub_short_paper"
#  12 = "pub_long_paper"
#  13 = "pub_invited_talk"
publication_types:
  - 11  # default is 1 (conference), adjust as needed

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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-662-43652-3_18.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-662-43652-3_18
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/prinzs14/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/prinzs14/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/prinzs14/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/prinzs14/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

While sequential Abstract State Machines (ASM) capture the essence of sequential computation, it is not clear that this is true of distributed ASM. This paper looks at two kinds of distributed process, one based on a global state and one based on variable access. Their commonalities are extracted and conclusions for the general understanding of distributed computation are drawn, providing integration between global state and variable access.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-662-43652-3_18.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-662-43652-3_18.pdf" >}}

## Reference

```
% BibTex
@inproceedings{PrinzS14,
  author       = {Andreas Prinz and
                  Edel Sherratt},
  editor       = {Yamine A{\"{\i}}t Ameur and
                  Klaus{-}Dieter Schewe},
  title        = {Distributed {ASM} - Pitfalls and Solutions},
  booktitle    = {Abstract State Machines, Alloy, B, TLA, VDM, and {Z} - 4th International
                  Conference, {ABZ} 2014, Toulouse, France, June 2-6, 2014. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {8477},
  pages        = {210--215},
  publisher    = {Springer},
  year         = {2014},
  url          = {https://doi.org/10.1007/978-3-662-43652-3\_18},
  doi          = {10.1007/978-3-662-43652-3\_18},
  timestamp    = {Sat, 30 Sep 2023 09:34:45 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/PrinzS14.bib},
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

