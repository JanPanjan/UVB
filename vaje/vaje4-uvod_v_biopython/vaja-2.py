from Bio.Seq import Seq

forward_probe = Seq("CATTACGGTTGCTTCACTTGGGTCGACTAGCCAGACATTC")
reverse_probe = Seq("GTCAGATTGCGCCCATCGACAACTGCAATCAAACTAAGTCG")

print("""
Transverzija (G/A) je vrsta mutacije, kjer pride do zamenjave purina (G) s pirimidinom
(A). Je ena od vrst točkovnih mutacij

IUPAC 'R' koda se uporablja za predstavitev purina na določenem mestu v zaporedju
nukleotidov. Na tem mestu je torej lahko prisoten v našem primeru G ali A.
""")

print(
    f"""
    a) dolzina 3' obmocja: {len(forward_probe)}, dolzina 5' obmocja: {len(reverse_probe)}
    b)
    """
)
