---
title: "Solver-Based Sketching of Alloy Models Using Test Valuations"

authors:
  - Kaiyuan Wang
  - Allison Sullivan
  - Darko Marinov
  - Sarfraz Khurshid


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-319-91271-4_9.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-319-91271-4_9
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/wangsmk18/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/wangsmk18/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/wangsmk18/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/wangsmk18/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

We introduce ASketch, the first framework for sketching models in the Alloy language. The Alloy Analyzer is a SAT-based constraint solver that allows users to create valuations for relations with respect to given constraints and bound on the universe of discourse. Alloy users routinely use the valuations to validate their models: enumerate some valuations and inspect them to detect underconstraints or overconstraints. Our key insight is that valid and invalid valuations enable sketching Alloy models where the user writes a partial model with holes and provides some valuations, and the sketching infrastructure completes the model by synthesizing Alloy fragments for the holes. ASketch offers the following extensions to Alloy: (1) it expands the Alloy grammar, allowing users to write holes in an Alloy model; (2) it can parse regular expressions and automatically generate pools of matching fragments to replace the holes; (3) it includes a solver-based technique that encodes the model with holes, the fragments for each hole, and the expected valuations to a meta-model which completes the holes when solved. Experimental results show that ASketch works well for different Alloy models with various number of holes, providing a promising approach to bring the success of traditional program sketching for imperative and functional programs to declarative, relational logic.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-319-91271-4_9.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-319-91271-4_9.pdf" >}}

## Reference

```
% BibTex
@inproceedings{WangSMK18,
  author       = {Kaiyuan Wang and
                  Allison Sullivan and
                  Darko Marinov and
                  Sarfraz Khurshid},
  editor       = {Michael J. Butler and
                  Alexander Raschke and
                  Thai Son Hoang and
                  Klaus Reichl},
  title        = {Solver-Based Sketching of Alloy Models Using Test Valuations},
  booktitle    = {Abstract State Machines, Alloy, B, TLA, VDM, and {Z} - 6th International
                  Conference, {ABZ} 2018, Southampton, UK, June 5-8, 2018, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {10817},
  pages        = {121--136},
  publisher    = {Springer},
  year         = {2018},
  url          = {https://doi.org/10.1007/978-3-319-91271-4\_9},
  doi          = {10.1007/978-3-319-91271-4\_9},
  timestamp    = {Thu, 14 Oct 2021 10:31:49 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/WangSMK18.bib},
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

