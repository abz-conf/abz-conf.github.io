---
title: "Refactoring Abstract State Machine Models"

authors:
  - Hamed Yaghoubi Shahir
  - Roozbeh Farahbod
  - Uwe Glässer


date: 2012-01-01

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


publication: "3rd International Conference on ASM, Alloy, B, VDM, and Z (ABZ'12)"
publication_short: "ABZ'12"

tags:
  - ABZ'12

categories: []

featured: false

# enable this for case studies
# projects:
#   - abz12

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-642-30885-7_28.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-642-30885-7_28
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/shahirfg12/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/shahirfg12/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/shahirfg12/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/shahirfg12/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

The Abstract State Machine (ASM) method proposes the concept of ground models for analyzing a target system based on pseudo-code-like descriptions for reasoning about system properties in terms of state machine runs over abstract data structures. This highly iterative process builds on stepwise refinement of ground models that evolve with progressing understanding of functional system requirements. Usually, as complexity increases, reorganization of a model’s internal structure helps enhance its flexibility and robustness. While this approach is common practice, the underlying principles are usually left implicit. In this paper, we propose refactoring patterns to restructure abstract machine models with the goal of improving their intelligibility and maintainability.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-642-30885-7_28.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-642-30885-7_28.pdf" >}}

## Reference

```
% BibTex
@inproceedings{ShahirFG12,
  author       = {Hamed Yaghoubi Shahir and
                  Roozbeh Farahbod and
                  Uwe Gl{\"{a}}sser},
  editor       = {John Derrick and
                  John S. Fitzgerald and
                  Stefania Gnesi and
                  Sarfraz Khurshid and
                  Michael Leuschel and
                  Steve Reeves and
                  Elvinia Riccobene},
  title        = {Refactoring Abstract State Machine Models},
  booktitle    = {Abstract State Machines, Alloy, B, VDM, and {Z} - Third International
                  Conference, {ABZ} 2012, Pisa, Italy, June 18-21, 2012. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {7316},
  pages        = {345--348},
  publisher    = {Springer},
  year         = {2012},
  url          = {https://doi.org/10.1007/978-3-642-30885-7\_28},
  doi          = {10.1007/978-3-642-30885-7\_28},
  timestamp    = {Sun, 02 Jun 2019 21:23:59 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/ShahirFG12.bib},
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

