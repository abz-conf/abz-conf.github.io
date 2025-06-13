---
title: "Alloy+HotCore: A Fast Approximation to Unsat Core"

authors:
  - Nicolás D&apos;Ippolito
  - Marcelo F. Frias
  - Juan P. Galeotti
  - Esteban Lanzarotti
  - Sergio Mera


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
    url: https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_13.pdf
    icon_pack: fas
    icon: file-pdf
  - name: Printed
    url: https://doi.org/10.1007/978-3-642-11811-1_13
    icon_pack: fas
    icon: book
  - name: Abstract
    url: publication/dippolitofglm10/#abstract
    icon_pack: fas
    icon: file-alt
  - name: View
    url: publication/dippolitofglm10/#document
    icon_pack: fas
    icon: glasses
  - name: Cite
    url: publication/dippolitofglm10/#reference
    icon_pack: fas
    icon: quote-right

#   - name: Source
#     url: publication/dippolitofglm10/#sources
#     icon_pack: fas
#     icon: database


---

## Abstract

Identifying a minimal unsatisfiable core in an Alloy model proved to be a very useful feature in many scenarios. We extend this concept to hot core, an approximation to unsat core that enables the user to obtain valuable feedback when the Alloy’s sat-solving process is abruptly interrupted. We present some use cases that exemplify this new feature and explain the applied heuristics. The NP-completeness nature of the verification problem makes hot core specially appealing, since it is quite frequent for users of the Alloy Analyzer to stop the analysis when some time threshold is exceeded. We provide experimental results showing very promising outcomes supporting our proposal.

## Document

If you cannot see the document below, the PDF document is most likely not freely accessible. In this case, please try to access the document via this <a href="https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_13.pdf">link</a>.

{{< embed-pdf url="https://link.springer.com/content/pdf/10.1007%2F978-3-642-11811-1_13.pdf" >}}

## Reference

```
% BibTex
@inproceedings{DIppolitoFGLM10,
  author       = {Nicol{\'{a}}s D'Ippolito and
                  Marcelo F. Frias and
                  Juan P. Galeotti and
                  Esteban Lanzarotti and
                  Sergio Mera},
  editor       = {Marc Frappier and
                  Uwe Gl{\"{a}}sser and
                  Sarfraz Khurshid and
                  R{\'{e}}gine Laleau and
                  Steve Reeves},
  title        = {Alloy+HotCore: {A} Fast Approximation to Unsat Core},
  booktitle    = {Abstract State Machines, Alloy, {B} and Z, Second International Conference,
                  {ABZ} 2010, Orford, QC, Canada, February 22-25, 2010. Proceedings},
  series       = {Lecture Notes in Computer Science},
  volume       = {5977},
  pages        = {160--173},
  publisher    = {Springer},
  year         = {2010},
  url          = {https://doi.org/10.1007/978-3-642-11811-1\_13},
  doi          = {10.1007/978-3-642-11811-1\_13},
  timestamp    = {Mon, 03 Mar 2025 20:58:01 +0100},
  biburl       = {https://dblp.org/rec/conf/asm/DIppolitoFGLM10.bib},
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

