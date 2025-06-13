---
title: "Loose Observation in Event-B"

authors:
  - Stefan Hallerstede


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_7.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-031-63790-2_7
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/hallerstede24/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/hallerstede24/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/hallerstede24/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/hallerstede24/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Refinement of Event-B machines is based on changing internal variables to obtain different data representations. One approach is expressed only in terms of internal variables. In the extreme case it permits refining a machine by another by choosing the gluing invariant “true”. The other one is based on relating external variables that can be refined functionally, so that properties expressed in terms of external variables are preserved. In practice, the first approach is used and gluing invariants are suitably chosen to achieve a meaningful relationship between refined machines. The second approach is based on the idea of observing a machine in terms of its external variables. It is more complicated, restrictive and not commonly used. In this paper we propose a different approach to observing Event-B machines that is more constraining than the first approach but less complicated and restrictive than the second approach. We extend Event-B refinement by permitting introducing new events and eliminating old events. The concept of observation is made more flexible by permitting non-observation of certain states as well as observing sets of values related to a states. Although this complicates relating observed fixed points and traces of machines, the proof obligations remain uncomplicated.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_7.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-031-63790-2_7.pdf" >}}

## Reference

```
% BibTex
@inproceedings{Hallerstede24,
  author       = {Stefan Hallerstede},
  editor       = {Silvia Bonfanti and
                  Angelo Gargantini and
                  Michael Leuschel and
                  Elvinia Riccobene and
                  Patrizia Scandurra},
  title        = {Loose Observation in Event-B},
  booktitle    = {Rigorous State-Based Methods - 10th International Conference, {ABZ}
                  2024, Bergamo, Italy, June 25-28, 2024, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {14759},
  pages        = {105--122},
  publisher    = {Springer},
  year         = {2024},
  url          = {https://doi.org/10.1007/978-3-031-63790-2\_7},
  doi          = {10.1007/978-3-031-63790-2\_7},
  timestamp    = {Thu, 04 Jul 2024 22:05:23 +0200},
  biburl       = {https://dblp.org/rec/conf/zum/Hallerstede24.bib},
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

