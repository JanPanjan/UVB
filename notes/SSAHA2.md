*Sequence Search and Alignment by Hashing Algorithm.* 

It's designed to search large DNA databases very rapidly. Commonly used to map [[Next Generation Sequenceing (NGS)|NGS reads]] to a reference genome.

---

An input file includes the **genomic reference sequence** (e.g. human genome) in the FASTA format.

It converts this database into a **hash table** with a fixed word length (user selected $k-$mers). This hash table can be searched quickly for matches by pairwise alignment.

**Sequencing reads** in the FASTQ format are **mapped against the genomic reference**. Exactly matching seeds are identified and aligned usign a modified Smith-Waterman algorithm.