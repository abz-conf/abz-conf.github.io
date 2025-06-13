---
title: "Reactivising Classical B"

authors:
  - Steve Dunne
  - Frank Zeyda


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
#  10 = "pub_short_paper"
#  11 = "pub_long_paper"
publication_types:
  - 1   # default is 1 (conference), adjust as needed

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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_23.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-642-11811-1_23
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/dunnez10/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/dunnez10/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/dunnez10/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/dunnez10/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

We propose what is essentially a recasting of Circus, the Z-and-CSP-based concurrent language for refinement, into a B context by means of a modest extension of classical B which introduces a new structural component called a reactive-B process. This specifies the channels via which the process can communicate with its environment, and actions by which its behaviour is specified. Such actions are expressed in a new action notation in the same syntactic spirit as B’s Abstract Machine Notation, but with a similar Unifying Theories of Programming relational semantics to that of the actions of Circus. Crucially, by including ordinary abstract machines these reactive-B processes can also acquire persistent state, which their actions can manipulate by invoking the operations of those included machines.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_23.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_23.pdf" >}}

## Reference

```
% BibTex
@inproceedings{DunneZ10,
  author       = {Steve Dunne and
                  Frank Zeyda},
  editor       = {Marc Frappier and
                  Uwe Gl{\"{a}}sser and
                  Sarfraz Khurshid and
                  R{\'{e}}gine Laleau and
                  Steve Reeves},
  title        = {Reactivising Classical {B}},
  booktitle    = {Abstract State Machines, Alloy, {B} and Z, Second International Conference,
                  {ABZ} 2010, Orford, QC, Canada, February 22-25, 2010. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {5977},
  pages        = {302--318},
  publisher    = {Springer},
  year         = {2010},
  url          = {https://doi.org/10.1007/978-3-642-11811-1\_23},
  doi          = {10.1007/978-3-642-11811-1\_23},
  timestamp    = {Mon, 05 Feb 2024 20:35:41 +0100},
  biburl       = {https://dblp.org/rec/conf/asm/DunneZ10.bib},
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

