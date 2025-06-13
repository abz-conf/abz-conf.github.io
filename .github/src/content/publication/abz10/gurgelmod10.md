---
title: "Integrating SMT-Solvers in Z and B Tools"

authors:
  - Alessandro Cavalcante Gurgel
  - Valério Gutemberg de Medeiros
  - Marcel Vinícius Medeiros Oliveira
  - David Boris Paul Déharbe


date: 2010-01-01

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


publication: "2nd International Conference on ASM, Alloy, B, and Z (ABZ'10)"
publication_short: "ABZ'10"

tags:
  - ABZ'10

categories: []

featured: false

# enable this for case studies
# projects:
#   - abz10

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_45.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-642-11811-1_45
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/gurgelmod10/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/gurgelmod10/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/gurgelmod10/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/gurgelmod10/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

An important frequent task in both Z and B is the proof of verification conditions (VCs). In Z and B, VCs can be predicates to be discharged as a result of refinement steps, some proof about initialization properties or domain checking. Ideally, a tool that supports any Z and B technique should automatically discharge as many VCs as possible. Here, we present ZB2SMT, a Java package designed to clearly and directly integrate both Z and B tools to the satisfiability module theory (SMT) solvers such as veriT [1], a first-order logic (FOL) theorem prover that accepts the SMT syntax [4] as input. By having the SMT syntax as target we are able to easily integrate with further eleven automatic theorem provers. ZB2SMT is currently used by Batcave [2], an open source tool that generates VCs for the B method and CRefine [3], a tool that supports the Circus refinement calculus. Much of the VCs generated to validate the refinement law applications, are based on FOL predicates. Hence, CRefine uses the ZB2SMT package to automatically prove such predicates. The package integrates elements of Z and B predicates in a common language and transforms these predicates into SMT syntax. In this process, a SMT file is generated containing the predicate and some definitions. It is sent to a chosen SMT solver which yields a Boolean value for the predicate or it can be sent to several SMT solvers in a parallel approach. In order to improve the performance of the proof system, ZB2SMT has a module that can call different instances of solvers at different computers, according to a configuration file. It improves the proof process by allowing different strategies to be performed in parallel, reducing the verification time.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_45.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_45.pdf" >}}

## Reference

```
% BibTex
@inproceedings{GurgelMOD10,
  author       = {Alessandro Cavalcante Gurgel and
                  Val{\'{e}}rio Gutemberg de Medeiros and
                  Marcel Vin{\'{\i}}cius Medeiros Oliveira and
                  David Boris Paul D{\'{e}}harbe},
  editor       = {Marc Frappier and
                  Uwe Gl{\"{a}}sser and
                  Sarfraz Khurshid and
                  R{\'{e}}gine Laleau and
                  Steve Reeves},
  title        = {Integrating SMT-Solvers in {Z} and {B} Tools},
  booktitle    = {Abstract State Machines, Alloy, {B} and Z, Second International Conference,
                  {ABZ} 2010, Orford, QC, Canada, February 22-25, 2010. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {5977},
  pages        = {412--413},
  publisher    = {Springer},
  year         = {2010},
  url          = {https://doi.org/10.1007/978-3-642-11811-1\_45},
  doi          = {10.1007/978-3-642-11811-1\_45},
  timestamp    = {Tue, 14 May 2019 10:00:50 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/GurgelMOD10.bib},
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

