---
title: "Formal Modeling and Analysis of Apache Kafka in Alloy 6"

authors:
  - Saloni Sinha
  - Eunsuk Kang


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_2.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-031-63790-2_2
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/sinhak24/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/sinhak24/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/sinhak24/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/sinhak24/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Apache Kafka is a distributed, fault-tolerant and highly available open-source technology that utilizes a publish-subscribe communication model to stream large volumes of data. It is widely being used in various domains such as finance, entertainment, online education, and e-commerce for real-time data processing and analytics. This paper demonstrates an application of Alloy 6—the latest version of Alloy with built-in temporal logic operators—to formal modeling and analysis of a complex distributed system like Kafka. The architecture and key operations of Kakfa are modeled, and its various properties, including fault-tolerance, data availability, service availability, consistency, and recoverability, are analyzed using the Alloy Analyzer. The result of the analysis provides insights into how Kafka maintains the properties that it claims to have, and the circumstances under which these properties may be violated.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_2.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_2.pdf" >}}

## Reference

```
% BibTex
@inproceedings{SinhaK24,
  author       = {Saloni Sinha and
                  Eunsuk Kang},
  editor       = {Silvia Bonfanti and
                  Angelo Gargantini and
                  Michael Leuschel and
                  Elvinia Riccobene and
                  Patrizia Scandurra},
  title        = {Formal Modeling and Analysis of Apache Kafka in Alloy 6},
  booktitle    = {Rigorous State-Based Methods - 10th International Conference, {ABZ}
                  2024, Bergamo, Italy, June 25-28, 2024, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {14759},
  pages        = {25--42},
  publisher    = {Springer},
  year         = {2024},
  url          = {https://doi.org/10.1007/978-3-031-63790-2\_2},
  doi          = {10.1007/978-3-031-63790-2\_2},
  timestamp    = {Thu, 27 Jun 2024 16:32:24 +0200},
  biburl       = {https://dblp.org/rec/conf/zum/SinhaK24.bib},
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

