---
title: "MAZE: An Extension of Object-Z for Multi-Agent Systems"

authors:
  - Graeme Smith 0001
  - Qin Li 0002


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-662-43652-3_6.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-662-43652-3_6
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/smithl14/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/smithl14/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/smithl14/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/smithl14/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

The formal development of multi-agent systems (MAS) may involve consideration of system functionality at three distinct levels of abstraction. The macro level focusses on the system’s overall, global behaviour, independently of how the agents of the system operate and interact. The meso level focusses on agent interactions, and the micro level on the operation of individual agents. While Object-Z with its high-level support for component-based specifications is well suited to modelling MAS at the macro and meso levels, it can become cumbersome at the micro level where the low-level mechanisms required for dealing with asynchronous communication between agents and timing constraints need to be explicitly defined. In this paper we introduce MAZE, an extension of Object-Z supporting (i) action refinement to facilitate the development process from the macro to micro level, and (ii) a number of syntactic conventions to facilitate micro-level specification. The syntactic conventions are shorthands for existing Object-Z notation and so require no redefinition of Object-Z’s semantics.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-662-43652-3_6.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-662-43652-3_6.pdf" >}}

## Reference

```
% BibTex
@inproceedings{SmithL14,
  author       = {Graeme Smith and
                  Qin Li},
  editor       = {Yamine A{\"{\i}}t Ameur and
                  Klaus{-}Dieter Schewe},
  title        = {{MAZE:} An Extension of Object-Z for Multi-Agent Systems},
  booktitle    = {Abstract State Machines, Alloy, B, TLA, VDM, and {Z} - 4th International
                  Conference, {ABZ} 2014, Toulouse, France, June 2-6, 2014. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {8477},
  pages        = {72--85},
  publisher    = {Springer},
  year         = {2014},
  url          = {https://doi.org/10.1007/978-3-662-43652-3\_6},
  doi          = {10.1007/978-3-662-43652-3\_6},
  timestamp    = {Thu, 07 Apr 2022 08:44:28 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/SmithL14.bib},
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

