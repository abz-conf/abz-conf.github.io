---
title: "Supporting Reuse in Event B Development: Modularisation Approach"

authors:
  - Alexei Iliasov
  - Elena Troubitsyna
  - Linas Laibinis
  - Alexander B. Romanovsky
  - Kimmo Varpaaniemi
  - Dubravka Ilic
  - Timo Latvala


date: 2010-01-01

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

publication: "2nd International Conference on ASM, Alloy, B, and Z (ABZ'10)"
publication_short: "ABZ'10"

tags:
  - ABZ'10

categories: []

featured: false

# enable this for case studies
# projects:
#   - abz10

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_14.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-642-11811-1_14
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/iliasovtlrvil10/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/iliasovtlrvil10/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/iliasovtlrvil10/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/iliasovtlrvil10/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Recently, Space Systems Finland has undertaken formal Event B development of a part of the on-board software for the BepiColombo space mission. As a result, lack of modularisation mechanisms in Event B has been identified as a serious obstacle to scalability. One of the main benefits of modularisation is that it allows us to decompose system models into components that can be independently developed. It also helps to manage complexity of models that in the industrial setting are usually very large and difficult to comprehend. On the other hand, modularisation enables reuse of formally developed components in the formal product line development. In this paper we propose a conservative extension of Event B formalism to support modularisation. We demonstrate how our approach can support reuse in the formal development in the space domain.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_14.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_14.pdf" >}}

## Reference

```
% BibTex
@inproceedings{IliasovTLRVIL10,
  author       = {Alexei Iliasov and
                  Elena Troubitsyna and
                  Linas Laibinis and
                  Alexander B. Romanovsky and
                  Kimmo Varpaaniemi and
                  Dubravka Ilic and
                  Timo Latvala},
  editor       = {Marc Frappier and
                  Uwe Gl{\"{a}}sser and
                  Sarfraz Khurshid and
                  R{\'{e}}gine Laleau and
                  Steve Reeves},
  title        = {Supporting Reuse in Event {B} Development: Modularisation Approach},
  booktitle    = {Abstract State Machines, Alloy, {B} and Z, Second International Conference,
                  {ABZ} 2010, Orford, QC, Canada, February 22-25, 2010. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {5977},
  pages        = {174--188},
  publisher    = {Springer},
  year         = {2010},
  url          = {https://doi.org/10.1007/978-3-642-11811-1\_14},
  doi          = {10.1007/978-3-642-11811-1\_14},
  timestamp    = {Mon, 05 Feb 2024 20:35:41 +0100},
  biburl       = {https://dblp.org/rec/conf/asm/IliasovTLRVIL10.bib},
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

