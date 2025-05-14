When we consider a [[Proteini in peptidi|protein (or gene)]], one of the most fundamental questions is *what other proteins are related?*

Biological sequences often occur in **families**, which may consist of

- [[Orthologs]]
- [[Polymorphic variants]]
- [[Paralogs]]

Sequences diverge from each other due to **duplication** within a genome or **specification** (leading to the existence of orthologs).

**Domains** or **motifs** that characterize a protein family are defined by the existence of a MSA of a group of [[Homologs|homologous]] sequences.

> [!abstract] Definition of multiple sequence alignment
> A MSA is a collection of three or more [[Proteini in peptidi|protein]] (or nucleic acid) sequences that are partically or completely aligned.
>
> Homologous residues are aligned in columns and these **aligned columns characterize a MSA**. Aligned columns are homologous in an
> - **evolutionary sense** : presumably derived from a common ancestor
> - **structural sense** : aligned [[Aminokislinski ostanek|amino acid residues]] tend to occupy corresponding positions in the [[Terciarna struktura proteinov|three-dimensional structure]] of each aligned protein.
>

The alignment may be determined due to features of the amino acids, such as:

| feature                                                              | e.g.                                                                                                  |
| -------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| **highly conserved residues**                                        | cysteins which involved in forming [[Disulfidne vezi \| disulfide bridges]].                               |
| **conserved motifs**                                                 | transmembrane span, immunoglobulin domain ...                                                            |
| **conserved features of the secondary structure of the proteins**    | residues that contribute to [[Alfa heliksi         \| alpha-helices]] or [[Beta lističi \| beta-sheets]] |
| **regions that show consistent patterns of insertions or deletions** | yes                                                                                                      | 

It has many useful applications:

- Useful in showing that **proteins in the same protein family have similarities**.
- Useful for **discovering related proteins** when used in database searching, due to its ability to detect conserved regions.
- Useful for **predicting secondary structure** of proteins.

# Why multiple sequence alignment?

## 1. Alignment of a protein family

==Sequences within a protein family tend to evolve way faster than their structures.==

> We saw that two sequences can have low similarity and the same structure.

It may be impossible to identify the residues that should be aligned as defined by the three-dimensional structures of proteins in the family. **We don't have high-resolution structural data available**.

Similary **we often don't have functional data to identify domains** (e.g. amino acids that form the catalytic site of an enzyme).

This is why we rely on sequence data of these proteins. It's possible to compare results of MSAs generated from sequence data and then to examine known structures of those proteins.

> For two **divergent but significantly related protein sequences** (sharing e.g. 30% identity), **about 50%** of the residues are **superimposable** in the two structures (*Chotia and Lesk, 1986*).

## 2. Unsignificant results of pairwise alignment

Proteins can have **similar biological function** and **similar tridimensional structure** while ==not having significant similarity of their sequences==.

Only with multiple sequence alignment we can get significant results by taking into account **many** sequences instead of just 2.

> For example, pairwise alignment of `POLICA` and `PTICA` gives two optimal alignments:
> 
> ```
> P O L I C A     P O L I C A
> P - T I C A     P T - I C A
> ```
> 
> Only with a third sequence, `POTICA`, it becomes clear that the first alignment is probably the right one.
> 
> ```
> P O L I C A
> P O T I C A
> P - T I C A
> ```

Most protein families also have distantly related proteins. MSA is **far more sensitive** to distantly related sequences than pairwise alignment.

> e.g. [[DELTA-BLAST]] and [[Hidden Markov Models|HMM]] rely on profiles generated based on MSAs.

## 3. Detecting harmful gene variants

Each human genome harbours about 11'000 nonsynonymous single-nucleotide variants of which about 300 are predicted to be *deleterious*.

Algorithms that predict whether variants are harmful often rely on MSAs, since deleterious vaiants tend to occur at more conserved positions.

---

Check more about MSA [[Multiple sequence alignment|here]].