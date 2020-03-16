# HybridMiner
Fast and accurate parental allele inheritance prediction tool for hybrid species

Author: Soukaina Timouma
Institution: Manchester Institute of Biotechnology, University of Manchester
Corresponding mail: soukaina.timouma@manchester.ac.uk


- Install BLASTP 2.6.0+ program on your machine.
ubuntu machine:
>sudo apt-get install ncbi-blast+
          
In Current Directory, create:
- Script directory
- Data directory

In the "Script" Directory, make sure there is the following scripts:
- pipeline.sh (the main execution file)
- blast_parse.pl
- orthologs.py
- paralogs.py
- prediction_allele_inheritance

In the "Data" Directory:
- [Hybrid]_orf.fasta
- [ParentA]_orf.fasta
- [ParentB]_orf.fasta
Replace [Hybrid], [ParentA] and [ParentB] by the name of the organisms of interest.

For example:
- Spastorianus_orf.fasta for the Saccharomyces pastorianus hybrid
- Scerevisiae_orf.fasta for the Saccharomyces cerevisiae parental strain
- Seubayanus_orf.fasta for the Saccharomyces eubayanus parental strain


#####################################

          Instructions
          
#####################################
--- From the script directory, launch the script pipeline.sh in the following way:
> bash pipeline.sh [Hybrid name] [ParentA name] [ParentB name]

For example, in our example, it would be:
> bash pipeline.sh Spastorianus Scerevisiae Seubayanus

The script will go automatically on the Data folder to pick the corresponding ORFs fasta files.





