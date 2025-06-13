---
title: "Model Checking Event-B by Encoding into Alloy"

authors:
  - Paulo J. Matos
  - João Marques-Silva 0001


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_34.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-540-87603-8_34
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/matosm08/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/matosm08/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/matosm08/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/matosm08/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Current day systems are ever more detailed and complex leading to the necessity of developing models that abstract unimportant implementation details while emphasizing their structure. Until recently it was only possible to perform temporal model checking in an Event-B model by converting the model to B-METHOD and then using ProB [1]. More recently, a prototype ProB plug in [2] for the RODIN tool has been developed. Nevertheles, encoding Event-B to Alloy allows building on top of the Alloy model finding engine therefore benefiting from all of its optimizations. An extended version of this work is in [3].

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_34.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_34.pdf" >}}

## Reference

```
% BibTex
@inproceedings{MatosM08,
  author       = {Paulo J. Matos and
                  Jo{\~{a}}o Marques{-}Silva},
  editor       = {Egon B{\"{o}}rger and
                  Michael J. Butler and
                  Jonathan P. Bowen and
                  Paul Boca},
  title        = {Model Checking Event-B by Encoding into Alloy},
  booktitle    = {Abstract State Machines, {B} and Z, First International Conference,
                  {ABZ} 2008, London, UK, September 16-18, 2008. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {5238},
  pages        = {346},
  publisher    = {Springer},
  year         = {2008},
  url          = {https://doi.org/10.1007/978-3-540-87603-8\_34},
  doi          = {10.1007/978-3-540-87603-8\_34},
  timestamp    = {Mon, 24 Feb 2020 19:23:27 +0100},
  biburl       = {https://dblp.org/rec/conf/asm/MatosM08.bib},
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

