# extract taxon list from title in seq matrix,
# as Acronema_Kham10_699, Acronema_astrantiifolium_zzs292, Arcuatopterus_thalictroideus_EU236160_1
# to just taxon name for investigation what genus and species has ben smapled in the sequence matrix

import sys
from Bio import SeqIO

userParameters=sys.argv[1:]

f = open(userParameters[1], "w")
f.write("TaxonList"+"\n")

for seq in SeqIO.parse(userParameters[0], "fasta"):
	taxon = str(seq.id).split("_")
	# print len(taxon)
	if len(taxon) > 1:
		taxon_list = taxon[0]+" "+taxon[1]
		# print taxon[0]+" "+taxon[1]
	else:
		taxon_list = taxon[0]
		# print taxon[0]
	f.write(str(taxon_list)+"\n")
f.close()

print "Extract taxon list!!! Chekck file => " + userParameters[1]
