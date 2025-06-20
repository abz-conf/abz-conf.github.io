---
title: "Formal Specification of the Semantics of Control State Diagrams"

authors:
  - Markus Leitz
  - Alexander Raschke


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
#  11 = "pub_short_paper"
#  12 = "pub_long_paper"
#  13 = "pub_invited_talk"
publication_types:
  - 11   # default is 1 (conference), adjust as needed

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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-319-91271-4_26.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-319-91271-4_26
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/leitzr18/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/leitzr18/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/leitzr18/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/leitzr18/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Control State Diagrams (CSD) are a graphical representation of Control State Abstract State Machines, a subclass of Abstract State Machines (ASM). We extend the existing semi-formal specification of this diagram type by a concrete syntax and its formal semantics. The semantics is given by a translation approach that transforms combinations of nodes into ASM snippets which are inserted into a textual ASM. This node-by-node translation is not only the basis for a code generation tool, but it also allows users to capture the behavior of a CSD more easily.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-319-91271-4_26.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-319-91271-4_26.pdf" >}}

## Reference

```
% BibTex
@inproceedings{LeitzR18,
  author       = {Markus Leitz and
                  Alexander Raschke},
  editor       = {Michael J. Butler and
                  Alexander Raschke and
                  Thai Son Hoang and
                  Klaus Reichl},
  title        = {Formal Specification of the Semantics of Control State Diagrams},
  booktitle    = {Abstract State Machines, Alloy, B, TLA, VDM, and {Z} - 6th International
                  Conference, {ABZ} 2018, Southampton, UK, June 5-8, 2018, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {10817},
  pages        = {374--379},
  publisher    = {Springer},
  year         = {2018},
  url          = {https://doi.org/10.1007/978-3-319-91271-4\_26},
  doi          = {10.1007/978-3-319-91271-4\_26},
  timestamp    = {Tue, 14 May 2019 10:00:50 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/LeitzR18.bib},
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

