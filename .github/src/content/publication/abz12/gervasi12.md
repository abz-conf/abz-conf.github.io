---
title: "An ASM Model of Concurrency in a Web Browser"

authors:
  - Vincenzo Gervasi


date: 2012-01-01

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

publication: "3rd International Conference on ASM, Alloy, B, VDM, and Z (ABZ'12)"
publication_short: "ABZ'12"

tags:
  - ABZ'12

categories: []

featured: false

# enable this for case studies
# projects:
#   - abz12

links:
  - name: Digital
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-642-30885-7_6.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-642-30885-7_6
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/gervasi12/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/gervasi12/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/gervasi12/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/gervasi12/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

We define an abstract standards-compliant web browser model. The model focuses on those parts of the browser behaviour which are most relevant for the deployment and execution of web applications, such as interaction with a scripting language (here, ECMAScript), cookies, and asynchronous behaviour of the network layer, while hiding other aspects, such as page navigation and presentational issues. We use a multi-agent Abstract State Machine as our formal model, showing how the browser behaviour can be partitioned into a number of distinct components, and specifying precisely their interactions. The specification can also be used as basis to prove consistency properties of common frameworks for web applications.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-642-30885-7_6.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-642-30885-7_6.pdf" >}}

## Reference

```
% BibTex
@inproceedings{Gervasi12,
  author       = {Vincenzo Gervasi},
  editor       = {John Derrick and
                  John S. Fitzgerald and
                  Stefania Gnesi and
                  Sarfraz Khurshid and
                  Michael Leuschel and
                  Steve Reeves and
                  Elvinia Riccobene},
  title        = {An {ASM} Model of Concurrency in a Web Browser},
  booktitle    = {Abstract State Machines, Alloy, B, VDM, and {Z} - Third International
                  Conference, {ABZ} 2012, Pisa, Italy, June 18-21, 2012. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {7316},
  pages        = {79--93},
  publisher    = {Springer},
  year         = {2012},
  url          = {https://doi.org/10.1007/978-3-642-30885-7\_6},
  doi          = {10.1007/978-3-642-30885-7\_6},
  timestamp    = {Sun, 25 Oct 2020 23:07:20 +0100},
  biburl       = {https://dblp.org/rec/conf/asm/Gervasi12.bib},
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

