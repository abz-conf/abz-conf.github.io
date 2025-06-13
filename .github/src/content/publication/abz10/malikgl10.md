---
title: "Translating Z to Alloy"

authors:
  - Petra Malik
  - Lindsay Groves
  - Clare Lenihan


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_28.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-642-11811-1_28
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/malikgl10/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/malikgl10/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/malikgl10/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/malikgl10/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Few tools are available to help with the difficult task of validating that a Z specification captures its intended meaning. One tool that has been proven to be useful for validating specifications is the Alloy Analyzer, an interactive tool for checking and visualising Alloy models. However, Z specifications need to be translated to Alloy notation to make use of the Alloy Analyzer. These translations have been performed manually so far, which is a cumbersome and error-prone activity. The aim of this paper is to explore to what extent this process can be automated. The paper identifies a subset of Z that can be straightforwardly translated to Alloy, and the translation for this subset is formalised. More complex constructs, like schemas, are harder to translate. The paper gives a brief overview of the problems, and discusses alternative translation approaches.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_28.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_28.pdf" >}}

## Reference

```
% BibTex
@inproceedings{MalikGL10,
  author       = {Petra Malik and
                  Lindsay Groves and
                  Clare Lenihan},
  editor       = {Marc Frappier and
                  Uwe Gl{\"{a}}sser and
                  Sarfraz Khurshid and
                  R{\'{e}}gine Laleau and
                  Steve Reeves},
  title        = {Translating {Z} to Alloy},
  booktitle    = {Abstract State Machines, Alloy, {B} and Z, Second International Conference,
                  {ABZ} 2010, Orford, QC, Canada, February 22-25, 2010. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {5977},
  pages        = {377--390},
  publisher    = {Springer},
  year         = {2010},
  url          = {https://doi.org/10.1007/978-3-642-11811-1\_28},
  doi          = {10.1007/978-3-642-11811-1\_28},
  timestamp    = {Tue, 14 May 2019 10:00:50 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/MalikGL10.bib},
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

