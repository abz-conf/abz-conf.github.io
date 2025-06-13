---
title: "Using B and ProB for Data Validation Projects"

authors:
  - Dominik Hansen
  - David Schneider 0001
  - Michael Leuschel


date: 2016-01-01

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

publication: "5th International Conference on ASM, Alloy, B, TLA, VDM, and Z (ABZ'16)"
publication_short: "ABZ'16"

tags:
  - ABZ'16

categories: []

featured: false

# enable this for case studies
# projects:
#   - abz16

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-319-33600-8_10.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-319-33600-8_10
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/hansensl16/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/hansensl16/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/hansensl16/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/hansensl16/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Constraint satisfaction and data validation problems can be expressed very elegantly in state-based formal methods such as B. However, is B suited for developing larger applications and are there existing tools that scale for these projects? In this paper, we present our experiences on two real-world data validation projects from different domains which are based on the B language and use ProB as the central validation tool. The first project is the validation of university timetables, and the second project is the validation of railway topologies. Based on these two projects, we present a general structure of a data validation project in B and outline common challenges along with various solutions. We also discuss possible evolutions of the B language to make it (even) more suitable for such projects.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-319-33600-8_10.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-319-33600-8_10.pdf" >}}

## Reference

```
% BibTex
@inproceedings{HansenSL16,
  author       = {Dominik Hansen and
                  David Schneider and
                  Michael Leuschel},
  editor       = {Michael J. Butler and
                  Klaus{-}Dieter Schewe and
                  Atif Mashkoor and
                  Mikl{\'{o}}s Bir{\'{o}}},
  title        = {Using {B} and ProB for Data Validation Projects},
  booktitle    = {Abstract State Machines, Alloy, B, TLA, VDM, and {Z} - 5th International
                  Conference, {ABZ} 2016, Linz, Austria, May 23-27, 2016, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {9675},
  pages        = {167--182},
  publisher    = {Springer},
  year         = {2016},
  url          = {https://doi.org/10.1007/978-3-319-33600-8\_10},
  doi          = {10.1007/978-3-319-33600-8\_10},
  timestamp    = {Tue, 14 May 2019 10:00:50 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/HansenSL16.bib},
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

