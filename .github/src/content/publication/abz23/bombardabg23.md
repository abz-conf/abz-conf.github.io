---
title: "formal MVC: A Pattern for the Integration of ASM Specifications in UI Development"

authors:
  - Andrea Bombarda
  - Silvia Bonfanti
  - Angelo Gargantini


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
#  11 = "pub_short_paper"
#  12 = "pub_long_paper"
#  13 = "pub_invited_talk"
#  14 = "pub_phd_symposium"
publication_types:
  - 10  # default is 1 (conference), adjust as needed

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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_25.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-031-33163-3_25
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/bombardabg23/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/bombardabg23/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/bombardabg23/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/bombardabg23/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Using architectural patterns is of paramount importance for guaranteeing the correct functionality, maintainability and modularity, especially for complex software systems. The model-view-controller (MVC) pattern is typically used in user interfaces (UIs), since it allows the separation between the internal representation of the information and the way it is shown to users. The main problem of using this approach in a formal setting, where formal models are used to specify the requirements and prove safety properties, is that those models are not directly used within the MVC pattern and, thus, all the activities performed at model-level are somehow lost when implementing the UI. For this reason, in this paper, we present the formal MVC pattern (fMVC), an extension of the classical MVC where the model is a formal specification, written using Abstract State Machines. This pattern is supported by the AsmetaFMVCLib, which allows the user to link the formal model with the view and the controller by using simple Java annotations. We present the application of fMVC on a simple example of a calculator for explanatory purposes, then we apply it to the AMAN case study, which has inspired the definition of fMVC. We discuss the advantages of fMVC and its shortcomings, trying to identify the scenarios where it should be applied and possible alternatives.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_25.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_25.pdf" >}}

## Reference

```
% BibTex
@inproceedings{BombardaBG23,
  author       = {Andrea Bombarda and
                  Silvia Bonfanti and
                  Angelo Gargantini},
  editor       = {Uwe Gl{\"{a}}sser and
                  Jos{\'{e}} Creissac Campos and
                  Dominique M{\'{e}}ry and
                  Philippe A. Palanque},
  title        = {formal {MVC:} {A} Pattern for the Integration of {ASM} Specifications
                  in {UI} Development},
  booktitle    = {Rigorous State-Based Methods - 9th International Conference, {ABZ}
                  2023, Nancy, France, May 30 - June 2, 2023, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {14010},
  pages        = {340--357},
  publisher    = {Springer},
  year         = {2023},
  url          = {https://doi.org/10.1007/978-3-031-33163-3\_25},
  doi          = {10.1007/978-3-031-33163-3\_25},
  timestamp    = {Fri, 02 Jun 2023 21:23:53 +0200},
  biburl       = {https://dblp.org/rec/conf/zum/BombardaBG23.bib},
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

