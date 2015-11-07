# statistics for DNA sequence matrix, get idea how many genus, species have been sampled
# in the sequence matrix.
# output results should be as following:
#
# Need three user input file, 1. DNA sequence filename, 2. produced taxon list filename;
# 3. produced statistics filename

import sys
from Bio import SeqIO

userParameters=sys.argv[1:]

f = open(userParameters[1], "w")
#f.write("TaxonList"+"\n")

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

fa = open(userParameters[2], "w")
num_lines = open(userParameters[1]).read().count('\n')
sample_total = num_lines - 1

taxon_name = []
genus_name = []
for line in open(userParameters[1]):
  taxon_name.append(line)
  taxon_name_str = str(line).split(" ")
  genus_name.append(taxon_name_str[0])

fa.write("################################################################################################################################################################################"+"\n")
fa.write("Your DNA sequence matrix include "+ str(len(set(genus_name))) + " genera, and " + str(len(set(taxon_name))) + " species, there are total " + str(sample_total) + " samples" + "\n")
fa.write("################################################################################################################################################################################"+"\n"+"\n")

fa.write("####################################################################"+"\n")
fa.write("Population sample number for each taxon ordered by taxon name"+"\n")
fa.write("####################################################################"+"\n")
#taxon_name = taxon_name.remove("TaxonList"+"\n")

from collections import Counter
population_sample_number = Counter(taxon_name)
for x in sorted(population_sample_number.items()):
  #print x[0], x[1]
  fa.write(x[0].rstrip() + " "+ str(x[1])+"\n")

fa.write("####################################################################"+"\n")
fa.write("Population sample number for each taxon ordered sample number"+"\n")
fa.write("####################################################################"+"\n")
#taxon_name = taxon_name.remove("TaxonList"+"\n")

from collections import Counter
population_sample_number = Counter(taxon_name).most_common()
for x in population_sample_number:
  #print x[0], x[1]
  fa.write(x[0].rstrip() + " "+ str(x[1])+"\n")

fa.write("####################################################################"+"\n")
fa.write("Population sample number for each genus ordered by genus name"+"\n")
fa.write("####################################################################"+"\n")

species_sample_number = Counter(genus_name)
for y in sorted(species_sample_number.items()):
  #print y[0], y[1]
  fa.write(y[0] + " "+ str(y[1])+"\n")

fa.write("###################################################################################################"+"\n")
fa.write("Species and population [species, population] sample number under each genus ordered by genus name"+"\n")
fa.write("###################################################################################################"+"\n")


taxon_sample_list = dict(Counter(taxon_name))
taxon_name_list = sorted(taxon_sample_list.keys())

genus_name_a=[]
for x in taxon_name_list:
  taxon_name_a = str(x).split(" ")
  genus_name_a.append(str(taxon_name_a[0]))

from collections import defaultdict

counter = dict(sorted(Counter(genus_name_a).items()))
# for x in counter:
#   fa.write(x[0].rstrip() + " "+ str(x[1])+"\n")


species_sample_number = dict(sorted(Counter(genus_name).items()))
# for y in sorted(species_sample_number.items()):
#   for x in counter:
#   fa.write(x[0].rstrip() + " "+ str(x[1])+"\n")
#   fa.write(y[0] + " "+ str(y[1])+"\n")
dd = defaultdict(list)
for d in (counter, species_sample_number):
  for key, value in d.iteritems():
      dd[key].append(value)

# print sorted(dd.items())

for x in sorted(dd.items()):
  fa.write(x[0].rstrip() + " "+ str(x[1])+"\n")

fa.close()

print "=> &&& Your DNA sequence data matrix statistcs finished, please check your file => "+userParameters[2]
# print genus_name
# print taxon_name
# print species_sample_number
# print population_sample_number


