---
title: "Diverse Scenario Exploration in Model Finders Using Graph Kernels and Clustering"

authors:
  - Robert Clarisó
  - Jordi Cabot


date: 2020-01-01

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

publication: "7th International Conference on Rigorous State Based Methods (ABZ'20)"
publication_short: "ABZ'20"

tags:
  - ABZ'20

categories: []

featured: false

# enable this for case studies
# projects:
#   - abz20

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-030-48077-6_3.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-030-48077-6_3
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/clarisoc20/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/clarisoc20/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/clarisoc20/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/clarisoc20/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Complex software systems can be described using modeling notations such as UML/OCL or Alloy. Then, some correctness properties of these systems can be checked using model finders, which compute sample scenarios either fulfilling the desired properties or illustrating potential faults. Such scenarios allow designers to validate, verify and test the system under development. Nevertheless, when asked to produce several scenarios, model finders tend to produce similar solutions. This lack of diversity impairs their effectiveness as testing or validation assets. To solve this problem, we propose the use of graph kernels, a family of methods for computing the (dis)similarity among pairs of graphs. With this metric, it is possible to cluster scenarios effectively, improving the usability of model finders and making testing and validation more efficient.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-030-48077-6_3.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-030-48077-6_3.pdf" >}}

## Reference

```
% BibTex
@inproceedings{ClarisoC20,
  author       = {Robert Claris{\'{o}} and
                  Jordi Cabot},
  editor       = {Alexander Raschke and
                  Dominique M{\'{e}}ry and
                  Frank Houdek},
  title        = {Diverse Scenario Exploration in Model Finders Using Graph Kernels
                  and Clustering},
  booktitle    = {Rigorous State-Based Methods - 7th International Conference, {ABZ}
                  2020, Ulm, Germany, May 27-29, 2020, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {12071},
  pages        = {27--43},
  publisher    = {Springer},
  year         = {2020},
  url          = {https://doi.org/10.1007/978-3-030-48077-6\_3},
  doi          = {10.1007/978-3-030-48077-6\_3},
  timestamp    = {Mon, 15 Jun 2020 17:09:54 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/ClarisoC20.bib},
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

