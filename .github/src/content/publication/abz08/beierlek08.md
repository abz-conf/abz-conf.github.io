---
title: "A Verified AsmL Implementation of Belief Revision"

authors:
  - Christoph Beierle
  - Gabriele Kern-Isberner


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_9.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-540-87603-8_9
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/beierlek08/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/beierlek08/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/beierlek08/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/beierlek08/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Belief revision is a key functionality for any intelligent agent being able to perceive pieces of knowledge from its environment and to give back sentences she believes to be true with a certain degree of belief. We report on a refinement of a previous, abstract ASM specification of Condor, a system modeling such an agent, to a fully operational specification implemented in AsmL. The complete AsmL implementation of various belief revision operators is presented, demonstrating how using AsmL enabled a high-level implementation that minimizes the gap between the abstract specification of the underlying concepts and the executable code in the implemented system. Based on ASM refinement and verification concepts, a full mathematical correctness proof for different belief revision operators realized in Condor@AsmL is given.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_9.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_9.pdf" >}}

## Reference

```
% BibTex
@inproceedings{BeierleK08,
  author       = {Christoph Beierle and
                  Gabriele Kern{-}Isberner},
  editor       = {Egon B{\"{o}}rger and
                  Michael J. Butler and
                  Jonathan P. Bowen and
                  Paul Boca},
  title        = {A Verified AsmL Implementation of Belief Revision},
  booktitle    = {Abstract State Machines, {B} and Z, First International Conference,
                  {ABZ} 2008, London, UK, September 16-18, 2008. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {5238},
  pages        = {98--111},
  publisher    = {Springer},
  year         = {2008},
  url          = {https://doi.org/10.1007/978-3-540-87603-8\_9},
  doi          = {10.1007/978-3-540-87603-8\_9},
  timestamp    = {Tue, 14 May 2019 10:00:50 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/BeierleK08.bib},
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

