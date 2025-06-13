---
title: "Generating Event-B Specifications from Algorithm Descriptions"

authors:
  - Joy Clark
  - Jens Bendisposto
  - Stefan Hallerstede
  - Dominik Hansen
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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-319-33600-8_11.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-319-33600-8_11
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/clarkbhhl16/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/clarkbhhl16/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/clarkbhhl16/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/clarkbhhl16/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

We present a high-level algorithm description language which is translated to Event-B specifications for simulation, model checking and proof. Rather than trying to recover the program structure from a lower-level Event-B specification, we start with a high-level description of the algorithm. Our goals are more tractable code generation and more convenient modelling, while keeping the power of the Event-B method in terms of proof and refinement. We present various examples of algorithm descriptions and show that our translation ensures that they can be completely proven within Rodin while achieving a high-level of automatic proof.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-319-33600-8_11.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-319-33600-8_11.pdf" >}}

## Reference

```
% BibTex
@inproceedings{ClarkBHHL16,
  author       = {Joy Clark and
                  Jens Bendisposto and
                  Stefan Hallerstede and
                  Dominik Hansen and
                  Michael Leuschel},
  editor       = {Michael J. Butler and
                  Klaus{-}Dieter Schewe and
                  Atif Mashkoor and
                  Mikl{\'{o}}s Bir{\'{o}}},
  title        = {Generating Event-B Specifications from Algorithm Descriptions},
  booktitle    = {Abstract State Machines, Alloy, B, TLA, VDM, and {Z} - 5th International
                  Conference, {ABZ} 2016, Linz, Austria, May 23-27, 2016, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {9675},
  pages        = {183--197},
  publisher    = {Springer},
  year         = {2016},
  url          = {https://doi.org/10.1007/978-3-319-33600-8\_11},
  doi          = {10.1007/978-3-319-33600-8\_11},
  timestamp    = {Tue, 14 May 2019 10:00:50 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/ClarkBHHL16.bib},
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

