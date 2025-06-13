---
title: "Clarification of Ambiguity for the Simple Authentication and Security Layer"

authors:
  - Farah Al-Shareefi
  - Alexei Lisitsa 0001
  - Clare Dixon


date: 2018-01-01

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

publication: "6th International Conference on ASM, Alloy, B, TLA, VDM, and Z (ABZ'18)"
publication_short: "ABZ'18"

tags:
  - ABZ'18

categories: []

featured: false

# enable this for case studies
# projects:
#   - abz18

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-319-91271-4_13.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-319-91271-4_13
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/al-shareefild18/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/al-shareefild18/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/al-shareefild18/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/al-shareefild18/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

The Simple Authentication and Security Layer (SASL) is a framework for enabling application protocols to support authentication, integrity and confidentiality services. The SASL was originally specified in RFC 2222, and later updated in RFC 4422, using natural language. However, due to the richness of natural language this involves ambiguities and imprecision. Whilst there is an Oracle implementation of SASL, its documentation also contains informal descriptions and under-defined specifications of the RFCs. This paper provides clarification of ambiguity in SASL using Abstract State Machines (ASMs). This clarification is based on two ASM essential notions: a ground model to capture the intended SASL behavior in an understandable way, and a refinement notion to accurately explicate the ambiguous parts of the behavior. We also show some differences between RFCs and the description of the Oracle implementation. We believe our work can serve as a basis for further implementation and for formal analysis.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-319-91271-4_13.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-319-91271-4_13.pdf" >}}

## Reference

```
% BibTex
@inproceedings{Al-ShareefiLD18,
  author       = {Farah Al{-}Shareefi and
                  Alexei Lisitsa and
                  Clare Dixon},
  editor       = {Michael J. Butler and
                  Alexander Raschke and
                  Thai Son Hoang and
                  Klaus Reichl},
  title        = {Clarification of Ambiguity for the Simple Authentication and Security
                  Layer},
  booktitle    = {Abstract State Machines, Alloy, B, TLA, VDM, and {Z} - 6th International
                  Conference, {ABZ} 2018, Southampton, UK, June 5-8, 2018, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {10817},
  pages        = {189--203},
  publisher    = {Springer},
  year         = {2018},
  url          = {https://doi.org/10.1007/978-3-319-91271-4\_13},
  doi          = {10.1007/978-3-319-91271-4\_13},
  timestamp    = {Sun, 02 Oct 2022 15:55:03 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/Al-ShareefiLD18.bib},
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

