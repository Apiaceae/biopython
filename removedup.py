# remove duplicate sequence from fasta file according to actual sequence content
# rather than title
from Bio import SeqIO
from Bio.SeqUtils.CheckSum import seguid

def remove_dup_seqs(records):
    """"SeqRecord iterator to removing duplicate sequences."""
    checksums = set()
    for record in records:
        checksum = seguid(record.seq)
        if checksum in checksums:
            print "Ignoring %s" % record.id
            continue
        checksums.add(checksum)
        yield record

records = remove_dup_seqs(SeqIO.parse("demo.fasta", "fasta"))
count = SeqIO.write(records, "demo_no_dups.fasta", "fasta")
print "Saved %i records" % count

