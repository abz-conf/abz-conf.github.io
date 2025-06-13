---
title: "Multi-model Animation with JeB"

authors:
  - Jean-Pierre Jacquot


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_16.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-031-63790-2_16
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/jacquot24/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/jacquot24/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/jacquot24/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/jacquot24/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

A challenge posed by model-based formal methods such as Event-B is the validation of the models. This has been recognized and some tools have been created to provide modelers with means to animate models and to explore their behaviour through graphical display. These tools are quite effective on standalone models but lack the ability to connect the model to other external models. CPS systems fall under this category, as well as systems built of components interacting through a communication network. In the context of Jeb, an animation tool for Event-B models based on JavaScript, we explore the possibility of connecting models through Websockets. The paper presents a simple protocol to connect simulations. Using an example inspired by the Lung Ventilator case study, it shows how the implementation expands JeB functionality without modifying its core.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_16.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_16.pdf" >}}

## Reference

```
% BibTex
@inproceedings{Jacquot24,
  author       = {Jean{-}Pierre Jacquot},
  editor       = {Silvia Bonfanti and
                  Angelo Gargantini and
                  Michael Leuschel and
                  Elvinia Riccobene and
                  Patrizia Scandurra},
  title        = {Multi-model Animation with JeB},
  booktitle    = {Rigorous State-Based Methods - 10th International Conference, {ABZ}
                  2024, Bergamo, Italy, June 25-28, 2024, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {14759},
  pages        = {223--232},
  publisher    = {Springer},
  year         = {2024},
  url          = {https://doi.org/10.1007/978-3-031-63790-2\_16},
  doi          = {10.1007/978-3-031-63790-2\_16},
  timestamp    = {Thu, 04 Jul 2024 22:05:23 +0200},
  biburl       = {https://dblp.org/rec/conf/zum/Jacquot24.bib},
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

