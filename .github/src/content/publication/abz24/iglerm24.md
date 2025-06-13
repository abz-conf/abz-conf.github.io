---
title: "ThoR: An Alloy5-Like DSL for Interactive Theorem Proving in Coq"

authors:
  - Bodo Igler
  - Andreas Mayer


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_19.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-031-63790-2_19
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/iglerm24/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/iglerm24/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/iglerm24/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/iglerm24/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

The steep learning curve associated with interactive theorem proving poses a significant entry barrier for the learner. While the Alloy specification language [1] has simplified the introduction to and application of formal methods, transitioning to interactive theorem proving, such as with Coq [2], remains daunting due to the inherent complexity of formal reasoning and the sophisticated tooling required. We introduce ThoR, an extension for the Coq proof assistant that incorporates an Alloy5-like domain-specific language: Specifications, propositions and proofs are formulated in an Alloy5-like syntax. This reduces tool and language complexity, and makes interactive theorem proving more accessible. The implementation is based on Coq’s syntax extension capabilities and the mathematical components library (mathcomp) [4]. This paper reports on work in progress. It contributes an approach for the embedding of Alloy into Coq based on a set-theoretic interpretation, a proof calculus for Alloy with soundness by construction, a prototypical implementation and its validation via a simple token ring example.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_19.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_19.pdf" >}}

## Reference

```
% BibTex
@inproceedings{IglerM24,
  author       = {Bodo Igler and
                  Andreas Mayer},
  editor       = {Silvia Bonfanti and
                  Angelo Gargantini and
                  Michael Leuschel and
                  Elvinia Riccobene and
                  Patrizia Scandurra},
  title        = {ThoR: An Alloy5-Like {DSL} for Interactive Theorem Proving in Coq},
  booktitle    = {Rigorous State-Based Methods - 10th International Conference, {ABZ}
                  2024, Bergamo, Italy, June 25-28, 2024, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {14759},
  pages        = {248--254},
  publisher    = {Springer},
  year         = {2024},
  url          = {https://doi.org/10.1007/978-3-031-63790-2\_19},
  doi          = {10.1007/978-3-031-63790-2\_19},
  timestamp    = {Thu, 04 Jul 2024 22:05:23 +0200},
  biburl       = {https://dblp.org/rec/conf/zum/IglerM24.bib},
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

