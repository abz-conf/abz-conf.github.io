---
title: "Modeling a landing gear system in Event-B"

authors:
- Amel Mammarue
- Régine Laleau

date: 2015-08-22

# Schedule page publish date (NOT publication's date).
# publishDate: 2020-06-19T16:42:07+02:00

publication_types:
-  2 # journal article

publication: "International Journal on Software Tools for Technology Transfer (STTT)"
publication_short: "STTT"

tags:
- ABZ'14

categories: []

featured: false

# projects:
# - abz14

links:
- name: Digital
  url: https://www.researchgate.net/profile/Amel-Mammar/publication/283184853_Modeling_a_Landing_Gear_System_in_Event-B/links/57a106fc08aeef35741b7e43/Modeling-a-Landing-Gear-System-in-Event-B.pdf
  icon_pack: fas
  icon: file-pdf
- name: Printed
  url: https://doi.org/10.1007/s10009-015-0391-0
  icon_pack: fas
  icon: book
- name: Abstract
  url: "publication/mammar2015sttt/#abstract"
  icon_pack: fas
  icon: file-alt
# - name: View
#   url: "publication/mammar2015sttt/#document"
#   icon_pack: fas
#   icon: glasses
- name: Cite
  url: "publication/mammar2015sttt/#reference"
  icon_pack: fas
  icon: quote-right

slides: ""
---

## Abstract

This article describes the Event-B modeling of a landing gear system of an aircraft whose complete description can be found in Boniol and Wiels (The Landing Gear System Case Study, ABZ Case Study, Communications in Computer Information Science, vol 433, Springer, Berlin, 2014). This real-life case study has been proposed by the ABZ’2014 track that took place in Toulouse, the European capital of the aeronautic industry. Our modeling is based on the Parnas and Madey’s 4-Variable Model that permits to consider the different parts of a system. These parts are incrementally introduced using the Event-B refinement technique. The entire development has been carried out with the Rodin toolset. To ensure the correctness of the different components, we use several verification techniques (animation, model checking and proof) depending on the complexity and the kind of the properties to verify. Basically, prior to the proof phase that can be tedious and complex, we use the animator ANIMB and the model checker PROB that permit to discover some trivial inconsistencies. Once no error is reported, we start the proof phase by using the Atelier B and SMT provers which we installed on Rodin. We conclude the article by drawing up some key findings of and lessons learned from this experience.

<!-- ## Document

{{< embed-pdf url="/mammar2015sttt.pdf" >}}
-->

## Reference

~~~
% BibTex
@Article{Mammar2017,
author="Mammar, Amel
and Laleau, R{\'e}gine",
title="Modeling a landing gear system in Event-B",
journal="International Journal on Software Tools for Technology Transfer",
year="2017",
month="Apr",
day="01",
volume="19",
number="2",
pages="167--186",
abstract="This article describes the Event-B modeling of a landing gear system of an aircraft whose complete description can be found in Boniol and Wiels (The Landing Gear System Case Study, ABZ Case Study, Communications in Computer Information Science, vol 433, Springer, Berlin, 2014). This real-life case study has been proposed by the ABZ'2014 track that took place in Toulouse, the European capital of the aeronautic industry. Our modeling is based on the Parnas and Madey's 4-Variable Model that permits to consider the different parts of a system. These parts are incrementally introduced using the Event-B refinement technique. The entire development has been carried out with the Rodin toolset. To ensure the correctness of the different components, we use several verification techniques (animation, model checking and proof) depending on the complexity and the kind of the properties to verify. Basically, prior to the proof phase that can be tedious and complex, we use the animator AnimB and the model checker ProB that permit to discover some trivial inconsistencies. Once no error is reported, we start the proof phase by using the Atelier B and SMT provers which we installed on Rodin. We conclude the article by drawing up some key findings of and lessons learned from this experience.",
issn="1433-2787",
doi="10.1007/s10009-015-0391-0",
url="https://doi.org/10.1007/s10009-015-0391-0"
}
~~~

Model Archive : Not available
Presentation : Not available
Used formal method : Event-B
Resources and tools : Rodin, ProB
Required OS : Linux, Mac, Windows
Website : Not available
Remarks and recommendation : No
