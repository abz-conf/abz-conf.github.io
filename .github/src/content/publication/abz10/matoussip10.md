---
title: "Improving Traceability between KAOS Requirements Models and B Specifications"

authors:
  - Abderrahman Matoussi
  - Dorian Petit


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_36.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-642-11811-1_36
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/matoussip10/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/matoussip10/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/matoussip10/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/matoussip10/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

The aim of this paper is to give some feedback about the B specification [1] of a localization software component which is one of the most critical parts in the land transportation system. The main difficulties when we develop a localization component is: (i) to find the correct algorithm that merges positioning data (ii) to take into account all the properties we have to deal with. At this stage, we think that a semi formal model such as KAOS [2], a goal-based requirements engineering method, will be very useful in order to have guidelines on how to do. For that, we will just focus on the architecture of the B specifications and how using KAOS help us to build it. Since goals play an important role in requirements engineering process, rather than establishing traceability from the KAOS requirements model as a whole, we propose to establish traceability from individual goals that are part of the KAOS goal model. The main idea is to specify a correspondence rule between each concept of the goal model and B elements. Up to now, we consider only functional goals of type Achieve [2]. A B machine is associated to each goal. This machine contains an operation that “realizes” the goal; i.e. it describes the “work” to perform to reach the goal, in terms of generalized substitutions. The refinement of a goal is represented by a B refinement machine that refines the machine; the abstract operation is refined by a concrete one. This operation is built by combining operations of the machines that correspond to the sub-goals of the more abstract goal and are included in the B machine via the inclusion relationship. The nature of the combination depends on the goal refinement pattern (Milestone, AND, OR). The reader can refer to [3] for more details. The main contribution of our approach is that it establishes the first brick toward the construction of the bridge between the nonformal and the formal worlds as narrow and concise as possible. Furthermore, by discharging the proof obligations generated by the B refinement process, we can prove some properties of consistency on the goal model. Regarding the different KAOS goal model concepts, we need now to consider the translation of the concepts of domain properties and non functional goals.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_36.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_36.pdf" >}}

## Reference

```
% BibTex
@inproceedings{MatoussiP10,
  author       = {Abderrahman Matoussi and
                  Dorian Petit},
  editor       = {Marc Frappier and
                  Uwe Gl{\"{a}}sser and
                  Sarfraz Khurshid and
                  R{\'{e}}gine Laleau and
                  Steve Reeves},
  title        = {Improving Traceability between {KAOS} Requirements Models and {B}
                  Specifications},
  booktitle    = {Abstract State Machines, Alloy, {B} and Z, Second International Conference,
                  {ABZ} 2010, Orford, QC, Canada, February 22-25, 2010. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {5977},
  pages        = {401--402},
  publisher    = {Springer},
  year         = {2010},
  url          = {https://doi.org/10.1007/978-3-642-11811-1\_36},
  doi          = {10.1007/978-3-642-11811-1\_36},
  timestamp    = {Tue, 14 May 2019 10:00:50 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/MatoussiP10.bib},
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

