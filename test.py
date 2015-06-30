from Bio import SeqIO
# sizes = [len(rec) for rec in SeqIO.parse("umbel_all.fasta", "fasta")]

# f = open("seq_length.txt", "w")
# f.write("Length"+"\n")
# for seq in SeqIO.parse("umbel_all.fasta", "fasta"):
# 	f.write(str(len(seq))+"\n")
# f.close()


# import pylab
# pylab.hist(sizes, bins=20)
# pylab.title("%i Umbel blast sequences\nLengths %i to %i" \
#             % (len(sizes),min(sizes),max(sizes)))
# pylab.xlabel("Sequence length (bp)")
# pylab.ylabel("Count")
# pylab.show()

f = open("seq_great_4000_length.txt", "w")
for seq in SeqIO.parse("umbel.fasta", "fasta"):
	if len(seq) >= 4000:
		f.write(str(seq)+"\n")