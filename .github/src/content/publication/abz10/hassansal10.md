---
title: "Secrecy UML Method for Model Transformations"

authors:
  - Waël Hassan
  - Nadera Slimani
  - Kamel Adi
  - Luigi Logrippo


date: 2010-01-01

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


publication: "2nd International Conference on ASM, Alloy, B, and Z (ABZ'10)"
publication_short: "ABZ'10"

tags:
  - ABZ'10

categories: []

featured: false

# enable this for case studies
# projects:
#   - abz10

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_35.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-642-11811-1_35
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/hassansal10/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/hassansal10/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/hassansal10/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/hassansal10/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

This paper introduces the subject of secrecy models development by transformation, with formal validation. In an enterprise, constructing a secrecy model is a participatory exercise involving policy makers and implementers. Policy makers iteratively provide business governance requirements, while policy implementers formulate rules of access in computer-executable terms. The process is error prone and may lead to undesirable situations thus threatening the security of the enterprise. At each iteration, a security officer (SO) needs to guarantee business continuity by ensuring property preservation; as well, he needs to check for potential threats due to policy changes. This paper proposes a method that is meant to address both aspects: the formal analysis of transformation results and the formal proof that transformations are property preserving. UML is used for expressing and transforming models [1], and the Alloy analyzer is used to perform integrity checks [3]. Governance requirements dictate a security policy, that regulates access to information. This policy is implemented by means of secrecy models. Hence, the SO defines the mandatory secrecy rules as a part of enterprise governance model in order to implement security policy. For instance, a secrecy rule may state: higher-ranking officers have read rights to information at lower ranks. Automation helps reduce design errors of combined and complex secrecy models [2]. However, current industry practices do not include precise methods for constructing and validating enterprise governance models. Our research proposes a formal transformation method to construct secrecy models by way of applying transformations to a base UML model (BM). For example, starting from the BM, with only three primitives: Subject/Verb/Object, we can generate RBAC0 in addition to SecureUML [2] model. By way of examples and by means of formal analysis we intend to show that, using our method, a SO is able to build different types of secrecy models and validate them for consistency, in addition to detecting scenarios resulting from unpreserved properties.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_35.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_35.pdf" >}}

## Reference

```
% BibTex
@inproceedings{HassanSAL10,
  author       = {Wa{\"{e}}l Hassan and
                  Nadera Slimani and
                  Kamel Adi and
                  Luigi Logrippo},
  editor       = {Marc Frappier and
                  Uwe Gl{\"{a}}sser and
                  Sarfraz Khurshid and
                  R{\'{e}}gine Laleau and
                  Steve Reeves},
  title        = {Secrecy {UML} Method for Model Transformations},
  booktitle    = {Abstract State Machines, Alloy, {B} and Z, Second International Conference,
                  {ABZ} 2010, Orford, QC, Canada, February 22-25, 2010. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {5977},
  pages        = {400},
  publisher    = {Springer},
  year         = {2010},
  url          = {https://doi.org/10.1007/978-3-642-11811-1\_35},
  doi          = {10.1007/978-3-642-11811-1\_35},
  timestamp    = {Sat, 31 May 2025 23:08:41 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/HassanSAL10.bib},
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

