---
title: "Task Model Design and Analysis with Alloy"

authors:
  - Alcino Cunha
  - Nuno Macedo 0001
  - Eunsuk Kang


date: 2023-01-01

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

publication: "9th International Conference on Rigorous State Based Methods (ABZ'23)"
publication_short: "ABZ'23"

tags:
  - ABZ'23

categories: []

featured: false

# enable this for case studies
# projects:
#   - abz23

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_23.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-031-33163-3_23
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/cunhamk23/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/cunhamk23/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/cunhamk23/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/cunhamk23/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

This paper describes a methodology for task model design and analysis using the Alloy Analyzer, a formal, declarative modeling tool. Our methodology leverages (1) a formalization of the HAMSTERS task modeling notation in Alloy and (2) a method for encoding a concrete task model and compose it with a model of the interactive system. The Analyzer then automatically verifies the overall model against desired properties, revealing counter-examples (if any) in terms of interaction scenarios between the operator and the system. In addition, we demonstrate how Alloy can be used to encode various types of operator errors (e.g., inserting or omitting an action) into the base HAMSTERS model and generate erroneous interaction scenarios. Our methodology is applied to a task model describing the interaction of a traffic air controller with a semi-autonomous Arrival MANager (AMAN) planning tool.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_23.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_23.pdf" >}}

## Reference

```
% BibTex
@inproceedings{CunhaMK23,
  author       = {Alcino Cunha and
                  Nuno Macedo and
                  Eunsuk Kang},
  editor       = {Uwe Gl{\"{a}}sser and
                  Jos{\'{e}} Creissac Campos and
                  Dominique M{\'{e}}ry and
                  Philippe A. Palanque},
  title        = {Task Model Design and Analysis with Alloy},
  booktitle    = {Rigorous State-Based Methods - 9th International Conference, {ABZ}
                  2023, Nancy, France, May 30 - June 2, 2023, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {14010},
  pages        = {303--320},
  publisher    = {Springer},
  year         = {2023},
  url          = {https://doi.org/10.1007/978-3-031-33163-3\_23},
  doi          = {10.1007/978-3-031-33163-3\_23},
  timestamp    = {Tue, 25 Jun 2024 21:03:18 +0200},
  biburl       = {https://dblp.org/rec/conf/zum/CunhaMK23.bib},
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

