# extract seqid(title) to check population sample consistent between different DNS sequence matrx, such as ITS, MatK, rbck, ETS, 
# filnal result should as: Acronema_Kham10_699, Acronema_astrantiifolium_zzs292, Arcuatopterus_thalictroideus_EU236160_1
# for example, Acronema_Kham10_699 is a seqid(title) extract from ITS sequence matrix
#  Does this population sample is also in MatK, rbcl, ETS or Tran sequence matrix

import sys
from Bio import SeqIO

userParameters=sys.argv[1:]

f = open(userParameters[1], "w")
f.write("TitleList"+"\n")

for seq in SeqIO.parse(userParameters[0], "fasta"):
	title = seq.id
	f.write(str(title)+"\n")
f.close()

print "Extract title list!!! Chekck file => " +userParameters[1]