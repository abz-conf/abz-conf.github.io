---
title: "Complex Hardware Modules Can Now be Made Free of Functional Errors without Sacrificing Productivity"

authors:
  - Wolfram Büttner


date: 2008-01-01

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
  - 13   # default is 1 (conference), adjust as needed

publication: "1st International Conference on ASM, B, and Z (ABZ'08)"
publication_short: "ABZ'08"

tags:
  - ABZ'08

categories: []

featured: false

# enable this for case studies
# projects:
#   - abz08

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_1.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-540-87603-8_1
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/buttner08/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/buttner08/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/buttner08/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/buttner08/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Complementary to the systems and software focus of the conference, this presentation will be about chips and the progress that has been made in their functional verification. Common ground will be high-level, still cycleaccurate, state-based models of hardware functionalities called Abstract RT. RT stands for register transfer descriptions of hardware such as VHDL or Verilog. An Abstract RT model is a formal specification which permits an automated formal comparison with its implementation, thus detecting any functional discrepancy between code and formal specification. The first part of the presentation will sketch the big picture: Moore‘s Law still holds and permits building huge chips comprising up to hundreds of millions of gates. Under the constraints of shrinking budgets and development times, these so-called systems-on-chip (SoC) can no longer be developed from scratch but must largely be assembled from pre-designed, pre-verified design components such as processors, controllers, a plethora of peripherals and large amounts of memories. Therefore, getting a SoC right depends to a large extent on the quality of these design components - IP for short. At stake are critical errors making it into silicon. These may cost millions of Euros due to delayed market entry, additional engineering and re-production efforts. Hence, the lion’s share of today’s verification efforts goes into the functional verification of such IP.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_1.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_1.pdf" >}}

## Reference

```
% BibTex
@inproceedings{Buttner08,
  author       = {Wolfram B{\"{u}}ttner},
  editor       = {Egon B{\"{o}}rger and
                  Michael J. Butler and
                  Jonathan P. Bowen and
                  Paul Boca},
  title        = {Complex Hardware Modules Can Now be Made Free of Functional Errors
                  without Sacrificing Productivity},
  booktitle    = {Abstract State Machines, {B} and Z, First International Conference,
                  {ABZ} 2008, London, UK, September 16-18, 2008. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {5238},
  pages        = {1--3},
  publisher    = {Springer},
  year         = {2008},
  url          = {https://doi.org/10.1007/978-3-540-87603-8\_1},
  doi          = {10.1007/978-3-540-87603-8\_1},
  timestamp    = {Tue, 14 May 2019 10:00:50 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/Buttner08.bib},
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

