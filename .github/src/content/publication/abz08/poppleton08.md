---
title: "The Composition of Event-B Models"

authors:
  - Michael Poppleton


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_17.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-540-87603-8_17
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/poppleton08/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/poppleton08/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/poppleton08/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/poppleton08/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

The transition from classical B [2] to the Event-B language and method [3] has seen the removal of some forms of model structuring and composition, with the intention of reinventing them in future. This work contributes to that reinvention. Inspired by a proposed method for state-based decomposition and refinement [5] of an Event-B model, we propose a familiar parallel event composition (over disjoint state variable lists), and the less familiar event fusion (over intersecting state variable lists). A brief motivation is provided for these and other forms of composition of models, in terms of feature-based modelling. We show that model consistency is preserved under such compositions. More significantly we show that model composition preserves refinement.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_17.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_17.pdf" >}}

## Reference

```
% BibTex
@inproceedings{Poppleton08,
  author       = {Michael Poppleton},
  editor       = {Egon B{\"{o}}rger and
                  Michael J. Butler and
                  Jonathan P. Bowen and
                  Paul Boca},
  title        = {The Composition of Event-B Models},
  booktitle    = {Abstract State Machines, {B} and Z, First International Conference,
                  {ABZ} 2008, London, UK, September 16-18, 2008. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {5238},
  pages        = {209--222},
  publisher    = {Springer},
  year         = {2008},
  url          = {https://doi.org/10.1007/978-3-540-87603-8\_17},
  doi          = {10.1007/978-3-540-87603-8\_17},
  timestamp    = {Tue, 14 May 2019 10:00:50 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/Poppleton08.bib},
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

