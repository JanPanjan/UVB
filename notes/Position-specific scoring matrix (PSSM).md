---
aliases:
- PSSM
- PSSMs
---

Captures information about **substitution patterns** for each [[Aminokisline|amino acid]] in a query. 
Its dimension is $L \times 20$.

- $L$ is length of query
- 20 for each amino acid residue

**Redundant sequences with more than 94% identity are eliminated** to ensure that a group of very closely related protein sequences will not overly bias the construction of a PSSM in [[PSI-BLAST]].

![[Pasted image 20250506151635.png]]

Numeric values are scores assigned to residues. 

- Example of alanine:
	- where it has scores like +3, it tends to occur frequently for many proteins in this family
	- where it has scores like +1, it tends to occur less frequently and is not well conserved
- Example of glycine:
	- position 10 has score +2; sum across all columns is -37 $\implies$ alignment of glycine with any other amino acid is not likely
	- position 20 has score +7; sum across all columns is -64 $\implies$ even less likely $\implies$ occurence of glycine is very likely

The fact that a *score varies for the same amino acid* is the main feature of a PSSM.

## Example for fungi

Enter `NP_000509` (human beta globin), PSI-BLAST, RefSeq database restricted to fungi. With default parameters, there are over 60 hits, 9 having significant $E-$values.

> By inspection, they are hypothetical proteins, so it's not clear from their names alone whether they are globins.
> Some unsignificant matches are distantly related proteins and are authentic globins (similar 3D-structure, related biological functions as carriers).

Upon selecting all significant hits, a [[Multiple sequence alignment]] is made and from it the PSSM. This unique profile is used then to search the database again. New proteins are added to the alignment. Number of significant hits rises from 9 to 182. In subsequent iterations to 206. Once convergence is reached, no more database matches are found and the search ends.

**Result:** after a few iterations, over 200 matches were identified, many of them are distantly related proteins.

### Understanding the sensitivity of search with *Candida albicans*


| iteration | $E-$value  | bit-score | length of alignment |
| --------- | ---------- | --------- | ------------------ |
| 1         | $4e{-04}$  | 43.5      | 87                  |
| 2         | $10e{-36}$ | 136       | 110                 |
| 3         | $2e{-33}$  | 128       | 146                 | 

$E-$value drops and score of alignment increases along with length of the alignment. This is because of the **specifically constructed scoring matrix for this family of proteins**.