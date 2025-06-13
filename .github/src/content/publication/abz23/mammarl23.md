---
title: "Modeling and Verifying an Arrival Manager Using Event-B"

authors:
  - Amel Mammar
  - Michael Leuschel


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_24.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-031-33163-3_24
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/mammarl23/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/mammarl23/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/mammarl23/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/mammarl23/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

The present paper describes an Event-B model of the Arrival MANager system (called AMAN), the case study provided by the ABZ’23 conference. The goal of this safety critical interactive system is to schedule the arrival times of aircraft at airports. This system includes two parts: an autonomous part which predicts the arrival time of an aircraft from external sources (flight plan information, radar and weather information, etc.) and an interface part that permits to the Air Traffic Controller (ATCo) to submit requests to AMAN like changes regarding the arrival times of aircraft. To formally model and verify this critical system, we use a correct-by-construction approach with the Event-B formal method and its refinement process. We mainly consider functional features of the case study; all proof obligations have been discharged using the provers of the Rodin platform under which we carried out our development. To help users understand how AMAN works and its main functionalities, a visualisation of the Event-B models was achieved using the VisB component of ProB. Our models have been validated using ProB by applying scenarios related to different functional aspects of the system.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_24.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-031-33163-3_24.pdf" >}}

## Reference

```
% BibTex
@inproceedings{MammarL23,
  author       = {Amel Mammar and
                  Michael Leuschel},
  editor       = {Uwe Gl{\"{a}}sser and
                  Jos{\'{e}} Creissac Campos and
                  Dominique M{\'{e}}ry and
                  Philippe A. Palanque},
  title        = {Modeling and Verifying an Arrival Manager Using Event-B},
  booktitle    = {Rigorous State-Based Methods - 9th International Conference, {ABZ}
                  2023, Nancy, France, May 30 - June 2, 2023, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {14010},
  pages        = {321--339},
  publisher    = {Springer},
  year         = {2023},
  url          = {https://doi.org/10.1007/978-3-031-33163-3\_24},
  doi          = {10.1007/978-3-031-33163-3\_24},
  timestamp    = {Fri, 02 Jun 2023 21:23:53 +0200},
  biburl       = {https://dblp.org/rec/conf/zum/MammarL23.bib},
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

