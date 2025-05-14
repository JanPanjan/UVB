This [[Progressive Sequence Alignment|progressive algorithm]] for [[Multiple sequence alignment|MSAs]] proceeds in **3 stages**. 

> [!important]
> The examples will show alignment of two groups of **globins** - one of **distantly related** ones and the other of **closely related** ones.
>
> In this example the selected proteins have their 3D-structure solved by X-ray crystallography, which will help us interpret the accuracy of alignment from a **structural** as well as **evolutionary** perspective.

# 1. Global Alignment

The global alignment of Needleman and Wunsch is used to creae pairwise alignments of **every protein** of our group.

![[Pasted image 20250514194541.png]]

Algorithms that do pairwise alignments generate [[Raw similarity scores]]. For ClustalW the default setting for scores are the **percent identities**.

Many progressive methods use a **distance matrix** rather than a similarity matrix to describe how the proteins are related. The **conversion** from similarity scores to distances is described [[Conversion from Similarity Scores to Distances between proteins|here]].

