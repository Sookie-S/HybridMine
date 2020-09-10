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

		# ParentA_X_Hybrid(orthologs):
		echo "\n-Parent A query VS Hybrid database-"
		blastn -query ../Data/$2 -db ../Results/0_BlastDB/hybrid_orf -out ../Results/1_Raw_Blast_output/output_blastn_parentA_vs_hybrid.txt -num_threads 4 -num_alignments 1 -evalue 0.05
		echo "---------------Parsing BLAST output file---------------"
		perl blast_parser.pl ../Results/1_Raw_Blast_output/output_blastn_parentA_vs_hybrid.txt parentA hybrid ../Results/2_Best_hits #->ParentA-Hybrid.csv
		

		# Hybrid_X_ParentB(orthologs):
		echo "\n-Hybrid query VS Parent B database-"
		blastn -query ../Data/$1 -db ../Results/0_BlastDB/parentB_orf -out ../Results/1_Raw_Blast_output/output_blastn_hybrid_vs_parentB.txt -num_threads 4 -num_alignments 1 -evalue 0.05
		echo "---------------Parsing BLAST output file"
		perl blast_parser.pl ../Results/1_Raw_Blast_output/output_blastn_hybrid_vs_parentB.txt hybrid parentB ../Results/2_Best_hits #->Hybrid-ParentB.csv

		# ParentB_X_Hybrid(orthologs):
		echo "\n-Parent B query VS Hybrid database-"
		blastn -query ../Data/$3 -db ../Results/0_BlastDB/hybrid_orf -out ../Results/1_Raw_Blast_output/output_blastn_parentB_vs_hybrid.txt -num_threads 4 -num_alignments 1 -evalue 0.05
		echo "---------------Parsing BLAST output file---------------"
		perl blast_parser.pl ../Results/1_Raw_Blast_output/output_blastn_parentB_vs_hybrid.txt parentB hybrid ../Results/2_Best_hits #->ParentB-Hybrid.csv


		# Hybrid_X_Hybrid(paralogs):
		echo "\n-Hybrid query VS Hybrid database-"
		blastn -query ../Data/$1 -db ../Results/0_BlastDB/hybrid_orf -out ../Results/1_Raw_Blast_output/output_blastn_hybrid_vs_hybrid.txt -num_threads 4 -evalue 1e-10 -outfmt "6 qseqid sseqid qlen slen length nident mismatch positive gapopen gaps pident ppos qstart qend sstart send evalue bitscore score"


		# ParentA_X_ParentA(paralogs):
		echo "\n-Parent A query VS Parent A database-"
		blastn -query ../Data/$2 -db ../Results/0_BlastDB/parentA_orf -out ../Results/1_Raw_Blast_output/output_blastn_parentA_vs_parentA.txt -num_threads 4 -evalue 1e-10 -outfmt "6 qseqid sseqid qlen slen length nident mismatch positive gapopen gaps pident ppos qstart qend sstart send evalue bitscore score"


		# ParentB_X_ParentB(paralogs):
		echo "\n-Parent B query VS Parent B database-"
		blastn -query ../Data/$3 -db ../Results/0_BlastDB/parentB_orf -out ../Results/1_Raw_Blast_output/output_blastn_parentB_vs_parentB.txt -num_threads 4 -evalue 1e-10  -outfmt "6 qseqid sseqid qlen slen length nident mismatch positive gapopen gaps pident ppos qstart qend sstart send evalue bitscore score"
		
	python3 homologs.py  --nb 2

	#Search 1:1 orthologies:
	echo "\n ---------------Search 1:1 orthologies Hybrid - Parent A ---------------"
	python3 orthologs.py --name hybrid_parentA --ortho1 ../Results/2_Best_hits/hybrid-parentA.csv --ortho2 ../Results/2_Best_hits/parentA-hybrid.csv 
	echo "\n ---------------Search 1:1 orthologies Hybrid - Parent B ---------------"
	python3 orthologs.py --name hybrid_parentB --ortho1 ../Results/2_Best_hits/hybrid-parentB.csv --ortho2 ../Results/2_Best_hits/parentB-hybrid.csv


	tothyb=$(grep ">" ../Data/$1 | wc -l)
	totparA=$(grep ">" ../Data/$2 | wc -l)
	totparB=$(grep ">" ../Data/$3 | wc -l)

	#echo "$tothyb"
	#echo "$totparA"
	#echo "$totparB"


	# Allele prediction
	echo "\n ---------------Allele prediction---------------"
	python3 prediction.py  --nb 2 --hyb $tothyb --pA $totparA --pB $totparB

	

fi


########################### 3 Parental organisms



if [ "$three" = true ]; then

	echo "Hybrid file: $1"
	echo "Parent A file: $2"
	echo "Parent B file: $3"
	echo "Parent C file: $4"

	echo "\n--------Creation of BLAST databases--------------"

	makeblastdb -in ../Data/$1 -out ../Results/0_BlastDB/hybrid_orf -dbtype nucl
	makeblastdb -in ../Data/$2 -out ../Results/0_BlastDB/parentA_orf -dbtype nucl
	makeblastdb -in ../Data/$3 -out ../Results/0_BlastDB/parentB_orf -dbtype nucl
	makeblastdb -in ../Data/$4 -out ../Results/0_BlastDB/parentC_orf -dbtype nucl


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

		# ParentA_X_Hybrid(orthologs):
		echo "\n-Parent A query VS Hybrid database-"
		blastn -query ../Data/$2 -db ../Results/0_BlastDB/hybrid_orf -out ../Results/1_Raw_Blast_output/output_blastn_parentA_vs_hybrid.txt -num_threads 4 -num_alignments 1 -evalue 0.05
		echo "---------------Parsing BLAST output file---------------"
		perl blast_parser.pl ../Results/1_Raw_Blast_output/output_blastn_parentA_vs_hybrid.txt parentA hybrid ../Results/2_Best_hits #->ParentA-Hybrid.csv
		

		# Hybrid_X_ParentB(orthologs):
		echo "\n-Hybrid query VS Parent B database-"
		blastn -query ../Data/$1 -db ../Results/0_BlastDB/parentB_orf -out ../Results/1_Raw_Blast_output/output_blastn_hybrid_vs_parentB.txt -num_threads 4 -num_alignments 1 -evalue 0.05
		echo "---------------Parsing BLAST output file"
		perl blast_parser.pl ../Results/1_Raw_Blast_output/output_blastn_hybrid_vs_parentB.txt hybrid parentB ../Results/2_Best_hits #->Hybrid-ParentB.csv

		# ParentB_X_Hybrid(orthologs):
		echo "\n-Parent B query VS Hybrid database-"
		blastn -query ../Data/$3 -db ../Results/0_BlastDB/hybrid_orf -out ../Results/1_Raw_Blast_output/output_blastn_parentB_vs_hybrid.txt -num_threads 4 -num_alignments 1 -evalue 0.05
		echo "---------------Parsing BLAST output file---------------"
		perl blast_parser.pl ../Results/1_Raw_Blast_output/output_blastn_parentB_vs_hybrid.txt parentB hybrid ../Results/2_Best_hits #->ParentB-Hybrid.csv

		# Hybrid_X_ParentC(orthologs):
		echo "\n-Hybrid query VS Parent C database-"
		blastn -query ../Data/$1 -db ../Results/0_BlastDB/parentC_orf -out ../Results/1_Raw_Blast_output/output_blastn_hybrid_vs_parentC.txt -num_threads 4 -num_alignments 1 -evalue 0.05
		echo "---------------Parsing BLAST output file"
		perl blast_parser.pl ../Results/1_Raw_Blast_output/output_blastn_hybrid_vs_parentC.txt hybrid parentC ../Results/2_Best_hits #->Hybrid-ParentB.csv

		# ParentC_X_Hybrid(orthologs):
		echo "\n-Parent C query VS Hybrid database-"
		blastn -query ../Data/$4 -db ../Results/0_BlastDB/hybrid_orf -out ../Results/1_Raw_Blast_output/output_blastn_parentC_vs_hybrid.txt -num_threads 4 -num_alignments 1 -evalue 0.05
		echo "---------------Parsing BLAST output file---------------"
		perl blast_parser.pl ../Results/1_Raw_Blast_output/output_blastn_parentC_vs_hybrid.txt parentC hybrid ../Results/2_Best_hits #->ParentB-Hybrid.csv






		# Hybrid_X_Hybrid(paralogs):
		echo "\n-Hybrid query VS Hybrid database-"
		blastn -query ../Data/$1 -db ../Results/0_BlastDB/hybrid_orf -out ../Results/1_Raw_Blast_output/output_blastn_hybrid_vs_hybrid.txt -num_threads 4 -evalue 1e-10 -outfmt "6 qseqid sseqid qlen slen length nident mismatch positive gapopen gaps pident ppos qstart qend sstart send evalue bitscore score"


		# ParentA_X_ParentA(paralogs):
		echo "\n-Parent A query VS Parent A database-"
		blastn -query ../Data/$2 -db ../Results/0_BlastDB/parentA_orf -out ../Results/1_Raw_Blast_output/output_blastn_parentA_vs_parentA.txt -num_threads 4 -evalue 1e-10 -outfmt "6 qseqid sseqid qlen slen length nident mismatch positive gapopen gaps pident ppos qstart qend sstart send evalue bitscore score"


		# ParentB_X_ParentB(paralogs):
		echo "\n-Parent B query VS Parent B database-"
		blastn -query ../Data/$3 -db ../Results/0_BlastDB/parentB_orf -out ../Results/1_Raw_Blast_output/output_blastn_parentB_vs_parentB.txt -num_threads 4 -evalue 1e-10  -outfmt "6 qseqid sseqid qlen slen length nident mismatch positive gapopen gaps pident ppos qstart qend sstart send evalue bitscore score"

		# ParentC_X_ParentC(paralogs):
		echo "\n-Parent C query VS Parent C database-"
		blastn -query ../Data/$4 -db ../Results/0_BlastDB/parentC_orf -out ../Results/1_Raw_Blast_output/output_blastn_parentC_vs_parentC.txt -num_threads 4 -evalue 1e-10  -outfmt "6 qseqid sseqid qlen slen length nident mismatch positive gapopen gaps pident ppos qstart qend sstart send evalue bitscore score"



	python3 homologs.py  --nb 3

	#Search 1:1 orthologies:
	echo "\n ---------------Search 1:1 orthologies Hybrid - Parent A ---------------"
	python3 orthologs.py --name hybrid_parentA --ortho1 ../Results/2_Best_hits/hybrid-parentA.csv --ortho2 ../Results/2_Best_hits/parentA-hybrid.csv 
	echo "\n ---------------Search 1:1 orthologies Hybrid - Parent B ---------------"
	python3 orthologs.py --name hybrid_parentB --ortho1 ../Results/2_Best_hits/hybrid-parentB.csv --ortho2 ../Results/2_Best_hits/parentB-hybrid.csv
	echo "\n ---------------Search 1:1 orthologies Hybrid - Parent C ---------------"
	python3 orthologs.py --name hybrid_parentC --ortho1 ../Results/2_Best_hits/hybrid-parentC.csv --ortho2 ../Results/2_Best_hits/parentC-hybrid.csv


	tothyb=$(grep ">" ../Data/$1 | wc -l)
	totparA=$(grep ">" ../Data/$2 | wc -l)
	totparB=$(grep ">" ../Data/$3 | wc -l)
	totparC=$(grep ">" ../Data/$4 | wc -l)
	
	# Allele prediction
	echo "\n ---------------Allele prediction---------------"
	python3 prediction.py  --nb 3 --hyb $tothyb --pA $totparA --pB $totparB --pC $totparC


fi




########################### 4 Parental organisms


if [ "$four" = true ]; then

	echo "Hybrid file: $1"
	echo "Parent A file: $2"
	echo "Parent B file: $3"
	echo "Parent C file: $4"
	echo "Parent D file: $5"

	echo "\n--------Creation of BLAST databases--------------"

	makeblastdb -in ../Data/$1 -out ../Results/0_BlastDB/hybrid_orf -dbtype nucl
	makeblastdb -in ../Data/$2 -out ../Results/0_BlastDB/parentA_orf -dbtype nucl
	makeblastdb -in ../Data/$3 -out ../Results/0_BlastDB/parentB_orf -dbtype nucl
	makeblastdb -in ../Data/$4 -out ../Results/0_BlastDB/parentC_orf -dbtype nucl
	makeblastdb -in ../Data/$5 -out ../Results/0_BlastDB/parentD_orf -dbtype nucl


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

		# ParentA_X_Hybrid(orthologs):
		echo "\n-Parent A query VS Hybrid database-"
		blastn -query ../Data/$2 -db ../Results/0_BlastDB/hybrid_orf -out ../Results/1_Raw_Blast_output/output_blastn_parentA_vs_hybrid.txt -num_threads 4 -num_alignments 1 -evalue 0.05
		echo "---------------Parsing BLAST output file---------------"
		perl blast_parser.pl ../Results/1_Raw_Blast_output/output_blastn_parentA_vs_hybrid.txt parentA hybrid ../Results/2_Best_hits #->ParentA-Hybrid.csv
		

		# Hybrid_X_ParentB(orthologs):
		echo "\n-Hybrid query VS Parent B database-"
		blastn -query ../Data/$1 -db ../Results/0_BlastDB/parentB_orf -out ../Results/1_Raw_Blast_output/output_blastn_hybrid_vs_parentB.txt -num_threads 4 -num_alignments 1 -evalue 0.05
		echo "---------------Parsing BLAST output file"
		perl blast_parser.pl ../Results/1_Raw_Blast_output/output_blastn_hybrid_vs_parentB.txt hybrid parentB ../Results/2_Best_hits #->Hybrid-ParentB.csv

		# ParentB_X_Hybrid(orthologs):
		echo "\n-Parent B query VS Hybrid database-"
		blastn -query ../Data/$3 -db ../Results/0_BlastDB/hybrid_orf -out ../Results/1_Raw_Blast_output/output_blastn_parentB_vs_hybrid.txt -num_threads 4 -num_alignments 1 -evalue 0.05
		echo "---------------Parsing BLAST output file---------------"
		perl blast_parser.pl ../Results/1_Raw_Blast_output/output_blastn_parentB_vs_hybrid.txt parentB hybrid ../Results/2_Best_hits #->ParentB-Hybrid.csv


		# Hybrid_X_ParentC(orthologs):
		echo "\n-Hybrid query VS Parent C database-"
		blastn -query ../Data/$1 -db ../Results/0_BlastDB/parentC_orf -out ../Results/1_Raw_Blast_output/output_blastn_hybrid_vs_parentC.txt -num_threads 4 -num_alignments 1 -evalue 0.05
		echo "---------------Parsing BLAST output file"
		perl blast_parser.pl ../Results/1_Raw_Blast_output/output_blastn_hybrid_vs_parentC.txt hybrid parentC ../Results/2_Best_hits #->Hybrid-ParentC.csv

		# ParentC_X_Hybrid(orthologs):
		echo "\n-Parent C query VS Hybrid database-"
		blastn -query ../Data/$4 -db ../Results/0_BlastDB/hybrid_orf -out ../Results/1_Raw_Blast_output/output_blastn_parentC_vs_hybrid.txt -num_threads 4 -num_alignments 1 -evalue 0.05
		echo "---------------Parsing BLAST output file---------------"
		perl blast_parser.pl ../Results/1_Raw_Blast_output/output_blastn_parentC_vs_hybrid.txt parentC hybrid ../Results/2_Best_hits #->ParentC-Hybrid.csv


		# Hybrid_X_ParentD(orthologs):
		echo "\n-Hybrid query VS Parent D database-"
		blastn -query ../Data/$1 -db ../Results/0_BlastDB/parentD_orf -out ../Results/1_Raw_Blast_output/output_blastn_hybrid_vs_parentD.txt -num_threads 4 -num_alignments 1 -evalue 0.05
		echo "---------------Parsing BLAST output file"
		perl blast_parser.pl ../Results/1_Raw_Blast_output/output_blastn_hybrid_vs_parentD.txt hybrid parentD ../Results/2_Best_hits #->Hybrid-ParentD.csv

		# ParentD_X_Hybrid(orthologs):
		echo "\n-Parent D query VS Hybrid database-"
		blastn -query ../Data/$5 -db ../Results/0_BlastDB/hybrid_orf -out ../Results/1_Raw_Blast_output/output_blastn_parentD_vs_hybrid.txt -num_threads 4 -num_alignments 1 -evalue 0.05
		echo "---------------Parsing BLAST output file---------------"
		perl blast_parser.pl ../Results/1_Raw_Blast_output/output_blastn_parentD_vs_hybrid.txt parentD hybrid ../Results/2_Best_hits #->ParentD-Hybrid.csv





		# Hybrid_X_Hybrid(paralogs):
		echo "\n-Hybrid query VS Hybrid database-"
		blastn -query ../Data/$1 -db ../Results/0_BlastDB/hybrid_orf -out ../Results/1_Raw_Blast_output/output_blastn_hybrid_vs_hybrid.txt -num_threads 4 -evalue 1e-10 -outfmt "6 qseqid sseqid qlen slen length nident mismatch positive gapopen gaps pident ppos qstart qend sstart send evalue bitscore score"


		# ParentA_X_ParentA(paralogs):
		echo "\n-Parent A query VS Parent A database-"
		blastn -query ../Data/$2 -db ../Results/0_BlastDB/parentA_orf -out ../Results/1_Raw_Blast_output/output_blastn_parentA_vs_parentA.txt -num_threads 4 -evalue 1e-10 -outfmt "6 qseqid sseqid qlen slen length nident mismatch positive gapopen gaps pident ppos qstart qend sstart send evalue bitscore score"


		# ParentB_X_ParentB(paralogs):
		echo "\n-Parent B query VS Parent B database-"
		blastn -query ../Data/$3 -db ../Results/0_BlastDB/parentB_orf -out ../Results/1_Raw_Blast_output/output_blastn_parentB_vs_parentB.txt -num_threads 4 -evalue 1e-10  -outfmt "6 qseqid sseqid qlen slen length nident mismatch positive gapopen gaps pident ppos qstart qend sstart send evalue bitscore score"


		# ParentC_X_ParentC(paralogs):
		echo "\n-Parent C query VS Parent C database-"
		blastn -query ../Data/$4 -db ../Results/0_BlastDB/parentC_orf -out ../Results/1_Raw_Blast_output/output_blastn_parentC_vs_parentC.txt -num_threads 4 -evalue 1e-10  -outfmt "6 qseqid sseqid qlen slen length nident mismatch positive gapopen gaps pident ppos qstart qend sstart send evalue bitscore score"

		# ParentD_X_ParentD(paralogs):
		echo "\n-Parent D query VS Parent D database-"
		blastn -query ../Data/$5 -db ../Results/0_BlastDB/parentD_orf -out ../Results/1_Raw_Blast_output/output_blastn_parentD_vs_parentD.txt -num_threads 4 -evalue 1e-10  -outfmt "6 qseqid sseqid qlen slen length nident mismatch positive gapopen gaps pident ppos qstart qend sstart send evalue bitscore score"

		
	python3 homologs.py --nb 4

	#Search 1:1 orthologies:
	echo "\n ---------------Search 1:1 orthologies Hybrid - Parent A ---------------"
	python3 orthologs.py --name hybrid_parentA --ortho1 ../Results/2_Best_hits/hybrid-parentA.csv --ortho2 ../Results/2_Best_hits/parentA-hybrid.csv 
	echo "\n ---------------Search 1:1 orthologies Hybrid - Parent B ---------------"
	python3 orthologs.py --name hybrid_parentB --ortho1 ../Results/2_Best_hits/hybrid-parentB.csv --ortho2 ../Results/2_Best_hits/parentB-hybrid.csv
	echo "\n ---------------Search 1:1 orthologies Hybrid - Parent C ---------------"
	python3 orthologs.py --name hybrid_parentC --ortho1 ../Results/2_Best_hits/hybrid-parentC.csv --ortho2 ../Results/2_Best_hits/parentC-hybrid.csv
	echo "\n ---------------Search 1:1 orthologies Hybrid - Parent D ---------------"
	python3 orthologs.py --name hybrid_parentD --ortho1 ../Results/2_Best_hits/hybrid-parentD.csv --ortho2 ../Results/2_Best_hits/parentD-hybrid.csv

	tothyb=$(grep ">" ../Data/$1 | wc -l)
	totparA=$(grep ">" ../Data/$2 | wc -l)
	totparB=$(grep ">" ../Data/$3 | wc -l)
	totparC=$(grep ">" ../Data/$4 | wc -l)
	totparD=$(grep ">" ../Data/$5 | wc -l)
	
	# Allele prediction
	echo "\n ---------------Allele prediction---------------"
	python3 prediction.py  --nb 4 --hyb $tothyb --pA $totparA --pB $totparB --pC $totparC --pD $totparD

fi



