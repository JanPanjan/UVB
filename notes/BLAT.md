Designed to perform extremely rapid genomic DNA searches to find matches between queries that share 95% nucleotide identity.

![[Pasted image 20250506160944.png]]

---

In some ways it is a mirror image of [[BLAST]]. 
BLAST parses a query into words and then searches a database with words above a threshold value.

**BLAT** parses an entire genomic DNA database into an **index of words** (non-overlapping 11-mers in the genome, excluding repetitive DNA sequences). Then it searches a query using these words.

---

The database indexing strategy has been adopted by [[MegaBLAST]]. Although they are conceptually similar, BLAT is way faster.