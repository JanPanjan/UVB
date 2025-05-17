This [[Progressive Sequence Alignment|progressive algorithm]] for [[Multiple sequence alignment|MSAs]] proceeds in **3 stages**. 

> [!important]
> The examples will show alignment of two groups of **globins** - one of **distantly related** ones (NP_000509, NP_005359, NP_067080, 1FSL, 1D8U) and the other of **closely related** ones. (NP_000509, XP_508242, XP_537902, NP_058652)
>
> In this example the selected proteins have their 3D-structure solved by X-ray crystallography, which will help us interpret the accuracy of alignment from a **structural** as well as **evolutionary** perspective.

# 1. Global Alignment

The global alignment of Needleman and Wunsch is used to create pairwise alignments of **every protein** of our group.

Algorithms that do pairwise alignments generate [[Raw similarity scores]]. For ClustalW the default setting for scores are the **percent identities**.

Many progressive methods use a **distance matrix** rather than a similarity matrix to describe how the proteins are related. The **conversion** from similarity scores to distances is described [[Conversion from Similarity Scores to Distances between proteins|here]].

---

For distantly related proteins, the best score is assigned to soybean and rice globin.

![[Pasted image 20250514194541.png]]

For a group of closely related proteins, all have high scores.

![[Pasted image 20250516133019.png]] ^4d6f57

# 2. Guide tree

A guide tree is calculate from the distance matrix. There are two main ways of doing this - either with **UPGMA** (unweighted pair group method of arithmetic averages) or with **k-means** (the neihgbor-joining method).

Main features of the tree:

- its **topology** - branching order
- **branch lengths** - can be drawn so they are proportional to evolutionary distance

The tree reflects the **relatedeness of all the proteins to be multiply aligned**.

---

And correctly so, distantly related proteins (first picture) have longer branches, while the closely related have shorter branches (second picture).

![[Pasted image 20250516133434.png]]

The [[ClustalW algorithm#^4d6f57|chicken globin (gallus gallus)]] has the lowest score relative to the human, chimpanzee, dog and mouse beta globins, which is reflected in the tree.

![[Pasted image 20250516133456.png]]

> [!warning] Guide vs Phylogenetic tree
>
> A guide tree is not considered a phylogenetic treem since it doesn't include a model that accounts for substitutions that commonly occur at positions where residues are aligned.

# 3. Multiple sequence alignment

The MSA is created based on the order of the guide tree. First the two most closely related sequences are selected to create a pairwise alignment (leaves of the tree). 

The next sequence is either added to this alignment or used in another pairwise alignment. At some point these groups (profiles) are aligned to eachother.

It ends when the root of the tree is reached and all sequences have been aligned.

---

For example, soybean and rice globin will be aligned first since they're the most closely related.

![[Pasted image 20250516134432.png]]

<br>

| sign           | explanation                                                  |
| -------------- | ------------------------------------------------------------ |
| `*` (asterisk) | positions in which the residue is 100% conserved in a column |
| `:` (colon)    | conservative substitutions                                   |
| `.` (dot )     | less conservative substitutions                              |

Regions of [[Alfa heliksi|alpha helices]] based on X-ray cristalography are colored red.

3 **highly conserved regions** are in bold blue colors - *phe44, his65* and *his93* of myoglobin. The two [[Histidin|histidines]] are important in coordinating protein binding to **heme** group.

![[Pasted image 20250516135908.png]]

In closely related proteins the arrows point to *phe44, his72* and *his104* of the human beta globin. The green box corresponds to the same region as in the alignment of distantly related ones.

ClustalW colors amino acid groups (e.g. acidic amino acids are colored blue, basic are colored magenta, hydrophobic are colored red, etc.).

The asterisks highlight dozen column positions of conserved positions among all closely related globins. There's also no gaps since the level of conservation is so high and therefore no ambiguity of how to align these sequences.