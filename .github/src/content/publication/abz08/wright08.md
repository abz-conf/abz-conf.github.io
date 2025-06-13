---
title: "Using EventB to Create a Virtual Machine Instruction Set Architecture"

authors:
  - Stephen Wright


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_21.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-540-87603-8_21
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/wright08/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/wright08/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/wright08/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/wright08/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

A Virtual Machine (VM) is a program running on a conventional microprocessor that emulates the binary instruction set, registers, and memory space of an idealized computing machine, a well-known example being the Java Virtual Machine (JVM). Despite there being many binary Instruction Set Architectures (ISA) in existence, all share a set of core properties which have been tailored to their particular applications. An abstract model may capture these generic properties and be subsequently refined to a particular machine, providing a reusable template for development of formally proven ISAs: this is a task to which the EventB [16,18] notation is well suited. This paper describes a project to use the RODIN tool-set [24] to perform such a process, ultimately producing the MIDAS (Microprocessor Instruction and Data Abstraction System) VM, capable of running binary executables compiled from high-level languages such as C [9]. The abstract model is incrementally refined to a model capable of automatic translation to C source code, and compilation for a hardware platform using a standard compiler. A second C compiler, targeted to the VM itself, allows C programs to be executed on it.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_21.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_21.pdf" >}}

## Reference

```
% BibTex
@inproceedings{Wright08,
  author       = {Stephen Wright},
  editor       = {Egon B{\"{o}}rger and
                  Michael J. Butler and
                  Jonathan P. Bowen and
                  Paul Boca},
  title        = {Using EventB to Create a Virtual Machine Instruction Set Architecture},
  booktitle    = {Abstract State Machines, {B} and Z, First International Conference,
                  {ABZ} 2008, London, UK, September 16-18, 2008. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {5238},
  pages        = {265--279},
  publisher    = {Springer},
  year         = {2008},
  url          = {https://doi.org/10.1007/978-3-540-87603-8\_21},
  doi          = {10.1007/978-3-540-87603-8\_21},
  timestamp    = {Tue, 14 May 2019 10:00:50 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/Wright08.bib},
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

