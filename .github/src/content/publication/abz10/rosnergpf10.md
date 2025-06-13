---
title: "ParAlloy: Towards a Framework for Efficient Parallel Analysis of Alloy Models"

authors:
  - Nicolás Rosner
  - Juan P. Galeotti
  - Carlos López Pombo
  - Marcelo F. Frias


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_33.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-642-11811-1_33
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/rosnergpf10/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/rosnergpf10/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/rosnergpf10/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/rosnergpf10/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Alloy [Jac02a] is a widely adopted relational modeling language. Its appealing syntax and the support provided by the Alloy Analyzer [Jac02b] tool make model analysis accessible to a public of non-specialists. A model and property are translated to a propositional formula, which is fed to a SAT-solver to search for counterexamples. The translation strongly depends on user-provided bounds for data domains called scopes - the larger the scopes, the more confident the user is about the correctness of the model. Due to the intrinsic complexity of the SAT-solving step, it is often the case that analyses do not scale well enough to remain feasible as scopes grow.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_33.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_33.pdf" >}}

## Reference

```
% BibTex
@inproceedings{RosnerGPF10,
  author       = {Nicol{\'{a}}s Rosner and
                  Juan P. Galeotti and
                  Carlos L{\'{o}}pez Pombo and
                  Marcelo F. Frias},
  editor       = {Marc Frappier and
                  Uwe Gl{\"{a}}sser and
                  Sarfraz Khurshid and
                  R{\'{e}}gine Laleau and
                  Steve Reeves},
  title        = {ParAlloy: Towards a Framework for Efficient Parallel Analysis of Alloy
                  Models},
  booktitle    = {Abstract State Machines, Alloy, {B} and Z, Second International Conference,
                  {ABZ} 2010, Orford, QC, Canada, February 22-25, 2010. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {5977},
  pages        = {396--397},
  publisher    = {Springer},
  year         = {2010},
  url          = {https://doi.org/10.1007/978-3-642-11811-1\_33},
  doi          = {10.1007/978-3-642-11811-1\_33},
  timestamp    = {Mon, 03 Mar 2025 20:58:01 +0100},
  biburl       = {https://dblp.org/rec/conf/asm/RosnerGPF10.bib},
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

