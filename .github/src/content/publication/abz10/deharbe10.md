---
title: "Automatic Verification for a Class of Proof Obligations with SMT-Solvers"

authors:
  - David Déharbe


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_17.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-642-11811-1_17
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/deharbe10/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/deharbe10/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/deharbe10/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/deharbe10/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Software development in B and Event-B generates proof obligations that have to be discharged using theorem provers. The cost of such developments therefore depends directly on the degree of automation and efficiency of theorem proving techniques for the logics in which these lemmas are expressed. This paper presents and formalizes an approach to transform a class of proof obligations generated in the Rodin platform in a language that can be addressed by state-of-the-art SMT solvers. The work presented in the paper handles proof obligations with Booleans, integer arithmetics and basic sets.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_17.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_17.pdf" >}}

## Reference

```
% BibTex
@inproceedings{Deharbe10,
  author       = {David D{\'{e}}harbe},
  editor       = {Marc Frappier and
                  Uwe Gl{\"{a}}sser and
                  Sarfraz Khurshid and
                  R{\'{e}}gine Laleau and
                  Steve Reeves},
  title        = {Automatic Verification for a Class of Proof Obligations with SMT-Solvers},
  booktitle    = {Abstract State Machines, Alloy, {B} and Z, Second International Conference,
                  {ABZ} 2010, Orford, QC, Canada, February 22-25, 2010. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {5977},
  pages        = {217--230},
  publisher    = {Springer},
  year         = {2010},
  url          = {https://doi.org/10.1007/978-3-642-11811-1\_17},
  doi          = {10.1007/978-3-642-11811-1\_17},
  timestamp    = {Tue, 14 May 2019 10:00:50 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/Deharbe10.bib},
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

