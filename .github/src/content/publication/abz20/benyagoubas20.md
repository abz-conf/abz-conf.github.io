---
title: "Event-B-Supported Choreography-Defined Communicating Systems - Correctness and Completeness"

authors:
  - Sarah Benyagoub
  - Yamine Aït Ameur
  - Klaus-Dieter Schewe


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
#  10 = "pub_short_paper"
#  11 = "pub_long_paper"
publication_types:
  - 1   # default is 1 (conference), adjust as needed

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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-030-48077-6_11.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-030-48077-6_11
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/benyagoubas20/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/benyagoubas20/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/benyagoubas20/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/benyagoubas20/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Choreographies prescribe the rendez-vous synchronisation of messages in a communicating system. Such a system is called realisable, if the traces of the prescribed communication coincide with those of the asynchronous system of peers, where the communication channels either use FIFO queues or multiset mailboxes. It has recently been shown that realisability can be characterised by two necessary conditions that together are also sufficient, whereas in general the synchronisability of communicating peers is undecidable. The sufficiency of the conditions permits the construction of correct communicating systems; their necessity shows that all choreography-defined communicating system can be obtained in this way. This article provides an integrated framework based on Event-B for such a construction with a major emphasis on Rodin-based proofs of correctness and completeness.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-030-48077-6_11.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-030-48077-6_11.pdf" >}}

## Reference

```
% BibTex
@inproceedings{BenyagoubAS20,
  author       = {Sarah Benyagoub and
                  Yamine A{\"{\i}}t Ameur and
                  Klaus{-}Dieter Schewe},
  editor       = {Alexander Raschke and
                  Dominique M{\'{e}}ry and
                  Frank Houdek},
  title        = {Event-B-Supported Choreography-Defined Communicating Systems - Correctness
                  and Completeness},
  booktitle    = {Rigorous State-Based Methods - 7th International Conference, {ABZ}
                  2020, Ulm, Germany, May 27-29, 2020, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {12071},
  pages        = {155--168},
  publisher    = {Springer},
  year         = {2020},
  url          = {https://doi.org/10.1007/978-3-030-48077-6\_11},
  doi          = {10.1007/978-3-030-48077-6\_11},
  timestamp    = {Mon, 25 May 2020 12:33:39 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/BenyagoubAS20.bib},
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

