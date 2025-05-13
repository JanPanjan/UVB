*Pattern-hit initiated [[BLAST]]*. Specialized BLAST program that allows you to find matches that match a specified [[Amino acid residue pattern]] and are significantly **related** to the query.

---

## Example of a PHI-BLAST search with human RBP4

### 1. Defining a pattern

A [[BLAST#^1693a8|BLASTP]] search of bacterial sequences using human RBP4 (`NP_006735`) as query in the refseq database gives (in 2015) **7 significant hits** with small $E-$values. 

> From past experiments and literature, we know there are a lot more bacterial lipocalins distantly related to our query.

Select top 3 best-scoring hits and [[Multiple sequence alignment|align them]] with human RBP4. The alignment shows which amino acid residues are shared between sequences. We can try and define a [[Amino acid residue pattern|pattern]].

Examining the alignment, we can define our pattern as `NFDX(5)GXW[YF]` (similar to a regular expression).

![[Pasted image 20250506132500.png]]

- `X(5)` - five positions that can be any amino acid residue
- `[YF]` - this position may be a [[tirozin|tyrosine]] (Y) or a [[fenilanin|phenilanine]] (F) 

### 2. Using PHI-BLAST

With this pattern we search the database again, but now with PHI-BLAST. We get 28 significant matches, that are all bacterial lipocalins.

Output result is identical to [[PSI-BLAST]] with an adition of a series of asterisks that give information to where the query and hit match the given pattern.

![[Pasted image 20250506132520.png]]