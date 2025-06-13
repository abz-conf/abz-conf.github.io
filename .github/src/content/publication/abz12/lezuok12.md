---
title: "A Unified Processor Model for Compiler Verification and Simulation Using ASM"

authors:
  - Roland Lezuo
  - Andreas Krall


date: 2012-01-01

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


publication: "3rd International Conference on ASM, Alloy, B, VDM, and Z (ABZ'12)"
publication_short: "ABZ'12"

tags:
  - ABZ'12

categories: []

featured: false

# enable this for case studies
# projects:
#   - abz12

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-642-30885-7_24.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-642-30885-7_24
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/lezuok12/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/lezuok12/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/lezuok12/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/lezuok12/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

For safety critical embedded systems the correctness of the processor, toolchain and compiler is an important issue. Translation validation is one approach for compiler verification. A common semantic framework to represent source and target language is needed and Abstract State Machines (ASMs) are a well suited and established method. In this paper we present a method to show correctness of instruction selection by performing fully automated simulation proofs over symbolic execution traces of state transformations using an automated first-order theorem prover. We applied this approach to an industrial-strength compiler and created the ASM models in such a way that we are able to reuse them to create a cycle-accurate simulator. To achieve fast simulation we compile the ASM models to C++ and present the compilation scheme in this paper. Finally we present our preliminary results which indicate that a unified ASM model is sufficient for proving correct instruction selection and generating efficient cycle-accurate simulators.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-642-30885-7_24.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-642-30885-7_24.pdf" >}}

## Reference

```
% BibTex
@inproceedings{LezuoK12,
  author       = {Roland Lezuo and
                  Andreas Krall},
  editor       = {John Derrick and
                  John S. Fitzgerald and
                  Stefania Gnesi and
                  Sarfraz Khurshid and
                  Michael Leuschel and
                  Steve Reeves and
                  Elvinia Riccobene},
  title        = {A Unified Processor Model for Compiler Verification and Simulation
                  Using {ASM}},
  booktitle    = {Abstract State Machines, Alloy, B, VDM, and {Z} - Third International
                  Conference, {ABZ} 2012, Pisa, Italy, June 18-21, 2012. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {7316},
  pages        = {327--330},
  publisher    = {Springer},
  year         = {2012},
  url          = {https://doi.org/10.1007/978-3-642-30885-7\_24},
  doi          = {10.1007/978-3-642-30885-7\_24},
  timestamp    = {Sun, 02 Jun 2019 21:23:59 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/LezuoK12.bib},
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

