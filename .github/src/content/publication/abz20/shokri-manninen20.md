---
title: "Integration of iUML-B and UPPAAL Timed Automata for Development of Real-Time Systems with Concurrent Processes"

authors:
  - Fatima Shokri-Manninen
  - Leonidas Tsiopoulos
  - Jüri Vain
  - Marina Waldén


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
#  10 = "pub_short_paper"
#  11 = "pub_long_paper"
publication_types:
  - 1   # default is 1 (conference), adjust as needed

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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-030-48077-6_13.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-030-48077-6_13
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/shokri-manninen20/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/shokri-manninen20/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/shokri-manninen20/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/shokri-manninen20/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Developing safety-critical systems requires to consider safety and real-time requirements in addition to functional requirements. Event-B is a formalism that is visualised by iUML-B and supports the development of functional aspects having rich verification and validation tools. However, it lacks well-established support for timing analysis. UPPAAL Timed Automata (UTA), on the other hand, address timing aspects of systems, and enable model checking reachability and timing properties. By integrating iUML-B and UTA, we combine the best verifying and validating practices from the two methods achieving a formal development of systems. We present the mapping for translating iUML-B constructs to UTA. The novel aspect is the use of a multi-process trigger-response pattern to address the modelling and verification of reachability properties of complex systems with concurrent processes. The approach is demonstrated on an airport control system, where timing, fairness, as well as liveness properties play a vital role in proving safety requirements.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-030-48077-6_13.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-030-48077-6_13.pdf" >}}

## Reference

```
% BibTex
@inproceedings{Shokri-Manninen20,
  author       = {Fatima Shokri{-}Manninen and
                  Leonidas Tsiopoulos and
                  J{\"{u}}ri Vain and
                  Marina Wald{\'{e}}n},
  editor       = {Alexander Raschke and
                  Dominique M{\'{e}}ry and
                  Frank Houdek},
  title        = {Integration of iUML-B and {UPPAAL} Timed Automata for Development
                  of Real-Time Systems with Concurrent Processes},
  booktitle    = {Rigorous State-Based Methods - 7th International Conference, {ABZ}
                  2020, Ulm, Germany, May 27-29, 2020, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {12071},
  pages        = {186--202},
  publisher    = {Springer},
  year         = {2020},
  url          = {https://doi.org/10.1007/978-3-030-48077-6\_13},
  doi          = {10.1007/978-3-030-48077-6\_13},
  timestamp    = {Fri, 09 Apr 2021 18:50:59 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/Shokri-Manninen20.bib},
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

