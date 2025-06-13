---
title: "Architecture as an Independent Variable for Aspect-Oriented Application Descriptions"

authors:
  - Hamid Bagheri
  - Kevin J. Sullivan


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_32.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-642-11811-1_32
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/bagheris10/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/bagheris10/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/bagheris10/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/bagheris10/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Software architecture researchers have long assumed that architecture independent application descriptions can be mapped to architectures in many styles, that results vary in quality attributes, and that the choice of a style is driven by consideration of such attributes. In our previous work [1], we demonstrated the feasibility of formally treating architectural style as an independent variable. Given an application description and architectural style description in Alloy [3], we map them to software architecture description that refines the given application in conformance with the given style. To represent a map, we extend a traditional architectural style description (in Alloy) with predicates for mapping application descriptions in a given style to architectural descriptions in the given style. These predicates take application descriptions as parameters and define relationships required to hold between them and computed architectural descriptions. Given an application description, and a map, Alloy computes corresponding architectural descriptions guaranteed to conform to the given architectural style. This paper extends our earlier work to aspect-oriented structures. In doing so, we describe an aspect-enabled application description style and a map taking application descriptions in this style to pipe-and-filter architectures. We use the Alloy Analyzer to compute architecture descriptions, represented as satisfying solutions to the constraints of a map given an application description. The A2A transformer application, developed in our research group, then converts the Alloy-computed architecture to an architecture description in a traditional architecture description language (ADL): here, AspectualACME[2].

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_32.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_32.pdf" >}}

## Reference

```
% BibTex
@inproceedings{BagheriS10,
  author       = {Hamid Bagheri and
                  Kevin J. Sullivan},
  editor       = {Marc Frappier and
                  Uwe Gl{\"{a}}sser and
                  Sarfraz Khurshid and
                  R{\'{e}}gine Laleau and
                  Steve Reeves},
  title        = {Architecture as an Independent Variable for Aspect-Oriented Application
                  Descriptions},
  booktitle    = {Abstract State Machines, Alloy, {B} and Z, Second International Conference,
                  {ABZ} 2010, Orford, QC, Canada, February 22-25, 2010. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {5977},
  pages        = {395},
  publisher    = {Springer},
  year         = {2010},
  url          = {https://doi.org/10.1007/978-3-642-11811-1\_32},
  doi          = {10.1007/978-3-642-11811-1\_32},
  timestamp    = {Tue, 14 May 2019 10:00:50 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/BagheriS10.bib},
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

