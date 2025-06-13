---
title: "From ABZ to Cryptography"

authors:
  - Eerke A. Boiten


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_40.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-540-87603-8_40
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/boiten08/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/boiten08/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/boiten08/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/boiten08/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Three Steps from the Ideal Ideally correctness is by construction; post-hoc verification is second choice; verification of proofs is the next step down. In the application area of modern cryptographic protocol verification, the latter would be viewed as serious progress. Modern Cryptographic Protocols and Security A modern cryptographic protocol may have the following properties: its functionality is clear, but its security definition incomplete; it contains explicit probabilistic elements; its notion of security (correctness) is approximate, and relative to computational resources available for an attack against it; its security is proved relative to some problem being hard; primitives cannot be implemented compositionally. All this means that the standard techniques and good intentions of formal methods do not work straight out of the box. Many approaches to bridging the gap between formal methods and modern cryptography exist – but none of these are too close in spirit to the ABZ world.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_40.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-540-87603-8_40.pdf" >}}

## Reference

```
% BibTex
@inproceedings{Boiten08,
  author       = {Eerke A. Boiten},
  editor       = {Egon B{\"{o}}rger and
                  Michael J. Butler and
                  Jonathan P. Bowen and
                  Paul Boca},
  title        = {From {ABZ} to Cryptography},
  booktitle    = {Abstract State Machines, {B} and Z, First International Conference,
                  {ABZ} 2008, London, UK, September 16-18, 2008. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {5238},
  pages        = {353},
  publisher    = {Springer},
  year         = {2008},
  url          = {https://doi.org/10.1007/978-3-540-87603-8\_40},
  doi          = {10.1007/978-3-540-87603-8\_40},
  timestamp    = {Tue, 14 May 2019 10:00:50 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/Boiten08.bib},
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

