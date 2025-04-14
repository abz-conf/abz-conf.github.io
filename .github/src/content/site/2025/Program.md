---
title: ABZ 2025 – 11th International Conference on Rigorous State Based Methods
date:  "2024-09-17T00:00:00+01:00"
draft: false
share: false
contacts: true
commentable: false
editable: false

# Optional header image (relative to `static/img/` folder).
header:
  caption: ""
  image: ""

skyline: 
  image: "DuesseldorfSkyline_alternative_small.svg"
  url: "https://de.wikipedia.org/wiki/Düsseldorf"
---



## Program

To be announced in April/May 2025.

|                                                   |                  |
|---------------------------------------------------|------------------|
| **Workshops and Tutorials (Düsseldorf, Germany)** | June 10, 2025    |
| **ABZ 2025 Conference (Düsseldorf, Germany)**     | June 11-13, 2025 |


## Accepted Papers

### Main Track

<details>
  <summary>Klaus-Dieter Schewe and Flavio Ferrarotti. <b>Behavioural Theory of Reflective Parallel Algorithms.</b></summary>
    <p style="border: 2px solid gray; padding: 10px;">
        We develop a behavioural theory of reflective parallel
        algorithms (RAs), i.e. synchronous parallel algorithms that
        can modify their own behaviour. The theory comprises a set
        of postulates defining the class of RAs, an abstract
        machine model, and the proof that all RAs are captured by
        this machine model. RAs are sequential-time, parallel
        algorithms, where every state includes a representation of
        the algorithm in that state, thus enabling linguistic
        reflection. Bounded exploration is preserved using multiset
        comprehension terms as values. The model of reflective
        abstract state machines (rASMs) extends ASMs using extended
        states that include an updatable representation of the main
        ASM rule to be executed by the machine in that state.
    </p>
</details>

<details>
  <summary>Chiara Braghin, Giuseppe Del Castillo, Elvinia Riccobene
and Simone Valentini. <b>Using Symbolic Model Execution to Detect Vulnerabilities of
Smart Contracts.</b></summary>
    <p style="border: 2px solid gray; padding: 10px;">
        Smart contracts are programs that automate agreements
        between parties without the need for intermediaries.
        Embedded in a blockchain, they ensure transparency,
        immutability, and trustworthiness. While efficient, their
        immutable nature and reliance on internet-connected nodes
        make them susceptible to attacks. Identifying
        vulnerabilities before deployment is critical to mitigate
        risks, prevent catastrophic events, and avoid significant
        financial losses.
        This paper presents an approach to detecting vulnerable
        aspects of smart contracts written in Solidity and running
        on the Ethereum blockchain. Starting from an Abstract State
        Machine (ASM) model of a smart contract, the absence of
        certain vulnerabilities is expressed as model invariants.
        Symbolic execution of the ASM model is then used to reveal
        faulty execution paths resulting in invariant violations.
        In this way, vulnerable execution scenarios of the smart
        contract can be generated.
        As a proof of concept, we show the approach on a running
        case study, the "Auction" smart contract. Furthermore, we
        discuss the results of applying the technique to a number
        of Solidity smart contracts.
    </p>
</details>

<details>
  <summary>Vincent Trélat. <b>Safely Encoding B Proof Obligations in SMT-LIB.</b></summary>
     <p style="border: 2px solid gray; padding: 10px;">
        This paper presents a sound encoding of B proof obligations
        in SMT-LIB 2.7, leveraging the recent extensions of SMT-LIB
        to higher-order logic. Our encoding improves upon previous
        approaches by eliminating uninterpreted membership
        predicates and by avoiding the complexity of encoding
        functions as relations. Through SMT-LIB's support for
        higher-order constructs, we achieve a more natural
        representation of B's set theory, while ensuring soundness
        of the translation. Preliminary experimental results are
        promising and indicate that our encoding allows solvers to
        efficiently handle certain proof obligations that
        previously failed.
    </p>
</details>

<details>
  <summary>Nikolaj Jakobsen. <b>State-Based Modelling with a Concept DSL.</b></summary>
     <p style="border: 2px solid gray; padding: 10px;">
        Concept-based design is a new emerging formalism that uses
        concepts to facilitate the construction of modular and
        reusable software.
        Concepts are independent and generic units of functionality
        that can be
        composed to form complex applications. This work presents
        Conceptual,
        a domain-specific language for defining and composing
        concepts. A compiler from this language to Alloy6 is
        implemented, establishing a way to formally model and
        validate concept specifications of software. The practical
        application of Conceptual is examined qualitatively by
        leveraging Alloy’s analysis tools to reason about existing
        concept specifications in the literature.
    </p>
</details>

<details>
  <summary>Soaibuzzaman, Salar Kalantari and Jan Oliver Ringert. <b>On Writing Alloy Models: Metrics and a new Dataset.</b></summary>
     <p style="border: 2px solid gray; padding: 10px;">
        Alloy is a modeling language that combines relational
        first-order logic and temporal logic while providing
        powerful automated analyses via the Alloy Analyzer. Recent
        efforts in tool development and teaching of Alloy have
        contributed the Alloy4Fun dataset enabling many analyses of
        fine-grained model editing histories.
        We present a smaller, but complementary dataset of similar
        editing granularity. While the Alloy4Fun dataset captures
        users filling in predefined predicates, our dataset is more
        diverse and users develop all parts of Alloy models
        including signatures, fields, facts, and commands.
        We illustrate the differences between the datasets, define
        a Halstead metric to measure the difficulty of models, and
        evaluate model revision histories from both datasets on
        various metrics.
    </p>
</details>

<details>
  <summary>Linas Laibinis, Alexei Iliasov and Alexander Romanovsky. <b>Proof Semantics of Railway Interlocking.</b></summary>
     <p style="border: 2px solid gray; padding: 10px;">
        SafeCap is a modern toolkit for modelling, simulation and
        formal verification of railway networks, focused on
        fully-automated scalable safety verification of solid state
        interlocking (SSI) programs – a technology at the heart of
        many railway signalling solutions worldwide. In this paper,
        we elaborate on the formal foundations of the employed
        method by presenting the formal proof semantics of the
        modelled systems and the properties we are interested in
        verifying. We discuss the composite nature of this
        semantics, namely, interrelationships between signalling
        programs, signalling plan data, and the safety principles
        we need to ensure. The main focus is to formally justify
        derivation of a number of proof obligations that a specific
        interlocking solution must satisfy. The semantic
        definitions, properties, and inference rules are formalised
        with the proof assistant Coq.
    </p>
</details>

<details>
  <summary>Frederic Reiter, Roman Wetenkamp, Robert Schmid, Richard
Kretzschmar and Lukas Iffländer. <b>Towards an End-to-End Tool Chain for Traceable and
Verifiable Railway Signalling Specifications.</b></summary>
     <p style="border: 2px solid gray; padding: 10px;">
        Specifications for safety-critical railway signaling
        systems have
        traditionally been expressed in natural language. Due to a
        lack of trace-
        ability features, these requirements are difficult to
        reason about and thus
        very resistant to change. Validation and verification
        processes of cyber-
        physical components based on such specifications require
        extensive man-
        ual review and are prone to inefficiencies.
        This paper describes our work towards a comprehensive
        methodology for
        deriving formal specifications for railway signaling and
        generating veri-
        fied software for it. Our method focuses on accessibility
        for domain ex-
        perts and industrial applicability. To this effect, we
        integrate established
        techniques into a unified tool chain comprising (1) fault
        tree analysis,
        (2) the goal-oriented requirements engineering method KAOS,
        and (3)
        formal modelling with AdaCore SPARK. We aim to facilitate
        end-to-end
        traceability of requirements through all artifacts.
        Currently, we are ap-
        plying our methodology to a case study that involves the
        specification of
        a new ETCS-based moving block signalling system.
    </p>
</details>

<details>
  <summary>Pedro Silva, Nuno Macedo and José N. Oliveira. <b>On Quantitative Solution Iteration in QAlloy.</b></summary>
     <p style="border: 2px solid gray; padding: 10px;">
        A key feature of model finding techniques allows users to
        enumerate and explore alternative solutions. However, it is
        challenging to guarantee that the generated instances are
        relevant to the user, representing effectively different
        scenarios.
        This challenge is exacerbated in quantitative modeling,
        where one must consider both the qualitative, structural
        part of a model, and the quantitative data on top of it.
        This results in a search space of possibly infinite
        candidate solutions, often infinitesimally similar to one
        another.
        Thus, research on instance enumeration in qualitative model
        finding is not directly applicable to the quantitative
        context, which requires more sophisticated methods to
        navigate the solution space effectively.
        The goal of this paper is to explore and showcase
        different, generic strategies for navigating quantitative
        solution spaces, aiming to generate instances that differ
        considerably from those previously seen, ensuring a larger
        coverage of the search space.
        Such generic strategies are implemented in QAlloy – a
        quantitative extension to Alloy – and are evaluated against
        several examples ranging, in particular, over the integer
        and fuzzy domains.
    </p>
</details>

<details>
  <summary>Peter Riviere, Duong Dinh Tran, Takashi Tomita and Toshiaki Aoki. <b>A reasoning and explicit algebraic theory for BBSL in
Event-B: EB4BBSL framework.</b></summary>
     <p style="border: 2px solid gray; padding: 10px;">
        Automated Driving Systems (ADS) are major engineering and
        research topics, and ensuring the safety of such a critical
        system becomes crucial. Nevertheless, ADS are inherently
        complex, with many of their components, particularly
        sensors, relying on Artificial Intelligence. In addition to
        traditional environment data, ADS now processes object
        recognition outputs. To handle this new type of
        information, the Bounding Box Specification Language (BBSL)
        has been formalised to capture the relation between the
        abstraction of the image with the bounding box and the
        correct action to be performed. However, this language has
        a lightweight semantics, leading to multiple
        interpretations when no tools are available and its
        semantics remain implicit. In this paper, we propose a
        framework that fully formalises the language and allows the
        manipulation of the elements of the language as a
        first-class citizen in algebraic theory. We introduce three
        BBSL proof obligations and a mechanism to automatically
        generate and discharge the proof obligation. We also
        propose an extension of BBSL by explicitly formalising the
        semantics and behaviour of external interactions, such as
        importing information from outside sources.
        Furthermore, we also propose two instantiation mechanisms,
        deep-modelling and shallow-modelling, and we use an
        interpretation of BBSL in an Event-B machine. We
        demonstrate our approach in an example of BBSL
        specifications for the braking systems.
    </p>
</details>

<details>
  <summary>Anne Grieu, Jean-Paul Bodeveix and Mamoun Filali-Amine. <b>Translating Event-B models and  development proofs  to TLA.</b></summary>
     <p style="border: 2px solid gray; padding: 10px;">
        The work presented here is done in the context of the
        French ANR ICSPA (https://anr.fr/Projet-ANR-21-CE25-0015)
        project which aims at studying formal methods based on set
        theory (B, Event-B, TLA+). The first goal of this project
        concerns the verification of the proofs built with this
        systems through their translation to the pivot language
        LambdaPi. The second goal is the exchange of models and
        proofs between the considered set-based environments
        (Rodin, TLAPS, Atelier B).
        In this paper, we present our preliminary work were we
        translate Event-B models, proof obligations and their
        proofs to the TLA+ environment. The translation of models
        has already been studied in [HL16].
        Here, we also generate the proof obligations linked to
        invariant preservation in TLA+. Lastly, we translate proof
        interactively built using the Rodin platform to the TLA+
        proof language.
    </p>
</details>

<details>
  <summary>Dominique Cansell and Jean-Raymond Abrial. <b>The Proved Construction of a Protocol with an Example.</b></summary>
     <p style="border: 2px solid gray; padding: 10px;">
        This paper present a complete proved development of a
        protocol  inspired by the Lamport's Paxos protocol. Our
        protocol is not fault-tolerant. This work was carried out
        at the end of 2019.
    </p>
</details>

<details>
  <summary>Akram Idani and Aurélien Pepin. <b>Insider Threat Simulation Through Ant Colonies and ProB.</b></summary>
     <p style="border: 2px solid gray; padding: 10px;">
        In cyber-security, insider threats are particularly
        challenging to prevent because they are carried out by
        individuals who already have legitimate access to the
        information system (IS). In fact, insiders exploit their
        privileges to perform unauthorized actions. In previous
        works we proposed to tackle this problem via a backward
        symbolic search  built on a formal B specification of the
        IS. Unfortunately this approach is not performant because
        many proof obligations and constraints must be solved
        interactively. In this paper, we provide a heuristic-based
        forward search based on the ant colony optimization
        algorithm (API); that we implemented using ProB.
        We show how the API algorithm can be used to search for
        malicious scenarios and we present the results of our
        experiments in comparison with other approaches.
    </p>
</details>

<details>
  <summary>Alexander Onofrei, Marc Frappier and Émilie Bernard. <b>Model-Based Testing of Non-Deterministic Systems.</b></summary>
     <p style="border: 2px solid gray; padding: 10px;">
        Testing non-deterministic systems is challenging due to un-
        predictable behaviours arising from timing, concurrency,
        and random in-
        puts. This paper explores the application of model-based
        testing (MBT)
        to tackle these challenges, leveraging formal methods and
        tools to en-
        sure systematic test coverage. We employ ProB, a model
        checker for the
        B method, to analyse a formal model of the system under
        test (SUT)
        and generate test scenarios from the formal B model. As a
        proof of con-
        cept, we apply MBT to the TLS 1.3 protocol, a widely used
        complex
        cryptographic standard, and test one of its implementation
        using the
        BouncyCastle OpenSSL Java API. While the TLS handshake is
        primar-
        ily deterministic, it includes non-deterministic components
        like cipher
        selection and random value generation, making it an
        excellent candidate
        for evaluating MBT’s effectiveness. We present the design
        and logic of
        our proof of concept, showcasing its flexibility to support
        various mod-
        els and SUTs. This study demonstrates that combining formal
        meth-
        ods, non-deterministic analysis, and state-based testing
        can effectively
        address the challenges of non-deterministic systems,
        enabling improved
        testing strategies and greater system reliability.
    </p>
</details>

<details>
  <summary>Colin Snook, Asieh Salehi Fathabadi, Thai Son Hoang, Robert
Thorburn, Michael Butler, Leonardo Aniello and Vladimiro
Sassone. <b>Developing safe exception recovery mechanisms  for CHERI
capability hardware using UML-B formal analysis.</b></summary>
     <p style="border: 2px solid gray; padding: 10px;">
        While detection of suspicious or erroneous CPU behaviour
        can be achieved by generic mechanisms such as memory safe
        processors, recovering safely from the resulting exceptions
        is an application specific problem.
        The challenge is to ensure that a complex closed system
        including controller and its environment remain in a safe
        state while undertaking abnormal state changes in the
        controller as part of its exception recovery process.
        Handling exceptional error events is a complex task
        requiring insight and domain expertise to ensure that
        potential abnormal conditions are identified and a recovery
        process is designed to return the system to a safe state.
        Exception handling relies on a notion of
        transactions in order to identify how the system can
        be systematically returned to a consistent state.
        Formal methods can address this complexity, by supporting
        the analysis of transactions and exception handling at the
        abstract design stages utilising mathematical modelling and
        proofs.
        Event-B is a state-based formal method for modelling and
        verifying the consistency of discrete systems, however it
        lacks explicit support for analysing the handling of
        exceptions.
        UML-B is a diagrammatic front-end for Event-B modelling
        which allows models to be constructed using class diagrams
        and state-machines.
        In this paper, we use UML-B state machines to support the
        modelling of normal behaviour, with a notion of consistency
        and augment this with a technique for modelling
        'transactions' which may either complete to reach a
        consistent state or encounter exceptional errors that have
        to return the system to a consistent state despite the
        non-completion of the transaction. We also discuss an
        implementation of the modelled exception handling in the
        `C' programming language as a first stage towards automatic
        code generation of exception handlers.
    </p>
</details>

<details>
  <summary>Ben M. Andrew. <b>Weakening Goals in Logical Specifications.</b></summary>
     <p style="border: 2px solid gray; padding: 10px;">
        Logical specifications are widely used to represent
        software systems and their desired properties. Under system
        degradation or environmental changes, commonly seen in
        complex real-world robotic systems, these properties may no
        longer hold and so traditional verification methods will
        simply fail to construct a proof. However, weaker versions
        of these properties do still hold and can be useful for
        understanding the system’s behaviour in uncertain
        conditions, as well as aiding compositional verification.
        We present a counterexample-guided technique for
        iteratively weakening properties, apply it to propositional
        logic specifications, and discuss planned extensions to
        state-based representations.
    </p>
</details>

<details>
  <summary>Christophe Chen. <b>Formal modelling and reasoning on Assurance Cases expressed
with GSN in Event-B.</b></summary>
     <p style="border: 2px solid gray; padding: 10px;">
        An Assurance Case (AC) is a structured argumentation for
        certification describing how industrial activities support
        system requirements. The principle of AC relies on a goal
        (requirement) decomposition strategy that recursively
        breaks down an abstract goal into more concrete sub-goals
        until evidences become directly relevant to substantiate
        the goal. The most widely used notation for AC is the Goal
        Structuring Notation (GSN), which provides a graphical
        representation of argument structures.
        Despite the advances in the definition of a methodology for
        developing AC using the GSN, establishing the soundness of
        ACs relies essentially on experts reviews. Indeed, the lack
        of rigorous semantics for the GSN hinders the application
        of formal methods to check the consistency of ACs.
        The objective of our work is to design a logical (i.e.,
        proof-based) framework supporting the definition of
        formalised ACs, in order to assist system designers and
        certification authorities in building goal structures and
        check their consistency with respect to the formalised
        semantics and domain knowledge model formalising system
        specific concepts. The proposed framework will be grounded
        on the Event-B method and associated algebraic theories.
        The proposed framework shall define formal semantics for
        each GSN component (goal, evidence, assumption, strategy,
        etc. ) and formalise the implicit rationale behind goal
        decomposition. By leveraging a clear proof mechanism for
        the AC expressed in GSN, the impact analysis on argument
        modification will be controlled. Moreover, references to
        knowledge models and system models will be made explicit in
        order to enhance traceability.
    </p>
</details>

### Case Study

<details>
  <summary>Andrea Bombarda, Silvia Bonfanti, Angelo Gargantini, Nico
Pellegrinelli and Patrizia Scandurra. <b>Safety enforcement for autonomous driving on a simulated
highway using Asmeta models@run.time.</b></summary>
     <p style="border: 2px solid gray; padding: 10px;">
        Mission-critical systems, such as autonomous vehicles,
        operate in dynamic environments where unexpected events
        should be managed while guaranteeing safe behavior.
        Ensuring the safety of these complex systems is a major
        open challenge and requires robust mechanisms to enforce
        correct behavior during runtime. This paper illustrates a
        run-time safety enforcement framework for the output
        sanitization of an autonomous driving agent on a highway.
        The enforcement mechanism is based on a (formally validated
        and verified) Asmeta model representing the enforcement
        rules and used at run-time to eventually steer the driving
        agent to behave safely and avoid collisions. We demonstrate
        both efficacy and efficiency of the proposed enforcement
        approach by conducting an experimental evaluation. We
        connected our safety enforcer with the
        highway simulation environment and co-executed it with the
        pre-trained (unsafe) AI agents as provided by the ABZ 2025
        case study. We consider the single-lane case with the
        safety requirement and one scenario of the multi-lane case
        about preferring the right-most lane.
    </p>
</details>

<details>
  <summary>Duong Dinh Tran, Akira Hasegawa, Peter Riviere, Takashi
Tomita and Toshiaki Aoki. <b>Enhancing Decision-making Safety in Autonomous Driving
Through Online Model Checking.</b></summary>
     <p style="border: 2px solid gray; padding: 10px;">
        While artificial intelligence (AI) offers promising
        approaches
        for developing intelligent autonomous driving (AD) agents,
        ensuring the
        safety of these AI-driven AD systems is a critical
        challenge. This paper
        proposes an approach to enhancing AD safety through the
        development
        of a safety shield based on online model checking. The
        safety shield acts
        as a real-time verification layer, monitoring and
        validating the actions
        proposed by the AI agent before execution. We demonstrate
        the practicality and efficiency of our approach through a
        highway driving case
        study with different AI agents trained. We construct a
        formal model
        of the driving environment, capturing the states and
        behaviors of the
        ego vehicle and surrounding traffic, and specify the safety
        requirements
        within this model. For each proposed action, we leverage
        Maude’s invariant model checker to determine if executing
        the action would violate the
        safety requirements. Our experimental results demonstrate
        the capability
        of online model checking to enhance the safety of AI-driven
        autonomous
        vehicles.
    </p>
</details>

<details>
  <summary>Enguerrand Prebet, Samuel Teuber and André Platzer. <b>Modelling and Verification of Highway Car Control with
KeYmaera X.</b></summary>
     <p style="border: 2px solid gray; padding: 10px;">
        This article presents a formal model and formal safety
        proofs for the ABZ’25 case study in differential dynamic
        logic (dL). The case study considers an autonomous car
        driving on a highway avoiding collisions with neighbouring
        cars. Using KeYmaera X’s dL implementation, we prove
        absence of collision on an infinite time horizon which
        ensures
        that safety is preserved independently of trip length. The
        safety guarantees hold for time-varying reaction time and
        brake force. Our dL model considers the single lane
        scenario with cars ahead or behind. We demonstrate that dL
        with its tools is a rigorous foundation for runtime
        monitoring, shielding, and neural network verification.
        Doing so sheds light on inconsistencies between the
        provided specification and simulation environment
        highway-env of the ABZ’25 study. We attempt to fix these
        inconsistencies and uncover numerous counterexamples which
        also indicate issues in the provided reinforcement learning
        environment.
    </p>
</details>

<details>
  <summary>Paolo Crisafulli, Adrien Durier, Benjamin Puyobro and
Burkhart Wolff. <b>Polychronous RSS in a Process-Algebraic Framework - A Case
Study in Autonomous Driving Safety.</b></summary>
    <p style="border: 2px solid gray; padding: 10px;">
        The ABZ 2025 conference case study focuses on developing a
        safety controller for autonomous
        highway driving. Within this context, we present a model of
        interacting agents that synchronize
        with a global state at specific points in time.
        These agents follow the differential equations of standard
        kinematics, operating within a
        physical environment. They can make non-deterministic
        decisions regarding acceleration and follow
        strategies to avoid collisions.
        We instantiate our model according to the
        Responsibility-Sensitive Safety (RSS) setting.
        By defining agent properties such as extensions,
        cycle times, and acceleration limits, we concentrate on the
        single-lane model specified in the case
        study requirements document.
        A key feature of our instantiation is the consideration
        of agents operating with independent clocks. We
        demonstrate that the safety invariants defined by RSS
        still hold even when agents have independent and mutually
        unknown clocks. This enhances the model’s realism and
        makes it well-suited for refinement into implementations
        using synchronous languages such as Lustre and SCADE,
        enabling the development of safe and certifiable systems
        for the automotive industry.
    </p>
</details>

<details>
  <summary>Sebastian Betancourt and Valentina Castiglioni. <b>On The Road Again (Safely): Modelling and Analysis of
Autonomous Driving with Stark.</b></summary>
    <p style="border: 2px solid gray; padding: 10px;">
        The Stark tool has been introduced for the the
        specification, analysis and verification of cyber-physical
        systems operating under uncertainty.
        In this paper, we apply it to the modelling and safety
        analysis of several instances of a highway environment with
        autonomous vehicles: one vehicle will be controlled by a
        Stark agent, while the others are modelled as part of a
        Stark environment.
        Given the unpredictable behaviour of the environment, we
        analyse some safety guarantees on the behaviour of the
        agent in terms of its robustness against perturbations.
        To this end, we make use of the temporal logic RobTL and
        statistical model checking.
        We then discuss the use of Stark for the validation of the
        behaviour of reinforcement learning agents in the highway
        environment with the temporal logic DisTL.
    </p>
</details>

