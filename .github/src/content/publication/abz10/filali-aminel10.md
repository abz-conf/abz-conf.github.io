---
title: "Development of a Synchronous Subset of AADL"

authors:
  - Mamoun Filali-Amine
  - Julia Lawall


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_19.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-642-11811-1_19
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/filali-aminel10/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/filali-aminel10/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/filali-aminel10/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/filali-aminel10/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

We study the definition and the mapping of an AADL subset: the so called synchronous subset. We show that the data port protocol used for delayed and immediate connections between periodic threads can be interpreted in a synchronous way. In this paper, we formalize this interpretation and study the development of its mapping such that the original synchronous semantics is preserved. For that purpose, we use refinements through the Event B method.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_19.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_19.pdf" >}}

## Reference

```
% BibTex
@inproceedings{Filali-AmineL10,
  author       = {Mamoun Filali{-}Amine and
                  Julia Lawall},
  editor       = {Marc Frappier and
                  Uwe Gl{\"{a}}sser and
                  Sarfraz Khurshid and
                  R{\'{e}}gine Laleau and
                  Steve Reeves},
  title        = {Development of a Synchronous Subset of {AADL}},
  booktitle    = {Abstract State Machines, Alloy, {B} and Z, Second International Conference,
                  {ABZ} 2010, Orford, QC, Canada, February 22-25, 2010. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {5977},
  pages        = {245--258},
  publisher    = {Springer},
  year         = {2010},
  url          = {https://doi.org/10.1007/978-3-642-11811-1\_19},
  doi          = {10.1007/978-3-642-11811-1\_19},
  timestamp    = {Mon, 17 Jan 2022 15:20:19 +0100},
  biburl       = {https://dblp.org/rec/conf/asm/Filali-AmineL10.bib},
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

