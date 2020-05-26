#!/bin/sh

###################################################################
#Script Name	: pipeline.sh                                                                                          
#Description	: this script runs the pipeline to predict allele inheritance in hybrids                                                                               
#Args           	: 3 arguments are required                                                                                      
#Author       	: Soukaina Timouma                                             
#Email         	: soukaina.timouma@manchester.ac.uk                                           
###################################################################

if [ "$1" = "" ]; then
    echo "Error: missing arguments"
    echo "./pipeline.sh hybrid parentA parentB"
    exit 1
    break
fi

if [ "$2" = "" ]; then
    echo "Error: missing arguments"
    echo "./pipeline.sh hybrid parentA parentB"
    exit 1
    break
fi

if [ "$3" = "" ]; then
    echo "Error: missing arguments"
    echo "./pipeline.sh hybrid parentA parentB"
    exit 1
    break
fi

echo "Hybrid file: $1"
echo "Parent A file: $2"
echo "Parent B file: $3"


echo "\n--------Creation of BLAST databases--------------"

makeblastdb -in ../Data/$1 -out ../Results/0_BlastDB/hybrid_orf -dbtype nucl
makeblastdb -in ../Data/$2 -out ../Results/0_BlastDB/parentA_orf -dbtype nucl
makeblastdb -in ../Data/$3 -out ../Results/0_BlastDB/parentB_orf -dbtype nucl


echo "\n-----BLASTN------"

mkdir -p ../Results/1_Raw_Blast_output
mkdir -p ../Results/2_Best_hits
mkdir -p ../Results/3_Orthologs_Paralogs
mkdir -p ../Results/4_Parental_alleles_prediction


#Run blastn and parse:
	# Hybrid_X_ParentA(orthologs):
	echo "\n-Hybrid query VS Parent A database-"
	blastn -query ../Data/$1 -db ../Results/0_BlastDB/parentA_orf -out ../Results/1_Raw_Blast_output/output_blastn_hybrid_vs_parentA.txt -num_threads 4 -num_alignments 1 -evalue 0.05
	echo "---------------Parsing BLAST output file---------------"
	perl blast_parser.pl ../Results/1_Raw_Blast_output/output_blastn_hybrid_vs_parentA.txt hybrid parentA ../Results/2_Best_hits #->Hybrid-ParentA.csv
	#rm ../Results/1_Raw_Blast_output/output_blastn_$1_vs_$2.txt

	# ParentA_X_Hybrid(orthologs):
	echo "\n-Parent A query VS Hybrid database-"
	blastn -query ../Data/$2 -db ../Results/0_BlastDB/hybrid_orf -out ../Results/1_Raw_Blast_output/output_blastn_parentA_vs_hybrid.txt -num_threads 4 -num_alignments 1 -evalue 0.05
	echo "---------------Parsing BLAST output file---------------"
	perl blast_parser.pl ../Results/1_Raw_Blast_output/output_blastn_parentA_vs_hybrid.txt parentA hybrid ../Results/2_Best_hits #->ParentA-Hybrid.csv
	#rm ../Results/1_Raw_Blast_output/output_blastn_$2_vs_$1.txt
	

	# Hybrid_X_ParentB(orthologs):
	echo "\n-Hybrid query VS Parent B database-"
	blastn -query ../Data/$1 -db ../Results/0_BlastDB/parentB_orf -out ../Results/1_Raw_Blast_output/output_blastn_hybrid_vs_parentB.txt -num_threads 4 -num_alignments 1 -evalue 0.05
	echo "---------------Parsing BLAST output file"
	perl blast_parser.pl ../Results/1_Raw_Blast_output/output_blastn_hybrid_vs_parentB.txt hybrid parentB ../Results/2_Best_hits #->Hybrid-ParentB.csv
	#rm ../Results/1_Raw_Blast_output/output_blastn_$1_vs_$3.txt

	# ParentB_X_Hybrid(orthologs):
	echo "\n-Parent B query VS Hybrid database-"
	blastn -query ../Data/$3 -db ../Results/0_BlastDB/hybrid_orf -out ../Results/1_Raw_Blast_output/output_blastn_parentB_vs_hybrid.txt -num_threads 4 -num_alignments 1 -evalue 0.05
	echo "---------------Parsing BLAST output file---------------"
	perl blast_parser.pl ../Results/1_Raw_Blast_output/output_blastn_parentB_vs_hybrid.txt parentB hybrid ../Results/2_Best_hits #->ParentB-Hybrid.csv
	#rm ../Results/1_Raw_Blast_output/output_blastn_$3_vs_$1.txt


	# Hybrid_X_Hybrid(paralogs):
	echo "\n-Hybrid query VS Hybrid database-"
	#0_BlastDBcmd -entry all -db ../Results/0_BlastDB/$1 -dbtype nucl -outfmt %g | head -1 | \ tee exclude_me
	#blastn -query ../Data/$1_orf.fasta -db ../Results/0_BlastDB/$1_orf -negative_gilist exclude_me -out ../Results/1_Raw_Blast_output/output_blastn_$1_vs_$1.txt -num_threads 4 -num_alignments 1 -evalue 0.05
	blastn -query ../Data/$1 -db ../Results/0_BlastDB/hybrid_orf -out ../Results/1_Raw_Blast_output/output_blastn_hybrid_vs_hybrid.txt -num_threads 4 -evalue 1e-10 -outfmt "6 qseqid sseqid qlen slen length nident mismatch positive gapopen gaps pident ppos qstart qend sstart send evalue bitscore score"
	#echo "---------------Parsing BLAST output file---------------"
	#perl blast_parser.pl ../Results/1_Raw_Blast_output/output_blastn_$1_vs_$1.txt $1 $1 ../Results/2_Best_hits #->Hybrid-Hybrid.csv
	#rm ../Results/1_Raw_Blast_output/output_blastn_$1_vs_$1.txt


	# ParentA_X_ParentA(paralogs):
	echo "\n-Parent A query VS Parent A database-"
	#0_BlastDBcmd -entry all -db ../Results/0_BlastDB/$2 -dbtype nucl -outfmt %g | head -1 | \ tee exclude_me
	#blastn -query ../Data/$2_orf.fasta -db ../Results/0_BlastDB/$2_orf -negative_gilist exclude_me -out ../Results/1_Raw_Blast_output/output_blastn_$2_vs_$2.txt -num_threads 4 -num_alignments 1 -evalue 0.05
	blastn -query ../Data/$2 -db ../Results/0_BlastDB/parentA_orf -out ../Results/1_Raw_Blast_output/output_blastn_parentA_vs_parentA.txt -num_threads 4 -evalue 1e-10 -outfmt "6 qseqid sseqid qlen slen length nident mismatch positive gapopen gaps pident ppos qstart qend sstart send evalue bitscore score"
	#echo "---------------Parsing BLAST output file---------------"
	#perl blast_parser.pl ../Results/1_Raw_Blast_output/output_blastn_$2_vs_$2.txt $2 $2 ../Results/2_Best_hits #->ParentA-ParentA.csv
	#rm ../Results/1_Raw_Blast_output/output_blastn_$2_vs_$2.txt


	# ParentB_X_ParentB(paralogs):
	echo "\n-Parent B query VS Parent B database-"
	#0_BlastDBcmd -entry all -db ../Results/0_BlastDB/$3 -dbtype nucl -outfmt %g | head -1 | \ tee exclude_me
	#blastn -query ../Data/$3_orf.fasta -db ../Results/0_BlastDB/$3_orf -negative_gilist exclude_me -out ../Results/1_Raw_Blast_output/output_blastn_$3_vs_$3.txt -num_threads 4 -num_alignments 1 -evalue 0.05
	blastn -query ../Data/$3 -db ../Results/0_BlastDB/parentB_orf -out ../Results/1_Raw_Blast_output/output_blastn_parentB_vs_parentB.txt -num_threads 4 -evalue 1e-10  -outfmt "6 qseqid sseqid qlen slen length nident mismatch positive gapopen gaps pident ppos qstart qend sstart send evalue bitscore score"
	#echo "---------------Parsing BLAST output file---------------"
	#perl blast_parser.pl ../Results/1_Raw_Blast_output/output_blastn_$3_vs_$3.txt $3 $3 ../Results/2_Best_hits #->ParentB-ParentB.csv
	#rm ../Results/1_Raw_Blast_output/output_blastn_$3_vs_$3.txt
	
python3 homologs.py

#Search 1:1 orthologies:
echo "\n ---------------Search 1:1 orthologies Hybrid - Parent A ---------------"
python3 orthologs.py --name hybrid_parentA --ortho1 ../Results/2_Best_hits/hybrid-parentA.csv --ortho2 ../Results/2_Best_hits/parentA-hybrid.csv 
echo "\n ---------------Search 1:1 orthologies Hybrid - Parent B ---------------"
python3 orthologs.py --name hybrid_parentB --ortho1 ../Results/2_Best_hits/hybrid-parentB.csv --ortho2 ../Results/2_Best_hits/parentB-hybrid.csv

# Allele prediction
echo "\n ---------------Allele prediction---------------"
python3 prediction.py

	




