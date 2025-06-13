---
title: "Modeling and Analysis of a Safety-Critical Interactive System Through Validation Obligations"

authors:
  - David Geleßus
  - Sebastian Stock 0002
  - Fabian Vu
  - Michael Leuschel
  - Atif Mashkoor


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
  - 10   # default is 1 (conference), adjust as needed

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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_22.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-031-33163-3_22
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/gelessussvlm23/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/gelessussvlm23/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/gelessussvlm23/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/gelessussvlm23/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

This paper presents insights gained during modeling and analyzing the arrival manager (AMAN) case study in Event-B with validation obligations (VOs). AMAN is a safety-critical interactive system for air traffic controllers to organize the landing of airplanes at airports. The presented model consists of a human-machine interface comprising interactive and autonomous parts. We employ VOs to formalize requirements, uncover contradictions and ambiguities, and validate the model’s compliance with the requirements. To capture the AMAN’s human-machine interaction, we implement an interactive domain-specific visualization and an automatic simulation using the VisB and SimB components of ProB.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_22.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_22.pdf" >}}

## Reference

```
% BibTex
@inproceedings{GelessusSVLM23,
  author       = {David Gele{\ss}us and
                  Sebastian Stock and
                  Fabian Vu and
                  Michael Leuschel and
                  Atif Mashkoor},
  editor       = {Uwe Gl{\"{a}}sser and
                  Jos{\'{e}} Creissac Campos and
                  Dominique M{\'{e}}ry and
                  Philippe A. Palanque},
  title        = {Modeling and Analysis of a Safety-Critical Interactive System Through
                  Validation Obligations},
  booktitle    = {Rigorous State-Based Methods - 9th International Conference, {ABZ}
                  2023, Nancy, France, May 30 - June 2, 2023, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {14010},
  pages        = {284--302},
  publisher    = {Springer},
  year         = {2023},
  url          = {https://doi.org/10.1007/978-3-031-33163-3\_22},
  doi          = {10.1007/978-3-031-33163-3\_22},
  timestamp    = {Fri, 02 Jun 2023 21:23:53 +0200},
  biburl       = {https://dblp.org/rec/conf/zum/GelessusSVLM23.bib},
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

