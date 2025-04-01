from Bio.Seq import Seq
from Bio.Seq import MutableSeq
from Bio.SeqUtils import gc_fraction

def main():
    t = Seq("ACGTCATCA")
    gc = gc_fraction(t)
    # dela!!!
    print("len: ", len(t), "gc: ", round(gc, 2))
    print("Hello from uvb!")


if __name__ == "__main__":
    main()
