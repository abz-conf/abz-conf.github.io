---
title: "Refinement Plans for Informed Formal Design"

authors:
  - Gudmund Grov
  - Andrew Ireland
  - Maria Teresa Llano


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
#  10 = "pub_short_paper"
#  11 = "pub_long_paper"
publication_types:
  - 1   # default is 1 (conference), adjust as needed

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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-642-30885-7_15.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-642-30885-7_15
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/grovil12/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/grovil12/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/grovil12/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/grovil12/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Refinement is a powerful technique for tackling the complexities that arise when formally modelling systems. Here we focus on a posit-and-prove style of refinement, and specifically where a user requires guidance in order to overcome a failed refinement step. We take an integrated approach – combining the complementary strengths of top-down planning and bottom-up theory formation. In this paper we focus mainly on the planning perspective. Specifically, we propose a new technique called refinement plans which combines both modelling and reasoning perspectives. When a refinement step fails, refinement plans provide a basis for automatically generating modelling guidance by abstracting away from the details of low-level proof failures. The refinement plans described here are currently being implemented for the Event-B modelling formalism, and have been assessed on paper using case studies drawn from the literature. Longer-term, our aim is to identify refinement plans that are applicable to a range of modelling formalisms.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-642-30885-7_15.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-642-30885-7_15.pdf" >}}

## Reference

```
% BibTex
@inproceedings{GrovIL12,
  author       = {Gudmund Grov and
                  Andrew Ireland and
                  Maria Teresa Llano},
  editor       = {John Derrick and
                  John S. Fitzgerald and
                  Stefania Gnesi and
                  Sarfraz Khurshid and
                  Michael Leuschel and
                  Steve Reeves and
                  Elvinia Riccobene},
  title        = {Refinement Plans for Informed Formal Design},
  booktitle    = {Abstract State Machines, Alloy, B, VDM, and {Z} - Third International
                  Conference, {ABZ} 2012, Pisa, Italy, June 18-21, 2012. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {7316},
  pages        = {208--222},
  publisher    = {Springer},
  year         = {2012},
  url          = {https://doi.org/10.1007/978-3-642-30885-7\_15},
  doi          = {10.1007/978-3-642-30885-7\_15},
  timestamp    = {Sun, 02 Jun 2019 21:23:59 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/GrovIL12.bib},
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

