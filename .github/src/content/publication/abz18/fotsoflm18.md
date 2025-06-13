---
title: "Modeling the Hybrid ERTMS/ETCS Level 3 Standard Using a Formal Requirements Engineering Approach"

authors:
- Steve Jeffrey Tueno Fotso
- Marc Frappier
- Régine Laleau
- Amel Mammar

date: 2018-05-01

# Schedule page publish date (NOT publication's date).
# publishDate: 2020-06-19T16:42:07+02:00

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
  - 10  # default is 1 (conference), adjust as needed

publication: "6th International Conference on ASM, Alloy, B, TLA, VDM, and Z (ABZ'18)"
publication_short: "ABZ'18"

tags:
- ABZ'18

categories: []

featured: false

projects:
- abz18

links:
- name: Digital
  url: http://info.usherbrooke.ca/mfrappier/abz2018-ERTMS-Case-Study-Formose/ABZ2018-_ERTMS_Case_Study.pdf
  icon_pack: fas
  icon: file-pdf
- name: Printed
  url: https://doi.org/10.1007/978-3-319-91271-4_18
  icon_pack: fas
  icon: book
- name: Abstract
  url: "publication/fotso2018abz/#abstract"
  icon_pack: fas
  icon: file-alt
- name: View
  url: "publication/fotso2018abz/#document"
  icon_pack: fas
  icon: glasses
- name: Cite
  url: "publication/fotso2018abz/#reference"
  icon_pack: fas
  icon: quote-right
- name: Source
  url: "publication/fotso2018abz/#sources"
  icon_pack: fas
  icon: database

slides: ""
---

## Abstract

This paper presents a specification of the hybrid ERTMS/ETCS level 3 standard in the framework of the case study proposed for the 6th edition of the ABZ conference. The specification is based on the method and tools, developed in the ANR FORMOSE project, for the modeling and formal verification of critical and complex system requirements. The requirements are specified with SysML/KAOS goal diagrams and are automatically translated into B System specifications, in order to obtain the architecture of the formal specification. Domain properties are specified by ontologies with the SysML/KAOS domain modeling language, based on OWL and PLIB. Their automatic translation completes the structural part of the formal specification. The only part of the specification, which must be manually completed, is the body of events. The construction is incremental, based on the refinement mechanisms existing within the involved methods. The formal specification of the case study is composed of seven refinement levels and all the proofs have been discharged with the Rodin prover.

## Document

{{< embed-pdf url="http://info.usherbrooke.ca/mfrappier/abz2018-ERTMS-Case-Study-Formose/ABZ2018-_ERTMS_Case_Study.pdf" >}}

## Reference

~~~
% BibTex
@InProceedings{10.1007/978-3-319-91271-4_18,
author="Tueno Fotso, Steve Jeffrey
and Frappier, Marc
and Laleau, R{\'e}gine
and Mammar, Amel",
editor="Butler, Michael
and Raschke, Alexander
and Hoang, Thai Son
and Reichl, Klaus",
title="Modeling the Hybrid ERTMS/ETCS Level 3 Standard Using a Formal Requirements Engineering Approach",
booktitle="Abstract State Machines, Alloy, B, TLA, VDM, and Z",
year="2018",
publisher="Springer International Publishing",
address="Cham",
pages="262--276",
isbn="978-3-319-91271-4"
}
~~~

## Sources

- **Model Archive:**
  [ZIP](/data/abz18/fotso2018abz.zip)
- **Presentation:**
  [PDF](/data/abz18/fotso2018abz.pdf)
- **Used formal method:**
  [Event-B](/method/event-b), [B Method](/method/b), and SysML/KAOS Requirements Engineering Method
- **Resources and tools:**
  Openflexo, Rodin, The SysMLKaos Domain Modeling Tool
- **Required OS:**
  Linux, Mac, Windows
- **Website:**
  https://github.com/stuenofotso/SysML_KAOS_Domain_Model_Parser/tree/master/ABZ18_ERTMS
- **Remarks and recommendation:**
  The developed model focuses on formal verification of the main requirements of the protocol. Its main objective is to assess the SysML/KAOS method and to compare it with direct specification approaches using only plain Event-B.
