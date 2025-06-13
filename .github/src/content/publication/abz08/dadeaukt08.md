---
title: "Combining Scenario- and Model-Based Testing to Ensure POSIX Compliance"

authors:
  - Frédéric Dadeau
  - Adrien De Kermadec
  - Régis Tissot


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
#  10 = "pub_short_paper"
#  11 = "pub_long_paper"
publication_types:
  - 1   # default is 1 (conference), adjust as needed

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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_13.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-540-87603-8_13
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/dadeaukt08/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/dadeaukt08/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/dadeaukt08/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/dadeaukt08/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

We present in this paper a way to produce test suites for the POSIX mini-challenge, based on a formal model of a file system manager, written using a B machine. By this case study, we illustrate the limitations of a fully-automated testing process, which justifies the use of scenarios that complements the classical functional testing approach. Scenarios are expressed through schemas, focusing only on operation chaining. They are played on the model using a symbolic animation engine in order to automatically compute pertinent operation parameter values, based on model coverage criteria such as behavioral or data coverage. We concretize our experimentation by testing the POSIX conformance of two different file systems: a recent Linux distribution, and a customized Java implementation of POSIX used to evaluate the relevance of our approach.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_13.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_13.pdf" >}}

## Reference

```
% BibTex
@inproceedings{DadeauKT08,
  author       = {Fr{\'{e}}d{\'{e}}ric Dadeau and
                  Adrien De Kermadec and
                  R{\'{e}}gis Tissot},
  editor       = {Egon B{\"{o}}rger and
                  Michael J. Butler and
                  Jonathan P. Bowen and
                  Paul Boca},
  title        = {Combining Scenario- and Model-Based Testing to Ensure {POSIX} Compliance},
  booktitle    = {Abstract State Machines, {B} and Z, First International Conference,
                  {ABZ} 2008, London, UK, September 16-18, 2008. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {5238},
  pages        = {153--166},
  publisher    = {Springer},
  year         = {2008},
  url          = {https://doi.org/10.1007/978-3-540-87603-8\_13},
  doi          = {10.1007/978-3-540-87603-8\_13},
  timestamp    = {Tue, 14 May 2019 10:00:50 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/DadeauKT08.bib},
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

