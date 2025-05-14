Most commonly used algorithms that produce [[Introduction to Multiple sequence alignment|MSAs]] are derived from this alignment method.

It was proposed by Fitch and Yasunobu (1975) and popularized by Da-Fei Feng and Russel Doolittle (1987, 1990).

*Progressive* because the strategy calculates pairwise alignments between all of sequences, strarts with the best one and progressively aligns others to it one by one.

- ==Pro== : it permits **rapid alignment** of hundreds (or thousands) of sequences.
- ==Con== : the final alignment depends on the **order** in which sequences were joined and is therefore now guranteed to provide the most accurate alignment.

From 1990s till now the most popular web-based program for progressive MSAs has been **ClustalW**. Newer programs were developed which offer **improved performance** (e.g. MAFFT, ProbCons, MUSLE, T-COFFEE). The ClustalW algorithm is explained [[ClustalW algorithm|here]].