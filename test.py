from Bio import SeqIO
sizes = [len(rec) for rec in SeqIO.parse("dd.fasta", "fasta")]

import pylab
pylab.hist(sizes, bins=20)
pylab.title("%i Umbel blast sequences\nLengths %i to %i" \
            % (len(sizes),min(sizes),max(sizes)))
pylab.xlabel("Sequence length (bp)")
pylab.ylabel("Count")
pylab.show()