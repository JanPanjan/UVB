*Limites Area Global Alignment of Nucleotides* is a pairwise alignment tool for genomic DNA that utilizes *anchors*.

![[Pasted image 20250506161150.png]]

---

The algorithm proceeds in 3 steps:

1. It generates a local alignment between 2 sequences, identifying a set of **anchors**.
2. Creates a rough global map consisting of a maximally scoring ordered subset of the alignments (anchors).
3. Compuets a final global alignment, restricting the operations to the limited are defined by the map.

This search strategy **avoids doing a costly global alignment** with the Needleman-Wunsch algorithm.