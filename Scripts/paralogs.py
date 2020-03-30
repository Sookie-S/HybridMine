#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

'''
Get a list of keys from dictionary which has the given value
'''

def getKeysByValue(dictOfElements, valueToFind):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] == valueToFind:
            listOfKeys.append(item[0])
    return  listOfKeys

#%%
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
        id1 = id1.split(str(hybrid_name)+".")[1]
        id2 = line[1]
        id2 = id2.split(str(hybrid_name)+".")[1]
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

#%%
        
dic_alleles = {**dic_ParB_alleles, **dic_ParA_alleles}

        
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
                
               
