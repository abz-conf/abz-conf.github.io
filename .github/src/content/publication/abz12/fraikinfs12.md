---
title: "Modeling the Supervisory Control Theory with Alloy"

authors:
  - Benoît Fraikin
  - Marc Frappier
  - Richard St-Denis


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-642-30885-7_7.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-642-30885-7_7
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/fraikinfs12/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/fraikinfs12/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/fraikinfs12/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/fraikinfs12/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Scientific literature reveals that symbolic representation techniques behind some formal methods are attractive to synthesize parts or verify properties of large discrete event systems. They involve, however, complex encoding schemata and fine tuning heuristic parameters in order to translate specific problems into efficient BDD or SAT-based representations. This approach may be too costly when the main goal is to explore a theory, understand by simulation its underlying concepts and computation procedures, and conduct experiments by applying them to small problems. Based on previous work with Alloy on the synthesis of observers and nonblocking supervisors of a system organized hierarchically with a flat state space estimated to 1031 states, this paper investigates more deeply issues raised with its use in the modeling and prototyping of the supervisory control theory, including the application of models to practical problems. This study was conducted in a broader context than just hierarchical control since it embraces various variants of this theory.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-642-30885-7_7.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-642-30885-7_7.pdf" >}}

## Reference

```
% BibTex
@inproceedings{FraikinFS12,
  author       = {Beno{\^{\i}}t Fraikin and
                  Marc Frappier and
                  Richard St{-}Denis},
  editor       = {John Derrick and
                  John S. Fitzgerald and
                  Stefania Gnesi and
                  Sarfraz Khurshid and
                  Michael Leuschel and
                  Steve Reeves and
                  Elvinia Riccobene},
  title        = {Modeling the Supervisory Control Theory with Alloy},
  booktitle    = {Abstract State Machines, Alloy, B, VDM, and {Z} - Third International
                  Conference, {ABZ} 2012, Pisa, Italy, June 18-21, 2012. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {7316},
  pages        = {94--107},
  publisher    = {Springer},
  year         = {2012},
  url          = {https://doi.org/10.1007/978-3-642-30885-7\_7},
  doi          = {10.1007/978-3-642-30885-7\_7},
  timestamp    = {Sun, 02 Oct 2022 15:55:03 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/FraikinFS12.bib},
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

