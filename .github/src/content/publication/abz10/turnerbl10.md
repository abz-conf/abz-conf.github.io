---
title: "A Refinement-Based Correctness Proof of Symmetry Reduced Model Checking"

authors:
  - Edd Turner
  - Michael J. Butler
  - Michael Leuschel


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_18.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-642-11811-1_18
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/turnerbl10/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/turnerbl10/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/turnerbl10/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/turnerbl10/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Symmetry reduction is a model checking technique that can help alleviate the problem of state space explosion, by preventing redundant state space exploration. In previous work, we have developed three effective approaches to symmetry reduction for B that have been implemented into the ProB model checker, and we have proved the soundness of our state symmetries. However, it is also important to show our techniques are sound with respect to standard model checking, at the algorithmic level. In this paper, we present a retrospective B development that addresses this issue through a series of B refinements. This work also demonstrates the valuable insights into a system that can be gained through formal modelling.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_18.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_18.pdf" >}}

## Reference

```
% BibTex
@inproceedings{TurnerBL10,
  author       = {Edd Turner and
                  Michael J. Butler and
                  Michael Leuschel},
  editor       = {Marc Frappier and
                  Uwe Gl{\"{a}}sser and
                  Sarfraz Khurshid and
                  R{\'{e}}gine Laleau and
                  Steve Reeves},
  title        = {A Refinement-Based Correctness Proof of Symmetry Reduced Model Checking},
  booktitle    = {Abstract State Machines, Alloy, {B} and Z, Second International Conference,
                  {ABZ} 2010, Orford, QC, Canada, February 22-25, 2010. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {5977},
  pages        = {231--244},
  publisher    = {Springer},
  year         = {2010},
  url          = {https://doi.org/10.1007/978-3-642-11811-1\_18},
  doi          = {10.1007/978-3-642-11811-1\_18},
  timestamp    = {Sun, 02 Jun 2019 21:23:59 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/TurnerBL10.bib},
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

