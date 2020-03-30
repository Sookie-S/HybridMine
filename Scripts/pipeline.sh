#!/bin/sh

###################################################################
#Script Name	: pipeline.sh                                                                                          
#Description	: this script runs the pipeline to predict allele inheritance in hybrids                                                                               
#Args           	: 3 arguments are required                                                                                      
#Author       	:                                          
#Email         	:                                           
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

echo "Hybrid: $1"
echo "Parent A: $2"
echo "Parent B: $3"


echo "\n--------Creation of BLAST databases--------------"

makeblastdb -in ../Data/$1_orf.fasta -out ../Results/BlastDB/$1_orf -dbtype nucl
makeblastdb -in ../Data/$2_orf.fasta -out ../Results/BlastDB/$2_orf -dbtype nucl
makeblastdb -in ../Data/$3_orf.fasta -out ../Results/BlastDB/$3_orf -dbtype nucl


echo "\n-----BLASTN------"

mkdir -p ../Results/
mkdir -p ../Results/Blast_results
mkdir -p ../Results/Orthologs_and_paralogs
mkdir -p ../Results/Blastn_best_hits
mkdir -p ../Results/Parental_alleles_prediction

#Run blastn and parse:
	# Hybrid_X_ParentA(orthologs):
	echo "\n---------------Hybrid: $1 query VS Parent A: $2 database---------------"
	blastn -query ../Data/$1_orf.fasta -db ../Results/BlastDB/$2_orf -out ../Results/Blast_results/output_blastn_$1_vs_$2.txt -num_threads 4 -num_alignments 1 -evalue 0.05
	echo "---------------Parsing BLAST output file---------------"
	perl blast_parse.pl ../Results/Blast_results/output_blastn_$1_vs_$2.txt $1 $2 ../Results/Blastn_best_hits #->Hybrid-ParentA.csv
	#rm ../Results/Blast_results/output_blastn_$1_vs_$2.txt

	# ParentA_X_Hybrid(orthologs):
	echo "\n---------------Parent A: $2 query VS Hybrid: $1 database---------------"
	blastn -query ../Data/$2_orf.fasta -db ../Results/BlastDB/$1_orf -out ../Results/Blast_results/output_blastn_$2_vs_$1.txt -num_threads 4 -num_alignments 1 -evalue 0.05
	echo "---------------Parsing BLAST output file---------------"
	perl blast_parse.pl ../Results/Blast_results/output_blastn_$2_vs_$1.txt $2 $1 ../Results/Blastn_best_hits #->ParentA-Hybrid.csv
	#rm ../Results/Blast_results/output_blastn_$2_vs_$1.txt
	
	# Hybrid_X_Hybrid(paralogs):
	echo "\n---------------Hybrid: $1 query VS Hybrid: $1 database---------------"
	blastn -query ../Data/$1_orf.fasta -db ../Results/BlastDB/$1_orf -out ../Results/Blast_results/output_blastn_$1_vs_$1.txt -num_threads 4 -num_alignments 1 -evalue 0.05
	echo "---------------Parsing BLAST output file---------------"
	perl blast_parse.pl ../Results/Blast_results/output_blastn_$1_vs_$1.txt $1 $1 ../Results/Blastn_best_hits #->Hybrid-Hybrid.csv
	#rm ../Results/Blast_results/output_blastn_$1_vs_$1.txt

	# ParentA_X_ParentA(paralogs):
	echo "\n---------------Parent A: $2 query VS Parent A: $2 database---------------"
	blastn -query ../Data/$2_orf.fasta -db ../Results/BlastDB/$2_orf -out ../Results/Blast_results/output_blastn_$2_vs_$2.txt -num_threads 4 -num_alignments 1 -evalue 0.05
	echo "---------------Parsing BLAST output file---------------"
	perl blast_parse.pl ../Results/Blast_results/output_blastn_$2_vs_$2.txt $2 $2 ../Results/Blastn_best_hits #->ParentA-ParentA.csv
	#rm ../Results/Blast_results/output_blastn_$2_vs_$2.txt

	# Hybrid_X_ParentB(orthologs):
	echo "\n---------------Hybrid: $1 query VS Parent B: $3 database---------------"
	blastn -query ../Data/$1_orf.fasta -db ../Results/BlastDB/$3_orf -out ../Results/Blast_results/output_blastn_$1_vs_$3.txt -num_threads 4 -num_alignments 1 -evalue 0.05
	echo "---------------Parsing BLAST output file"
	perl blast_parse.pl ../Results/Blast_results/output_blastn_$1_vs_$3.txt $1 $3 ../Results/Blastn_best_hits #->Hybrid-ParentB.csv
	#rm ../Results/Blast_results/output_blastn_$1_vs_$3.txt

	# ParentB_X_Hybrid(orthologs):
	echo "\n---------------Parent B: $3 query VS Hybrid: $1 database---------------"
	blastn -query ../Data/$3_orf.fasta -db ../Results/BlastDB/$1_orf -out ../Results/Blast_results/output_blastn_$3_vs_$1.txt -num_threads 4 -num_alignments 1 -evalue 0.05
	echo "---------------Parsing BLAST output file---------------"
	perl blast_parse.pl ../Results/Blast_results/output_blastn_$3_vs_$1.txt $3 $1 ../Results/Blastn_best_hits #->ParentB-Hybrid.csv
	#rm ../Results/Blast_results/output_blastn_$3_vs_$1.txt

	# ParentB_X_ParentB(paralogs):
	echo "\n---------------Parent B: $3 query VS Parent B: $3 database---------------"
	blastn -query ../Data/$3_orf.fasta -db ../Results/BlastDB/$3_orf -out ../Results/Blast_results/output_blastn_$3_vs_$3.txt -num_threads 4 -num_alignments 1 -evalue 0.05
	echo "---------------Parsing BLAST output file---------------"
	perl blast_parse.pl ../Results/Blast_results/output_blastn_$3_vs_$3.txt $3 $3 ../Results/Blastn_best_hits #->ParentB-ParentB.csv
	#rm ../Results/Blast_results/output_blastn_$3_vs_$3.txt
	
	

#Search 1:1 orthologies:
echo "\n ---------------Search 1:1 orthologies with $2---------------"
python3 orthologs.py --name $1_$2 --ortho1 ../Results/Blastn_best_hits/$1-$2.csv --ortho2 ../Results/Blastn_best_hits/$2-$1.csv --para1 ../Results/Blastn_best_hits/$2-$2.csv --para2 ../Results/Blastn_best_hits/$1-$1.csv
echo "\n ---------------Search 1:1 orthologies with $3---------------"
python3 orthologs.py --name $1_$3 --ortho1 ../Results/Blastn_best_hits/$1-$3.csv --ortho2 ../Results/Blastn_best_hits/$3-$1.csv --para1 ../Results/Blastn_best_hits/$3-$3.csv --para2 ../Results/Blastn_best_hits/$1-$1.csv

# Allele prediction
echo "\n ---------------Allele prediction---------------"
python3 prediction_allele_inheritance.py --hybrid $1 --parentA $2 --parentB $3

echo "\n ---------------Paralogs grouping---------------"
python3 paralogs.py --name $1_$2_$3




