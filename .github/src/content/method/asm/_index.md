---
title: Abstract State Machine (ASM)

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

The ASM method applies Abstract State Machines (ASMs) to support **_traceable rigorous design and analysis_** (by experimental testing and/or mathematical verification) of software-intensive systems. 
The following **_three ingredients_** of the method support to **_develop executable code from specifications by stepwise refinement_** where at each step both mathematical verification of desired properties and experimental model validation by testing can be applied and fully documented to permit design for change.

<!-- @ppaulweber: update "the concept ..." -->

- the concept of ASM 
  ------------------- 
  defined in [1], a semantically well-founded and arguably most general form of conceptually executable pseudo-code.
  The definition provides a uniform language to express any intended computational system at any development stage in terms of operations at an appropriate level of abstraction operating directly over objects (read: the system STATE, including input and output) determined by that level of abstraction.
 
- the concept of ASM ground model
  -------------------------------
  defined in [2], i.e. a rigorous requirements model that is expressed in application domain terms.
  A ground model ASM turns natural language requirements into a mathematical form that supports the inspection of the model by both domain and software experts, whereby the intended correctness and completeness of the requirements can be effectively checked and documented.

- the concept of ASM refinement 
  -----------------------------
  defined in [3]. It permits to develop a system in well-documented controllable modular steps, linking ASMs at different levels of abstraction, say an abstract and a more detailed model, in a way the software engineer can justify as correct implementation step.
  The executability of ASMs supports using testing methods to validate the models whereas their mathematical nature allows one to adopt mathematical verification techniques where appropriate. 

The entire set of refinement steps transforms a ground model into well-documented executable code.
The model analysis at different levels of abstraction helps to avoid and to identify and correct fundamental design errors, which are difficult to detect and expensive to correct in code.
The intermediate models also support model reuse and design (programming) for change. 

Note that the development process is by no means linear, as is illustrated by the following diagram:

![](overview.svg)

For an introductory **text book** with lecture slides see the _Modeling Book_ [4] or the _Asm Book_ [5].

For **case studies** which illustrate typical applications of the method see the JBook [6] and provided [case studies](/case-studies) on this page.

For **tools** which support the ASM method see 
* [Asmeta](https://asmeta.github.io/)
* [CASM](https://casm-lang.org/)
* [CoreASM](https://github.com/CoreASM)
* [AsmGofer](https://tydo.eu/AsmGofer)

For the **early history** -- of the development of the method and early applications in various fields of computer science -- up to 2003 see [7] (available from https://www.jucs.org/jucs_8_1/the_origins_and_the/Boerger_E.pdf) and http://web.eecs.umich.edu/gasm/subjects/montage.html. 

The **epistemological motivation** for the definition of ASMs was to improve Turing's thesis, which has been proved in [2] from three natural axioms for sequential algorithms.
For the further development of such axiomatic and corresponding ASM-characterizations of algorithmic concepts (e.g. recursive algorithms, reflective algorithms, synchronous parallel algorithms, concurrent algorithms, communicating algorithms, etc.) see [9].
In practice, this so-called behavioral theory of ASMs supports the arguably most general form of ASMs as system specification.

In DBLP you can find a list of the **[ASM Workshops](https://dblp.org/db/conf/asm/index.html)** (partially including links to workshop proceedings) from 1994 to 2007 (preceding the merge of those workshops with the user meetings of Z and B to the ABZ Conference, started in 2008). 

## REFERENCES

[1] Y. Gurevich, *"Evolving algebras 1993: Lipari Guide"*. In: "Specification and Validation Methods", Oxford University Press, pp. 9-36, 1995. 

[2] E. Börger, *"The ASM ground model method as a foundation of requirements engineering"*. In: N. Dershowitz (ed.), "Verification: Theory and Practice", LNCS Volume 2772, Springer-Verlag, pp. 145-160, 2003.

[3] E. Börger, *"The ASM Refinement Method"*. In: Formal Aspects of Computing, volume 15, pp. 237-257, 2003. 

[4] E. Börger and A. Raschke, *"[Modeling Companion for Software Practitioners](https://modelingbook.informatik.uni-ulm.de)"*, Springer, 2018.
  
[5] E. Börger and R. F. Stärk, *"Abstract State Machines. A Method for High-Level System Design and Analysis"*, Springer, 2003.

[6] R. F. Stärk and J. Schmid and E. Börger, *"Java and the Java Virtual Machine: Definition, Verification, Validation"*, Springer-Verlag, 2001. 

[7] E. Börger, *"The Origins and the Development of the {ASM} Method for High-Level System Design and Analysis"*. In: J. Universal Computer Science, 8(1), pp. 2-74, 2002. 

[8] Y. Gurevich, *"Sequential {Abstract State Machines} Capture Sequential Algorithms"*. In: ACM Trans. Computational Logic, 1(1), pp. 77-111, 2000. 

[9] K.-D. Schewe, *"Computation on Structures: Behavioural Theory, Logic, Complexity"*. In: A. Raschke, E. Riccobene, K.-D. Schewe (eds.), "Logic, Computation and Rigorous Methods. Essays Dedicated to Egon Börger on the Occasion of His 75th Birthday", LNCS 12750, pp. 266-282, Springer, 2021. 
