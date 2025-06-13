---
title: "Systematic Generation of Non-equivalent Expressions for Relational Algebra"

authors:
  - Kaiyuan Wang
  - Allison Sullivan
  - Manos Koukoutos
  - Darko Marinov
  - Sarfraz Khurshid


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-319-91271-4_8.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-319-91271-4_8
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/wangskmk18/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/wangskmk18/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/wangskmk18/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/wangskmk18/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Relational algebra forms the semantic foundation in multiple domains, e.g., Alloy models, OCL constraints, UML metamodels, and SQL queries. Synthesis and repair techniques in such domains require an efficient procedure to generate (non-equivalent) expressions subject to relational constraints, e.g., the types of sets and relations, their cardinality, size of expressions, maximum arity of the intermediate expressions, etc. This paper introduces the first generator for relational expressions that are non-equivalent with respect to the semantics of relational algebra. We present the algorithms that define our generator, its embodiment based on the Alloy tool-set, and an experimental evaluation to show the effectiveness of its non-equivalent generation for a variety of problems with relational constraints.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-319-91271-4_8.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-319-91271-4_8.pdf" >}}

## Reference

```
% BibTex
@inproceedings{WangSKMK18,
  author       = {Kaiyuan Wang and
                  Allison Sullivan and
                  Manos Koukoutos and
                  Darko Marinov and
                  Sarfraz Khurshid},
  editor       = {Michael J. Butler and
                  Alexander Raschke and
                  Thai Son Hoang and
                  Klaus Reichl},
  title        = {Systematic Generation of Non-equivalent Expressions for Relational
                  Algebra},
  booktitle    = {Abstract State Machines, Alloy, B, TLA, VDM, and {Z} - 6th International
                  Conference, {ABZ} 2018, Southampton, UK, June 5-8, 2018, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {10817},
  pages        = {105--120},
  publisher    = {Springer},
  year         = {2018},
  url          = {https://doi.org/10.1007/978-3-319-91271-4\_8},
  doi          = {10.1007/978-3-319-91271-4\_8},
  timestamp    = {Thu, 14 Oct 2021 10:31:49 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/WangSKMK18.bib},
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

