# tidy up sequence long til
## gi|817992084|gb|KM360852.1|:26-1318 Ligusticum scoticum ribulose-1,5-bisphosphate carboxylase/oxygenase large subunit (rbcL) gene, partial cds; plastid
# as short title
## Ligusticum_scoticum_KM360852_1

import sys
from Bio import SeqIO

def tidy_seq_title(records):
    sequences = set()
    for record in records:
        seq_accession_id = record.description.split("|")[3]
        seq_taxon_long = record.description.replace(str(record.id), "")
        seq_taxon = seq_taxon_long.split()
        seq_title_long = str(seq_taxon[0]+" "+seq_taxon[1]+" "+seq_accession_id)
        seq_title = seq_title_long.replace(" ", "_").replace(".", "_")

        record.id =  seq_title
        record.seq = record.seq
        record.name = ""
        record.description = ""

        sequences.add(record)
        yield record


userParameters=sys.argv[1:]
records = tidy_seq_title(SeqIO.parse(userParameters[0], "fasta"))

count = SeqIO.write(records, userParameters[1], "fasta")
print "Saved %i records" % count

print "Tidy title!!!\nPlease check!"

