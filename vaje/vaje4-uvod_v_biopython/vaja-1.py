exon = (11065, 11154)
snp = 11111

print("ali je snp 11111 v eksonu? ", end="")
if snp in range(exon[0], exon[1]):
    print("ja - vpliva")
else:
    print("ne - ne vpliva")

snp2 = 11288

print("ali je snp 11288 v eksonu? ", end="")
if snp2 in range(exon[0], exon[1]):
    print("ja - vpliva")
else:
    print("ne - ne vpliva")
