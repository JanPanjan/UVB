from Bio.Seq import Seq, MutableSeq
# from Bio.SeqUtils import gc_fraction # NEDELA

# ustvarimo sequence
seq = Seq("AGTACACTGGT")
print(seq)

# Seq objekti so immutable
try:
    print("seq[3] = 'o'")
    seq[3] = "o"
except:
    print("Error: ne moreš substituirat nukleotidov, punk\n")

# 1. ustvari MutableSeq it string (nemoreš iz Seq)
# 2. zamenjaj stvari
# 3. pretvori MutableSeq nazaj v Seq
my_seq = Seq("GCCATTGTAATGGGCCGCTGAAAGGGTGCCCGA")
mutable_seq = MutableSeq(my_seq)
mutable_seq[4:14] = "L"
mutable_seq.remove("G")
new_seq = Seq(mutable_seq)

print(
    f"""
    im seq:  {my_seq}
    new seq: {mutable_seq} """
)

# Seq objekt ima count metodo (kot strings), ki prešteje
# neprekrivajoče se objekte
print(
    f'''
    AAAA:      {"AAAA".count("AA")}
    AAAA(seq): {Seq("AAAA").count("AA")} '''
)

# komplement sekvence
compl = seq.complement()
rev_compl = seq.reverse_complement()
print(
    f"""
    komplement {seq}: {compl}
    reverse komplement {seq}: {rev_compl} """
)

# # GC content NEDELA
# gc = (seq.count("G") + seq.count("C")) / len(seq)
# gc_bio = gc_fraction(seq)
# print(f"gc: {gc}, gc_fraction: {gc_bio}")

# konkatenacija zaporedij
list_of_seqs = [Seq("AAA"), Seq("CCC"), Seq("GGTT")]
conc = Seq("").join(list_of_seqs)
print(
    f"""
    {[i for i in list_of_seqs]}
    konkatenirane sekvence: {conc} """
)

# upper to lower in obratno
new_seq = Seq("acgtACGT")
low_seq = new_seq.lower()
up_seq = new_seq.upper()
print(
    f"""
    seq:     {new_seq}
    low_seq: {low_seq}
    up_seq:  {up_seq}"""
)

# transkripcija
coding_dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
template_dna = coding_dna.reverse_complement()

# transkripcija v mRNA (zamenja T z U)
mRNA = template_dna.reverse_complement().transcribe()

# translacija v aminokislinsko zaporedje. * pomeni
ak_seq = mRNA.translate()

# za translacijo se uporablja standardna genetska koda. če imamo mitohnodrijsko
# zaporedje, moramo to podati kot argument
mito = coding_dna.translate(table="Vertebrate Mitochondrial")
# enako: mito = coding_dna.translate(table=2)

# translacija do prvega stop kodona
stop = coding_dna.translate(to_stop=True)
mito_stop = coding_dna.translate(table=2, to_stop=True)

# genomi ki ne uporabljajo standardnega začetnega kodona (metionin)
# GTG (GUG) je valin v standardni kodi ampak metionin (start) v bakterijski kodi
# sekvenca se mora začet s metioninom in končat s stop kodonom
bac_gene = Seq("GTGAAAAAGATGCATCACCGCTAA")

print(
    f"""
    5'->3':        {coding_dna}
    3'->5':        {template_dna}
    mRNA:          {mRNA}
    AK seq:        {ak_seq}
    stop:          {stop}
    Mitochondrial: {mito} (prvi stop kodon ni več stop kodon)
    mito stop:     {mito_stop}

    bac wrong: {bac_gene.translate(table="Bacterial")} (prvi je valin, stop-a ni)
    bac right: {bac_gene.translate(table="Bacterial", cds=True)}  (prvi je metionin, je stop)
    """
)
