---
title: "Proof-Based Approach to Hybrid Systems Development: Dynamic Logic and Event-B"

authors:
  - Guillaume Dupont
  - Yamine Aït Ameur
  - Marc Pantel
  - Neeraj Kumar Singh 0001


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-319-91271-4_11.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-319-91271-4_11
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/dupontaps18/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/dupontaps18/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/dupontaps18/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/dupontaps18/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

The design of hybrid systems controllers requires one to handle both discrete and continuous functionalities in a single development framework. In this paper, we propose the design and verification of such controllers using a correct-by-construction approach. We use proof-based formal methods to model and verify the required safety properties of the given controllers. Both Event-B with Rodin, and hybrid programs and dynamic differential logic with KeYmaera are experimented on a common case study related to the modelling of a car controller. Finally, we discuss the lessons learnt from these experiments and draw the first steps towards a generic method for modelling hybrid systems in Event-B.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-319-91271-4_11.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-319-91271-4_11.pdf" >}}

## Reference

```
% BibTex
@inproceedings{DupontAPS18,
  author       = {Guillaume Dupont and
                  Yamine A{\"{\i}}t Ameur and
                  Marc Pantel and
                  Neeraj Kumar Singh},
  editor       = {Michael J. Butler and
                  Alexander Raschke and
                  Thai Son Hoang and
                  Klaus Reichl},
  title        = {Proof-Based Approach to Hybrid Systems Development: Dynamic Logic
                  and Event-B},
  booktitle    = {Abstract State Machines, Alloy, B, TLA, VDM, and {Z} - 6th International
                  Conference, {ABZ} 2018, Southampton, UK, June 5-8, 2018, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {10817},
  pages        = {155--170},
  publisher    = {Springer},
  year         = {2018},
  url          = {https://doi.org/10.1007/978-3-319-91271-4\_11},
  doi          = {10.1007/978-3-319-91271-4\_11},
  timestamp    = {Thu, 10 Nov 2022 08:55:26 +0100},
  biburl       = {https://dblp.org/rec/conf/asm/DupontAPS18.bib},
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

