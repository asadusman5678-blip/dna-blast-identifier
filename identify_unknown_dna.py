"""
identify_unknown_dna.py

Takes an unknown DNA sequence from a FASTA file (given as a command line
argument) and identifies its likely species/origin by searching it against
NCBI's nucleotide database using BLAST (via Biopython).

Usage:
    python identify_unknown_dna.py <fasta_file>
"""

import sys
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML


def read_sequence_from_fasta(filename):
    """Reads a single DNA sequence from a FASTA file and returns it as one string."""
    try:
        f = open(filename)
    except FileNotFoundError:
        print(f"File {filename} does not exist!!")
        sys.exit(1)

    sequence = ""
    for line in f:
        line = line.rstrip()
        if line.startswith(">"):
            continue  # skip header line(s)
        sequence += line

    f.close()
    return sequence


# ----- Get the filename from the command line -----
if len(sys.argv) < 2:
    print("Usage: python identify_unknown_dna.py <fasta_file>")
    sys.exit(1)

filename = sys.argv[1]
sequence = read_sequence_from_fasta(filename)

print(f"Loaded sequence ({len(sequence)} bases) from {filename}")
print("Submitting BLAST query to NCBI... (This might take a minute or two)")

# qblast parameters: program="blastn", database="nt", sequence
try:
    result_handle = NCBIWWW.qblast("blastn", "nt", sequence)
except Exception as e:
    print(f"BLAST query failed: {e}")
    sys.exit(1)

print("BLAST query finished. Parsing results...")

# Parse the XML results
blast_records = NCBIXML.parse(result_handle)
blast_record = next(blast_records)

# Extract and display the top hit
if blast_record.alignments:
    top_alignment = blast_record.alignments[0]
    print(f"\nTop Match Found:")
    print(f"Species/Definition: {top_alignment.title}")
    print(f"Accession: {top_alignment.accession}")
    print(f"E-value of top hit: {top_alignment.hsps[0].expect}")
else:
    print("No matching species found.")

# Always close the handle
result_handle.close()
