---
title: "Towards Modelling Obligations in Event-B"

authors:
  - Juan Bicarregui
  - Alvaro Arenas
  - Benjamin Aziz
  - Philippe Massonet
  - Christophe Ponsard


date: 2008-01-01

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

publication: "1st International Conference on ASM, B, and Z (ABZ'08)"
publication_short: "ABZ'08"

tags:
  - ABZ'08

categories: []

featured: false

# enable this for case studies
# projects:
#   - abz08

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_15.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-540-87603-8_15
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/bicarreguiaamp08/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/bicarreguiaamp08/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/bicarreguiaamp08/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/bicarreguiaamp08/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

We propose a syntactic extension of Event-B incorporating a limited notion of obligation described by triggers. The trigger of an event is the dual of the guard: when a guard is not true, an event must not occur, whereas when a trigger is true, the event must occur. The obligation imposed by a trigger is interpreted as a constraint on when the other events are permitted. For example, the simplest trigger next, which states that the event must be the next one to be executed when the trigger becomes true, is modelled as an extra guard on each of the other events which prohibits their execution at this time. In this paper we describe the modelling of triggers in Event-B, and analyse refinement and abstract scheduling of triggered events.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_15.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_15.pdf" >}}

## Reference

```
% BibTex
@inproceedings{BicarreguiAAMP08,
  author       = {Juan Bicarregui and
                  Alvaro Arenas and
                  Benjamin Aziz and
                  Philippe Massonet and
                  Christophe Ponsard},
  editor       = {Egon B{\"{o}}rger and
                  Michael J. Butler and
                  Jonathan P. Bowen and
                  Paul Boca},
  title        = {Towards Modelling Obligations in Event-B},
  booktitle    = {Abstract State Machines, {B} and Z, First International Conference,
                  {ABZ} 2008, London, UK, September 16-18, 2008. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {5238},
  pages        = {181--194},
  publisher    = {Springer},
  year         = {2008},
  url          = {https://doi.org/10.1007/978-3-540-87603-8\_15},
  doi          = {10.1007/978-3-540-87603-8\_15},
  timestamp    = {Thu, 14 Oct 2021 10:31:49 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/BicarreguiAAMP08.bib},
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

