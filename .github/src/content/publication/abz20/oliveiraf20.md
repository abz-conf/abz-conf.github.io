---
title: "Verifying SGAC Access Control Policies: A Comparison of ProB, Alloy and Z3"

authors:
  - Diego de Azevedo Oliveira
  - Marc Frappier


date: 2020-01-01

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

publication: "7th International Conference on Rigorous State Based Methods (ABZ'20)"
publication_short: "ABZ'20"

tags:
  - ABZ'20

categories: []

featured: false

# enable this for case studies
# projects:
#   - abz20

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-030-48077-6_15.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-030-48077-6_15
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/oliveiraf20/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/oliveiraf20/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/oliveiraf20/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/oliveiraf20/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

This paper describes the formalisation of SGAC access control policies using Z3 and then we compare the performance with ProB and Alloy. SGAC is an attribute-based, fine-grain access control model that uses acyclic subject and resource graphs to provide rule inheritance and streamline policy specification. To ensure patient privacy and safety, four types of properties are checked: accessibility, availability, contextuality and rule effectiveness. Automatic translation of SGAC policies into each specification language has been defined. ProB offers the best verification performances, by two orders of magnitude. The performances of Alloy and Z3 are similar.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-030-48077-6_15.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-030-48077-6_15.pdf" >}}

## Reference

```
% BibTex
@inproceedings{OliveiraF20,
  author       = {Diego de Azevedo Oliveira and
                  Marc Frappier},
  editor       = {Alexander Raschke and
                  Dominique M{\'{e}}ry and
                  Frank Houdek},
  title        = {Verifying {SGAC} Access Control Policies: {A} Comparison of ProB,
                  Alloy and {Z3}},
  booktitle    = {Rigorous State-Based Methods - 7th International Conference, {ABZ}
                  2020, Ulm, Germany, May 27-29, 2020, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {12071},
  pages        = {223--229},
  publisher    = {Springer},
  year         = {2020},
  url          = {https://doi.org/10.1007/978-3-030-48077-6\_15},
  doi          = {10.1007/978-3-030-48077-6\_15},
  timestamp    = {Mon, 25 May 2020 12:33:39 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/OliveiraF20.bib},
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

