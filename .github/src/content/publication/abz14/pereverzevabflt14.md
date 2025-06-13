---
title: "Formal Derivation of Distributed MapReduce"

authors:
  - Inna Pereverzeva
  - Michael J. Butler
  - Asieh Salehi Fathabadi
  - Linas Laibinis
  - Elena Troubitsyna


date: 2014-01-01

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

publication: "4th International Conference on ASM, Alloy, B, TLA, VDM, and Z (ABZ'14)"
publication_short: "ABZ'14"

tags:
  - ABZ'14

categories: []

featured: false

# enable this for case studies
# projects:
#   - abz14

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-662-43652-3_21.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-662-43652-3_21
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/pereverzevabflt14/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/pereverzevabflt14/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/pereverzevabflt14/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/pereverzevabflt14/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

MapReduce is a powerful distributed data processing model that is currently adopted in a wide range of domains to efficiently handle large volumes of data, i.e., cope with the big data surge. In this paper, we propose an approach to formal derivation of the MapReduce framework. Our approach relies on stepwise refinement in Event-B and, in particular, the event refinement structure approach – a diagrammatic notation facilitating formal development. Our approach allows us to derive the system architecture in a systematic and well-structured way. The main principle of MapReduce is to parallelise processing of data by first mapping them to multiple processing nodes and then merging the results. To facilitate this, we formally define interdependencies between the map and reduce stages of MapReduce. This formalisation allows us to propose an alternative architectural solution that weakens blocking between the stages and, as a result, achieves a higher degree of parallelisation of MapReduce computations.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-662-43652-3_21.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-662-43652-3_21.pdf" >}}

## Reference

```
% BibTex
@inproceedings{PereverzevaBFLT14,
  author       = {Inna Pereverzeva and
                  Michael J. Butler and
                  Asieh Salehi Fathabadi and
                  Linas Laibinis and
                  Elena Troubitsyna},
  editor       = {Yamine A{\"{\i}}t Ameur and
                  Klaus{-}Dieter Schewe},
  title        = {Formal Derivation of Distributed MapReduce},
  booktitle    = {Abstract State Machines, Alloy, B, TLA, VDM, and {Z} - 4th International
                  Conference, {ABZ} 2014, Toulouse, France, June 2-6, 2014. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {8477},
  pages        = {238--254},
  publisher    = {Springer},
  year         = {2014},
  url          = {https://doi.org/10.1007/978-3-662-43652-3\_21},
  doi          = {10.1007/978-3-662-43652-3\_21},
  timestamp    = {Tue, 14 May 2019 10:00:50 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/PereverzevaBFLT14.bib},
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

