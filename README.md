# DNA Sequence Identifier (BLAST via Biopython)

A Python script that identifies an unknown DNA sequence by searching it against NCBI's nucleotide database using BLAST, and reports the closest known match.

## What it does
- Takes an unknown DNA sequence as input
- Submits it to NCBI's BLAST server using Biopython's `NCBIWWW.qblast()`
- Parses the returned results (XML format) using `NCBIXML`
- Reports the top matching species/sequence, its accession number, and the E-value (a statistical measure of how significant the match is)

## Setup
Install the required dependency:
```
pip install -r requirements.txt
```


## How to run
```
python identify_unknown_dna.py sample_unknown.fa
```
A sample test file (`sample_unknown.fa`) is included in this repo so you can try it immediately.

Note: this script makes a live call to NCBI's servers, so it typically takes 30 seconds to a few minutes depending on server load.

## Example output
```
Top Match Found:
Species/Definition: Drosophila melanogaster ...
Accession: XXXXXXX
E-value of top hit: 2.3e-95
```

## Understanding the E-value
The E-value estimates how likely it is that a match this good could occur purely by chance. Smaller E-values (e.g. 1e-50 or lower) indicate highly significant, trustworthy matches. Larger E-values (close to 1 or higher) suggest the match may just be random noise.

## Notes
This script implements a sequence identification workflow using Biopython's interface to NCBI's BLAST API — the underlying BLAST algorithm and database are provided by NCBI; this project focuses on understanding and applying that interface correctly, not on building the search algorithm itself.

## Built with
Python 3, Biopython — Genomic Data Science coursework, BS Bioinformatics, NUST
