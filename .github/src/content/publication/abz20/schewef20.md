---
title: "A Logic for Reflective ASMs"

authors:
  - Klaus-Dieter Schewe
  - Flavio Ferrarotti


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-030-48077-6_7.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-030-48077-6_7
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/schewef20/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/schewef20/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/schewef20/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/schewef20/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Reflective algorithms are algorithms that can modify their own behaviour. Recently a behavioural theory of reflective algorithms has been developed, which shows that they are captured by reflective abstract state machines (rASMs). Reflective ASMs exploit extended states that include an updatable representation of the ASM signature and rules to be executed by the machine in that state. Updates to the representation of ASM signatures and rules are realised by means of a sophisticated tree algebra defined in the background of the rASM. In this paper the theory is taken further by an extension of the logic of ASMs to capture inferences on rASMs. The key is the introduction of terms that are interpreted by ASM rules stored in some location. We show that fragments of the logic with a fixed bound on the number of steps preserve completeness, whereas the full run-logic for rASMs becomes incomplete.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-030-48077-6_7.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-030-48077-6_7.pdf" >}}

## Reference

```
% BibTex
@inproceedings{ScheweF20,
  author       = {Klaus{-}Dieter Schewe and
                  Flavio Ferrarotti},
  editor       = {Alexander Raschke and
                  Dominique M{\'{e}}ry and
                  Frank Houdek},
  title        = {A Logic for Reflective ASMs},
  booktitle    = {Rigorous State-Based Methods - 7th International Conference, {ABZ}
                  2020, Ulm, Germany, May 27-29, 2020, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {12071},
  pages        = {93--106},
  publisher    = {Springer},
  year         = {2020},
  url          = {https://doi.org/10.1007/978-3-030-48077-6\_7},
  doi          = {10.1007/978-3-030-48077-6\_7},
  timestamp    = {Mon, 25 May 2020 12:33:39 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/ScheweF20.bib},
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

