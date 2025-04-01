from Bio.SeqIO import parse
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

import os

fpath = "V5-datoteke/protein.faa"

file = open(fpath, "r")
records = parse(file, "fasta")

for r in records:
    print("id: %s" % r.id)
