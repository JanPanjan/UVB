One of approaches of [[Aligning NGS reads to a reference genome]]. 

![[Pasted image 20250506172559.png]]

---

Hash table indexing adopts the seed-and-extend strategy that [[BLAST]] uses. Two inputs:

1. Reference genome
2. Large set of short reads

Begins the same way as BLAST - positions of $k-$mers are stored in a hash table and scanned for $k-$mer **exact** matches (seeds). These are then extended using dynamic programming.

> [[PatternHunter|Spaced seeds]] are commonly used because they increase sensitivity.

### MAQ

One of the earliest programs to use this approach. 

It builds **multiple hash tables** to index the reads. Then it **scans the reference database** against the hash tables to identify hits.

> Multiple hash tables ensure that all reads that have 0, 1 or 2 mismatches will be identified.

---

A limitation of this approach is that it can require **tens of gigabytes of memory** to store the indexed reads.

---

Check [[Alignment based on Suffix Trees]].