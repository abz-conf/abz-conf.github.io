---
title: "Towards Formalizing Network Architectural Descriptions"

authors:
  - Joud S. Khoury
  - Chaouki T. Abdallah
  - Gregory L. Heileman


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_11.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-642-11811-1_11
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/khouryah10/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/khouryah10/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/khouryah10/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/khouryah10/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Despite the rich literature on network architecture and communication system design, the current practice of describing architectures remains informal and idiosyncratic. Such practice has evolved based on idiomatic terminology and hence, it is failing to provide a formal framework for representing and for reasoning about network architectures. This state of affairs has led to the overloading of architectural terms, and to the emergence of a large body of network architecture proposals with no clear indication of their cross similarities, their compatibility points, their unique properties, and their architectural performance and soundness. Formalizing network architectural descriptions is therefore a timely contribution, and this paper presents a first step in that direction. The paper builds upon architectural style modeling concepts from the software engineering field, and applies them to the network architecture space. Our approach is presented through a case study detailing a formal model for a common class of network architectures. The model uses a simple declarative language based on relations and first-order logic.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_11.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_11.pdf" >}}

## Reference

```
% BibTex
@inproceedings{KhouryAH10,
  author       = {Joud S. Khoury and
                  Chaouki T. Abdallah and
                  Gregory L. Heileman},
  editor       = {Marc Frappier and
                  Uwe Gl{\"{a}}sser and
                  Sarfraz Khurshid and
                  R{\'{e}}gine Laleau and
                  Steve Reeves},
  title        = {Towards Formalizing Network Architectural Descriptions},
  booktitle    = {Abstract State Machines, Alloy, {B} and Z, Second International Conference,
                  {ABZ} 2010, Orford, QC, Canada, February 22-25, 2010. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {5977},
  pages        = {132--145},
  publisher    = {Springer},
  year         = {2010},
  url          = {https://doi.org/10.1007/978-3-642-11811-1\_11},
  doi          = {10.1007/978-3-642-11811-1\_11},
  timestamp    = {Wed, 07 Dec 2022 23:14:20 +0100},
  biburl       = {https://dblp.org/rec/conf/asm/KhouryAH10.bib},
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

