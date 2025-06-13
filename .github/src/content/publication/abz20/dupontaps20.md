---
title: "Formally Verified Architecture Patterns of Hybrid Systems Using Proof and Refinement with Event-B"

authors:
  - Guillaume Dupont
  - Yamine Aït Ameur
  - Marc Pantel
  - Neeraj Kumar Singh 0001


date: 2020-01-01

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

publication: "7th International Conference on Rigorous State Based Methods (ABZ'20)"
publication_short: "ABZ'20"

tags:
  - ABZ'20

categories: []

featured: false

# enable this for case studies
# projects:
#   - abz20

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-030-48077-6_12.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-030-48077-6_12
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/dupontaps20/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/dupontaps20/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/dupontaps20/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/dupontaps20/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Cyber-Physical Systems (CPS) play a central role in modern days technology. From simple thermostat controllers to more advanced autonomous cars, their versatility makes them perfect candidates for many applications, in particular for safety critical ones. Thus, their certification is a key issue and formal methods are good candidates to assess safety and produce associated certificates. Hybrid systems show continuous-time dynamics depending on mode that is required in several stages of the architecture of Cyber-Physical Systems. Our work addresses the problem of formally verifying hybrid systems using refinement and proof with Event-B. Our previous work [14] presented formally verified generic architecture patterns for designing centralised hybrid systems, based on our generic approach [15]. We extend this work and give a formally verified architecture pattern aimed at modelling distributed hybrid systems, featuring multiple plants and multiple controllers. We validate the approach and illustrate the use of the defined pattern on an extension of a very common case study, borrowed from literature.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-030-48077-6_12.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-030-48077-6_12.pdf" >}}

## Reference

```
% BibTex
@inproceedings{DupontAPS20,
  author       = {Guillaume Dupont and
                  Yamine A{\"{\i}}t Ameur and
                  Marc Pantel and
                  Neeraj Kumar Singh},
  editor       = {Alexander Raschke and
                  Dominique M{\'{e}}ry and
                  Frank Houdek},
  title        = {Formally Verified Architecture Patterns of Hybrid Systems Using Proof
                  and Refinement with Event-B},
  booktitle    = {Rigorous State-Based Methods - 7th International Conference, {ABZ}
                  2020, Ulm, Germany, May 27-29, 2020, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {12071},
  pages        = {169--185},
  publisher    = {Springer},
  year         = {2020},
  url          = {https://doi.org/10.1007/978-3-030-48077-6\_12},
  doi          = {10.1007/978-3-030-48077-6\_12},
  timestamp    = {Thu, 10 Nov 2022 08:55:26 +0100},
  biburl       = {https://dblp.org/rec/conf/asm/DupontAPS20.bib},
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

