# filter sequence by title name as we need to filter sequence by its gens regions,
# such as ITS, rbcL, matK
## >gi|874509553|gb|KP643924.1| Apiaceae sp. SNP_13_0333 ribulose-1,5-bisphosphate carboxylase/oxygenase large subunit (rbcL) gene, partial cds; chloroplast

import sys
import re
from Bio import SeqIO

def filter_seq_title(records):
  sequences = set()
  for record in records:
    seq_description = record.description

    #if re.search('.internal transcribed spacer.', seq_description):
    if re.search(userParameters[2], seq_description):
      sequences.add(record)
      yield record


# def filter_seq_title(records):
#     sequences = set()
#     for record in records:
#         seq_accession_id = record.description.split("|")[3]
#         seq_taxon_long = record.description.replace(str(record.id), "")
#         seq_taxon = seq_taxon_long.split()
#         seq_title_long = str(seq_taxon[0]+" "+seq_taxon[1]+" "+seq_accession_id)
#         seq_title = seq_title_long.replace(" ", "_").replace(".", "_")

        # record.id =  seq_title
        # record.seq = record.seq
        # record.name = ""
        # record.description = ""

#         sequences.add(record)
#         yield record


userParameters=sys.argv[1:]
records = filter_seq_title(SeqIO.parse(userParameters[0], "fasta"))

count = SeqIO.write(records, userParameters[1], "fasta")
print "Saved %i records" % count

print "filter finished !!!\nPlease check!"

