---
title: "Optimizing Alloy for Multi-objective Software Product Line Configuration"

authors:
  - Ed Zulkoski
  - Chris Kleynhans
  - Ming-Ho Yee
  - Derek Rayside
  - Krzysztof Czarnecki 0001


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-662-43652-3_34.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-662-43652-3_34
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/zulkoskikyrc14/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/zulkoskikyrc14/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/zulkoskikyrc14/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/zulkoskikyrc14/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Software product line (SPL) engineering involves the modeling, analysis, and configuration of variability-rich systems. We improve the performance of the multi-objective optimization of SPLs in Alloy by several orders of magnitude with two techniques. First, we rewrite the model to remove binary relations that map to integers, which enables removing most of the integer atoms from the universe. SPL models often require using large bitwidths, hence the number of integer atoms in the universe can be orders of magnitude more than the other atoms. In our approach, the tuples for these integer-valued relations are computed outside the sat solver before returning the solution to the user. Second, we add a checkpointing facility to Kodkod, which allows the multi-objective optimization algorithm to reuse previously computed internal sat solver state, after backtracking. Together these result in orders of magnitude improvement in using Alloy as a multi-objective optimization tool for software product lines.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-662-43652-3_34.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-662-43652-3_34.pdf" >}}

## Reference

```
% BibTex
@inproceedings{ZulkoskiKYRC14,
  author       = {Ed Zulkoski and
                  Chris Kleynhans and
                  Ming{-}Ho Yee and
                  Derek Rayside and
                  Krzysztof Czarnecki},
  editor       = {Yamine A{\"{\i}}t Ameur and
                  Klaus{-}Dieter Schewe},
  title        = {Optimizing Alloy for Multi-objective Software Product Line Configuration},
  booktitle    = {Abstract State Machines, Alloy, B, TLA, VDM, and {Z} - 4th International
                  Conference, {ABZ} 2014, Toulouse, France, June 2-6, 2014. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {8477},
  pages        = {328--333},
  publisher    = {Springer},
  year         = {2014},
  url          = {https://doi.org/10.1007/978-3-662-43652-3\_34},
  doi          = {10.1007/978-3-662-43652-3\_34},
  timestamp    = {Fri, 30 Dec 2022 23:08:53 +0100},
  biburl       = {https://dblp.org/rec/conf/asm/ZulkoskiKYRC14.bib},
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

