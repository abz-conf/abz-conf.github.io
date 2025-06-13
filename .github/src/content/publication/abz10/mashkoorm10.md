---
title: "Towards Validation of Requirements Models"

authors:
  - Atif Mashkoor
  - Abderrahman Matoussi


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_38.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-642-11811-1_38
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/mashkoorm10/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/mashkoorm10/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/mashkoorm10/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/mashkoorm10/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

The use of formal methods for software development is escalating over the period of time. The input to this formal specification phase is often the documents obtained during the requirements analysis activity which are either textual or semi-formal. Now there is a traceability gap between analysis and specification phases as verification of the semi-formal analysis model is difficult because of poor understandability of lower level of formalism of verification tools and validation of the formal specification is difficult for customers due to their inability to understand formal models. Our objective is to bridge this gap by a gradual introduction of formalism into the requirement model in order to facilitate its validation.We analyse our requirements with KAOS (Knowledge Acquisition in autOmated Specification) [1] which is a goal-oriented methodology for requirements modeling, then we translate the KAOS goal model, following our derived precise semantics [3], into an Event-B [2] formal specification, and finally we rigourously animate the obtained specification in order to validate its conformance to original requirements with the approach defined in [4].

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_38.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_38.pdf" >}}

## Reference

```
% BibTex
@inproceedings{MashkoorM10,
  author       = {Atif Mashkoor and
                  Abderrahman Matoussi},
  editor       = {Marc Frappier and
                  Uwe Gl{\"{a}}sser and
                  Sarfraz Khurshid and
                  R{\'{e}}gine Laleau and
                  Steve Reeves},
  title        = {Towards Validation of Requirements Models},
  booktitle    = {Abstract State Machines, Alloy, {B} and Z, Second International Conference,
                  {ABZ} 2010, Orford, QC, Canada, February 22-25, 2010. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {5977},
  pages        = {404},
  publisher    = {Springer},
  year         = {2010},
  url          = {https://doi.org/10.1007/978-3-642-11811-1\_38},
  doi          = {10.1007/978-3-642-11811-1\_38},
  timestamp    = {Tue, 14 May 2019 10:00:50 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/MashkoorM10.bib},
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

