# detect unusual character such as: N, W, Y, R from DNA sequence matrix file
# need todo remove these characters and build a new sequence matrix

import sys
from Bio import SeqIO

userParameters=sys.argv[1:]
f = open(userParameters[1], "w")
f.write("Sequence Title/id"+"\n")

for record in SeqIO.parse(userParameters[0], "fasta"):
    sequence = str(record.seq)

    if 'M' in sequence:
        f.write(str(record.id)+"\n")
    if 'n' in sequence:
    	f.write(str(record.id)+"\n")
    if 'N' in sequence:
    	f.write(str(record.id)+"\n")
    if 'n' in sequence:
    	f.write(str(record.id)+"\n")
    if 'S' in sequence:
    	f.write(str(record.id)+"\n")
    if 's' in sequence:
    	f.write(str(record.id)+"\n")
    if 'Y' in sequence:
    	f.write(str(record.id)+"\n")
    if 'y' in sequence:
    	f.write(str(record.id)+"\n")

f.close()
print "Sequence bear with unusual character, please!!! Chekck file => " +userParameters[1]