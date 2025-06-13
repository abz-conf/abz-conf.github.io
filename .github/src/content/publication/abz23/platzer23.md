---
title: "Refinements of Hybrid Dynamical Systems Logic"

authors:
  - André Platzer


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_1.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-031-33163-3_1
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/platzer23/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/platzer23/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/platzer23/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/platzer23/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Hybrid dynamical systems describe the mixed discrete dynamics and continuous dynamics of cyber-physical systems such as aircraft, cars, trains, and robots. To justify correctness of their safety-critical controls for their physical models, differential dynamic logic (\(\textsf {dL}\)) provides deductive specification and verification techniques implemented in the theorem prover KeYmaera X. The logic \(\textsf {dL}\) is useful for proving, e.g., that all runs of a hybrid dynamical system are safe (\([{\alpha }]\varphi \)), or that there is a run of the hybrid dynamical system ultimately reaching the desired goal (\(\langle {\alpha }\rangle {\varphi }\)). Combinations of \(\textsf {dL}\)’s operators naturally represent safety, liveness, stability and other properties. Variations of \(\textsf {dL}\) serve additional purposes. Differential refinement logic (dRL) adds an operator \(\alpha \le \beta \) expressing that hybrid system \(\alpha \) refines hybrid system \(\beta \), which is useful, e.g., for relating concrete system implementations to their abstract verification models. Just like \(\textsf {dL}\), dRL is a logic closed under all operators, which opens up systematic ways of simultaneously relating systems and their properties, of reducing system properties to system relations or, vice versa, reducing system relations to system properties. Differential game logic (dGL) adds the ability of referring to winning strategies of players in hybrid games, which is useful for establishing correctness properties of systems where the actions of different agents may interfere. \(\textsf {dL}\) and its variations have been used in KeYmaera X for verifying ground robot obstacle avoidance, the Next-Generation Airborne Collision Avoidance System ACAS X, and the kinematics of train control in the Federal Railroad Administration model with track terrain influence and air pressure brake propagation.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_1.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_1.pdf" >}}

## Reference

```
% BibTex
@inproceedings{Platzer23,
  author       = {Andr{\'{e}} Platzer},
  editor       = {Uwe Gl{\"{a}}sser and
                  Jos{\'{e}} Creissac Campos and
                  Dominique M{\'{e}}ry and
                  Philippe A. Palanque},
  title        = {Refinements of Hybrid Dynamical Systems Logic},
  booktitle    = {Rigorous State-Based Methods - 9th International Conference, {ABZ}
                  2023, Nancy, France, May 30 - June 2, 2023, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {14010},
  pages        = {3--14},
  publisher    = {Springer},
  year         = {2023},
  url          = {https://doi.org/10.1007/978-3-031-33163-3\_1},
  doi          = {10.1007/978-3-031-33163-3\_1},
  timestamp    = {Fri, 02 Jun 2023 21:23:53 +0200},
  biburl       = {https://dblp.org/rec/conf/zum/Platzer23.bib},
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

