---
title: "Existence Proof Obligations for Constraints, Properties and Invariants in Atelier B"

authors:
  - Héctor Ruíz Barradas
  - Lilian Burdy
  - David Déharbe


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-030-48077-6_20.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-030-48077-6_20
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/barradasbd20/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/barradasbd20/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/barradasbd20/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/barradasbd20/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Proof obligations of the B method and of Event B use predicates in the Constraints, Sets, Properties and Invariant clauses as hypotheses in proof obligations. A contradiction in these predicates results in trivially valid proof obligations and essentially voids the development. A textbook on the B method [3] presents three “existence proof obligations” to show the satisfiability of the Constraints, Properties and Invariant clauses as soon as they are stated in a component. Together with new existence proof obligations for refinement, this prevents the introduction of such contradictions in the refinement chain. This paper presents a detailed formalization of these existence proof obligations, specifying their implementation in Atelier B.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-030-48077-6_20.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-030-48077-6_20.pdf" >}}

## Reference

```
% BibTex
@inproceedings{BarradasBD20,
  author       = {H{\'{e}}ctor Ru{\'{\i}}z Barradas and
                  Lilian Burdy and
                  David D{\'{e}}harbe},
  editor       = {Alexander Raschke and
                  Dominique M{\'{e}}ry and
                  Frank Houdek},
  title        = {Existence Proof Obligations for Constraints, Properties and Invariants
                  in Atelier {B}},
  booktitle    = {Rigorous State-Based Methods - 7th International Conference, {ABZ}
                  2020, Ulm, Germany, May 27-29, 2020, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {12071},
  pages        = {255--259},
  publisher    = {Springer},
  year         = {2020},
  url          = {https://doi.org/10.1007/978-3-030-48077-6\_20},
  doi          = {10.1007/978-3-030-48077-6\_20},
  timestamp    = {Mon, 25 May 2020 12:33:39 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/BarradasBD20.bib},
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

