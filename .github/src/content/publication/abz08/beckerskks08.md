---
title: "Direct Support for Model Checking Abstract State Machines by Utilizing Simulation"

authors:
  - Jörg Beckers
  - Daniel Klünder
  - Stefan Kowalewski
  - Bastian Schlich


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_10.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-540-87603-8_10
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/beckerskks08/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/beckerskks08/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/beckerskks08/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/beckerskks08/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

This paper presents an approach to model checking abstract state machines (ASMs) without the need for translation of the ASM specification into the modeling language of an existing model checker. Instead, our model checker [mc]square uses the simulation capabilities of CoreASM to build the state space, thereby directly supporting ASMs and circumventing a possible loss of expressiveness in a translation process. This enables our approach to present counterexamples and witnesses directly as sequences of ASM states and at the same time supports the major features of CoreASM like distributed ASMs, n-ary functions or extended rule forms. We show the applicability of this approach in a case study that also reveals possible improvements desirable for minimizing the duration needed for building the state space and its memory consumption.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_10.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_10.pdf" >}}

## Reference

```
% BibTex
@inproceedings{BeckersKKS08,
  author       = {J{\"{o}}rg Beckers and
                  Daniel Kl{\"{u}}nder and
                  Stefan Kowalewski and
                  Bastian Schlich},
  editor       = {Egon B{\"{o}}rger and
                  Michael J. Butler and
                  Jonathan P. Bowen and
                  Paul Boca},
  title        = {Direct Support for Model Checking Abstract State Machines by Utilizing
                  Simulation},
  booktitle    = {Abstract State Machines, {B} and Z, First International Conference,
                  {ABZ} 2008, London, UK, September 16-18, 2008. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {5238},
  pages        = {112--124},
  publisher    = {Springer},
  year         = {2008},
  url          = {https://doi.org/10.1007/978-3-540-87603-8\_10},
  doi          = {10.1007/978-3-540-87603-8\_10},
  timestamp    = {Tue, 14 May 2019 10:00:50 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/BeckersKKS08.bib},
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

