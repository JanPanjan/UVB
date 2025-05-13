The other method of [[BLAST#3. Aligning NGS reads to a reference genome|aligning NGS reads to a reference genome]].

This aproach is faster than using [[Alignment based on Hash Tables]]. It's done using suffix trees or suffix arrays.

![[Pasted image 20250506173707.png]]

---

Two of the most popular aligners are **BWA (Burrows-Wheeler alignment)** and **Bowtie2**. Both take into consideration read lengths, sequencing error rates, gap penalties and local vs global alignment of reads.

> Bowtie (predecessor to Bowtie2) is 30-fold faster than [[Alignment based on Hash Tables#MAQ|MAQ]].

Key feature is a method used to index a reference genome (as large as the human genome) into <2 GB of memory.

The ref. gen. is first modified using the **Burrows-Wheeler transform (BWT)**, which is a **lossless** method of compressing data. This modified data can then be compressed (e.g. with Huffman encoding) in a fast and efficient way.