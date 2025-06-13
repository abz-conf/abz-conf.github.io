---
title: "Preventing Arithmetic Overflows in Alloy"

authors:
  - Aleksandar Milicevic
  - Daniel Jackson 0001


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
#  10 = "pub_short_paper"
#  11 = "pub_long_paper"
publication_types:
  - 1   # default is 1 (conference), adjust as needed

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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-642-30885-7_8.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-642-30885-7_8
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/milicevicj12/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/milicevicj12/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/milicevicj12/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/milicevicj12/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

In a bounded analysis, arithmetic operators become partial, and a different semantics becomes necessary. One approach, mimicking programming languages, is for overflow to result in wrap-around. Although easy to implement, wrap-around produces unexpected counterexamples that do not correspond to cases that would arise in the unbounded setting. This paper describes a new approach, implemented in the latest version of the Alloy Analyzer, in which instances that would involve overflow are suppressed, and consequently, spurious counterexamples are eliminated. The key idea is to interpret quantifiers so that bound variables range only over values that do not cause overflow.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-642-30885-7_8.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-642-30885-7_8.pdf" >}}

## Reference

```
% BibTex
@inproceedings{MilicevicJ12,
  author       = {Aleksandar Milicevic and
                  Daniel Jackson},
  editor       = {John Derrick and
                  John S. Fitzgerald and
                  Stefania Gnesi and
                  Sarfraz Khurshid and
                  Michael Leuschel and
                  Steve Reeves and
                  Elvinia Riccobene},
  title        = {Preventing Arithmetic Overflows in Alloy},
  booktitle    = {Abstract State Machines, Alloy, B, VDM, and {Z} - Third International
                  Conference, {ABZ} 2012, Pisa, Italy, June 18-21, 2012. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {7316},
  pages        = {108--121},
  publisher    = {Springer},
  year         = {2012},
  url          = {https://doi.org/10.1007/978-3-642-30885-7\_8},
  doi          = {10.1007/978-3-642-30885-7\_8},
  timestamp    = {Sun, 02 Jun 2019 21:23:59 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/MilicevicJ12.bib},
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

