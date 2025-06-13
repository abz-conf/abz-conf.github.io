---
title: "Thread-Local, Step-Local Proof Obligations for Refinement of State-Based Concurrent Systems"

authors:
  - Gerhard Schellhorn
  - Stefan Bodenmüller
  - Wolfgang Reif


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_6.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-031-33163-3_6
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/schellhornbr23/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/schellhornbr23/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/schellhornbr23/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/schellhornbr23/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

This paper presents a proof technique for proving refinements for general state-based models of concurrent systems that reduces proving forward simulations to thread-local, step-local proof obligations. Instances of this proof technique should be applicable to systems specified with ASM rules, B events, or Z operations. To exemplify the proof technique, we demonstrate it with a simple case study that verifies linearizability of a lock-free implementation of concurrent hash sets by showing that it refines an abstract concurrent system with atomic operations. Our theorem prover KIV translates programs to a set of transition rules and generates proof obligations according to the technique.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_6.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_6.pdf" >}}

## Reference

```
% BibTex
@inproceedings{SchellhornBR23,
  author       = {Gerhard Schellhorn and
                  Stefan Bodenm{\"{u}}ller and
                  Wolfgang Reif},
  editor       = {Uwe Gl{\"{a}}sser and
                  Jos{\'{e}} Creissac Campos and
                  Dominique M{\'{e}}ry and
                  Philippe A. Palanque},
  title        = {Thread-Local, Step-Local Proof Obligations for Refinement of State-Based
                  Concurrent Systems},
  booktitle    = {Rigorous State-Based Methods - 9th International Conference, {ABZ}
                  2023, Nancy, France, May 30 - June 2, 2023, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {14010},
  pages        = {70--87},
  publisher    = {Springer},
  year         = {2023},
  url          = {https://doi.org/10.1007/978-3-031-33163-3\_6},
  doi          = {10.1007/978-3-031-33163-3\_6},
  timestamp    = {Mon, 26 Jun 2023 20:49:09 +0200},
  biburl       = {https://dblp.org/rec/conf/zum/SchellhornBR23.bib},
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

