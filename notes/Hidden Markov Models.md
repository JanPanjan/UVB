---
aliases:
- HMM
- HMMs
---

More versatile than [[Position-specific scoring matrix (PSSM)|PSSMs]] to generate scoring matrices. They are widely used in many bioinformatics areas:

- sequence alignment
- prediction of protein structure
- predictions of transmembrane regions in proteins
- analysis of chromosomal copy number changes
- gene finding algorithms

Its main strength is that it is a **probabilistic model** - it asses likelihood of matches/mismatches/insertions/deletions at a given position of an alignment.

It can convert a [[Multiple sequence alignment]] into a position-specific system.

## Structure of a Hidden Markov Model

A Markov chain is a data structure that contains a start sate, a finite discrete set of possible states and transition functions that describe how to move from one state to the next. This type of model is also reffered to as a *finite-state machine*.

The process occupies one state at a time and remains in that state or moves to another allowable state.

### Example of a nucleotide alignment of human and mouse beta globin

Focus on the position at which a T residue in human is aligned with a C residue in mouse

![[Pasted image 20250506140157.png]]

A Markov model displays transition probabilities for each nucleotide changing to any other.

![[Pasted image 20250506140314.png]]

Each circle is a state. 16 arrows represent probabilites of making a transition to another state (nucleotide). They can be summarized in a *transition matrix*:

![[Pasted image 20250506140425.png]]

> Simialr to the mutation probability matrix developed by Dayhoff and her colleagues.

The *hidden* in its name indicates, that we cannot observe the states directly, however we have observations from which we can infer the hidden states.

> **Observed states** = positions of amino acids (nucleotides) in a multiple sequence alignment.
>
> **Hidden states** = match/insert/delete states.

The states define a model for the sequence of that protein or nucleotide family.

Consider a slice of the alignment of five globin proteins:

![[Pasted image 20250506140934.png]]

A HMM can be calculated by estimating the probability of occurence of each amino acid in the five positions (resembling the [[Position-specific scoring matrix (PSSM)|PSSM]] of [[PSI-BLAST]]).

![[Pasted image 20250506141047.png]]

A score can be derived for the occurence of any specific pattern of a related query. Example for `HARTV`:

![[Pasted image 20250506141249.png]]

A **profile HMM** is constructed from a multiple sequence alignment to define a set of probabilites:

| shape    | labels                | name         | information                                                                  |
| -------- | --------------------- | ------------ | ---------------------------------------------------------------------------- |
| squares  | $m_{1}, \dots, m_{5}$ | main state   | *might* correspond to residues of an amino acid sequence (such as `HAEKL`)   |
| diamonds | $i_{1}, \dots, i_{5}$ | insert state | model variable regions where sequences can be inserted if neccessary         |
| circles  | $d_{1}, \dots, d_{5}$ | delete state | correspond to gaps in sequence and provide a path to skip columns in the MSA |

The sequence of a HMM is defined by a serios of states that are influenced by two main parameters:


| parameter              | information                                                                     |
| ---------------------- | ------------------------------------------------------------------------------- |
| transition probability | describes the path followed along the hidden state sequence of the Markov chain |
| emission probability   | probability of matching a particular amino acid residue                         |

Unlike [[PSI-BLAST]], HMMs include probabilities associated with insertions and deletions.