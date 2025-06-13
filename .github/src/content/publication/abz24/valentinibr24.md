---
title: "A Modeling and Verification Framework for Ethereum Smart Contracts"

authors:
  - Simone Valentini
  - Chiara Braghin
  - Elvinia Riccobene


date: 2024-01-01

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
#  14 = "pub_phd_symposium"
publication_types:
  - 10  # default is 1 (conference), adjust as needed

publication: "10th International Conference on Rigorous State Based Methods (ABZ'24)"
publication_short: "ABZ'24"

tags:
  - ABZ'24

categories: []

featured: false

# enable this for case studies
# projects:
#   - abz24

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_13.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-031-63790-2_13
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/valentinibr24/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/valentinibr24/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/valentinibr24/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/valentinibr24/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Blockchain has shown to be a versatile technology with applications ranging from financial services and supply chain management to healthcare, identity verification, etc. Thanks to the usage of smart contracts, blockchain can streamline and automate complex processes, eliminating the need for intermediaries and reducing administrative overhead. Smart contracts often handle valuable assets and execute critical functions, making them attractive targets for attackers. Thus, secure and reliable smart contracts are necessary. The long-term research we present aims to face the problem of safety and security assurance of smart contracts at design time. We are investigating the usage of the Abstract State Machine (ASM) formal method for the specification, validation, and verification of Ethereum smart contracts. We provide (i) a set of ASM libraries that simplify smart contracts modeling, (ii) models of malicious contracts to be used to check the robustness of a contract against some given attacks, (iii) patterns of properties to be checked to guarantee the operational correctness of the contract and its adherence to certain predefined properties.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_13.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_13.pdf" >}}

## Reference

```
% BibTex
@inproceedings{ValentiniBR24,
  author       = {Simone Valentini and
                  Chiara Braghin and
                  Elvinia Riccobene},
  editor       = {Silvia Bonfanti and
                  Angelo Gargantini and
                  Michael Leuschel and
                  Elvinia Riccobene and
                  Patrizia Scandurra},
  title        = {A Modeling and Verification Framework for Ethereum Smart Contracts},
  booktitle    = {Rigorous State-Based Methods - 10th International Conference, {ABZ}
                  2024, Bergamo, Italy, June 25-28, 2024, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {14759},
  pages        = {201--207},
  publisher    = {Springer},
  year         = {2024},
  url          = {https://doi.org/10.1007/978-3-031-63790-2\_13},
  doi          = {10.1007/978-3-031-63790-2\_13},
  timestamp    = {Fri, 19 Jul 2024 23:15:46 +0200},
  biburl       = {https://dblp.org/rec/conf/zum/ValentiniBR24.bib},
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

