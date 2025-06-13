---
title: "On an Extensible Rule-Based Prover for Event-B"

authors:
  - Issam Maamria
  - Michael J. Butler
  - Andrew Edmunds
  - Abdolbaghi Rezazadeh


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
#  11 = "pub_short_paper"
#  12 = "pub_long_paper"
#  13 = "pub_invited_talk"
publication_types:
  - 11   # default is 1 (conference), adjust as needed


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_40.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-642-11811-1_40
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/maamriaber10/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/maamriaber10/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/maamriaber10/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/maamriaber10/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Event-B [1] is a formalism for discrete system modelling. The Rodin platform [2] provides a toolset to carry out specification, refinement and proof in Event-B. The importance of proofs as part of formal modelling cannot be emphasised enough, and as such, it is imperative to provide effective tool support for it. An important aspect of this support is the extensibility of the prover, and more pressingly, how its soundness is preserved while allowing extensibility. Rodin has a limited support for adding rules as this requires (a) a deep understanding of the internal architecture and (b) knowledge of the Java language. Our approach attempts to provide support for user-defined proof rules. We initially focus on supporting rewrite rules to enhance the rewriting capabilities of Rodin. To achieve this objective, we introduce a theory construct distinct from contexts and machines. The theory construct provides a platform for the users to define rewrite rules both conditional and unconditional. As part of rule definition, users decide whether the rule is to be applied automatically or interactively. Each defined rule gives rise to proof obligations that serve to verify its conservativity. In this respect, it is required that validity and well-definedness are preserved by rules. After the conservativity of all rules contained in a theory is established, the theory can then be deployed and available to the proving activity. In order to apply rewrite rules, it is necessary to single out applicable rules to any given sequent. This is achieved through a pattern matching mechanism which is implemented as an extension to Rodin. Our approach has two advantages. Firstly, it offers a uniform mechanism to add proof rule without the need to write Java code. Secondly, it provides a means to verify added rules using proof obligations. Our work is still in progress, and research has to be carried out to (a) cover a larger set of rewrite and inference rules, and (b) provide guidelines to help the theory developer with deciding whether a given rule should be applied automatically.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_40.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_40.pdf" >}}

## Reference

```
% BibTex
@inproceedings{MaamriaBER10,
  author       = {Issam Maamria and
                  Michael J. Butler and
                  Andrew Edmunds and
                  Abdolbaghi Rezazadeh},
  editor       = {Marc Frappier and
                  Uwe Gl{\"{a}}sser and
                  Sarfraz Khurshid and
                  R{\'{e}}gine Laleau and
                  Steve Reeves},
  title        = {On an Extensible Rule-Based Prover for Event-B},
  booktitle    = {Abstract State Machines, Alloy, {B} and Z, Second International Conference,
                  {ABZ} 2010, Orford, QC, Canada, February 22-25, 2010. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {5977},
  pages        = {407},
  publisher    = {Springer},
  year         = {2010},
  url          = {https://doi.org/10.1007/978-3-642-11811-1\_40},
  doi          = {10.1007/978-3-642-11811-1\_40},
  timestamp    = {Tue, 14 May 2019 10:00:50 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/MaamriaBER10.bib},
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

