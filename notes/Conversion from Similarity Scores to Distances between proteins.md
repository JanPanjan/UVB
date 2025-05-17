One way to measure the distance between two sequences is to **count the number of mismatches in a pairwise alignment** (Levenstein distance).

Feng and Doolittle employed a method in their [[Progressive Sequence Alignment|progressive alignment algorithm]] which converts [[Raw similarity scores]] to distance scores:

$$
D = - \ln S_{\text{eff}}
$$

Where:
$$
S_{\text{eff}} = \frac{ S_{\text{real}(ij)} - S_{\text{rand}(ij)} }{ S_{\text{iden}(ij)} - S_{\text{rand}(ij)} } \times 100
$$

$S_{\text{real}(ij)}$ describes the **observed similarity score** for 2 aligned sequences $i$ and $j$.

$S_{\text{iden}(ij)}$ is the **average of the 2 scores** for the 2 sequences **compared to themselves** (if score $i$ to $i$ recieves score 20 and $j$ to $j$ recieves 10, then $S_{\text{iden}(ij)}=15$).

$S_{\text{rand}(ij)}$ is the **mean alignment score** derived from many **random** shufflings of the sequences.

$S_{\text{eff}}$ is a **normalized score**. 

- For **no similarity** between sequences $i$ and $j$, $S_{\text{eff}}=0$ and the distance is infinite.
- If they're **identical**, then $S_{\text{eff}}=1$ and the distance is 0.