---
title: "Communication Systems in ClawZ"

authors:
  - Michael Vernon
  - Frank Zeyda
  - Ana Cavalcanti 0001


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_25.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-642-11811-1_25
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/vernonzc10/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/vernonzc10/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/vernonzc10/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/vernonzc10/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

We investigate the use of ClawZ, a suite of tools for the verification of implementations of control laws, to construct formal models for control systems in the area of communications and signal-processing intensive applications. Whereas ClawZ has been successfully applied to verify control components in avionic systems, special requirements need to be identified and addressed to extend its use to the aforementioned application domain. This gives rise to several extensions, which we explain and subsequently validate by constructing the Z model of a software-defined radio communication device. The experience reported provides insight into general issues surrounding the use and extension of ClawZ.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_25.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_25.pdf" >}}

## Reference

```
% BibTex
@inproceedings{VernonZC10,
  author       = {Michael Vernon and
                  Frank Zeyda and
                  Ana Cavalcanti},
  editor       = {Marc Frappier and
                  Uwe Gl{\"{a}}sser and
                  Sarfraz Khurshid and
                  R{\'{e}}gine Laleau and
                  Steve Reeves},
  title        = {Communication Systems in ClawZ},
  booktitle    = {Abstract State Machines, Alloy, {B} and Z, Second International Conference,
                  {ABZ} 2010, Orford, QC, Canada, February 22-25, 2010. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {5977},
  pages        = {334--348},
  publisher    = {Springer},
  year         = {2010},
  url          = {https://doi.org/10.1007/978-3-642-11811-1\_25},
  doi          = {10.1007/978-3-642-11811-1\_25},
  timestamp    = {Mon, 05 Feb 2024 20:35:41 +0100},
  biburl       = {https://dblp.org/rec/conf/asm/VernonZC10.bib},
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

