---
title: "Refinement by Interface Instantiation"

authors:
  - Stefan Hallerstede
  - Thai Son Hoang


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
#  10 = "pub_short_paper"
#  11 = "pub_long_paper"
publication_types:
  - 1   # default is 1 (conference), adjust as needed

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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-642-30885-7_16.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-642-30885-7_16
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/hallerstedeh12/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/hallerstedeh12/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/hallerstedeh12/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/hallerstedeh12/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Decomposition is a technique to separate the design of a complex system into smaller sub-models, which improves scalability and team development. In the shared-variable decomposition approach for Event-B sub-models share external variables and communicate through external events which cannot be easily refined. Our first contribution hence is a proposal for a new construct called interface that encapsulates the external variables, along with a mechanism for interface instantiation. Using the new construct and mechanism, external variables can be refined consistently. Our second contribution is an approach for verifying the correctness of Event-B extensions using the supporting Rodin tool. We illustrate our approach by proving the correctness of interface instantiation.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-642-30885-7_16.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-642-30885-7_16.pdf" >}}

## Reference

```
% BibTex
@inproceedings{HallerstedeH12,
  author       = {Stefan Hallerstede and
                  Thai Son Hoang},
  editor       = {John Derrick and
                  John S. Fitzgerald and
                  Stefania Gnesi and
                  Sarfraz Khurshid and
                  Michael Leuschel and
                  Steve Reeves and
                  Elvinia Riccobene},
  title        = {Refinement by Interface Instantiation},
  booktitle    = {Abstract State Machines, Alloy, B, VDM, and {Z} - Third International
                  Conference, {ABZ} 2012, Pisa, Italy, June 18-21, 2012. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {7316},
  pages        = {223--237},
  publisher    = {Springer},
  year         = {2012},
  url          = {https://doi.org/10.1007/978-3-642-30885-7\_16},
  doi          = {10.1007/978-3-642-30885-7\_16},
  timestamp    = {Sun, 02 Jun 2019 21:23:59 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/HallerstedeH12.bib},
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

