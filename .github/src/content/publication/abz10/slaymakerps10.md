---
title: "Formalising and Validating RBAC-to-XACML Translation Using Lightweight Formal Methods"

authors:
  - Mark Slaymaker
  - David J. Power
  - Andrew Simpson 0001


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_26.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-642-11811-1_26
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/slaymakerps10/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/slaymakerps10/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/slaymakerps10/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/slaymakerps10/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

The topic of access control has received a new lease of life in recent years as the need for assurance that the correct access control policy is in place is seen by many as crucial to providing assurance to individuals that their data is being treated appropriately. This trend is likely to continue with the increase in popularity of social networking sites and shifts to ‘cloud’-like commercial services: in both contexts, a clear statement of “who can do what” to one’s data is key in engendering trust. While approaches such as role-based access control (RBAC) provide a degree of abstraction, therefore increasing manageability and accessibility, policy languages such as the XML-based XACML provide greater degrees of expressibility—and, as a result, increased complexity. In this paper we explore how the mutual benefits of both RBAC and XACML, and Alloy and Z, may be used to best effect. RBAC is used as an accessible conceptual model; XACML is used as a language of implementation. Our concern is to facilitate the construction and reuse of role-based policies, which may subsequently be deployed in terms of XACML. We wish to provide assurance that these representations and transformations are, in some sense, correct. To this end, we consider formal models of both RBAC and XACML in terms of Z. We also describe how we have taken initial steps in utilising the Alloy Analyzer tool to provide a level of assurance that the two representations are consistent.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_26.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_26.pdf" >}}

## Reference

```
% BibTex
@inproceedings{SlaymakerPS10,
  author       = {Mark Slaymaker and
                  David J. Power and
                  Andrew Simpson},
  editor       = {Marc Frappier and
                  Uwe Gl{\"{a}}sser and
                  Sarfraz Khurshid and
                  R{\'{e}}gine Laleau and
                  Steve Reeves},
  title        = {Formalising and Validating RBAC-to-XACML Translation Using Lightweight
                  Formal Methods},
  booktitle    = {Abstract State Machines, Alloy, {B} and Z, Second International Conference,
                  {ABZ} 2010, Orford, QC, Canada, February 22-25, 2010. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {5977},
  pages        = {349--362},
  publisher    = {Springer},
  year         = {2010},
  url          = {https://doi.org/10.1007/978-3-642-11811-1\_26},
  doi          = {10.1007/978-3-642-11811-1\_26},
  timestamp    = {Thu, 20 Jun 2024 12:26:13 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/SlaymakerPS10.bib},
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

