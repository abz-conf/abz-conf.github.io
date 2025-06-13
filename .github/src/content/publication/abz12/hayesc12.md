---
title: "Integrated Operational Semantics: Small-Step, Big-Step and Multi-step"

authors:
  - Ian J. Hayes
  - Robert Colvin


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
  - 13   # default is 1 (conference), adjust as needed


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-642-30885-7_2.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-642-30885-7_2
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/hayesc12/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/hayesc12/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/hayesc12/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/hayesc12/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Plotkin’s structural operational semantics provides a tried and tested method for defining the semantics of a programming language via sets of rules that define valid transitions between program configurations. Mosses’ modular structural operational semantics (MSOS) recasts the approach by making use of rules consisting of labelled transitions, allowing a more modular approach to defining language semantics. MSOS can be adapted by using “syntactic” labels that allow local variables and aliasing to be defined without augmenting the semantics with environments and locations. The syntactic labels allow both state-based constructs of imperative languages and event-based constructs of process algebras to the specified in an integrated manner. To illustrate the integrated approach we compare its rules with Plotkin’s original rules for both small-step and big-step operational semantics. One issue that arises is that defining concurrency requires the use of a small-step approach to handle interleaving, while defining a specification command requires a big-step approach. The integrated approach can be generalised to use a sequence of (small) steps as a label; we call this a multi-step operational semantics. This approach allows both concurrency and non-atomic specification commands to be defined.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-642-30885-7_2.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-642-30885-7_2.pdf" >}}

## Reference

```
% BibTex
@inproceedings{HayesC12,
  author       = {Ian J. Hayes and
                  Robert Colvin},
  editor       = {John Derrick and
                  John S. Fitzgerald and
                  Stefania Gnesi and
                  Sarfraz Khurshid and
                  Michael Leuschel and
                  Steve Reeves and
                  Elvinia Riccobene},
  title        = {Integrated Operational Semantics: Small-Step, Big-Step and Multi-step},
  booktitle    = {Abstract State Machines, Alloy, B, VDM, and {Z} - Third International
                  Conference, {ABZ} 2012, Pisa, Italy, June 18-21, 2012. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {7316},
  pages        = {21--35},
  publisher    = {Springer},
  year         = {2012},
  url          = {https://doi.org/10.1007/978-3-642-30885-7\_2},
  doi          = {10.1007/978-3-642-30885-7\_2},
  timestamp    = {Sun, 02 Jun 2019 21:23:59 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/HayesC12.bib},
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

