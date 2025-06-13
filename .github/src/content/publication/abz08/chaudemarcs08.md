---
title: "FDIR Architectures for Autonomous Spacecraft: Specification and Assessment with Event-B"

authors:
  - Jean-Charles Chaudemar
  - Charles Castel
  - Christel Seguin


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_45.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-540-87603-8_45
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/chaudemarcs08/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/chaudemarcs08/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/chaudemarcs08/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/chaudemarcs08/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

On-board Fault Detection, Isolation and Recovery (FDIR) systems are considered to ensure the safety and to increase the autonomy of spacecrafts. They shall be carefully designed and validated. Their implementation involves a relevant knowledge of items like functions and architectures of the system, and a fault model in relation with these items. Thus, the event-B method is well suited to correctly specify and validate on-board safety architectures. This paper focuses on the FDIR concept presentation and the use of event-B for formalising and for refining the FDIR concept. The paper is organised as follows: after a short presentation of on-board FDIR concept strongly bounded with autonomy architecture concept, we suggest activities enabling to implement FDIR concept. Then, we present the framework of formal modelling that we will use to describe our architecture and the properties related to this architecture. We illustrate our approach by modelling more specifically a safety architecture pattern that includes a primary functional component and a redundant one, under the hypothesis of no common fault. The safety property to be met is: “one single fault shall not lead to the total loss of the function”. The last section of the paper deals with the objectives for the future work.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_45.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_45.pdf" >}}

## Reference

```
% BibTex
@inproceedings{ChaudemarCS08,
  author       = {Jean{-}Charles Chaudemar and
                  Charles Castel and
                  Christel Seguin},
  editor       = {Egon B{\"{o}}rger and
                  Michael J. Butler and
                  Jonathan P. Bowen and
                  Paul Boca},
  title        = {{FDIR} Architectures for Autonomous Spacecraft: Specification and
                  Assessment with Event-B},
  booktitle    = {Abstract State Machines, {B} and Z, First International Conference,
                  {ABZ} 2008, London, UK, September 16-18, 2008. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {5238},
  pages        = {358},
  publisher    = {Springer},
  year         = {2008},
  url          = {https://doi.org/10.1007/978-3-540-87603-8\_45},
  doi          = {10.1007/978-3-540-87603-8\_45},
  timestamp    = {Sat, 19 Oct 2019 20:28:13 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/ChaudemarCS08.bib},
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

