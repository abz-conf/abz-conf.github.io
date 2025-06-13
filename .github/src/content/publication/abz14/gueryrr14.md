---
title: "Fixed-Point Arithmetic Modeled in B Software Using Reals"

authors:
  - Jérôme Guéry
  - Olivier Rolland
  - Joris Rehm


date: 2014-01-01

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
  - 11  # default is 1 (conference), adjust as needed

publication: "4th International Conference on ASM, Alloy, B, TLA, VDM, and Z (ABZ'14)"
publication_short: "ABZ'14"

tags:
  - ABZ'14

categories: []

featured: false

# enable this for case studies
# projects:
#   - abz14

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-662-43652-3_28.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-662-43652-3_28
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/gueryrr14/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/gueryrr14/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/gueryrr14/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/gueryrr14/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

This paper demonstrates how to introduce a fixed point arithmetic in software developed with the classical B method. The properties of this arithmetic are specified with real numbers in the AtelierB formal tool and linked to an implementation written in Ada programming language. This study has been conducted to control the loss of precision and possible overflow due to the use of fixed point arithmetic in the critical software part of a communication based train control system.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-662-43652-3_28.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-662-43652-3_28.pdf" >}}

## Reference

```
% BibTex
@inproceedings{GueryRR14,
  author       = {J{\'{e}}r{\^{o}}me Gu{\'{e}}ry and
                  Olivier Rolland and
                  Joris Rehm},
  editor       = {Yamine A{\"{\i}}t Ameur and
                  Klaus{-}Dieter Schewe},
  title        = {Fixed-Point Arithmetic Modeled in {B} Software Using Reals},
  booktitle    = {Abstract State Machines, Alloy, B, TLA, VDM, and {Z} - 4th International
                  Conference, {ABZ} 2014, Toulouse, France, June 2-6, 2014. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {8477},
  pages        = {298--302},
  publisher    = {Springer},
  year         = {2014},
  url          = {https://doi.org/10.1007/978-3-662-43652-3\_28},
  doi          = {10.1007/978-3-662-43652-3\_28},
  timestamp    = {Tue, 14 May 2019 10:00:50 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/GueryRR14.bib},
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

