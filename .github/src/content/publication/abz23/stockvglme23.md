---
title: "Validation by Abstraction and Refinement"

authors:
  - Sebastian Stock 0002
  - Fabian Vu
  - David Geleßus
  - Michael Leuschel
  - Atif Mashkoor
  - Alexander Egyed


date: 2023-01-01

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

publication: "9th International Conference on Rigorous State Based Methods (ABZ'23)"
publication_short: "ABZ'23"

tags:
  - ABZ'23

categories: []

featured: false

# enable this for case studies
# projects:
#   - abz23

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_12.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-031-33163-3_12
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/stockvglme23/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/stockvglme23/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/stockvglme23/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/stockvglme23/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

While refinement can help structure the modeling and proving process, it also forces the modeler to introduce features in a particular order. This means that features deeper in the refinement chain cannot be validated in isolation, making some reasoning unnecessarily intricate. In this paper, we present the AVoiR (Abstraction-Validation Obligation-Refinement) framework to ease validation of such complex refinement chains. The triptych AVoiR framework operates as follows: 1) We first simplify a complex model by abstracting away the noise, i.e., removing the information unrelated to properties under analysis. 2) Using the Validation Obligations (VOs) technique, we formalize the validation tasks of the desired property. 3) Finally, we trickle down the validation results by establishing the noiseless model as a parent of the initially investigated model through the standard refinement relationship. Furthermore, by using the technique of VO refinement, we establish the VOs of the abstract model on the initial model. We use a case study from the aviation domain to show the proposed framework’s effectiveness.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_12.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_12.pdf" >}}

## Reference

```
% BibTex
@inproceedings{StockVGLME23,
  author       = {Sebastian Stock and
                  Fabian Vu and
                  David Gele{\ss}us and
                  Michael Leuschel and
                  Atif Mashkoor and
                  Alexander Egyed},
  editor       = {Uwe Gl{\"{a}}sser and
                  Jos{\'{e}} Creissac Campos and
                  Dominique M{\'{e}}ry and
                  Philippe A. Palanque},
  title        = {Validation by Abstraction and Refinement},
  booktitle    = {Rigorous State-Based Methods - 9th International Conference, {ABZ}
                  2023, Nancy, France, May 30 - June 2, 2023, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {14010},
  pages        = {160--178},
  publisher    = {Springer},
  year         = {2023},
  url          = {https://doi.org/10.1007/978-3-031-33163-3\_12},
  doi          = {10.1007/978-3-031-33163-3\_12},
  timestamp    = {Fri, 02 Jun 2023 21:23:53 +0200},
  biburl       = {https://dblp.org/rec/conf/zum/StockVGLME23.bib},
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

