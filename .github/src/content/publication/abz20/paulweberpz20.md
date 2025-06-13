---
title: "Structuring the State and Behavior of ASMs: Introducing a Trait-Based Construct for Abstract State Machine Languages"

authors:
  - Philipp Paulweber
  - Emmanuel Pescosta
  - Uwe Zdun


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
#  11 = "pub_short_paper"
#  12 = "pub_long_paper"
#  13 = "pub_invited_talk"
publication_types:
  - 11   # default is 1 (conference), adjust as needed

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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-030-48077-6_17.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-030-48077-6_17
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/paulweberpz20/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/paulweberpz20/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/paulweberpz20/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/paulweberpz20/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Abstract State Machine (ASM) theory is a well-known state-based formal method to analyze, verify, and specify software and hardware systems. Nowadays, as in other state-based formal methods, the proposed specification languages for ASMs still lack easy-to-comprehend language constructs for type abstractions to describe reusable and maintainable specifications. Almost all built-in behaviors are implicitly defined inside a concrete ASM language implementation and thus, the behavior is hidden from the language user. In this paper, we present a new ASM syntax extension based on traits, which allows the specifier (language user) to define new type abstractions in the form of structure and behavior definitions to reuse, maintain, structure, and extend the functionality in ASM specifications. We describe the proposed language construct by defining its syntax and semantics. The decision to use a trait-based syntax extension over other object-oriented language constructs like interfaces or mixins was motivated and driven by the results of previously conducted empirical studies. Moreover, we outline details about the implementation of the trait-based syntax extension in our Corinthian Abstract State Machine (CASM) language implementation.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-030-48077-6_17.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-030-48077-6_17.pdf" >}}

## Reference

```
% BibTex
@inproceedings{PaulweberPZ20,
  author       = {Philipp Paulweber and
                  Emmanuel Pescosta and
                  Uwe Zdun},
  editor       = {Alexander Raschke and
                  Dominique M{\'{e}}ry and
                  Frank Houdek},
  title        = {Structuring the State and Behavior of ASMs: Introducing a Trait-Based
                  Construct for Abstract State Machine Languages},
  booktitle    = {Rigorous State-Based Methods - 7th International Conference, {ABZ}
                  2020, Ulm, Germany, May 27-29, 2020, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {12071},
  pages        = {237--243},
  publisher    = {Springer},
  year         = {2020},
  url          = {https://doi.org/10.1007/978-3-030-48077-6\_17},
  doi          = {10.1007/978-3-030-48077-6\_17},
  timestamp    = {Sun, 02 Oct 2022 15:55:03 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/PaulweberPZ20.bib},
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

