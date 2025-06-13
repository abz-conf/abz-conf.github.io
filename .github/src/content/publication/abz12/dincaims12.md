---
title: "Learn and Test for Event-B - A Rodin Plugin"

authors:
  - Ionut Dinca
  - Florentin Ipate
  - Laurentiu Mierla
  - Alin Stefanescu


date: 2012-01-01

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
  - 11   # default is 1 (conference), adjust as needed


publication: "3rd International Conference on ASM, Alloy, B, VDM, and Z (ABZ'12)"
publication_short: "ABZ'12"

tags:
  - ABZ'12

categories: []

featured: false

# enable this for case studies
# projects:
#   - abz12

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-642-30885-7_32.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-642-30885-7_32
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/dincaims12/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/dincaims12/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/dincaims12/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/dincaims12/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

The Event-B method is a formal approach for reliable systems specification and verification, being supported by the Rodin platform, which includes mature plugins for theorem-proving, model-checking, or model (de)composition features. In order to complement these techniques with test generation and state model inference from Event-B models, we developed a new feature as a Rodin plugin. Our plugin implements a model-learning approach to iteratively construct an approximate automaton model together with an associated test suite. Test suite optimization is further applied according to different optimization criteria.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-642-30885-7_32.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-642-30885-7_32.pdf" >}}

## Reference

```
% BibTex
@inproceedings{DincaIMS12,
  author       = {Ionut Dinca and
                  Florentin Ipate and
                  Laurentiu Mierla and
                  Alin Stefanescu},
  editor       = {John Derrick and
                  John S. Fitzgerald and
                  Stefania Gnesi and
                  Sarfraz Khurshid and
                  Michael Leuschel and
                  Steve Reeves and
                  Elvinia Riccobene},
  title        = {Learn and Test for Event-B - {A} Rodin Plugin},
  booktitle    = {Abstract State Machines, Alloy, B, VDM, and {Z} - Third International
                  Conference, {ABZ} 2012, Pisa, Italy, June 18-21, 2012. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {7316},
  pages        = {361--364},
  publisher    = {Springer},
  year         = {2012},
  url          = {https://doi.org/10.1007/978-3-642-30885-7\_32},
  doi          = {10.1007/978-3-642-30885-7\_32},
  timestamp    = {Sun, 02 Jun 2019 21:23:59 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/DincaIMS12.bib},
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

