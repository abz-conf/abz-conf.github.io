---
title: "Alloy Goes Fuzzy"

authors:
  - Pedro Silva
  - Alcino Cunha
  - Nuno Macedo 0001
  - José N. Oliveira


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
#  10 = "pub_short_paper"
#  11 = "pub_long_paper"
publication_types:
  - 1   # default is 1 (conference), adjust as needed

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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_4.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-031-63790-2_4
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/silvacmo24/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/silvacmo24/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/silvacmo24/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/silvacmo24/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Humans are good at understanding subjective or vague statements which, however, are hard to express in classical logic. Fuzzy logic is an evolution of classical logic that can cope with vague terms by handling degrees of truth and not just the crisp values true and false. Logic is the formal basis of computing, enabling the formal design of systems supported by tools such as model checkers and theorem provers.This paper shows how a model checker such as Alloy can evolve to handle both classical and fuzzy logic, enabling the specification of high-level quantitative relational models in the fuzzy domain. In particular, the paper showcases how QAlloy-F (a conservative, general-purpose quantitative extension to standard Alloy) can be used to tackle fuzzy problems, namely in the context of validating the design of fuzzy controllers. The evaluation of QAlloy-F against examples taken from various classes of fuzzy case studies shows the approach to be feasible.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_4.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_4.pdf" >}}

## Reference

```
% BibTex
@inproceedings{SilvaCMO24,
  author       = {Pedro Silva and
                  Alcino Cunha and
                  Nuno Macedo and
                  Jos{\'{e}} N. Oliveira},
  editor       = {Silvia Bonfanti and
                  Angelo Gargantini and
                  Michael Leuschel and
                  Elvinia Riccobene and
                  Patrizia Scandurra},
  title        = {Alloy Goes Fuzzy},
  booktitle    = {Rigorous State-Based Methods - 10th International Conference, {ABZ}
                  2024, Bergamo, Italy, June 25-28, 2024, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {14759},
  pages        = {61--79},
  publisher    = {Springer},
  year         = {2024},
  url          = {https://doi.org/10.1007/978-3-031-63790-2\_4},
  doi          = {10.1007/978-3-031-63790-2\_4},
  timestamp    = {Fri, 19 Jul 2024 23:15:46 +0200},
  biburl       = {https://dblp.org/rec/conf/zum/SilvaCMO24.bib},
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

