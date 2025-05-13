*Domain enhanced lookup time accelerated [[BLAST]]*. Most sensitive and accurate protein search tool at NCBI. 

It's scoring matrices are more sensitive at detecting significantly related sequences than PAM or BLOSUM matrices.

It begins with a [[RPS-BLAST]] search, then uses the resulting [[Position-specific scoring matrix (PSSM)|PSSM]] to search a protein database.

---

Advantages:

- Larger, more complete PSSMs (relies on the well curated [[RPS-BLAST#^157c86|CDD database]])
- More sensitive than [[BLAST#^a458d1|BLASTN]] and [[PSI-BLAST]] (about 3-times more homologous hits).
- Better quality alignment than [[BLAST#^1693a8|BLASTP]].
- Fast

---

It won't report information about user-selected [[Amino acid residue pattern|patterns]]. This is why [[PHI-BLAST]] was created.