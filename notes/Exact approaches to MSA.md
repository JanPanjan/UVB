Dynamic programming for pairwise sequence alignment, as described by *Needleman and Wunsch (1970)* is guranteed to find **optimal global alignments**.

==Exact methods== for [[Introduction to Multiple Sequence Alignment|MSA]] use dynamic programming although the matrix is now **multi-dimensional**, rather than 2-dimensional, which brings with it a lot more complexity.

![[Pasted image 20250514143740.png]]

The goal is to **maximize** the summed alignment score of each pair of sequences.

![[Pasted image 20250514143820.png]]

These methods generate optimal alignments but are **not feasible in time or space** for more than a few sequences.

For $N$ sequences of average length $L$, the time-complexity is $O(2^N L^N)$.

---

For feasible methods check [[Non-exact approaches to MSA]].