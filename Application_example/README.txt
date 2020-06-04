HybridMine package is composed by two folders, “Script” and “Data”, which needs to stay co-located in the same directory when downloaded. The user places in the "Data" directory the 3 fasta format files, containing the ORFs of the hybrid to annotate, the ORFs of the parent A and the ORFs of the parent B. Subsequently, the user launches the main execution file (pipeline.sh) from the “Script” directory, specifying as input the FASTA files containing the genes sequence of the hybrid to annotate and its two parental organism (i.e. command line: bash pipeline.sh [Hybrid.fasta] [ParentA.fasta] [ParentB.fasta]

An example of HybridMine usage is presented below.

We annotated Saccharomyces pastorianus WS 34/70 strain, which is an allopolyploid sterile yeast hybrid used in brewing to produce lager-style beers.

1- We downloaded from NCBI the assembled genome sequence of Saccharomyces pastorianus WS 34/70 strain [https://www.ncbi.nlm.nih.gov/bioproject/PRJDB4073/] (Okuno et al., 2016). The Yeast Genome Annotation Pipeline (Proux-Wéra et al., 2012) has been used to predict the position of potential open reading frames (ORFs) and tRNAs in this yeast hybrid genome.

S. cerevisiae S288C genome has been used as a reference to annotate the S. cerevisiae-like genome content in this S. pastorianus strain. The last released S. cerevisiae genome has been downloaded from the Saccharomyces Genome Database (SGD). S. eubayanus FM1318 strain has been used as a reference to annotate the S. eubayanus-like genome content in S. pastorianus. Its genome assembly and annotation provided by the Tokyo Institute of Technology have been taken from NCBI database.


2- We put in the "Data" directory 3 fasta format files, containing the ORFs of the hybrid to annotate (here S. pastorianus WS 34/70), the ORFs of the parent A (here S. cerevisiae S288C) and the ORFs of the parent B (here S. eubayanus FM1318).

Our "Data" folder contains:
- WS3470_orf.fasta
- Scerevisiae_orf.fasta
- Seubayanus_FM1318_orf.fasta

3- From the "Script" directory, we opened a Unix terminal, and we launched HybridMine pipeline by running the following command:
>pipeline.sh WS3470_orf.fasta Scerevisiae_orf.fasta Seubayanus_FM1318_orf.fasta

5- As output, HybridMine created a "Results" folder.
In that folder, HybridMine created 5 sub-folders organizing the outputs:
- "0_BlastDB" folder: contains the BLAST databases created
- "1_Raw_Blast_output" folder: contains raw BLAST outputs of the alignments done by HybridMine
- "2_Best_hits" folder: contains the files resuming the Best hits for each alignments done
- "3_Orthologs_Paralogs" folder: contains the 1:1 orthologs identified and the groups of homologs found in the hybrid genome
- "4_Parental_alleles_prediction" folder: contains the parental alleles prediction

##### THE END ########
While your job is running:

Why Can't You Trust Atoms? 

...
...

They make up everything.

