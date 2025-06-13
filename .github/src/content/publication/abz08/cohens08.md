---
title: "Stability of Real-Time Abstract State Machines under Desynchronization"

authors:
  - Joëlle Cohen
  - Anatol Slissenko


date: 2008-01-01

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

publication: "1st International Conference on ASM, B, and Z (ABZ'08)"
publication_short: "ABZ'08"

tags:
  - ABZ'08

categories: []

featured: false

# enable this for case studies
# projects:
#   - abz08

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_29.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-540-87603-8_29
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/cohens08/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/cohens08/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/cohens08/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/cohens08/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

In our paper TR-LACL-2008–02 (www.univ-paris12.fr/lacl/) we give sufficient conditions that permit to implement a real-time ASM with instantaneous actions (IA-ASM) by an ASM with delayed actions (DA-ASM) with approximate bisimulation of runs. The time is continuous and time constraints are linear inequalities with rational coefficients. As IA-ASM we consider ASM whose programs are blocks of if guard then blockOfUpdates. The implementation is an ASM of more general type. It works by 2 phases: backup phase memorizes the values of functions, and update phase makes the updates using the backed up values. Such an implementation implies shifts of time instants and, consequently, of the values of the real-valued functions. The approximation of runs (and, thus approximate bisimulation) is determined by 2 positive parameters , where bounds time shifts, and bounds the deviations of real-valued functions. We introduce a notion of -sturdy IA-ASM, and prove that the implementation of any such IA-ASM gives an DA-ASM with -approximately bisimular runs if the delay satisfies some constraints. An interesting point is that the sources of desynchronization that destroy the bisimulation are much more subtle and numerous than one can think a priori. Another conceptual consequence concerns the adequacy of the notion of IA-ASM that was introduced in Gurevich–Huggins (LNCS, vol. 1092, 1996), and later studied in Beauquier–Slissenko, (APAL, 113(1–3):13–52, 2002) for the specification of real-time system.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_29.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_29.pdf" >}}

## Reference

```
% BibTex
@inproceedings{CohenS08,
  author       = {Jo{\"{e}}lle Cohen and
                  Anatol Slissenko},
  editor       = {Egon B{\"{o}}rger and
                  Michael J. Butler and
                  Jonathan P. Bowen and
                  Paul Boca},
  title        = {Stability of Real-Time Abstract State Machines under Desynchronization},
  booktitle    = {Abstract State Machines, {B} and Z, First International Conference,
                  {ABZ} 2008, London, UK, September 16-18, 2008. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {5238},
  pages        = {341},
  publisher    = {Springer},
  year         = {2008},
  url          = {https://doi.org/10.1007/978-3-540-87603-8\_29},
  doi          = {10.1007/978-3-540-87603-8\_29},
  timestamp    = {Tue, 14 May 2019 10:00:50 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/CohenS08.bib},
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

