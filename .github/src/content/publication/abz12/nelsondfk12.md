---
title: "Toward a More Complete Alloy"

authors:
  - Timothy Nelson 0001
  - Daniel J. Dougherty
  - Kathi Fisler
  - Shriram Krishnamurthi


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-642-30885-7_10.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-642-30885-7_10
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/nelsondfk12/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/nelsondfk12/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/nelsondfk12/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/nelsondfk12/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Many model-finding tools, such as Alloy, charge users with providing bounds on the sizes of models. It would be preferable to automatically compute sufficient upper-bounds whenever possible. The Bernays-Schönfinkel-Ramsey fragment of first-order logic can relieve users of this burden in some cases: its sentences are satisfiable iff they are satisfied in a finite model, whose size is computable from the input problem. Researchers have observed, however, that the class of sentences for which such a theorem holds is richer in a many-sorted framework—which Alloy inhabits—than in the one-sorted case. This paper studies this phenomenon in the general setting of order-sorted logic supporting overloading and empty sorts. We establish a syntactic condition generalizing the Bernays-Schönfinkel-Ramsey form that ensures the Finite Model Property. We give a linear-time algorithm for deciding this condition and a polynomial-time algorithm for computing the bound on model sizes. As a consequence, model-finding is a complete decision procedure for sentences in this class. Our work has been incorporated into Margrave, a tool for policy analysis, and applies in real-world situations.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-642-30885-7_10.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-642-30885-7_10.pdf" >}}

## Reference

```
% BibTex
@inproceedings{NelsonDFK12,
  author       = {Timothy Nelson and
                  Daniel J. Dougherty and
                  Kathi Fisler and
                  Shriram Krishnamurthi},
  editor       = {John Derrick and
                  John S. Fitzgerald and
                  Stefania Gnesi and
                  Sarfraz Khurshid and
                  Michael Leuschel and
                  Steve Reeves and
                  Elvinia Riccobene},
  title        = {Toward a More Complete Alloy},
  booktitle    = {Abstract State Machines, Alloy, B, VDM, and {Z} - Third International
                  Conference, {ABZ} 2012, Pisa, Italy, June 18-21, 2012. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {7316},
  pages        = {136--149},
  publisher    = {Springer},
  year         = {2012},
  url          = {https://doi.org/10.1007/978-3-642-30885-7\_10},
  doi          = {10.1007/978-3-642-30885-7\_10},
  timestamp    = {Mon, 26 Jun 2023 20:48:45 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/NelsonDFK12.bib},
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

