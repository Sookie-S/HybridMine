
1- Genomic Source: Okuno et al., 2016

The assembled genome sequences of Saccharomyces pastorianus strains CBS1503, CBS1513, CBS1538 and WS34/70 have been downloaded from: https://www.ncbi.nlm.nih.gov/bioproject/PRJDB4073/

Files: 
- CBS1503.fasta
- CBS1513.fasta
- CBS1538.fasta
- WS34_70.fasta

2- We structurally annotated the four S. pastorianus strains using the Yeast Genome Annotation Pipeline (Proux-Wéra et al., 2012)

3- We extracted using a Python 3.6 script we developed all the ORFs sequences, and we stored them in new FASTA files
Files: 
- CBS1503_orf.fasta
- CBS1513_orf.fasta
- CBS1538_orf.fasta
- WS3470_orf.fasta

4- We applied HybridMine pipeline to the four strains
Files:
- Saccharomyces_pastorianus_CBS1503_orthologs_paralogs_inference.xlsx
- Saccharomyces_pastorianus_CBS1513_orthologs_paralogs_inference.xlsx
- Saccharomyces_pastorianus_CBS1538_orthologs_paralogs_inference.xlsx
- Saccharomyces_pastorianus_WS3470_orthologs_paralogs_inference.xlsx

5- We generated annotation files in GFF3 format. The fake gene IDs have been replaced by the parental allele name for all the genes identified as inherited from a parent. The files have been zipped due to their size.
Files:
- annotation_Saccharomyces_pastorianus_CBS1503.zip
- annotation_Saccharomyces_pastorianus_CBS1513.zip
- annotation_Saccharomyces_pastorianus_CBS1538.zip
- annotation_Saccharomyces_pastorianus_WS3470.zip
