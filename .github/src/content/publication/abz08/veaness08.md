---
title: "Using Satisfiability Modulo Theories to Analyze Abstract State Machines (Abstract)"

authors:
  - Margus Veanes
  - Ando Saabas


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
#  11 = "pub_short_paper"
#  12 = "pub_long_paper"
#  13 = "pub_invited_talk"
publication_types:
  - 11   # default is 1 (conference), adjust as needed


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_42.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-540-87603-8_42
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/veaness08/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/veaness08/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/veaness08/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/veaness08/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

We look at a fragment of ASMs used to model protocol-like aspects of software systems. Such models are used industrially as part of documentation and oracles in model-based testing of application-level network protocols. Correctness assumptions about the model are often expressed through state invariants. An important problem is to validate the model prior to its use as an oracle. We discuss a technique of using Satisfiability Modulo Theories or SMT to perform bounded reachability analysis of such models. We use the Z3 solver for our implementation and we use AsmL as the modeling language.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_42.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_42.pdf" >}}

## Reference

```
% BibTex
@inproceedings{VeanesS08,
  author       = {Margus Veanes and
                  Ando Saabas},
  editor       = {Egon B{\"{o}}rger and
                  Michael J. Butler and
                  Jonathan P. Bowen and
                  Paul Boca},
  title        = {Using Satisfiability Modulo Theories to Analyze Abstract State Machines
                  (Abstract)},
  booktitle    = {Abstract State Machines, {B} and Z, First International Conference,
                  {ABZ} 2008, London, UK, September 16-18, 2008. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {5238},
  pages        = {355},
  publisher    = {Springer},
  year         = {2008},
  url          = {https://doi.org/10.1007/978-3-540-87603-8\_42},
  doi          = {10.1007/978-3-540-87603-8\_42},
  timestamp    = {Tue, 14 May 2019 10:00:50 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/VeanesS08.bib},
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

