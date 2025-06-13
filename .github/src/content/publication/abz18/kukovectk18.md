---
title: "Extracting Symbolic Transitions from TLA+ Specifications"

authors:
  - Jure Kukovec
  - Thanh-Hai Tran 0002
  - Igor Konnov 0001


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-319-91271-4_7.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-319-91271-4_7
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/kukovectk18/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/kukovectk18/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/kukovectk18/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/kukovectk18/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

In \(\textsc {TLA}^{+}\), a system specification is written as a logical formula that restricts the system behavior. As a logic, \(\textsc {TLA}^{+}\) does not have assignments and other imperative statements that are used by model checkers to compute the successor states of a system state. Model checkers compute successors either explicitly — by evaluating program statements — or symbolically — by translating program statements to an SMT formula and checking its satisfiability. To efficiently enumerate the successors, TLA’s model checker TLC introduces side effects. For instance, an equality \(x' = e\) is interpreted as an assignment of e to the yet unbound variable x. Inspired by TLC, we introduce an automatic technique for discovering expressions in \(\textsc {TLA}^{+}\) formulas such as \(x' = e\) and \(x' \in \{e_1, \dots , e_k\}\) that can be provably used as assignments. In contrast to TLC, our technique does not explicitly evaluate expressions, but it reduces the problem of finding assignments to the satisfiability of an SMT formula. Hence, we give a way to slice a \(\textsc {TLA}^{+}\) formula in symbolic transitions, which can be used as an input to a symbolic model checker. Our prototype implementation successfully extracts symbolic transitions from a few \(\textsc {TLA}^{+}\) benchmarks.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-319-91271-4_7.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-319-91271-4_7.pdf" >}}

## Reference

```
% BibTex
@inproceedings{KukovecTK18,
  author       = {Jure Kukovec and
                  Thanh{-}Hai Tran and
                  Igor Konnov},
  editor       = {Michael J. Butler and
                  Alexander Raschke and
                  Thai Son Hoang and
                  Klaus Reichl},
  title        = {Extracting Symbolic Transitions from TLA\({}^{\mbox{+}}\) Specifications},
  booktitle    = {Abstract State Machines, Alloy, B, TLA, VDM, and {Z} - 6th International
                  Conference, {ABZ} 2018, Southampton, UK, June 5-8, 2018, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {10817},
  pages        = {89--104},
  publisher    = {Springer},
  year         = {2018},
  url          = {https://doi.org/10.1007/978-3-319-91271-4\_7},
  doi          = {10.1007/978-3-319-91271-4\_7},
  timestamp    = {Thu, 18 Nov 2021 13:33:08 +0100},
  biburl       = {https://dblp.org/rec/conf/asm/KukovecTK18.bib},
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

