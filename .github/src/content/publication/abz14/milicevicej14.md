---
title: "αRby - An Embedding of Alloy in Ruby"

authors:
  - Aleksandar Milicevic
  - Ido Efrati
  - Daniel Jackson 0001


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
#  10 = "pub_short_paper"
#  11 = "pub_long_paper"
publication_types:
  - 1   # default is 1 (conference), adjust as needed

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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-662-43652-3_5.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-662-43652-3_5
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/milicevicej14/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/milicevicej14/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/milicevicej14/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/milicevicej14/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

We present αRby—an embedding of the Alloy language in Ruby—and demonstrate the benefits of having a declarative modeling language (backed by an automated solver) embedded in a traditional object-oriented imperative programming language. This approach aims to bring these two distinct paradigms (imperative and declarative) together in a novel way. We argue that having the other paradigm available within the same language is beneficial to both the modeling community of Alloy users and the object-oriented community of Ruby programmers. In this paper, we primarily focus on the benefits for the Alloy community, namely, how αRby provides elegant solutions to several well-known, outstanding problems: (1) mixed execution, (2) specifying partial instances, (3) staged model finding.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-662-43652-3_5.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-662-43652-3_5.pdf" >}}

## Reference

```
% BibTex
@inproceedings{MilicevicEJ14,
  author       = {Aleksandar Milicevic and
                  Ido Efrati and
                  Daniel Jackson},
  editor       = {Yamine A{\"{\i}}t Ameur and
                  Klaus{-}Dieter Schewe},
  title        = {{\(\alpha\)}Rby - An Embedding of Alloy in Ruby},
  booktitle    = {Abstract State Machines, Alloy, B, TLA, VDM, and {Z} - 4th International
                  Conference, {ABZ} 2014, Toulouse, France, June 2-6, 2014. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {8477},
  pages        = {56--71},
  publisher    = {Springer},
  year         = {2014},
  url          = {https://doi.org/10.1007/978-3-662-43652-3\_5},
  doi          = {10.1007/978-3-662-43652-3\_5},
  timestamp    = {Tue, 14 May 2019 10:00:50 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/MilicevicEJ14.bib},
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

