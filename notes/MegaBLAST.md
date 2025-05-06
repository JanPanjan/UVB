Optimized for rapid alignment of very large DNA queries. 

![[Pasted image 20250506160912.png]]

---

## Word size parameter

Default word size is 28 and can be as large as 256 (in contrast to default word size of 11 of [[BLAST#^a458d1|BLASTN]]). 

> Smaller word size makes BLASTN more sensitive, but slower.

This increases speed, since the word size corresponds to the minimal length of an exact match required to initiate an extension.

## Scores and identity parameters

With MegaBLAST you can also specify the percent identity threshold to be reported (e.g. only alignments sharing values such as 99%, 90% or 80% identity) as well as match and mismatch scores.

> For sequences sharing 95-99% identity, a match score of +1 and a mismatch score of -3. For sequences sharing 85-90% identity, the mismatch score is -2 instead.
>
> More permisible for a little less identical sequences.

Gap opening penalty is 0 with the benefit of increased speed but alignment with more gaps. Gap extension penalty is based on match and mismatch scores.

---

Check also [[Discontiguous MegaBLAST]].