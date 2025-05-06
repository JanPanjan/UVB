*Basic local alignement search tool*. There are many different types of a BLAST search based on **desired input and output**:

- BLASTN ^a458d1
- BLASTP ^1693a8
- TBLASTN
- TBLASTX

---

## Specialized (organism specific) BLAST sites:

==Ensembl== 
of Welcome Trust Sanger Institute (WTSI) & European Bioinformatics Institute (EBI). Mainly for studying the **human genome**.
Its benefit is also that the output shows location of database matches by chromosome and an alignment summary with emphasis on genomic loci

==Welcome Trust Sanger Institute== 
with support for over 100 organisms. Also has servers for *Vertebrate Genome Annotation (VEGA)* project for human, chimpanzee, mouse, rat, dog, pig, zebrafish... genomes

---

## Downsides of a normal BLAST search

### 1. Doesn't recognize distantly related proteins

> Although PAM250 is a superior scoring matrix for distantly related proteins, many of them are too distantly related to a query to be detected by a standard BLAST search. And those that are detected get quetionable E-values.
>
> *Many homologous proteins have small sequence identity. They may have the same 3D structures based on methods such as X-ray cristallography, but they don't appear to share similarity in pairwise alignments.*

Specialized variants that fix this issue:

| tool                          | improvement                                                                      |     |
| ----------------------------- | -------------------------------------------------------------------------------- | --- |
| [[PSI-BLAST]]                 | better scoring matrices                                                          |     |
| [[RPS-BLAST]]                 | searching CDD with predefined [[Position-specific scoring matrix (PSSM)\|PSSMs]] |     |
| [[DELTA-BLAST]]               | most sensitive and accurate results                                              |     |
| [[PHI-BLAST]]                 | [[Amino acid residue pattern\|pattern]] specific searches                        |     |
| [[Hidden Markov Models\|HMM]] | profile searches based on probabilites                                           |     |

### 2. Difficult to search genomic DNA databases

> The genomic DNA includes both exons and introns. Ideally an alignment tool should find the exons.
>
> Genomic DNA usually has sequencing errors that should be taken into account.
> 
> Algorithms should detect genomics changes (deletions, duplications, inversions, translocations) and find a significant alignment.
> 
> Algorithms should be able to find small differences between DNA sequences (e.g. SNPs).


Specialized variants that fix this issue:

| tool                        | improvement                                                          |
| --------------------------- | -------------------------------------------------------------------- |
| [[PatternHunter]]           | tolerates mismatches in an alignment                                 |
| [[BLASTZ]]                  | for comparing sequences of different organisms                       |
| [[MegaBLAST]]               | for fast alignmenet of large DNA queries                             |
| [[Discontiguous MegaBLAST]] | for comparing sequences from different organisms                     |
| [[BLAT]]                    | uses an index to search genomic DNA databases quickly                |
| [[LAGAN]]                   | global alignment tool that utilizes local alignments                 |
| [[SSAHA2]]                  | utilizes a hash-table to search a large genomic DNA database quickly |

### 3. [[Aligning NGS reads to a reference genome]]