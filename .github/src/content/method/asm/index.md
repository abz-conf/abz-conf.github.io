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
The following three ingredients of the method support to **_develop executable code from specifications by stepwise refinement_** where at each step both mathematical verification of desired properties and experimental model validation by testing can be applied and fully documented to permit design for change:

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

For **tools** which support the ASM method see ... TODO: various links, e.g. https://tydo.eu/AsmGofer

For the **early history** -- of the development of the method and early applications in various fields of computer science -- up to 2003 see [7] (available from http://www.jucs.org/jucs_8_1/the_origins_and_the) and ... (TODO: link to Michigan Website). 

The **epistemological motivation** for the definition of ASMs was to improve Turing's thesis, which has been proved in [2] from three natural axioms for sequential algorithms.
For the further development of such axiomatic and corresponding ASM-characterizations of algorithmic concepts (e.g. recursive algorithms, reflective algorithms, synchronous parallel algorithms, concurrent algorithms, communicating algorithms, etc.) see [9].
In practice, this so-called behavioral theory of ASMs supports the arguably most general form of ASMs as system specification.

The **ASM Workshop Proceedings** 1994-2007 (preceding the merge of those workshops with the user meetings of Z and B to the ABZ Conference, started in 2008):

~~~
@Proceedings{Asm94,
  title = 	 {Technology and {F}oundations. {I}nformation {P}rocessing'94},
  year = 	 {1994},
  editor = 	 {B. Pehrson and I. Simon},
  volume = 	 {{I}, Track 4, Stream C: Evolving Algebras},
  series = 	 {},
pages={ 377--441},
  publisher = {Elsevier},
  address   = {Hamburg (Germany)},
note = {Contains Proceedings of First ASM Workshop}
}

@Proceedings{Asm98,
  title = 	 {Fifth {I}nternational {W}orkshop on {A}bstract {S}tate {M}achines},
  year = 	 {1998},
  editor = 	 {U.Gl\"asser and P.Schmitt},
  volume = 	 {},
  series = 	 {},
  publisher = {Otto-von-Guericke-Universit\"at},
  address   = {Magdeburg (Germany)},
pages = {III+158},
note = {Contains Proceedings of Fifth International ASM Workshop at Informatik'98}
}

@Proceedings{Asm00,
  title = 	 {Abstradt {S}tate {M}achines. {T}heory and {A}pplications},
  year = 	 {2000},
  editor = 	 {Y.Gurevich and P.W.Kutter and M.Odersky and L.Thiele},
  volume = 	 {1912},
  series = 	 {LNCS},
  publisher = {Springer},
  address   = {Monte Verit\`a (Switzerland)},
note = {Proceedings of 7th International ASM Workshop}
}

@Proceedings{Asm01,
  title = 	 {Formal Methods and Tools for Computer Science. Eurocast 2001},
  year = 	 {2001},
  editor = 	 {R.Moreno-Diaz and A.Quesada-Arencibia},
  volume = 	 {},
  series = 	 {},
  publisher = {IUCTC Universida de Las Palmas de Gran Canaria},
  address   = {Las Palmas (Spain)},
note = {Contains Extended Abstracts of 8th ASM Workshop. For selected full workshop papers see \cite{BoeGla01}.}
}

@Book{Asm02,
  editor =	 {A.Blass and E.B\"orger and Y.Gurevich},
  title =	 {Theory and Application of Abstract State Machines},
  publisher =	 {Schloss Dagstuhl},
  year =	 {2002},
note = {Seminar Report 336. \url{https://www.dagstuhl.de/02101}}
} 

@Proceedings{Asm03,
  title = 	 {{Abstract State Machines} 2003. Advances in {T}heory and {P}ractice},
  year = 	 {2003},
  editor = 	 {E.B\"orger and A.Gargantini and E.Riccobene},
  volume = 	 {2589},
  series = 	 {LNCS},
  publisher = {Springer},
  address   = {},
note = {Contains Proceedings of 10th ASM Workshop (Taormina, Italy). For a selection of extended workshop papers see \cite{Asm03Tcs}.}
}

@BOOK{Asm03Tcs,
	EDITOR = {E.B\"orger},
	TITLE = {Abstract {S}tate {M}achines and high-level system design and analysis},
	YEAR = {2005},
	PUBLISHER = {Elsevier},
	SERIES = {Theoretical Computer Science (Special Issue)},
	VOLUME = {336 (2--3) },
      note = {ISSN 0304--3975. Selection of extended papers from ASM'03 (Taormina, Sicily)}
}


@Proceedings{Asm04,
  title = 	 {{Abstract State Machines} 2004. Advances in {T}heory and {P}ractice},
  year = 	 {2004},
  editor = 	 {W.Zimmermann and B.Thalheim},
  volume = 	 {3052},
  series = 	 {LNCS},
  publisher = {Springer},
  address   = {},
note = {Contains Proceedings of 11th ASM Workshop (Lutherstadt Wittenberg)}
}


@Misc{Asm05,
  author =	 {E.B\"orger and  D. Beauquier and A. Slissenko},
  title =	 {Proc. 12th International Workshop on {A}bstract {S}tate {M}achines 
{ASM}'05},
howpublished =	 { Universit\'e Paris 12 (France)},
year = {2005},
pages ={424},
note = {For a selection of extended workshop papers see \cite{Asm05FI}}
} 

@BOOK{Asm05FI,
	EDITOR = {E.B\"orger},
	TITLE = {The {A}bstract {S}tate {M}achines method},
	YEAR = {2007},
	PUBLISHER = {IOS Press},
	SERIES = {Fundamenta Informaticae (Special Issue)},
	VOLUME = {77},
      note = {ISSN 0169--2968. Selection of extended papers from ASM'05 (Paris)}
}

@BOOK{Asm07,
	EDITOR = {E.B\"orger and A.Prinz},
	TITLE = {Quo vadis {A}bstract {S}tate {M}achines?},
	YEAR = {2008},
	PUBLISHER = {},
	SERIES = {J. Universal Computer Science (Special Issue)},
	VOLUME = {14 (12)},
      pages = {1921--2071},
      note = {Selection of extended papers from ASM'07 (Grimstadt, Norway)}
}
~~~


## REFERENCES

~~~
[1] @InCollection{Gurevich94b,
  author =       {Y. Gurevich},
  title =        {{Evolving algebras 1993: Lipari Guide}},
  booktitle =    {Specification and Validation Methods},
  publisher =    {Oxford University Press},
  year =         {1995},
  pages =        {9--36},
  editor =       {E. B{\"o}rger}}

[2] @InProceedings{Boerger03a,
  author =	 {E. B{\"o}rger},
  title =	 {The {ASM} ground model method as a foundation of requirements                   engineering},
  booktitle =	 {Verification: Theory and Practice},
  pages =	 {145-160},
  year =	 {2003},
  editor =	 {N.Dershowitz},
  volume =	 {2772},
  series =	 {LNCS},
  publisher =	 {Springer-Verlag}}


[3] 
@Article{Boerger02b,
  author =	 {E. B{\"o}rger},
  title =	 {The {ASM} Refinement Method},
  journal =	 {Formal Aspects of Computing},
  volume =	 {15},
  year =	 {2003},
  pages =        {237-257}}

[4] @Book{BoeRas18,
  author = 	 {E. B{\"o}rger and A. Raschke},
  title = 	 {Modeling Companion for Software Practitioners},
  publisher = 	 {Springer},
  year = 	 {2018},
  note = 	 {ISBN 978-3-662-56641-1. For Corrigenda and lecture material on                              themes treated in the book
                  see \url{http://modelingbook.informatik.uni-ulm.de}}

[5] @Book{BoeSta03,
  author = 	 {E. B{\"o}rger and R. F. St{\"a}rk},
  title = 	 {Abstract {S}tate {M}achines. A Method for High-Level System
                  Design and Analysis},
  publisher = 	 {Springer},
  year = 	 {2003}}

[6] @Book{StScBo01,
  author =       {R. F. St{\"a}rk and J. Schmid and E. B{\"o}rger},
  title =        {Java and the Java Virtual Machine: Definition,
                  Verification, Validation},
  publisher =    {Springer-Verlag},
  year =         {2001}}



[7] @Article{Boerger02a,
  author =	 {E. B{\"o}rger},
  title =	 {The Origins and the Development of the {ASM} Method
                  for High-Level System Design and Analysis},
  journal =	 {J.~Universal Computer Science},
  volume =	 {8},
  number =	 {1},
  year =	 {2002},
  pages =	 {2--74}}

[8] @Article{Gurevich00,
  author =       {Y. Gurevich},
  title =        {Sequential {Abstract State Machines} Capture Sequential
                  Algorithms},
  journal =      {ACM Trans. Computational Logic},
  year =         {2000},
  month =        {July},
  volume =       {1},
  number =       {1},
  pages =        {77--111}}

[9] @inproceedings{Schewe21,
  author    = {K.-D. Schewe},
  title     = {Computation on Structures: Behavioural Theory, Logic, Complexity},
  booktitle = {Logic, Computation and Rigorous Methods. Essays Dedicated to Egon B\"orger
                   on the Occasion of His 75th Birthday},
  editor    = {A.Raschke and E. Riccobene and K.-D. Schewe},
  series    = {Lecture Notes in Computer Science},
  volume    = {1275},
  publisher = {Springer},
  pages     = {266--282},
  year      = {2021}
}
~~~
