---
title: "Proving the Safety of a Sliding Window Protocol with Event-B"

authors:
  - Sophie Coudert


date: 2021-01-01

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

publication: "8th International Conference on Rigorous State Based Methods (ABZ'21)"
publication_short: "ABZ'21"

tags:
  - ABZ'21

categories: []

featured: false

# enable this for case studies
# projects:
#   - abz21

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-030-77543-8_4.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-030-77543-8_4
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/coudert21/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/coudert21/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/coudert21/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/coudert21/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

This paper presents an Event-B modeling of the general version of the Sliding Window Protocol (SWP). SWPs ensure reliable data transfer over unreliable media by routing frames together with their indexes. Providing SWPs with formal guarantees is recognized to be quite complex. The experiment we present here shows that Event-B refinement is a suitable approach to ensure the safety of the protocol. First a simple model is developed with unbounded frame indexes. Then bounded indexes and modular arithmetic are introduced, as concrete indexes have fixed size. At this “hybrid” level, unbounded indexes are not used any more in computations but they are still useful to express some properties. Finally, abstract general media are refined towards queues, as an example of implementation. All unbounded indexes fully disappear in the final model.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-030-77543-8_4.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-030-77543-8_4.pdf" >}}

## Reference

```
% BibTex
@inproceedings{Coudert21,
  author       = {Sophie Coudert},
  editor       = {Alexander Raschke and
                  Dominique M{\'{e}}ry},
  title        = {Proving the Safety of a Sliding Window Protocol with Event-B},
  booktitle    = {Rigorous State-Based Methods - 8th International Conference, {ABZ}
                  2021, Ulm, Germany, June 9-11, 2021, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {12709},
  pages        = {50--65},
  publisher    = {Springer},
  year         = {2021},
  url          = {https://doi.org/10.1007/978-3-030-77543-8\_4},
  doi          = {10.1007/978-3-030-77543-8\_4},
  timestamp    = {Wed, 09 Jun 2021 12:14:31 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/Coudert21.bib},
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

