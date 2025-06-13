---
title: "Proving Determinacy of the PharOS Real-Time Operating System"

authors:
  - Selma Azaiez
  - Damien Doligez
  - Matthieu Lemerre
  - Tomer Libal
  - Stephan Merz


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
#  10 = "pub_short_paper"
#  11 = "pub_long_paper"
publication_types:
  - 1   # default is 1 (conference), adjust as needed

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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-319-33600-8_4.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-319-33600-8_4
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/azaiezdllm16/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/azaiezdllm16/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/azaiezdllm16/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/azaiezdllm16/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Executions in the PharOS real-time system are deterministic in the sense that the sequence of local states for every process is independent of the order in which processes are scheduled. The essential ingredient for achieving this property is that a temporal window of execution is associated with every instruction. Messages become visible to receiving processes only after the time window of the sending message has elapsed. We present a high-level model of PharOS in TLA+ and formally state and prove determinacy using the TLA+ Proof System.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-319-33600-8_4.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-319-33600-8_4.pdf" >}}

## Reference

```
% BibTex
@inproceedings{AzaiezDLLM16,
  author       = {Selma Azaiez and
                  Damien Doligez and
                  Matthieu Lemerre and
                  Tomer Libal and
                  Stephan Merz},
  editor       = {Michael J. Butler and
                  Klaus{-}Dieter Schewe and
                  Atif Mashkoor and
                  Mikl{\'{o}}s Bir{\'{o}}},
  title        = {Proving Determinacy of the PharOS Real-Time Operating System},
  booktitle    = {Abstract State Machines, Alloy, B, TLA, VDM, and {Z} - 5th International
                  Conference, {ABZ} 2016, Linz, Austria, May 23-27, 2016, Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {9675},
  pages        = {70--85},
  publisher    = {Springer},
  year         = {2016},
  url          = {https://doi.org/10.1007/978-3-319-33600-8\_4},
  doi          = {10.1007/978-3-319-33600-8\_4},
  timestamp    = {Sat, 09 Apr 2022 12:45:50 +0200},
  biburl       = {https://dblp.org/rec/conf/asm/AzaiezDLLM16.bib},
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

