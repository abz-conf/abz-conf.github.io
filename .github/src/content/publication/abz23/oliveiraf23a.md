---
title: "TASTD: A Real-Time Extension for ASTD"

authors:
  - Diego de Azevedo Oliveira
  - Marc Frappier


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
#  10 = "pub_short_paper"
#  11 = "pub_long_paper"
publication_types:
  - 1   # default is 1 (conference), adjust as needed

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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_11.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-031-33163-3_11
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/oliveiraf23a/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/oliveiraf23a/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/oliveiraf23a/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/oliveiraf23a/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

In ASTD, real-time models are not natively supported. Real-time requirements are pervasive in many systems, like control systems and cybersecurity. Timed Algebraic State Transition Diagrams (TASTD) is an extension of ASTD capable of specifying real-time models. TASTD gives ASTD the capability to handle time with new algebraic operators. This paper describes the syntax and semantics of these new time operators: delay, persistent delay, timeout, persistent timeout, and timed interrupt. These new time operators are specified using two new operators, persistent guard and interrupt. To illustrate our extension, we present a small case study of a sensor where we want to detect potential anomalies.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_11.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_11.pdf" >}}

## Reference

```
% BibTex
@inproceedings{OliveiraF23a,
  author       = {Diego de Azevedo Oliveira and
                  Marc Frappier},
  editor       = {Uwe Gl{\"{a}}sser and
                  Jos{\'{e}} Creissac Campos and
                  Dominique M{\'{e}}ry and
                  Philippe A. Palanque},
  title        = {{TASTD:} {A} Real-Time Extension for {ASTD}},
  booktitle    = {Rigorous State-Based Methods - 9th International Conference, {ABZ}
                  2023, Nancy, France, May 30 - June 2, 2023, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {14010},
  pages        = {142--159},
  publisher    = {Springer},
  year         = {2023},
  url          = {https://doi.org/10.1007/978-3-031-33163-3\_11},
  doi          = {10.1007/978-3-031-33163-3\_11},
  timestamp    = {Fri, 02 Jun 2023 21:23:53 +0200},
  biburl       = {https://dblp.org/rec/conf/zum/OliveiraF23a.bib},
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

