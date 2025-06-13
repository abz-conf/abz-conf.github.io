---
title: "ASM and Controller Synthesis"

authors:
  - Richard Banach
  - Huibiao Zhu
  - Wen Su
  - Xiaofeng Wu


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-642-30885-7_4.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-642-30885-7_4
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/banachzsw12/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/banachzsw12/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/banachzsw12/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/banachzsw12/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

While many systems are naturally viewed as the interaction between a controller subsystem and a controlled, or plant subsystem, they are often most easily understood and designed monolithically. A practical implementation needs to separate controller from plant. We study the problem of when a monolithic ASM system can be split into controller and plant subsystems along syntactic lines derived from variables’ natural affiliations. We give restrictions that enable the split to be carried out cleanly, and we give conditions that ensure that the resulting pair of controller and plant subsystems have the same behaviours as the original design. We illustrate the theory with a case study concerning eating with chopsticks. This leads to an extension of controller synthesis for continuous ASM systems, which are briefly covered. The case study is then extended into the continuous sphere.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-642-30885-7_4.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-642-30885-7_4.pdf" >}}

## Reference

```
% BibTex
@inproceedings{BanachZSW12,
  author       = {Richard Banach and
                  Huibiao Zhu and
                  Wen Su and
                  Xiaofeng Wu},
  editor       = {John Derrick and
                  John S. Fitzgerald and
                  Stefania Gnesi and
                  Sarfraz Khurshid and
                  Michael Leuschel and
                  Steve Reeves and
                  Elvinia Riccobene},
  title        = {{ASM} and Controller Synthesis},
  booktitle    = {Abstract State Machines, Alloy, B, VDM, and {Z} - Third International
                  Conference, {ABZ} 2012, Pisa, Italy, June 18-21, 2012. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {7316},
  pages        = {51--64},
  publisher    = {Springer},
  year         = {2012},
  url          = {https://doi.org/10.1007/978-3-642-30885-7\_4},
  doi          = {10.1007/978-3-642-30885-7\_4},
  timestamp    = {Mon, 03 Mar 2025 20:58:01 +0100},
  biburl       = {https://dblp.org/rec/conf/asm/BanachZSW12.bib},
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

