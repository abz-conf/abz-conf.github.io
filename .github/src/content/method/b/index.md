---
title: B / Event-B

date:  2021-06-16

draft: false
share: false
commentable: false
editable: true

# Optional header image (relative to `static/img/` folder).
header:
  caption: ""
  image: ""
---

Classical B (or just B) focuses on a tool-based refinement of a formal specification to code. It is based on the Z notation but slightly more low-level. In B a system consists of an abstract machine in which the modeler specifies the goal of the system. Via several refinement steps, this abstract goal is enhanced by more details on a less abstract level by adding details about data structures and algorithms that define how the goal is achieved. 
All steps are proven correct until a deterministic version (the implementation) is reached. 


https://methode-b.com



Event-B is an evolution of B with a simpler notation. Similar to B a system is modeled by different abstraction levels that are connected by a rigorous refinement proven correct. Whereas the B-method is intended to the development of correct-by-construction software, the purpose of Event-B is to model full systems (including hardware and operation environment). These two languages share almost the same mathematical language. 


http://www.event-b.org/