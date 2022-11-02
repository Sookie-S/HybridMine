#!/bin/sh

###################################################################
#Script Name	: pipeline.sh                                                                                          
#Description	: this script runs the pipeline to predict allele inheritance in hybrids                                                                               
#Args           	: 3 arguments are required                                                                                      
#Author       	: Soukaina Timouma                                             
#Email         	: soukaina.timouma@manchester.ac.uk                                           
###################################################################

two=false
three=false
four=false

if [ "$1" = "" ]; then
    echo "Error: missing arguments"
    echo "./pipeline.sh $1 $2 parentB"
    exit 1
    break
fi

if [ "$2" = "" ]; then
    echo "Error: missing arguments"
    echo "./pipeline.sh $1 $2 parentB"
    exit 1
    break
fi

if [ "$3" = "" ]; then
    echo "Error: missing arguments"
    echo "./pipeline.sh $1 $2 parentB"
    exit 1
    break
fi


if [ "$4" = "" ]; then
    echo "This hybrid has 2 parents"
    two=true
fi


if [ "$4" != "" ] && [ "$5" = "" ]; then
    echo "This hybrid has 3 parents"
    three=true
fi


if [ "$4" != "" ] && [ "$5" != "" ] && [ "$6" = "" ]; then
    echo "This hybrid has 4 parents"
    four=true
fi


########################### 2 Parental organisms

if [ "$two" = true ]; then

	echo "Hybrid file: $1"
	echo "Parent A file: $2"
	echo "Parent B file: $3"


	echo "\n--------Creation of BLAST databases--------------"

	makeblastdb -in ../Data/$1_orf.fasta -out ../Results/0_BlastDB/$1_orf -dbtype nucl
	makeblastdb -in ../Data/$2_orf.fasta -out ../Results/0_BlastDB/$2_orf -dbtype nucl
	makeblastdb -in ../Data/$3_orf.fasta -out ../Results/0_BlastDB/$3_orf -dbtype nucl


	echo "\n-----BLASTN------"

	mkdir -p ../Results/1_Raw_Blast_output
	mkdir -p ../Results/2_Best_hits
	mkdir -p ../Results/3_Orthologs_Paralogs
	mkdir -p ../Results/4_Parental_alleles_prediction


	#Run blastn and parse:
		# Hybrid_X_ParentA(orthologs):
		echo "\n-$1 query VS $2 database-"
		blastn -query ../Data/$1_orf.fasta -db ../Results/0_BlastDB/$2_orf -out ../Results/1_Raw_Blast_output/output_blastn_$1_vs_$2.txt -num_threads 4 -num_alignments 1 -evalue 0.05
		echo "---------------Parsing BLAST output file---------------"
		perl blast_parser.pl ../Results/1_Raw_Blast_output/output_blastn_$1_vs_$2.txt $1 $2 ../Results/2_Best_hits #->$1-$2.csv

		# ParentA_X_Hybrid(orthologs):
		echo "\n-$2 query VS $1 database-"
		blastn -query ../Data/$2_orf.fasta -db ../Results/0_BlastDB/$1_orf -out ../Results/1_Raw_Blast_output/output_blastn_$2_vs_$1.txt -num_threads 4 -num_alignments 1 -evalue 0.05
		echo "---------------Parsing BLAST output file---------------"
		perl blast_parser.pl ../Results/1_Raw_Blast_output/output_blastn_$2_vs_$1.txt $2 $1 ../Results/2_Best_hits #->$2-$1.csv
		

		# Hybrid_X_ParentB(orthologs):
		echo "\n-$1 query VS $3 database-"
		blastn -query ../Data/$1_orf.fasta -db ../Results/0_BlastDB/$3_orf -out ../Results/1_Raw_Blast_output/output_blastn_$1_vs_$3.txt -num_threads 4 -num_alignments 1 -evalue 0.05
		echo "---------------Parsing BLAST output file"
		perl blast_parser.pl ../Results/1_Raw_Blast_output/output_blastn_$1_vs_$3.txt $1 $3 ../Results/2_Best_hits #->$1-$3.csv

		# ParentB_X_Hybrid(orthologs):
		echo "\n-$3 query VS $1 database-"
		blastn -query ../Data/$3_orf.fasta -db ../Results/0_BlastDB/$1_orf -out ../Results/1_Raw_Blast_output/output_blastn_$3_vs_$1.txt -num_threads 4 -num_alignments 1 -evalue 0.05
		echo "---------------Parsing BLAST output file---------------"
		perl blast_parser.pl ../Results/1_Raw_Blast_output/output_blastn_$3_vs_$1.txt $3 $1 ../Results/2_Best_hits #->$3-$1.csv


		# Hybrid_X_Hybrid(paralogs):
		echo "\n-$1 query VS $1 database-"
		blastn -query ../Data/$1_orf.fasta -db ../Results/0_BlastDB/$1_orf -out ../Results/1_Raw_Blast_output/output_blastn_$1_vs_$1.txt -num_threads 4 -evalue 1e-10 -outfmt "6 qseqid sseqid qlen slen length nident mismatch positive gapopen gaps pident ppos qstart qend sstart send evalue bitscore score"


		# ParentA_X_ParentA(paralogs):
		echo "\n-$2 query VS $2 database-"
		blastn -query ../Data/$2_orf.fasta -db ../Results/0_BlastDB/$2_orf -out ../Results/1_Raw_Blast_output/output_blastn_$2_vs_$2.txt -num_threads 4 -evalue 1e-10 -outfmt "6 qseqid sseqid qlen slen length nident mismatch positive gapopen gaps pident ppos qstart qend sstart send evalue bitscore score"


		# ParentB_X_ParentB(paralogs):
		echo "\n-$3 query VS $3 database-"
		blastn -query ../Data/$3_orf.fasta -db ../Results/0_BlastDB/$3_orf -out ../Results/1_Raw_Blast_output/output_blastn_$3_vs_$3.txt -num_threads 4 -evalue 1e-10  -outfmt "6 qseqid sseqid qlen slen length nident mismatch positive gapopen gaps pident ppos qstart qend sstart send evalue bitscore score"
		
	python3 homologs.py  --nb 2

	#Search 1:1 orthologies:
	echo "\n ---------------Search 1:1 orthologies Hybrid - Parent A ---------------"
	python3 orthologs.py --name $1_$2 --ortho1 ../Results/2_Best_hits/$1-$2.csv --ortho2 ../Results/2_Best_hits/$2-$1.csv 
	echo "\n ---------------Search 1:1 orthologies Hybrid - Parent B ---------------"
	python3 orthologs.py --name $1_$3 --ortho1 ../Results/2_Best_hits/$1-$3.csv --ortho2 ../Results/2_Best_hits/$3-$1.csv


	tothyb=$(grep ">" ../Data/$1_orf.fasta | wc -l)
	totparA=$(grep ">" ../Data/$2_orf.fasta | wc -l)
	totparB=$(grep ">" ../Data/$3_orf.fasta | wc -l)

	#echo "$tothyb"
	#echo "$totparA"
	#echo "$totparB"


	# Allele prediction
	echo "\n ---------------Allele prediction---------------"
	python3 prediction.py  --nb 2 --fH $1 --fA $2 --fB $3 --hyb $tothyb --pA $totparA --pB $totparB

	

fi


########################### 3 Parental organisms



if [ "$three" = true ]; then

	echo "Hybrid file: $1"
	echo "Parent A file: $2"
	echo "Parent B file: $3"
	echo "Parent C file: $4"

	echo "\n--------Creation of BLAST databases--------------"

	makeblastdb -in ../Data/$1_orf.fasta -out ../Results/0_BlastDB/$1_orf -dbtype nucl
	makeblastdb -in ../Data/$2_orf.fasta -out ../Results/0_BlastDB/$2_orf -dbtype nucl
	makeblastdb -in ../Data/$3_orf.fasta -out ../Results/0_BlastDB/$3_orf -dbtype nucl
	makeblastdb -in ../Data/$4_orf.fasta -out ../Results/0_BlastDB/$4_orf -dbtype nucl


	echo "\n-----BLASTN------"

	mkdir -p ../Results/1_Raw_Blast_output
	mkdir -p ../Results/2_Best_hits
	mkdir -p ../Results/3_Orthologs_Paralogs
	mkdir -p ../Results/4_Parental_alleles_prediction


	#Run blastn and parse:
		# Hybrid_X_ParentA(orthologs):
		echo "\n-$1 query VS $2 database-"
		blastn -query ../Data/$1_orf.fasta -db ../Results/0_BlastDB/$2_orf -out ../Results/1_Raw_Blast_output/output_blastn_$1_vs_$2.txt -num_threads 4 -num_alignments 1 -evalue 0.05
		echo "---------------Parsing BLAST output file---------------"
		perl blast_parser.pl ../Results/1_Raw_Blast_output/output_blastn_$1_vs_$2.txt $1 $2 ../Results/2_Best_hits #->$1-$2.csv

		# ParentA_X_Hybrid(orthologs):
		echo "\n-$2 query VS $1 database-"
		blastn -query ../Data/$2_orf.fasta -db ../Results/0_BlastDB/$1_orf -out ../Results/1_Raw_Blast_output/output_blastn_$2_vs_$1.txt -num_threads 4 -num_alignments 1 -evalue 0.05
		echo "---------------Parsing BLAST output file---------------"
		perl blast_parser.pl ../Results/1_Raw_Blast_output/output_blastn_$2_vs_$1.txt $2 $1 ../Results/2_Best_hits #->$2-$1.csv
		

		# Hybrid_X_ParentB(orthologs):
		echo "\n-$1 query VS $3 database-"
		blastn -query ../Data/$1_orf.fasta -db ../Results/0_BlastDB/$3_orf -out ../Results/1_Raw_Blast_output/output_blastn_$1_vs_$3.txt -num_threads 4 -num_alignments 1 -evalue 0.05
		echo "---------------Parsing BLAST output file"
		perl blast_parser.pl ../Results/1_Raw_Blast_output/output_blastn_$1_vs_$3.txt $1 $3 ../Results/2_Best_hits #->$1-$3.csv

		# ParentB_X_Hybrid(orthologs):
		echo "\n-$3 query VS $1 database-"
		blastn -query ../Data/$3_orf.fasta -db ../Results/0_BlastDB/$1_orf -out ../Results/1_Raw_Blast_output/output_blastn_$3_vs_$1.txt -num_threads 4 -num_alignments 1 -evalue 0.05
		echo "---------------Parsing BLAST output file---------------"
		perl blast_parser.pl ../Results/1_Raw_Blast_output/output_blastn_$3_vs_$1.txt $3 $1 ../Results/2_Best_hits #->$3-$1.csv

		# Hybrid_X_ParentC(orthologs):
		echo "\n-$1 query VS $4 database-"
		blastn -query ../Data/$1_orf.fasta -db ../Results/0_BlastDB/$4_orf -out ../Results/1_Raw_Blast_output/output_blastn_$1_vs_$4.txt -num_threads 4 -num_alignments 1 -evalue 0.05
		echo "---------------Parsing BLAST output file"
		perl blast_parser.pl ../Results/1_Raw_Blast_output/output_blastn_$1_vs_$4.txt $1 $4 ../Results/2_Best_hits #->$1-$3.csv

		# ParentC_X_Hybrid(orthologs):
		echo "\n-$4 query VS $1 database-"
		blastn -query ../Data/$4_orf.fasta -db ../Results/0_BlastDB/$1_orf -out ../Results/1_Raw_Blast_output/output_blastn_$4_vs_$1.txt -num_threads 4 -num_alignments 1 -evalue 0.05
		echo "---------------Parsing BLAST output file---------------"
		perl blast_parser.pl ../Results/1_Raw_Blast_output/output_blastn_$4_vs_$1.txt $4 $1 ../Results/2_Best_hits #->$3-$1.csv






		# Hybrid_X_Hybrid(paralogs):
		echo "\n-$1 query VS $1 database-"
		blastn -query ../Data/$1_orf.fasta -db ../Results/0_BlastDB/$1_orf -out ../Results/1_Raw_Blast_output/output_blastn_$1_vs_$1.txt -num_threads 4 -evalue 1e-10 -outfmt "6 qseqid sseqid qlen slen length nident mismatch positive gapopen gaps pident ppos qstart qend sstart send evalue bitscore score"


		# ParentA_X_ParentA(paralogs):
		echo "\n-$2 query VS $2 database-"
		blastn -query ../Data/$2_orf.fasta -db ../Results/0_BlastDB/$2_orf -out ../Results/1_Raw_Blast_output/output_blastn_$2_vs_$2.txt -num_threads 4 -evalue 1e-10 -outfmt "6 qseqid sseqid qlen slen length nident mismatch positive gapopen gaps pident ppos qstart qend sstart send evalue bitscore score"


		# ParentB_X_ParentB(paralogs):
		echo "\n-$3 query VS $3 database-"
		blastn -query ../Data/$3_orf.fasta -db ../Results/0_BlastDB/$3_orf -out ../Results/1_Raw_Blast_output/output_blastn_$3_vs_$3.txt -num_threads 4 -evalue 1e-10  -outfmt "6 qseqid sseqid qlen slen length nident mismatch positive gapopen gaps pident ppos qstart qend sstart send evalue bitscore score"

		# ParentC_X_ParentC(paralogs):
		echo "\n-$4 query VS $4 database-"
		blastn -query ../Data/$4_orf.fasta -db ../Results/0_BlastDB/$4_orf -out ../Results/1_Raw_Blast_output/output_blastn_$4_vs_$4.txt -num_threads 4 -evalue 1e-10  -outfmt "6 qseqid sseqid qlen slen length nident mismatch positive gapopen gaps pident ppos qstart qend sstart send evalue bitscore score"



	python3 homologs.py  --nb 3

	#Search 1:1 orthologies:
	echo "\n ---------------Search 1:1 orthologies Hybrid - Parent A ---------------"
	python3 orthologs.py --name $1_$2 --ortho1 ../Results/2_Best_hits/$1-$2.csv --ortho2 ../Results/2_Best_hits/$2-$1.csv 
	echo "\n ---------------Search 1:1 orthologies Hybrid - Parent B ---------------"
	python3 orthologs.py --name $1_$3 --ortho1 ../Results/2_Best_hits/$1-$3.csv --ortho2 ../Results/2_Best_hits/$3-$1.csv
	echo "\n ---------------Search 1:1 orthologies Hybrid - Parent C ---------------"
	python3 orthologs.py --name $1_$4 --ortho1 ../Results/2_Best_hits/$1-$4.csv --ortho2 ../Results/2_Best_hits/$4-$1.csv


	tothyb=$(grep ">" ../Data/$1_orf.fasta | wc -l)
	totparA=$(grep ">" ../Data/$2_orf.fasta | wc -l)
	totparB=$(grep ">" ../Data/$3_orf.fasta | wc -l)
	totparC=$(grep ">" ../Data/$4_orf.fasta | wc -l)
	
	# Allele prediction
	echo "\n ---------------Allele prediction---------------"
	python3 prediction.py  --nb 3 --fH $1 --fA $2 --fB $3 --fC $4 --hyb $tothyb --pA $totparA --pB $totparB --pC $totparC


fi




########################### 4 Parental organisms


if [ "$four" = true ]; then

	echo "Hybrid file: $1"
	echo "Parent A file: $2"
	echo "Parent B file: $3"
	echo "Parent C file: $4"
	echo "Parent D file: $5"

	echo "\n--------Creation of BLAST databases--------------"

	makeblastdb -in ../Data/$1_orf.fasta -out ../Results/0_BlastDB/$1_orf -dbtype nucl
	makeblastdb -in ../Data/$2_orf.fasta -out ../Results/0_BlastDB/$2_orf -dbtype nucl
	makeblastdb -in ../Data/$3_orf.fasta -out ../Results/0_BlastDB/$3_orf -dbtype nucl
	makeblastdb -in ../Data/$4_orf.fasta -out ../Results/0_BlastDB/$4_orf -dbtype nucl
	makeblastdb -in ../Data/$5_orf.fasta -out ../Results/0_BlastDB/$5_orf -dbtype nucl


	echo "\n-----BLASTN------"

	mkdir -p ../Results/1_Raw_Blast_output
	mkdir -p ../Results/2_Best_hits
	mkdir -p ../Results/3_Orthologs_Paralogs
	mkdir -p ../Results/4_Parental_alleles_prediction


	#Run blastn and parse:
		# Hybrid_X_ParentA(orthologs):
		echo "\n-$1 query VS $2 database-"
		blastn -query ../Data/$1_orf.fasta -db ../Results/0_BlastDB/$2_orf -out ../Results/1_Raw_Blast_output/output_blastn_$1_vs_$2.txt -num_threads 4 -num_alignments 1 -evalue 0.05
		echo "---------------Parsing BLAST output file---------------"
		perl blast_parser.pl ../Results/1_Raw_Blast_output/output_blastn_$1_vs_$2.txt $1 $2 ../Results/2_Best_hits #->$1-$2.csv

		# ParentA_X_Hybrid(orthologs):
		echo "\n-$2 query VS $1 database-"
		blastn -query ../Data/$2_orf.fasta -db ../Results/0_BlastDB/$1_orf -out ../Results/1_Raw_Blast_output/output_blastn_$2_vs_$1.txt -num_threads 4 -num_alignments 1 -evalue 0.05
		echo "---------------Parsing BLAST output file---------------"
		perl blast_parser.pl ../Results/1_Raw_Blast_output/output_blastn_$2_vs_$1.txt $2 $1 ../Results/2_Best_hits #->$2-$1.csv
		

		# Hybrid_X_ParentB(orthologs):
		echo "\n-$1 query VS $3 database-"
		blastn -query ../Data/$1_orf.fasta -db ../Results/0_BlastDB/$3_orf -out ../Results/1_Raw_Blast_output/output_blastn_$1_vs_$3.txt -num_threads 4 -num_alignments 1 -evalue 0.05
		echo "---------------Parsing BLAST output file"
		perl blast_parser.pl ../Results/1_Raw_Blast_output/output_blastn_$1_vs_$3.txt $1 $3 ../Results/2_Best_hits #->$1-$3.csv

		# ParentB_X_Hybrid(orthologs):
		echo "\n-$3 query VS $1 database-"
		blastn -query ../Data/$3_orf.fasta -db ../Results/0_BlastDB/$1_orf -out ../Results/1_Raw_Blast_output/output_blastn_$3_vs_$1.txt -num_threads 4 -num_alignments 1 -evalue 0.05
		echo "---------------Parsing BLAST output file---------------"
		perl blast_parser.pl ../Results/1_Raw_Blast_output/output_blastn_$3_vs_$1.txt $3 $1 ../Results/2_Best_hits #->$3-$1.csv


		# Hybrid_X_ParentC(orthologs):
		echo "\n-$1 query VS $4 database-"
		blastn -query ../Data/$1_orf.fasta -db ../Results/0_BlastDB/$4_orf -out ../Results/1_Raw_Blast_output/output_blastn_$1_vs_$4.txt -num_threads 4 -num_alignments 1 -evalue 0.05
		echo "---------------Parsing BLAST output file"
		perl blast_parser.pl ../Results/1_Raw_Blast_output/output_blastn_$1_vs_$4.txt $1 $4 ../Results/2_Best_hits #->$1-$4.csv

		# ParentC_X_Hybrid(orthologs):
		echo "\n-$4 query VS $1 database-"
		blastn -query ../Data/$4_orf.fasta -db ../Results/0_BlastDB/$1_orf -out ../Results/1_Raw_Blast_output/output_blastn_$4_vs_$1.txt -num_threads 4 -num_alignments 1 -evalue 0.05
		echo "---------------Parsing BLAST output file---------------"
		perl blast_parser.pl ../Results/1_Raw_Blast_output/output_blastn_$4_vs_$1.txt $4 $1 ../Results/2_Best_hits #->$4-$1.csv


		# Hybrid_X_ParentD(orthologs):
		echo "\n-$1 query VS $5 database-"
		blastn -query ../Data/$1_orf.fasta -db ../Results/0_BlastDB/$5_orf -out ../Results/1_Raw_Blast_output/output_blastn_$1_vs_$5.txt -num_threads 4 -num_alignments 1 -evalue 0.05
		echo "---------------Parsing BLAST output file"
		perl blast_parser.pl ../Results/1_Raw_Blast_output/output_blastn_$1_vs_$5.txt $1 $5 ../Results/2_Best_hits #->$1-$5.csv

		# ParentD_X_Hybrid(orthologs):
		echo "\n-$5 query VS $1 database-"
		blastn -query ../Data/$5_orf.fasta -db ../Results/0_BlastDB/$1_orf -out ../Results/1_Raw_Blast_output/output_blastn_$5_vs_$1.txt -num_threads 4 -num_alignments 1 -evalue 0.05
		echo "---------------Parsing BLAST output file---------------"
		perl blast_parser.pl ../Results/1_Raw_Blast_output/output_blastn_$5_vs_$1.txt $5 $1 ../Results/2_Best_hits #->$5-$1.csv





		# Hybrid_X_Hybrid(paralogs):
		echo "\n-$1 query VS $1 database-"
		blastn -query ../Data/$1_orf.fasta -db ../Results/0_BlastDB/$1_orf -out ../Results/1_Raw_Blast_output/output_blastn_$1_vs_$1.txt -num_threads 4 -evalue 1e-10 -outfmt "6 qseqid sseqid qlen slen length nident mismatch positive gapopen gaps pident ppos qstart qend sstart send evalue bitscore score"


		# ParentA_X_ParentA(paralogs):
		echo "\n-$2 query VS $2 database-"
		blastn -query ../Data/$2_orf.fasta -db ../Results/0_BlastDB/$2_orf -out ../Results/1_Raw_Blast_output/output_blastn_$2_vs_$2.txt -num_threads 4 -evalue 1e-10 -outfmt "6 qseqid sseqid qlen slen length nident mismatch positive gapopen gaps pident ppos qstart qend sstart send evalue bitscore score"


		# ParentB_X_ParentB(paralogs):
		echo "\n-$3 query VS $3 database-"
		blastn -query ../Data/$3_orf.fasta -db ../Results/0_BlastDB/$3_orf -out ../Results/1_Raw_Blast_output/output_blastn_$3_vs_$3.txt -num_threads 4 -evalue 1e-10  -outfmt "6 qseqid sseqid qlen slen length nident mismatch positive gapopen gaps pident ppos qstart qend sstart send evalue bitscore score"


		# ParentC_X_ParentC(paralogs):
		echo "\n-$4 query VS $4 database-"
		blastn -query ../Data/$4_orf.fasta -db ../Results/0_BlastDB/$4_orf -out ../Results/1_Raw_Blast_output/output_blastn_$4_vs_$4.txt -num_threads 4 -evalue 1e-10  -outfmt "6 qseqid sseqid qlen slen length nident mismatch positive gapopen gaps pident ppos qstart qend sstart send evalue bitscore score"

		# ParentD_X_ParentD(paralogs):
		echo "\n-$5 query VS $5 database-"
		blastn -query ../Data/$5_orf.fasta -db ../Results/0_BlastDB/$5_orf -out ../Results/1_Raw_Blast_output/output_blastn_$5_vs_$5.txt -num_threads 4 -evalue 1e-10  -outfmt "6 qseqid sseqid qlen slen length nident mismatch positive gapopen gaps pident ppos qstart qend sstart send evalue bitscore score"

		
	python3 homologs.py --nb 4

	#Search 1:1 orthologies:
	echo "\n ---------------Search 1:1 orthologies Hybrid - Parent A ---------------"
	python3 orthologs.py --name $1_$2 --ortho1 ../Results/2_Best_hits/$1-$2.csv --ortho2 ../Results/2_Best_hits/$2-$1.csv 
	echo "\n ---------------Search 1:1 orthologies Hybrid - Parent B ---------------"
	python3 orthologs.py --name $1_$3 --ortho1 ../Results/2_Best_hits/$1-$3.csv --ortho2 ../Results/2_Best_hits/$3-$1.csv
	echo "\n ---------------Search 1:1 orthologies Hybrid - Parent C ---------------"
	python3 orthologs.py --name $1_$4 --ortho1 ../Results/2_Best_hits/$1-$4.csv --ortho2 ../Results/2_Best_hits/$4-$1.csv
	echo "\n ---------------Search 1:1 orthologies Hybrid - Parent D ---------------"
	python3 orthologs.py --name $1_$5 --ortho1 ../Results/2_Best_hits/$1-$5.csv --ortho2 ../Results/2_Best_hits/$5-$1.csv

	tothyb=$(grep ">" ../Data/$1_orf.fasta | wc -l)
	totparA=$(grep ">" ../Data/$2_orf.fasta | wc -l)
	totparB=$(grep ">" ../Data/$3_orf.fasta | wc -l)
	totparC=$(grep ">" ../Data/$4_orf.fasta | wc -l)
	totparD=$(grep ">" ../Data/$5_orf.fasta | wc -l)
	
	# Allele prediction
	echo "\n ---------------Allele prediction---------------"
	python3 prediction.py  --nb 4 --fH $1 --fA $2 --fB $3 --fC $4 --fD $5 --hyb $tothyb --pA $totparA --pB $totparB --pC $totparC --pD $totparD

fi



