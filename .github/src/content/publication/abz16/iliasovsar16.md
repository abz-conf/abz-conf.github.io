---
title: "Rodin Platform Why3 Plug-In"

authors:
  - Alexei Iliasov
  - Paulius Stankaitis
  - David Adjepon-Yamoah
  - Alexander B. Romanovsky


date: 2016-01-01

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
  - 11  # default is 1 (conference), adjust as needed

publication: "5th International Conference on ASM, Alloy, B, TLA, VDM, and Z (ABZ'16)"
publication_short: "ABZ'16"

tags:
  - ABZ'16

categories: []

featured: false

# enable this for case studies
# projects:
#   - abz16

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-319-33600-8_21.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-319-33600-8_21
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/iliasovsar16/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/iliasovsar16/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/iliasovsar16/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/iliasovsar16/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

We briefly present the motivation, architecture and usage experience as well as proof statistics for a new Rodin Platform proof back-end based on the Why3 umbrella prover. Why3 offers a simple and versatile notation as a common interface to a large number of automated provers including all the leading SMT-LIB and TPTP compliant tools. The plug-in can function either in a local mode when all the provers are installed locally, or remotely as a cloud service. We discuss the experience of building the tool, the current status and the potential advantages of a cloud-hosted proof infrastructure.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-319-33600-8_21.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-319-33600-8_21.pdf" >}}

## Reference

```
% BibTex
@inproceedings{IliasovSAR16,
  author       = {Alexei Iliasov and
                  Paulius Stankaitis and
                  David Adjepon{-}Yamoah and
                  Alexander B. Romanovsky},
  editor       = {Michael J. Butler and
                  Klaus{-}Dieter Schewe and
                  Atif Mashkoor and
                  Mikl{\'{o}}s Bir{\'{o}}},
  title        = {Rodin Platform Why3 Plug-In},
  booktitle    = {Abstract State Machines, Alloy, B, TLA, VDM, and {Z} - 5th International
                  Conference, {ABZ} 2016, Linz, Austria, May 23-27, 2016, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {9675},
  pages        = {275--281},
  publisher    = {Springer},
  year         = {2016},
  url          = {https://doi.org/10.1007/978-3-319-33600-8\_21},
  doi          = {10.1007/978-3-319-33600-8\_21},
  timestamp    = {Mon, 05 Feb 2024 20:35:41 +0100},
  biburl       = {https://dblp.org/rec/conf/asm/IliasovSAR16.bib},
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

