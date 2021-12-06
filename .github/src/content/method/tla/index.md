---
title: Temporal Logic of Actions (TLA)

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

TLA+ (Temporal Logic of Actions) was developed by Leslie Lamport to model, document, and verify especially concurrent and distributed systems. The language aims for defining the set of all correct system behaviors. It is organized in modules that contain a definition of states and (conditional) state transitions in form of steps. A "next-state-relations" defines how variables can change in any step. Similar to Z, B, and Event-B TLA+ is based on the Zermelo-Fraenkel set theory, but extended with built-in temporal logic operators. 

http://lamport.azurewebsites.net/tla/tla.html
