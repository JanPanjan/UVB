When we sequence a haploid human genome, which has about 3 billion bases, it is neccessary to obtain **adequate depth of coverage** (such as an *average of 30-fold redundancy for each base*) to have reliable base calls.

> This means that for each base in the genome reference, around 30 reads would cover (map back to) each nucleotide in the reference.

For **90 billion base pairs of sequence**, each read may be **100 bases in length** and there would be **900 million reads**.

---

## How are these reads aligned to a reference human genome?

When performing alignment, we need to consider some errors:

- ==matches and mismatches== - not all reads will map to the genome at **unique positions** (around 5% of the human genome has duplications, about 50% has other kinds of repetitive DNA).
- each genome is expected to gave ==single-nucleotide variants== and ==variants of tecnical error==.
- genome sizes and cumulative read sizes are so large that **dynamic programming algorithms** (e.g. Smith-Waterman) are ==too slow==. Some form of **indexing is required**

Two main approaches arose to solve this issues:

1. [[Alignment based on Hash Tables]]
2. [[Alignment based on Suffix Trees]]