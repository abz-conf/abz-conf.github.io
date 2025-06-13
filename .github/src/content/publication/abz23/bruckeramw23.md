---
title: "Using Deep Ontologies in Formal Software Engineering"

authors:
  - Achim D. Brucker
  - Idir Aït-Sadoune
  - Nicolas Méric
  - Burkhart Wolff


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
  - 13   # default is 1 (conference), adjust as needed

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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_2.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-031-33163-3_2
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/bruckeramw23/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/bruckeramw23/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/bruckeramw23/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/bruckeramw23/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Isabelle/DOF is an ontology framework on top of Isabelle. It allows for the formal development of ontologies as well as continuous conformity-checking of integrated documents annotated by ontological data. An integrated document may contain text, code, definitions, proofs, and user-programmed constructs supporting a wide range of formal methods Isabelle/DOF is designed to leverage traceability in integrated documents by supporting navigation in Isabelle’s IDE as well as the document generation process. In this paper, we extend Isabelle/DOF with annotations of \(\lambda \)-terms, a pervasive data-structure underlying Isabelle used to syntactically represent expressions and formulas. Rather than introducing an own programming language for meta-data, we use Higher-order Logic (HOL) for expressions, data-constraints, ontological invariants, and queries via code-generation and reflection. This allows both for powerful query languages and logical reasoning over ontologies in, for example, ontological mappings. Our application examples cover documents targeting formal certifications such as CENELEC 50128, or Common Criteria.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_2.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_2.pdf" >}}

## Reference

```
% BibTex
@inproceedings{BruckerAMW23,
  author       = {Achim D. Brucker and
                  Idir A{\"{\i}}t{-}Sadoune and
                  Nicolas M{\'{e}}ric and
                  Burkhart Wolff},
  editor       = {Uwe Gl{\"{a}}sser and
                  Jos{\'{e}} Creissac Campos and
                  Dominique M{\'{e}}ry and
                  Philippe A. Palanque},
  title        = {Using Deep Ontologies in Formal Software Engineering},
  booktitle    = {Rigorous State-Based Methods - 9th International Conference, {ABZ}
                  2023, Nancy, France, May 30 - June 2, 2023, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {14010},
  pages        = {15--32},
  publisher    = {Springer},
  year         = {2023},
  url          = {https://doi.org/10.1007/978-3-031-33163-3\_2},
  doi          = {10.1007/978-3-031-33163-3\_2},
  timestamp    = {Fri, 02 Jun 2023 21:23:53 +0200},
  biburl       = {https://dblp.org/rec/conf/zum/BruckerAMW23.bib},
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

