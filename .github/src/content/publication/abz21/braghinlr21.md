---
title: "Towards ASM-Based Automated Formal Verification of Security Protocols"

authors:
  - Chiara Braghin
  - Mario Lilli
  - Elvinia Riccobene


date: 2021-01-01

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

publication: "8th International Conference on Rigorous State Based Methods (ABZ'21)"
publication_short: "ABZ'21"

tags:
  - ABZ'21

categories: []

featured: false

# enable this for case studies
# projects:
#   - abz21

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-030-77543-8_2.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-030-77543-8_2
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/braghinlr21/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/braghinlr21/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/braghinlr21/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/braghinlr21/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

In the security protocols domain, formal verification is more and more highly demanded to guarantee security assurance: humans increasingly depend on the use of connected devices in their daily life, so they must be protected against possible threats and accidents. However, formal verification, and in general the use of formal methods, is slowed by myths and misconceptions, mainly due to their mathematical base, which discourages many designers or engineers from their adoption. In this paper, we pose the basis for the long-term development of an ASM-based user-friendly framework for the formal verification of security protocols. We introduce a mathematical-based set of templates to formalise common patterns in security protocols and a set of security properties. These templates facilitate the protocol formal verification by providing built-in functions and domains, as well as transition rules and property schema, to be customised according to the specific protocol to be verified. The effectiveness of this approach is shown by means of their application to a number of well-known cryptographic security protocols.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-030-77543-8_2.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-030-77543-8_2.pdf" >}}

## Reference

```
% BibTex
@inproceedings{BraghinLR21,
  author       = {Chiara Braghin and
                  Mario Lilli and
                  Elvinia Riccobene},
  editor       = {Alexander Raschke and
                  Dominique M{\'{e}}ry},
  title        = {Towards ASM-Based Automated Formal Verification of Security Protocols},
  booktitle    = {Rigorous State-Based Methods - 8th International Conference, {ABZ}
                  2021, Ulm, Germany, June 9-11, 2021, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {12709},
  pages        = {17--33},
  publisher    = {Springer},
  year         = {2021},
  url          = {https://doi.org/10.1007/978-3-030-77543-8\_2},
  doi          = {10.1007/978-3-030-77543-8\_2},
  timestamp    = {Tue, 15 Jun 2021 17:24:03 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/BraghinLR21.bib},
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

