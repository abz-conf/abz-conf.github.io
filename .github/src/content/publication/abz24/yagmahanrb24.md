---
title: "An Event-B Formal Model for Access Control and Resource Management of Serverless Apps"

authors:
  - Mehmet Said Nur Yagmahan
  - Abdolbaghi Rezazadeh
  - Michael J. Butler


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_11.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-031-63790-2_11
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/yagmahanrb24/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/yagmahanrb24/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/yagmahanrb24/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/yagmahanrb24/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Cloud computing technologies help developers build scalable distributed apps. Serverless architecture, or Function as a Service (FaaS), which separates app businesses into multiple functions, is one of the cloud-native architectures that has gained popularity. Those functions can be developed and deployed independently without provisioning infrastructure. Despite the considerable advantages and increasing popularity of cloud-native apps, developers face many challenges when building their cloud-native applications. To ensure the robustness and security of cloud-native apps and protect crucial resources, the design and implementation of functions and associated access control systems play a pivotal role. In this paper, we have employed formal methods and tools to develop a set of patterns to help cloud-native application developers to design robust serverless apps. We have used Event-B and its associated toolset, Rodin, to construct these formal patterns and demonstrated how these patterns can be used in practical case studies.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_11.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_11.pdf" >}}

## Reference

```
% BibTex
@inproceedings{YagmahanRB24,
  author       = {Mehmet Said Nur Yagmahan and
                  Abdolbaghi Rezazadeh and
                  Michael J. Butler},
  editor       = {Silvia Bonfanti and
                  Angelo Gargantini and
                  Michael Leuschel and
                  Elvinia Riccobene and
                  Patrizia Scandurra},
  title        = {An Event-B Formal Model for Access Control and Resource Management
                  of Serverless Apps},
  booktitle    = {Rigorous State-Based Methods - 10th International Conference, {ABZ}
                  2024, Bergamo, Italy, June 25-28, 2024, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {14759},
  pages        = {181--190},
  publisher    = {Springer},
  year         = {2024},
  url          = {https://doi.org/10.1007/978-3-031-63790-2\_11},
  doi          = {10.1007/978-3-031-63790-2\_11},
  timestamp    = {Thu, 04 Jul 2024 22:05:23 +0200},
  biburl       = {https://dblp.org/rec/conf/zum/YagmahanRB24.bib},
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

