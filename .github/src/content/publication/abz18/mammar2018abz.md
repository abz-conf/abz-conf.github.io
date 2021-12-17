---
title: "An Event-B Model of the Hybrid ERTMS/ETCS Level 3 Standard"

authors:
- Amel Mammar
- Marc Frappier
- Steve Jeffrey Tueno Fotso
- Régine Laleau

date: 2018-05-01

# Schedule page publish date (NOT publication's date).
# publishDate: 2020-06-19T16:42:07+02:00

publication_types:
-  1 # conference paper

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
  url: https://www.irit.fr/ABZ-CS/html_files/files/2018/PDF/MFJFL_ABZ2018.pdf
  icon_pack: fas
  icon: file-pdf
- name: Printed
  url: https://doi.org/10.1007/978-3-319-91271-4_24
  icon_pack: fas
  icon: book
- name: Abstract
  url: "publication/mammar2018abz/#abstract"
  icon_pack: fas
  icon: file-alt
- name: View
  url: "publication/mammar2018abz/#document"
  icon_pack: fas
  icon: glasses
- name: Cite
  url: "publication/mammar2018abz/#reference"
  icon_pack: fas
  icon: quote-right
- name: Source
  url: "publication/mammar2018abz/#sources"
  icon_pack: fas
  icon: database

slides: ""
---

## Abstract

This paper presents an Event-B model of the ABZ2018 case study on the European Rail Traffic Management System (ERTMS) standard. The case study focusses on the management of fixed virtual sub-sections (VSS). We model the hybrid level 3 of the standard, which assumes that trains may be either equipped with an on-board train integrity monitoring system (TIMS) and that they report their position and integrity, ERTMS trains not fitted with TIMS that report only their front position or non-ERTMS trains that do not report any information about their position. We take into account most of the main features of the case study. Our model is decomposed into four refinements. All proof obligations have been discharged using the Rodin provers, except those related to the computation of the VSS state machine, which was found to be ambiguous (nondeterministic). Our model has been validated using ProB. The main safety property, which is that ERTMS trains do not collide, is proved.

## Document

{{< embed-pdf url="https://www.irit.fr/ABZ-CS/html_files/files/2018/PDF/MFJFL_ABZ2018.pdf" >}}

## Reference

~~~
% BibTex
@inproceedings{DBLP:conf/asm/MammarFFL18,
  author    = {Amel Mammar and
               Marc Frappier and
               Steve Jeffrey Tueno Fotso and
               R{\'{e}}gine Laleau},
  title     = {An Event-B Model of the Hybrid {ERTMS/ETCS} Level 3 Standard},
  booktitle = {Abstract State Machines, Alloy, B, TLA, VDM, and {Z} - 6th International
               Conference, {ABZ} 2018, Southampton, UK, June 5-8, 2018, Proceedings},
  pages     = {353--366},
  year      = {2018},
  crossref  = {DBLP:conf/asm/2018}
	}
~~~

## Sources

- **Model Archive:**
  [ZIP](/data/abz18/mammar2018abz.zip)
- **Presentation:**
  Not available
- **Used formal method:**
  [Event-B](/method/event-b)
- **Resources and tools:**
  Rodin, ProB
- **Required OS:**
  Linux, Windows
- **Website:**
  http://info.usherbrooke.ca/mfrappier/abz2018-ERTMS-Case-Study
- **Remarks and recommendation:**
  Not available
