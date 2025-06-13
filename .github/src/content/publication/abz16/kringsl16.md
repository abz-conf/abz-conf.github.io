---
title: "Proof Assisted Symbolic Model Checking for B and Event-B"

authors:
  - Sebastian Krings
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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-319-33600-8_8.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-319-33600-8_8
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/kringsl16/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/kringsl16/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/kringsl16/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/kringsl16/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

We have implemented various symbolic model checking algorithms, like BMC, k-Induction and IC3 for B and Event-B. The high-level nature of B and Event-B accounts for complicated constraints arising in these symbolic analysis techniques. In this paper we suggest using static information stemming from proof obligations to simplify occurring constraints. We show how to include proof information in the aforementioned algorithms. Using different benchmarks we compare explicit state to symbolic model checking as well as techniques with and without proof assistance. In particular for models with large branching factor, e.g., due to complicated data values being manipulated, the symbolic techniques fare much better than explicit state model checking. The inclusion of proof information results in further clear performance improvements.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-319-33600-8_8.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-319-33600-8_8.pdf" >}}

## Reference

```
% BibTex
@inproceedings{KringsL16,
  author       = {Sebastian Krings and
                  Michael Leuschel},
  editor       = {Michael J. Butler and
                  Klaus{-}Dieter Schewe and
                  Atif Mashkoor and
                  Mikl{\'{o}}s Bir{\'{o}}},
  title        = {Proof Assisted Symbolic Model Checking for {B} and Event-B},
  booktitle    = {Abstract State Machines, Alloy, B, TLA, VDM, and {Z} - 5th International
                  Conference, {ABZ} 2016, Linz, Austria, May 23-27, 2016, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {9675},
  pages        = {135--150},
  publisher    = {Springer},
  year         = {2016},
  url          = {https://doi.org/10.1007/978-3-319-33600-8\_8},
  doi          = {10.1007/978-3-319-33600-8\_8},
  timestamp    = {Tue, 14 May 2019 10:00:50 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/KringsL16.bib},
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

