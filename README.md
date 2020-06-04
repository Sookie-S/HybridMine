# HybridMine
Fast and accurate parental allele inheritance prediction tool for hybrid species

- Install BLASTP 2.6.0+ program on your machine.
ubuntu machine:
>sudo apt-get install ncbi-blast+
          
In Current Directory, create:
- Script directory
- Data directory

In the "Script" Directory, make sure there is the following scripts:
- pipeline.sh (the main execution file)
- blast_parser.pl
- orthologs.py
- homologs.py
- prediction.py

In the "Data" Directory:
- [Hybrid].fasta
- [ParentA].fasta
- [ParentB].fasta

For example:
- Spastorianus_orf.fasta for the Saccharomyces pastorianus hybrid
- Scerevisiae_orf.fasta for the Saccharomyces cerevisiae parental strain
- Seubayanus_orf.fasta for the Saccharomyces eubayanus parental strain


#####################################

          Instructions
          
#####################################


--- From the script directory, launch the script pipeline.sh in the following way:
> bash pipeline.sh [Hybrid name] [ParentA name] [ParentB name]

For example, for the hybrid Saccharomyces pastorianus ("Spastorianus_orf.fasta" file), the parental strains are Saccharomyces eubayanus ("Seubayanus_orf.fasta" file) and Saccharomyces cerevisiae ("Scerevisiae_orf.fasta" file):
> bash pipeline.sh Spastorianus Scerevisiae Seubayanus

The script will go automatically on the Data folder to pick the corresponding ORFs fasta files.



######## THE END #########
On the meantine HybridMine is running... quick story:

A Wife Sends Her Software Engineer Husband to the Store 

"Could you please go shopping for me and buy one carton of milk. And if they have eggs, get six!"

Later, the husband comes back with six cartons of milk. The wife asks him why he bought six cartons of milk and he replied, "They had eggs."



