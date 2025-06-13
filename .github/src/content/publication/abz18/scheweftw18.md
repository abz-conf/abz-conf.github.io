---
title: "Distributed Adaptive Systems - Theory, Specification, Reasoning"

authors:
  - Klaus-Dieter Schewe
  - Flavio Ferrarotti
  - Loredana Tec
  - Qing Wang 0002


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-319-91271-4_2.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-319-91271-4_2
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/scheweftw18/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/scheweftw18/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/scheweftw18/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/scheweftw18/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

A distributed system can be characterised by autonomously acting agents, where each agent executes its own program, uses shared resources and communicates with the others, but otherwise is totally oblivious to the behaviour of the other agents. In a distributed adaptive system agents may change their programs, and enter or leave the collection at any time thereby changing the behaviour of the overall system. This article first develops a language-independent axiomatic definition of distributed adaptive systems and then presents concurrent reflective Abstract State Machines (crASMs), an abstract machine model for their specification. It can be proven that any distributed adaptive system as stipulated by the axiomatisation can be step-by-step simulated by a crASM. Proofs about crASMs can be grounded in a multiple-step logic, which extends known complete one-step logics for deterministic and non-deterministic ASMs.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-319-91271-4_2.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-319-91271-4_2.pdf" >}}

## Reference

```
% BibTex
@inproceedings{ScheweFTW18,
  author       = {Klaus{-}Dieter Schewe and
                  Flavio Ferrarotti and
                  Loredana Tec and
                  Qing Wang},
  editor       = {Michael J. Butler and
                  Alexander Raschke and
                  Thai Son Hoang and
                  Klaus Reichl},
  title        = {Distributed Adaptive Systems - Theory, Specification, Reasoning},
  booktitle    = {Abstract State Machines, Alloy, B, TLA, VDM, and {Z} - 6th International
                  Conference, {ABZ} 2018, Southampton, UK, June 5-8, 2018, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {10817},
  pages        = {16--30},
  publisher    = {Springer},
  year         = {2018},
  url          = {https://doi.org/10.1007/978-3-319-91271-4\_2},
  doi          = {10.1007/978-3-319-91271-4\_2},
  timestamp    = {Sun, 02 Oct 2022 15:55:03 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/ScheweFTW18.bib},
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

