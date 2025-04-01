from Bio.SeqIO import parse
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

import os
import sys

fpath = "V5-datoteke/proteome.gbk"


i = 0
for record in SeqIO.parse(fpath, "genbank"):
    print(record.id)
    i += 1
    if i is 10:
        break

ids = [record.id for record in SeqIO.parse(fpath, "genbank")]

rcr = list(SeqIO.parse(fpath, "genbank"))
fst_30_rc = rcr[1:60:2]

SeqIO.write(fst_30_rc, "V5-datoteke/first-30-records.fasta", "fasta")