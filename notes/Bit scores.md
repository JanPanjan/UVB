It's denoted as $S'$ and is calculated from [[Raw similarity scores]] by **normalizing** it with the **statistical variables that define the scoring system** used.

$$
S' = \frac{\lambda S - \ln K}{\ln 2}
$$

^c5fa34

The E-value corresponding to a given bit score is defined as:

![[E-value#^3c197a]]

This makes it possible for bit scores from **different** alignments to be **compared** (even those with different [[Scoring matrix|scoring matrices]] in separate BLAST searches).

# Why are bit scores useful

- [[Raw similarity scores]] are **unitless** and have **little meaning alone**.
- They account for the **scoring system** used in the alignment.
- They allow scores to be **compared** between **different database searches**.
- They can tell you the [[E-value]] if you know the **size of the search space** ($m\times n$).