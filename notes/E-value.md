The expect value tells us the *estimated* number of [[High scoring segment pairs|HSPs]] having some [[Raw similarity scores|raw score]] (or better) assigned to it by **chance alone**. 

> In other words, how many false positive hits the search generated.

It's defined as:

$$
E = K m n e^{- \lambda S}
$$

^3ae0df

<br>

| parameter      | explanation                           | 
| --------- | ------------------------------------ |
| $E$       | expect value                         |
| $S$       | [[Raw similarity scores\|raw score]] |
| $m$       | length of the query sequence         |
| $n$       | length of the database               |
| $\lambda$ | scaling factor of the scoring system |
| $K$       | scaling factor of the search space   |

> $K$ and $\lambda$ are often reffered to as the *Karlin-Altschul statistics*.

On the other hand, E-value corresponding to a [[Bit scores|bit score]] is defined as:

$$
E = m n \times 2^{- S'}
$$

^3c197a

# Relation to $p$ values

The $p$ value is the probability of a chance alignment occuring with the assigned score or better. 

It's calculated by relating the [[Raw similarity scores|raw (observed) score]] $S$ to the expected distribution of [[High scoring segment pairs|HSP scores]] from comparisons of **random sequences** of the **same length** and **composition** as the query.