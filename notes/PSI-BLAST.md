---
aliases:
  - PSSM
---


Specialized [[BLAST]] that is **more sensitive**. It's purpose is to look deeper into the database to find distantly related [[Proteini in peptidi|proteins]].

---

## Steps of PSI-BLAST

1. **Normal BLASTP search** using your query and a standard scoring matrix
2. Constructs a [[Multiple sequence alignment]] from search, from this it builds a [[Position-specific scoring matrix (PSSM)]], also reffered to as a *profile*
3. The PSSM is **used as a query** to search the database again
4. Estimates statistical signifance using parameters for **gapped** alignments
5. Continues search process i**teratively**, each time creating a new profile, ends when convergence is reached (no new matches) or after a few iterations.

---

## Problems of corruption

Main source of error is adition of sequences that are unrelated to the query. This occurs most often when the query contains **regions of highly biased amino acid composition**. 

> Corruption is defined as occuring when the PSSM produces at least one false positive (not homologous) alignment of $E < 1e{-4}$

There are 3 main approaches of stopping corruption.

==Applying a filtering algorithm that removes biased amino acid regions==
*Low entropy* regions = stretches of higly basic, acidic, rich in a residue amino acids

==Adjusting the expect value of search to a lower value==
Risky, since it can also interfere with true positive results

==Visually inspect==
each iteration's results, select and remove suspicious matches.