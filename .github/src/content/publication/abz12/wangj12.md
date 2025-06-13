---
title: "Active Attacking Multicast Key Management Protocol Using Alloy"

authors:
  - Ting Wang
  - Dongyao Ji


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-642-30885-7_12.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-642-30885-7_12
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/wangj12/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/wangj12/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/wangj12/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/wangj12/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

In this paper, we use Alloy Analyzer, a fully automatic checker, to detect vulnerabilities in the multicast key management protocol proposed by Tanaka and Sato, and discover some previously unknown attacks. We model an active intruder in Alloy, and use Alloy Analyzer to test whether the active intruder can successfully attack the protocol. In this analysis, we check four critical properties that should be satisfied by any secure multicast protocol. However, none of these properties are satisfied. The protocol cannot resist the active intruder. Two unknown flaws caused by the active intruder are disclosed, and another two flaws found by CORAL are identified.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-642-30885-7_12.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-642-30885-7_12.pdf" >}}

## Reference

```
% BibTex
@inproceedings{WangJ12,
  author       = {Ting Wang and
                  Dongyao Ji},
  editor       = {John Derrick and
                  John S. Fitzgerald and
                  Stefania Gnesi and
                  Sarfraz Khurshid and
                  Michael Leuschel and
                  Steve Reeves and
                  Elvinia Riccobene},
  title        = {Active Attacking Multicast Key Management Protocol Using Alloy},
  booktitle    = {Abstract State Machines, Alloy, B, VDM, and {Z} - Third International
                  Conference, {ABZ} 2012, Pisa, Italy, June 18-21, 2012. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {7316},
  pages        = {164--177},
  publisher    = {Springer},
  year         = {2012},
  url          = {https://doi.org/10.1007/978-3-642-30885-7\_12},
  doi          = {10.1007/978-3-642-30885-7\_12},
  timestamp    = {Sun, 02 Jun 2019 21:23:59 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/WangJ12.bib},
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

