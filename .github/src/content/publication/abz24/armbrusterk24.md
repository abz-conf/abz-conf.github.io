---
title: "Meta-programming Event-B - Advancing Tool Support and Language Extensions"

authors:
  - Julius Armbrüster
  - Philipp Körner


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_17.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-031-63790-2_17
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/armbrusterk24/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/armbrusterk24/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/armbrusterk24/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/armbrusterk24/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Transforming models based on their textual representation is a cumbersome task. This is particularly the case for Event-B, where the predominant representation is a set of XML files. As a consequence, tool support is lacking, even for minor refactoring operations. The contribution of this paper extends the lisb library with a front and backend based on Event-B. The aim is to bring benefits, that have been demonstrated for classical B, such as an easily transformable data representation of formal specifications as well as creation of custom DSLs and tooling, to Event-B. We see great benefits of such a meta-programming approach for formal specifications and advocate that similar mechanisms will be sensible extensions to the expressiveness of formal methods. Ultimately, our work facilitates language extensions (e.g., re-introducing if-then-else constructs to Event-B which generate multiple events or a proper macro system to avoid code duplication) and tool support (e.g., refactoring tools or automatic refinement).

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_17.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_17.pdf" >}}

## Reference

```
% BibTex
@inproceedings{ArmbrusterK24,
  author       = {Julius Armbr{\"{u}}ster and
                  Philipp K{\"{o}}rner},
  editor       = {Silvia Bonfanti and
                  Angelo Gargantini and
                  Michael Leuschel and
                  Elvinia Riccobene and
                  Patrizia Scandurra},
  title        = {Meta-programming Event-B - Advancing Tool Support and Language Extensions},
  booktitle    = {Rigorous State-Based Methods - 10th International Conference, {ABZ}
                  2024, Bergamo, Italy, June 25-28, 2024, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {14759},
  pages        = {233--240},
  publisher    = {Springer},
  year         = {2024},
  url          = {https://doi.org/10.1007/978-3-031-63790-2\_17},
  doi          = {10.1007/978-3-031-63790-2\_17},
  timestamp    = {Thu, 04 Jul 2024 22:05:23 +0200},
  biburl       = {https://dblp.org/rec/conf/zum/ArmbrusterK24.bib},
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

