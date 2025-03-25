from Bio.Seq import Seq, MutableSeq

def gcc(seq: Seq) -> float:
    return (seq.count("G") + seq.count("C")) / len(seq)

seq = Seq("AATGATACGGCGACCACCGAGATCTACACGCCTCCCTCGCGCATCGTGGGTCTCAGGTACCGCCTTACAGTCTTGCGCGACTATAATCCACGGCTCTTATTCTAGCGTGCGCGTACGCATCTAAGCGGTGGACTTCGGGGTTACGCTAC")

adapter = Seq("AATGATACGGCGACCACCGAGATCTACACGCCTCCCTCGCGCATCG")
adapter_id = seq.find(adapter)
# to je adapter najden v sekvenci
new_seq = seq[adapter_id:len(adapter)+1]

print("newseq: ", new_seq)

print(f"""
    a) dolzina odcitka: {len(seq)}
    b) gc delež: {gcc(seq)}
    c) ali je adapter v sekvenci: {adapter in seq}
    d) novi gc delež: {gcc(new_seq)}
""")
