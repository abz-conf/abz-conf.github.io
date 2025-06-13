---
title: "A Translation from Alloy to B"

authors:
  - Sebastian Krings
  - Joshua Schmidt
  - Carola Brings
  - Marc Frappier
  - Michael Leuschel


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-319-91271-4_6.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-319-91271-4_6
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/kringssbfl18/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/kringssbfl18/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/kringssbfl18/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/kringssbfl18/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

In this paper, we introduce a translation of the specification language Alloy to classical B. Our translation closely follows the Alloy grammar, each construct is translated into a semantically equivalent component of the B language. In addition to basic Alloy constructs, our approach supports integers and orderings. The translation is fully automated by the tool “Alloy2B”. We evaluate the usefulness by applying AtelierB and ProB to the translated models, and show benefits for proof and solving with integers and higher-order quantification.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-319-91271-4_6.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-319-91271-4_6.pdf" >}}

## Reference

```
% BibTex
@inproceedings{KringsSBFL18,
  author       = {Sebastian Krings and
                  Joshua Schmidt and
                  Carola Brings and
                  Marc Frappier and
                  Michael Leuschel},
  editor       = {Michael J. Butler and
                  Alexander Raschke and
                  Thai Son Hoang and
                  Klaus Reichl},
  title        = {A Translation from Alloy to {B}},
  booktitle    = {Abstract State Machines, Alloy, B, TLA, VDM, and {Z} - 6th International
                  Conference, {ABZ} 2018, Southampton, UK, June 5-8, 2018, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {10817},
  pages        = {71--86},
  publisher    = {Springer},
  year         = {2018},
  url          = {https://doi.org/10.1007/978-3-319-91271-4\_6},
  doi          = {10.1007/978-3-319-91271-4\_6},
  timestamp    = {Wed, 25 Sep 2019 18:19:23 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/KringsSBFL18.bib},
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

