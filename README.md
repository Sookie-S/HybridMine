# HybridMine
Fast and accurate parental allele inheritance prediction tool for hybrid species

DOI: 10.3390/microorganisms8101554 




Pre-requesite:

- Python 3.6
- Perl 

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

1 - In the "Data" Directory, please add the Fasta files containing the genes of the hybrid genome, and it's two (up to four) parental genomes:
- [Hybrid]_orf.fasta
- [ParentA]_orf.fasta
- [ParentB]_orf.fasta
- [ParentC]_orf.fasta (optional)
- [ParentD]_orf.fasta (optional)


For example, in our case we have one hybrid genome and two parental strains:
- Spastorianus_orf.fasta for the Saccharomyces pastorianus hybrid
- Scerevisiae_orf.fasta for the Saccharomyces cerevisiae parental strain
- Seubayanus_orf.fasta for the Saccharomyces eubayanus parental strain


2 - From the script directory, open a terminal and launch the script pipeline.sh in the following way:

if there is two parental genomes:
> bash pipeline.sh [Hybrid] [ParentA] [ParentB]

or if there is three parental genomes:
> bash pipeline.sh [Hybrid] [ParentA] [ParentB] [ParentC]

or if there is four parental genomes:
> bash pipeline.sh [Hybrid] [ParentA] [ParentB] [ParentC] [ParentD]


For example, for the hybrid Saccharomyces pastorianus ("Spastorianus_orf.fasta" file), the parental strains are Saccharomyces eubayanus ("Seubayanus_orf.fasta" file) and Saccharomyces cerevisiae ("Scerevisiae_orf.fasta" file), we type:
> bash pipeline.sh Spastorianus Scerevisiae eubayanus

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



