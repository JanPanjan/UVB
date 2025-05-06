*PatternHunter* uses **nonconsecutive** seeds to boost sensitivity.

---

Downside of a [[BLAST#^a458d1|BLASTN]] search is that it uses a seed typically consisiting of a word size of **11 consecutive nucleotides**. Exact matches are identified in a DNA database and extended into longer alignments. 

This means, that **no matches are tolerated**. If we denote 1 for a match and 0 for a mismatch, the BLASTN word has a form:

$$
11111111111
$$

---

**PatternHunter** solves this problem with its customized seed:

$$
110100110010101111
$$

This seed still has 11 matches, but t**hey are distributed over a range of 18 nucleotides**. A query may align with a database entry having a mismatch at a position with 0 - **the mismatch is ignored** and the extension can still occur.

In a BLASTN search, if a mismatch occurs, no extension is made.

![[Pasted image 20250506153946.png]]

This makes PatternHunter more sensitive for a given amount of similarity.

![[Pasted image 20250506154126.png]]

---

This *seed model* approach has been adopted by other algoritms, such as [[BLASTZ]] and [[MegaBLAST]].