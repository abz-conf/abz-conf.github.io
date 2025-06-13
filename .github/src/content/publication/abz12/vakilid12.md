---
title: "Temporal Logic Model Checking in Alloy"

authors:
  - Amirhossein Vakili
  - Nancy A. Day


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-642-30885-7_11.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-642-30885-7_11
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/vakilid12/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/vakilid12/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/vakilid12/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/vakilid12/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

The declarative and relational aspects of Alloy make it a desirable language to use for high-level modeling of transition systems. However, currently, these models must be translated to another tool to carry out full temporal logic model checking. In this article, we show how a symbolic representation of the semantics of computational tree logic with fairness constraints (CTLFC) can be written in first-order logic with the transitive closure operator, and therefore described in Alloy. Using this encoding, the question of whether a declarative model of a transition system satisfies a temporal logic formula can be solved using the Alloy Analyzer directly. Also, since a declarative description of a model may actually represent a family of transition systems, we define two distinct model checking questions on this family (existential and universal model checking) and show how these properties can be evaluated in the Alloy Analyzer.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-642-30885-7_11.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-642-30885-7_11.pdf" >}}

## Reference

```
% BibTex
@inproceedings{VakiliD12,
  author       = {Amirhossein Vakili and
                  Nancy A. Day},
  editor       = {John Derrick and
                  John S. Fitzgerald and
                  Stefania Gnesi and
                  Sarfraz Khurshid and
                  Michael Leuschel and
                  Steve Reeves and
                  Elvinia Riccobene},
  title        = {Temporal Logic Model Checking in Alloy},
  booktitle    = {Abstract State Machines, Alloy, B, VDM, and {Z} - Third International
                  Conference, {ABZ} 2012, Pisa, Italy, June 18-21, 2012. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {7316},
  pages        = {150--163},
  publisher    = {Springer},
  year         = {2012},
  url          = {https://doi.org/10.1007/978-3-642-30885-7\_11},
  doi          = {10.1007/978-3-642-30885-7\_11},
  timestamp    = {Sun, 02 Jun 2019 21:23:59 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/VakiliD12.bib},
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

