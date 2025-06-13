---
title: "Splitting Atoms with Rely/Guarantee Conditions Coupled with Data Reification"

authors:
  - Cliff B. Jones
  - Ken G. Pierce


date: 2008-01-01

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

publication: "1st International Conference on ASM, B, and Z (ABZ'08)"
publication_short: "ABZ'08"

tags:
  - ABZ'08

categories: []

featured: false

# enable this for case studies
# projects:
#   - abz08

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_47.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-540-87603-8_47
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/jonesp08/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/jonesp08/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/jonesp08/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/jonesp08/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

This paper presents a novel formal development of a non-trivial parallel program: Simpson’s implementation of asynchronous communication mechanisms (ACMs). Although the correctness of the “4-slot algorithm” has been shown elsewhere, earlier developments are by no means intuitive. The aims of this paper include both the presentation of an understandable (yet formal) design history and the establishment of another way of “splitting (software) atoms”. Using the “fiction of atomicity” as an aid to understanding the initial steps of development, the top-level specification is developed to code. The rely-guarantee approach is, here, combined with notions of read/write frames and “phased” specifications; the atomicity assumptions implied by rely/guarantee conditions are realised by clever choice of data representation. The development method herein is compared with other approaches –in a spirit of cooperation– as the authors believe that constructive comparison elucidates many of the finer points in the “4-slot” specification/development and of parallel programs in general.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_47.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_47.pdf" >}}

## Reference

```
% BibTex
@inproceedings{JonesP08,
  author       = {Cliff B. Jones and
                  Ken G. Pierce},
  editor       = {Egon B{\"{o}}rger and
                  Michael J. Butler and
                  Jonathan P. Bowen and
                  Paul Boca},
  title        = {Splitting Atoms with Rely/Guarantee Conditions Coupled with Data Reification},
  booktitle    = {Abstract State Machines, {B} and Z, First International Conference,
                  {ABZ} 2008, London, UK, September 16-18, 2008. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {5238},
  pages        = {360--377},
  publisher    = {Springer},
  year         = {2008},
  url          = {https://doi.org/10.1007/978-3-540-87603-8\_47},
  doi          = {10.1007/978-3-540-87603-8\_47},
  timestamp    = {Tue, 14 May 2019 10:00:50 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/JonesP08.bib},
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

