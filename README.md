# HybridMine
Fast and accurate parental allele inheritance prediction tool for hybrid species

Pre- requesite:

- Install BLAST 2.6.0+ program on your machine.
ubuntu machine:
>sudo apt-get install ncbi-blast+


#####################################

          Instructions
          
#####################################

In the "Script" Directory, there is:
- pipeline.sh (the main execution file)
- blast_parser.pl
- orthologs.py
- homologs.py
- prediction.py

1 - In the "Data" Directory, please add the Fasta files containing the genes of the hybrid genome, parent A and parentB:
- [Hybrid].fasta
- [ParentA].fasta
- [ParentB].fasta

For example:
- Spastorianus_orf.fasta for the Saccharomyces pastorianus hybrid
- Scerevisiae_orf.fasta for the Saccharomyces cerevisiae parental strain
- Seubayanus_orf.fasta for the Saccharomyces eubayanus parental strain


2 - From the script directory, open a terminal and launch the script pipeline.sh in the following way:
> bash pipeline.sh [Hybrid.fasta] [ParentA.fasta] [ParentB.fasta]

For example, for the hybrid Saccharomyces pastorianus ("Spastorianus_orf.fasta" file), the parental strains are Saccharomyces eubayanus ("Seubayanus_orf.fasta" file) and Saccharomyces cerevisiae ("Scerevisiae_orf.fasta" file):
> bash pipeline.sh Spastorianus_orf.fasta Scerevisiae_orf.fasta eubayanus_orf.fasta

The script will go automatically on the Data folder to pick the corresponding ORFs fasta files.


A full example of application is given in the directory "Application_example". The output files are also shown.
See https://github.com/Sookie-S/HybridMine/tree/master/Application_example/





#####################################

          THE END
          
#####################################


On the meantine HybridMine is running... quick story:

A Wife Sends Her Software Engineer Husband to the Store 

"Could you please go shopping for me and buy one carton of milk. And if they have eggs, get six!"

Later, the husband comes back with six cartons of milk. The wife asks him why he bought six cartons of milk and he replied, "They had eggs."



