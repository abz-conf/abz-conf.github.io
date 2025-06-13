---
title: "Event-B Code Generation: Type Extension with Theories"

authors:
  - Andrew Edmunds
  - Michael J. Butler
  - Issam Maamria
  - Renato Silva
  - Chris Lovell


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-642-30885-7_33.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-642-30885-7_33
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/edmundsbmsl12/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/edmundsbmsl12/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/edmundsbmsl12/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/edmundsbmsl12/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

The Event-B method is a formal modelling approach; our interest is the final step, of generating code for concurrent programs, from Event-B. Our Tasking Event-B tool integrates Event-B to facilitate code generation. The theory plug-in allows mathematical extensions to be added to an Event-B development. When working at the implementation level we need to consider how to translate the newly added types and operators into code. In this paper, we augment the theory plug-in, by adding a Translation Rules section to the tool. This enables us to define translation rules that map Event-B formulas to code. We illustrate the approach using a small case study, where we add a theory of arrays, and specify translation rules for generating Ada code.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-642-30885-7_33.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-642-30885-7_33.pdf" >}}

## Reference

```
% BibTex
@inproceedings{EdmundsBMSL12,
  author       = {Andrew Edmunds and
                  Michael J. Butler and
                  Issam Maamria and
                  Renato Silva and
                  Chris Lovell},
  editor       = {John Derrick and
                  John S. Fitzgerald and
                  Stefania Gnesi and
                  Sarfraz Khurshid and
                  Michael Leuschel and
                  Steve Reeves and
                  Elvinia Riccobene},
  title        = {Event-B Code Generation: Type Extension with Theories},
  booktitle    = {Abstract State Machines, Alloy, B, VDM, and {Z} - Third International
                  Conference, {ABZ} 2012, Pisa, Italy, June 18-21, 2012. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {7316},
  pages        = {365--368},
  publisher    = {Springer},
  year         = {2012},
  url          = {https://doi.org/10.1007/978-3-642-30885-7\_33},
  doi          = {10.1007/978-3-642-30885-7\_33},
  timestamp    = {Sun, 02 Jun 2019 21:23:59 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/EdmundsBMSL12.bib},
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

