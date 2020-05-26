#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Soukaina Timouma"
__credits__ = ["Soukaina Timouma", "Daniela Delneri", "Jean-Marc Schwartz"]
__version__ = "1.0.1"
__maintainer__ = "Soukaina Timouma"
__email__ = "soukaina.timouma@manchester.ac.uk"

"""
Created on Fri Feb 21 15:30:38 2020

@author: sookie
"""



############# HOMOLOG BEST HITS
hybrid_name = "hybrid"
parentA_name = "parentA"
parentB_name = "parentB"

organism = []
organism.append(parentA_name)
organism.append(parentB_name)
organism.append(hybrid_name)



i=0
for x in organism:
    pair_paralogs_check = []
    globals()["dic_paralogs_"+str(x)] = {}
#    print(x) 
    with open("../Results/1_Raw_Blast_output/output_blastn_"+str(x)+"_vs_"+str(x)+".txt", "r") as outputBlast:
        for line in outputBlast:
            i+=1
            line = line.split("\n")[0]
            line = line.split("\t")
            qseqid = line[0]
            sseqid = line[1]
            qstart = line[12]
            qend = line[13]
            sstart = line[14]
            send = line[15]
            
            
            pair = []
            pair.append(qseqid)
            pair.append(sseqid)
            
#            if int(line[2]) > int(line[3]):
#                perc = (float(line[5])/float(line[2]))*100
#            elif int(line[2]) < int(line[3]):
#                perc = (float(line[5])/float(line[3]))*100
            
            if qseqid == sseqid:
                next
#            elif int(perc) < 30:
#                next
            elif pair in pair_paralogs_check:
                next
            elif (int(qstart) < int(qend)) and (int(sstart) > int(send)): # overlapping genes
                next
            elif (int(qstart) > int(qend)) and (int(sstart) < int(send)): # overlapping genes
                next
            else:
                if qseqid in globals()["dic_paralogs_"+str(x)].keys():
#                    print(line[0])
                    globals()["dic_paralogs_"+str(x)][qseqid]['sseqid'].append(sseqid)
                    globals()["dic_paralogs_"+str(x)][qseqid]['qlen'].append(line[2])
                    globals()["dic_paralogs_"+str(x)][qseqid]['slen'].append(line[3])
                    globals()["dic_paralogs_"+str(x)][qseqid]['length'].append(line[4])
                    globals()["dic_paralogs_"+str(x)][qseqid]['nident'].append(line[5])
                    globals()["dic_paralogs_"+str(x)][qseqid]['mismatch'].append(line[6])
                    globals()["dic_paralogs_"+str(x)][qseqid]['positive'].append(line[7])
                    globals()["dic_paralogs_"+str(x)][qseqid]['gapopen'].append(line[8])
                    globals()["dic_paralogs_"+str(x)][qseqid]['gaps'].append(line[9])
                    globals()["dic_paralogs_"+str(x)][qseqid]['pident'].append(line[10])
                    globals()["dic_paralogs_"+str(x)][qseqid]['ppos'].append(line[11])
                    globals()["dic_paralogs_"+str(x)][qseqid]['qstart'].append(qstart)
                    globals()["dic_paralogs_"+str(x)][qseqid]['qend'].append(qend)
                    globals()["dic_paralogs_"+str(x)][qseqid]['sstart'].append(sstart)
                    globals()["dic_paralogs_"+str(x)][qseqid]['send'].append(send)
                    globals()["dic_paralogs_"+str(x)][qseqid]['evalue'].append(line[16])
                    globals()["dic_paralogs_"+str(x)][qseqid]['bitscore'].append(line[17])
                    globals()["dic_paralogs_"+str(x)][qseqid]['score'].append(line[18])               
                else:
                    globals()["dic_paralogs_"+str(x)][qseqid] = {'sseqid':[sseqid],
                    'qlen': [line[2]],
                    'slen':[line[3]],
                    'length':[line[4]],
                    'nident':[line[5]],
                    'mismatch':[line[6]],
                    'positive':[line[7]],
                    'gapopen':[line[8]],
                    'gaps':[line[9]],
                    'pident':[line[10]],
                    'ppos':[line[11]],
                    'qstart':[qstart],
                    'qend':[qend],
                    'sstart':[sstart],
                    'send':[send],
                    'evalue':[line[16]],
                    'bitscore':[line[17]],
                    'score':[line[18]]}
                
                pair_paralogs_check.append(pair)          
       
    done = []
    
    with open("../Results/2_Best_hits/"+str(x)+"-"+str(x)+".csv","w") as outputA:
        outputA.write("Sequence,Best Hit,e-value\n")
        for pairs in pair_paralogs_check:
        #    print(pairs)
            p1 = pairs[0]
            p2 = pairs[1]
            pairs2 =[]
            pairs2.append(p2)
            pairs2.append(p1)
            
            if pairs not in done:
                if p2 in globals()["dic_paralogs_"+str(x)].keys():
                    vals = globals()["dic_paralogs_"+str(x)][p2]['sseqid']
                    n = 0
                    for val in vals:
                        if val == p1:
                            evalues = globals()["dic_paralogs_"+str(x)][p2]['evalue']
                            outputA.write(str(p1)+","+str(p2)+","+str(evalues[n])+"\n")
                            done.append(pairs)
                            done.append(pairs2)
                        n+=1
