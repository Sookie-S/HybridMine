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

'''
Get a list of keys from dictionary which has the given value
'''
#
#def getKeysByValue(dictOfElements, valueToFind):
#    listOfKeys = list()
#    listOfItems = dictOfElements.items()
#    for item  in listOfItems:
#        if item[1] == valueToFind:
#            listOfKeys.append(item[0])
#    return  listOfKeys


#%%
import argparse

parser = argparse.ArgumentParser(description='Filenames')
parser.add_argument('--name', required=True, help='')

args = parser.parse_args()
name = args.name



global hybrid_name
hybrid_name = name.split("_")[0]
global parentA_name
parentA_name = name.split("_")[1]
global parentB_name
parentB_name = name.split("_")[2]

############# PARALOGS SEARCH
#%%TO DELETE#
import os
os.chdir("/home/sookie/Documents/HybridMine_test/Scripts")
parentA_name ="Scerevisiae"
parentB_name="FM1318"
hybrid_name="WS3470"
#%% 
organism = []
organism.append(parentA_name)
organism.append(parentB_name)
organism.append(hybrid_name)



for x in organism:
    pair_paralogs_check = []
    globals()["dic_paralogs_"+str(x)] = {}
#    print(x) 
    with open("../Results/Blast_results/output_blastn_"+str(x)+"_vs_"+str(x)+".txt", "r") as outputBlast:
        for line in outputBlast:
            line = line.split("\n")[0]
            line = line.split("\t")
            qseqid = line[0]
            sseqid = line[1]
            qstart = line[12]
            qend = line[13]
            sstart = line[14]
            send = line[15]
            globals()["dic_paralogs_"+str(x)][line[0]] = {'sseqid':line[1],
            'qlen': line[2],
            'slen':line[3],
            'length':line[4],
            'nident':line[5],
            'mismatch':[6],
            'positive':line[7],
            'gapopen':line[8],
            'gaps':line[9],
            'pident':line[10],
            'ppos':line[11],
            'qstart':line[12],
            'qend':line[13],
            'sstart':line[14],
            'send':line[15],
            'evalue':line[16],
            'bitscore':line[17],
            'score':line[18]}
            
            pair = []
            pair.append(qseqid)
            pair.append(sseqid)
            
            if int(line[2]) > int(line[3]):
                perc = (float(line[5])/float(line[2]))*100
            elif int(line[2]) < int(line[3]):
                perc = (float(line[5])/float(line[3]))*100
            
            if qseqid == sseqid:
                next
            elif int(perc) < 30:
                next
            elif pair in pair_paralogs_check:
                next
            elif (int(qstart) < int(qend)) and (int(sstart) > int(send)):
                next
            elif (int(qstart) > int(qend)) and (int(sstart) < int(send)):
                next
            else:
                pair_paralogs_check.append(pair)          
       
    done = []
    
    with open("../Results/Blastn_best_hits/"+str(x)+"-"+str(x)+".csv","w") as outputA:
        outputA.write("Sequence,Best Hit,e-value,Identities,Gaps,Percentage identity,Sequence length, Best Hit length\n")
        for pairs in pair_paralogs_check:
        #    print(pairs)
            p1 = pairs[0]
            p2 = pairs[1]
            pairs2 =[]
            pairs2.append(p2)
            pairs2.append(p1)
            if globals()["dic_paralogs_"+str(x)][p2]['sseqid'] == p1:
                if pairs not in done:
                    outputA.write(str(p1)+","+str(p2)+","+str(globals()["dic_paralogs_"+str(x)][p1]['evalue'])+","+str(globals()["dic_paralogs_"+str(x)][p1]['nident'])+","+str(globals()["dic_paralogs_"+str(x)][p1]['gaps'])+","+str(globals()["dic_paralogs_"+str(x)][p1]['pident'])+","+str(globals()["dic_paralogs_"+str(x)][p1]['qlen'])+","+str(globals()["dic_paralogs_"+str(x)][p1]['slen'])+"\n")
                    done.append(pairs)
                    done.append(pairs2)



#%%
#dic_paralogs_WS3470 
#dic_paralogs_Scerevisiae  

#dic_paralogs_FM1318    
#%%    

dic_ParB_alleles = {}
dic_ParA_alleles = {}

with open("../Results/Parental_alleles_prediction/genes_alleles_inherited_from_"+str(parentA_name)+".csv", "r") as parentalA:
    for line in parentalA:
        line = line.split("\n")[0]
        line = line.split(",")
        # print(line)
        dic_ParA_alleles[line[0]] = line[1]

with open("../Results/Parental_alleles_prediction/genes_alleles_inherited_from_"+str(parentB_name)+".csv", "r") as parentalB:
    next(parentalB)
    for line in parentalB:
        line = line.split("\n")[0]
        line = line.split(",")
        # print(line)
        dic_ParB_alleles[line[0]] = line[1]
  
dic_alleles = {**dic_ParB_alleles, **dic_ParA_alleles}


#%%       GROUPING PARALOGS      

dic_paralog = {}
list_paralog_already_processed = []

stop = 0
with open("../Results/Blastn_best_hits/"+str(hybrid_name)+"-"+str(hybrid_name)+".csv", "r") as hyb:
    next(hyb)
    for line in hyb:
        stop+=1
        line = line.split("\n")[0]
        line = line.split(",")
        id1 = line[0]
        id2 = line[1]
#        print(id1)
#        print(id2)
        
        if (id1 not in list_paralog_already_processed) and (id2 not in list_paralog_already_processed): # new dict[id1] = id2
            # print("############CASE 1")
            dic_paralog[id1] = [id2]
            list_paralog_already_processed.append(id1)
            list_paralog_already_processed.append(id2)
#            
#            for elm in dic_paralog:
#                print(str(elm) + " : " + str(dic_paralog[elm]))
                  
        elif (id1 in list_paralog_already_processed) and (id2 not in list_paralog_already_processed): # dict[id1] = append id2
            # print("############CASE 2")
            try:
                dic_paralog[id1].append(id2)
                list_paralog_already_processed.append(id2)
                
            except:
                try: 
                    for elm in dic_paralog:
                        for val in dic_paralog[elm]:
                            if val == str(id1):
#                                print("THE KEY IS "+str(elm))
                                dic_paralog[elm].append(id2)
                                list_paralog_already_processed.append(id2)                            
                except:
                    pass
                    # print("mmmm")
                    
        elif id1 not in list_paralog_already_processed and id2 in list_paralog_already_processed: # dict[id1] = append id2
            # print("############CASE 3")
            try:
                dic_paralog[id2].append(id1)
                list_paralog_already_processed.append(id1)
                
            except:
                try: 
                    for elm in dic_paralog:
                        for val in dic_paralog[elm]:
                            if val == str(id2):
#                                print("THE KEY IS "+str(elm))
                                dic_paralog[elm].append(id1)
                                list_paralog_already_processed.append(id1)   
                except:
                    pass
                    # print("mmmm")
                    
        elif id1 in list_paralog_already_processed and id2 in list_paralog_already_processed:
            pass
            # print("Already processed")
            

        else:
            pass
            # print("NO")
            # print("error with: id1 = "+str(id1)+" and id2 = "+str(id2))
            
            
#%%
nb = 0
total = 0
list_paralog = []
with open("../Results/Orthologs_and_paralogs/list_paralogs_"+str(hybrid_name)+".csv", "w") as output_paralog:
    output_paralog.write("Paralog_list"+"\t"+str(parentB_name)+"-like content"+"\t"+str(hybrid_name)+" content"+"\t"+str(parentA_name)+"-like content"+"\n") 
    for elm in dic_paralog:
        total += 1
#        nb = 0
        list_paralog = []
        hyb = []
        ParA = []
        ParB = []
        # print("\n------ELM is: "+str(elm))
        try:
            # print("TRY 1")
            # print(dic_alleles[elm])
            list_paralog.append(dic_alleles[elm])
            try:
                temp = dic_ParB_alleles[elm]
                ParB.append(dic_alleles[elm])
            except:
                ParA.append(dic_alleles[elm])      
        except:
            # print("EXCEPT 1")
            # print(elm) 
            list_paralog.append(elm)
            hyb.append(elm)
        # print("-----Values: ")
        for val in dic_paralog[elm]:
            nb+=1
            try:
                # print("TRY 2")
                # print(dic_alleles[val])
                list_paralog.append(dic_alleles[val])
                try:
                    temp = dic_ParB_alleles[val]
                    ParB.append(dic_alleles[val])                    
                except:
                    ParA.append(dic_alleles[val]) 
            except:
                # print("EXCEPT 2")
                # print(val) 
                list_paralog.append(val)
                hyb.append(val)
        # print(list_paralog)
        # print(hyb)
        # print(ParB)
        # print(ParA)
        output_paralog.write("; ".join(list_paralog)+"\t"+ "; ".join(ParB) + "\t" + "; ".join(hyb) + "\t" + "; ".join(ParA) + "\n")        
                
               