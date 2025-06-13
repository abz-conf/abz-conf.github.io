---
title: "Staged Evaluation of Partial Instances in a Relational Model Finder"

authors:
  - Vajih Montaghami
  - Derek Rayside


date: 2014-01-01

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
  - 11  # default is 1 (conference), adjust as needed

publication: "4th International Conference on ASM, Alloy, B, TLA, VDM, and Z (ABZ'14)"
publication_short: "ABZ'14"

tags:
  - ABZ'14

categories: []

featured: false

# enable this for case studies
# projects:
#   - abz14

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-662-43652-3_32.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-662-43652-3_32
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/montaghamir14/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/montaghamir14/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/montaghamir14/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/montaghamir14/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

To evaluate a property of the form ‘for all x there exists some y’ with a relational model finder requires a generator axiom to force all instances of y to exist in the universe of discourse. Without the generator axiom the model finder will produce a spurious counter-example by simply not including an important instance of y. Generator axioms are generally considered to be expensive to evaluate, significantly limiting the scope of the analysis. We demonstrate that evaluating the generator axiom in a separate stage from the property results in substantial improvements in analysis speed and scalability

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-662-43652-3_32.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-662-43652-3_32.pdf" >}}

## Reference

```
% BibTex
@inproceedings{MontaghamiR14,
  author       = {Vajih Montaghami and
                  Derek Rayside},
  editor       = {Yamine A{\"{\i}}t Ameur and
                  Klaus{-}Dieter Schewe},
  title        = {Staged Evaluation of Partial Instances in a Relational Model Finder},
  booktitle    = {Abstract State Machines, Alloy, B, TLA, VDM, and {Z} - 4th International
                  Conference, {ABZ} 2014, Toulouse, France, June 2-6, 2014. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {8477},
  pages        = {318--323},
  publisher    = {Springer},
  year         = {2014},
  url          = {https://doi.org/10.1007/978-3-662-43652-3\_32},
  doi          = {10.1007/978-3-662-43652-3\_32},
  timestamp    = {Tue, 14 May 2019 10:00:50 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/MontaghamiR14.bib},
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

