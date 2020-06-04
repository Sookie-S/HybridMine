#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Soukaina Timouma"
__credits__ = ["Soukaina Timouma", "Daniela Delneri", "Jean-Marc Schwartz"]
__version__ = "1.0.1"
__maintainer__ = "Soukaina Timouma"
__email__ = "soukaina.timouma@manchester.ac.uk"

"""
Created on Wed Oct 30 18:06:29 2019
"""

hybrid = "hybrid"
parentA = "parentA"
parentB = "parentB"


identity_file_ParentA = "../Results/2_Best_hits/"+str(hybrid)+"-"+str(parentA)+".csv"
identity_file_ParentB = "../Results/2_Best_hits/"+str(hybrid)+"-"+str(parentB)+".csv"
identity_file_ParentA_bis = "../Results/2_Best_hits/"+str(parentA)+"-"+str(hybrid)+".csv"
identity_file_ParentB_bis = "../Results/2_Best_hits/"+str(parentB)+"-"+str(hybrid)+".csv"

orthoParentA = "../Results/3_Orthologs_Paralogs/"+str(hybrid)+"_"+str(parentA)+"_orthologies.csv"
orthoParentB = "../Results/3_Orthologs_Paralogs/"+str(hybrid)+"_"+str(parentB)+"_orthologies.csv"


dic_ortho_sc_ParentA = {}
dic_ortho_sc_ParentB = {}
dic_identities_sc_ParentA = {}
dic_identities_sc_ParentB = {}

x = 0
with open(orthoParentA, "r") as orthoParentA, open(orthoParentB, "r") as orthoParentB:
    #print("\n----Hybrid - Parent A file")
    linePA = orthoParentA.readline().rstrip() #Line 0 = title
    #print("\n----Hybrid - Parent B file")
    linePB = orthoParentB.readline().rstrip() #Line 0 = title
    linePA = orthoParentA.readline().rstrip() #Line 1
    linePB = orthoParentB.readline().rstrip() #Line 1
    
    while(linePA):
        
        # print("--------------\n\n")
        # print(linePA)

        p_sc = linePA.split(',')
        # print(p_sc)
        p1_sc = p_sc[0]
        # print(p1_sc)
        p2_sc = p_sc[1]
        # print(p2_sc)
        dic_ortho_sc_ParentA[p1_sc] = p2_sc
        x+=1
        linePA = orthoParentA.readline().rstrip() #Line 1  

    while(linePB):
        # print("--------------\n\n")
        # print(linePB)
        p_se = linePB.split(',')
        # print(p_se)
        p1_se = p_se[0]
        # print(p1_se)
        p2_se = p_se[1]
        # print(p2_se)    
        dic_ortho_sc_ParentB[p1_se] = p2_se
        linePB = orthoParentB.readline().rstrip() #Line 1


with open(identity_file_ParentA, "r") as identity_file_ParentA, open(identity_file_ParentB, "r") as identity_file_ParentB, open(identity_file_ParentA_bis, "r") as identity_file_ParentA_bis, open(identity_file_ParentB_bis, "r") as identity_file_ParentB_bis:
    line_id_Sc = identity_file_ParentA.readline().rstrip() #Line 0 = title
    # print(line_id_Sc)
    line_id_Sc = identity_file_ParentA.readline().rstrip() #Line 1
    # print(line_id_Sc)

    line_id_Se = identity_file_ParentB.readline().rstrip() #Line 0 = title
    # print(line_id_Se)
    line_id_Se = identity_file_ParentB.readline().rstrip() #Line 1
    # print(line_id_Se)

    line_id_Sc_bis = identity_file_ParentA_bis.readline().rstrip() #Line 0 = title
    # print(line_id_Sc_bis)
    line_id_Sc_bis = identity_file_ParentA_bis.readline().rstrip() #Line 1
    # print(line_id_Sc_bis)

    line_id_Se_bis = identity_file_ParentB_bis.readline().rstrip() #Line 0 = title
    # print(line_id_Se_bis)
    line_id_Se_bis = identity_file_ParentB_bis.readline().rstrip() #Line 1
    # print(line_id_Se_bis)    
    
    while(line_id_Sc):
        # print(line_id_Sc)
        line_id_Sc = line_id_Sc.split(',')
        # print("\nTEST")
        name_sc = line_id_Sc[0].split(".")[1]
        # print(name_sc)
        ortho_sc = line_id_Sc[1].split(".")[1]
        # print(ortho_sc)      
        id_sc = int(line_id_Sc[3])
        # print(id_sc)
        gap_sc = int(line_id_Sc[4])
        # print(gap_sc)    
        
        dic_identities_sc_ParentA[name_sc] = {"Ortholog" :ortho_sc, "identities" : id_sc, "gaps" : gap_sc }
        line_id_Sc = identity_file_ParentA.readline().rstrip() 
    
    while(line_id_Se):

        line_id_Se = line_id_Se.split(',')
        name_se = line_id_Se[0].split(".")[1]
        # print(name_se)
        ortho_se = line_id_Se[1].split(".",1)[1]
        # print(ortho_se)
        id_se = int(line_id_Se[3])
        # print(id_se)
        gap_se = int(line_id_Se[4])
        # print(gap_se)    
        dic_identities_sc_ParentB[name_se] = {"Ortholog" :ortho_se, "identities" : id_se, "gaps" : gap_se }
        line_id_Se = identity_file_ParentB.readline().rstrip() 
        
    while(line_id_Sc_bis):
        # print(line_id_Sc_bis)
        line_id_Sc_bis = line_id_Sc_bis.split(',')
        # print("\nTEST")
        name_sc_bis = line_id_Sc_bis[0].split(".")[1]
        # print(name_sc_bis)
        ortho_sc_bis = line_id_Sc_bis[1].split(".")[1]
        # print(ortho_sc_bis)      
        id_sc_bis = int(line_id_Sc_bis[3])
        # print(id_sc_bis)
        gap_sc_bis = int(line_id_Sc_bis[4])
        # print(gap_sc_bis)    
        
        dic_identities_sc_ParentA[name_sc_bis] = {"Ortholog" :ortho_sc_bis, "identities" : id_sc_bis, "gaps" : gap_sc_bis }
        line_id_Sc_bis = identity_file_ParentA_bis.readline().rstrip() 
    
    while(line_id_Se_bis):
        line_id_Se_bis = line_id_Se_bis.split(',')
        name_se_bis = line_id_Se_bis[0].split(".")[1]
        # print(name_se_bis)
        ortho_se_bis = line_id_Se_bis[1].split(".",1)[1]
        # print(ortho_se_bis)
        id_se_bis = int(line_id_Se_bis[3])
        # print(id_se_bis)
        gap_se_bis = int(line_id_Se_bis[4])
        # print(gap_se_bis)    
        dic_identities_sc_ParentB[name_se_bis] = {"Ortholog" :ortho_se_bis, "identities" : id_se_bis, "gaps" : gap_se_bis }
        line_id_Se_bis = identity_file_ParentB_bis.readline().rstrip() 
    

x = 0
liste_p_hybrid = []

threshold = 80


with open("../Results/4_Parental_alleles_prediction/genes_inherited_from_"+str(parentA)+".csv","w") as output_Sc,  open("../Results/4_Parental_alleles_prediction/genes_inherited_from_"+str(parentB)+".csv","w") as output_Se,  open("../Results/4_Parental_alleles_prediction/identical_alleles_in_"+str(parentA)+"_AND_"+str(parentB)+".csv","w") as output_ScSe, open("../Results/4_Parental_alleles_prediction/potential_parental_alleles_less_80_percent_identity.csv","w") as output_dodgy:   
    output_Sc.write("Hybrid" + ',' + str(parentA)+"_ortholog" + ',' + "gene_identities" + ',' + "gene_gaps" + '\n')
    output_Se.write("Hybrid" + ',' + str(parentB)+"_ortholog" + ',' + "gene_identities" + ',' + "gene_gaps" + '\n')
    output_ScSe.write("Hybrid" + ',' + "Ortholog_ID" + ',' + "gene_identities" + ',' + "gene_gaps" + '\n')
    output_dodgy.write("Hybrid" + ',' + "Ortholog_ID" + ',' + "gene_identities" + ',' + "gene_gaps" + '\n')
   
    
    for k,v in dic_ortho_sc_ParentA.items():
    
        if k in dic_ortho_sc_ParentB.keys():
#            print("1:1 ortholog in Parent A and Parent B")
#            
#            print(k,v)
#            print(k,dic_ortho_sc_ParentB[k])
#            
#            print(dic_identities_sc_ParentA[k])
#            print(dic_identities_sc_ParentB[k])
#            
#            
#            print("trial")
#            print(dic_identities_sc_ParentA[k]['Ortholog'])
#            print(dic_identities_sc_ParentA[k]['identities'])
#            print(dic_identities_sc_ParentA[k]['positives'])
#            print(dic_identities_sc_ParentA[k]['gaps'])
#            
#            print(dic_identities_sc_ParentB[k]['Ortholog'])
#            print(dic_identities_sc_ParentB[k]['identities'])
#            print(dic_identities_sc_ParentB[k]['positives'])
#            print(dic_identities_sc_ParentB[k]['gaps'])
#            
#            
#            if int(dic_identities_sc_ParentA[k]['identities']) < 80 :
#               print("\nDODGY: "+str(k))
#               print(dic_identities_sc_ParentA[k]['Ortholog'])
#               print(dic_identities_sc_ParentA[k]['identities'])

                
            if int(dic_identities_sc_ParentA[k]['identities']) > int(dic_identities_sc_ParentB[k]['identities']):
                if int(dic_identities_sc_ParentA[k]['identities']) >= int(threshold):
                    # print("Parent A allele")
                    output_Sc.write(str(k) + ',' + str(dic_identities_sc_ParentA[k]['Ortholog']) + ',' + str(dic_identities_sc_ParentA[k]['identities']) + 
                                    ','  + str(dic_identities_sc_ParentA[k]['gaps']) + '\n')
                    x+=1
                else:
                    output_dodgy.write(str(k) + ',' + str(dic_identities_sc_ParentA[k]['Ortholog']) + ',' + str(dic_identities_sc_ParentA[k]['identities']) + 
                                    ','  + str(dic_identities_sc_ParentA[k]['gaps']) + '\n')
                    x+=1
                    
            elif int(dic_identities_sc_ParentA[k]['identities']) < int(dic_identities_sc_ParentB[k]['identities']):
                if int(dic_identities_sc_ParentB[k]['identities']) >= int(threshold):
                    # print("Parent B allele")
                    output_Se.write(str(k) + ',' + str(dic_identities_sc_ParentB[k]['Ortholog']) + ',' + str(dic_identities_sc_ParentB[k]['identities']) + 
                                    ','  + str(dic_identities_sc_ParentB[k]['gaps']) + '\n')
                    x+=1
                else:
                    output_dodgy.write(str(k) + ',' + str(dic_identities_sc_ParentB[k]['Ortholog']) + ',' + str(dic_identities_sc_ParentB[k]['identities']) + 
                                    ','  + str(dic_identities_sc_ParentB[k]['gaps']) + '\n')
                    x+=1
               
            else:
                # print("Same copy in Parent A and Parent B")
                output_ScSe.write(str(k) + ',' + str(dic_identities_sc_ParentA[k]['Ortholog']) + ',' + str(dic_identities_sc_ParentA[k]['identities']) + 
                                ','  + str(dic_identities_sc_ParentA[k]['gaps']) + '\n')
                output_ScSe.write(str(k) + ',' + str(dic_identities_sc_ParentB[k]['Ortholog']) + ',' + str(dic_identities_sc_ParentB[k]['identities']) + 
                                ','  + str(dic_identities_sc_ParentB[k]['gaps']) + '\n')
                  
                x+=1
                
            
        else: # if key not in dic Se
            if int(dic_identities_sc_ParentA[k]['identities']) >= int(threshold):
                output_Sc.write(str(k) + ',' + str(dic_identities_sc_ParentA[k]['Ortholog']) + ',' + str(dic_identities_sc_ParentA[k]['identities']) + 
                                ','  + str(dic_identities_sc_ParentA[k]['gaps']) + '\n')
                x+=1
            else:
                output_dodgy.write(str(k) + ',' + str(dic_identities_sc_ParentA[k]['Ortholog']) + ',' + str(dic_identities_sc_ParentA[k]['identities']) + 
                                ','  + str(dic_identities_sc_ParentA[k]['gaps']) + '\n')
                x+=1
                    
        liste_p_hybrid.append(k)
#    
#    
    for k,v in dic_ortho_sc_ParentB.items():
        if k not in liste_p_hybrid:
            
            
#            if int(dic_identities_sc_ParentB[k]['identities']) < 80 :
#               print("\nDODGY: "+str(k))
#               print(dic_identities_sc_ParentB[k]['Ortholog'])
#               print(dic_identities_sc_ParentB[k]['identities'])
               
            if k in dic_ortho_sc_ParentA.keys():
                   
                # print("1:1 ortholog in Parent A and Parent B")
                
                # print(k,v)
                # print(k,dic_ortho_sc_ParentB[k])
                
                # print(dic_identities_sc_ParentA[k])
                # print(dic_identities_sc_ParentB[k])
                
                
                # print("trial")
                # print(dic_identities_sc_ParentA[k]['Ortholog'])
                # print(dic_identities_sc_ParentA[k]['identities'])
                # print(dic_identities_sc_ParentA[k]['positives'])
                # print(dic_identities_sc_ParentA[k]['gaps'])
                
                # print(dic_identities_sc_ParentB[k]['Ortholog'])
                # print(dic_identities_sc_ParentB[k]['identities'])
                # print(dic_identities_sc_ParentB[k]['positives'])
                # print(dic_identities_sc_ParentB[k]['gaps'])
                
                           
                if int(dic_identities_sc_ParentA[k]['identities']) > int(dic_identities_sc_ParentB[k]['identities']):
                    
                    if int(dic_identities_sc_ParentA[k]['identities']) >= int(threshold):
                        # print("Parent A allele")
                        output_Sc.write(str(k) + ',' + str(dic_identities_sc_ParentA[k]['Ortholog']) + ',' + str(dic_identities_sc_ParentA[k]['identities']) + 
                                        ','  + str(dic_identities_sc_ParentA[k]['gaps']) + '\n')
                        x+=1
                    else:
                        output_dodgy.write(str(k) + ',' + str(dic_identities_sc_ParentA[k]['Ortholog']) + ',' + str(dic_identities_sc_ParentA[k]['identities']) + 
                                        ','  + str(dic_identities_sc_ParentA[k]['gaps']) + '\n')
                        x+=1
                        
                elif int(dic_identities_sc_ParentA[k]['identities']) < int(dic_identities_sc_ParentB[k]['identities']):
                    if int(dic_identities_sc_ParentB[k]['identities']) >= threshold:
                        # print("Parent B allele")
                        output_Se.write(str(k) + ',' + str(dic_identities_sc_ParentB[k]['Ortholog']) + ',' + str(dic_identities_sc_ParentB[k]['identities']) + 
                                        ','  + str(dic_identities_sc_ParentB[k]['gaps']) + '\n')
                        x+=1
                    else:
                        output_dodgy.write(str(k) + ',' + str(dic_identities_sc_ParentB[k]['Ortholog']) + ',' + str(dic_identities_sc_ParentB[k]['identities']) + 
                                        ','  + str(dic_identities_sc_ParentB[k]['gaps']) + '\n')
                        x+=1
                   
                else:
                    # print("Same copy in Parent A and Parent B")
                    output_ScSe.write(str(k) + ',' + str(dic_identities_sc_ParentA[k]['Ortholog']) + ',' + str(dic_identities_sc_ParentA[k]['identities']) + 
                                    ','  + str(dic_identities_sc_ParentA[k]['gaps']) + '\n')
                    output_ScSe.write(str(k) + ',' + str(dic_identities_sc_ParentB[k]['Ortholog']) + ',' + str(dic_identities_sc_ParentB[k]['identities']) + 
                                    ','  + str(dic_identities_sc_ParentB[k]['gaps']) + '\n')
                      
                    x+=1
                
            else: # key not in Sc
                if int(dic_identities_sc_ParentB[k]['identities']) >= threshold:
                    output_Se.write(str(k) + ',' + str(dic_identities_sc_ParentB[k]['Ortholog']) + ',' + str(dic_identities_sc_ParentB[k]['identities']) + 
                    ','  + str(dic_identities_sc_ParentB[k]['gaps']) + '\n')
                    x+=1
                    
                else:
                    output_dodgy.write(str(k) + ',' + str(dic_identities_sc_ParentB[k]['Ortholog']) + ',' + str(dic_identities_sc_ParentB[k]['identities']) + 
                                    ','  + str(dic_identities_sc_ParentB[k]['gaps']) + '\n')
                    x+=1    
                    
                    
            liste_p_hybrid.append(k)    
            


#%%       GROUPING PARALOGS      

dic_ParB_alleles = {}
dic_ParA_alleles = {}

with open("../Results/4_Parental_alleles_prediction/genes_inherited_from_"+str(parentA)+".csv", "r") as parentalA:
    for line in parentalA:
        line = line.split("\n")[0]
        line = line.split(",")
        # print(line)
        dic_ParA_alleles[line[0]] = line[1]

with open("../Results/4_Parental_alleles_prediction/genes_inherited_from_"+str(parentB)+".csv", "r") as parentalB:
    next(parentalB)
    for line in parentalB:
        line = line.split("\n")[0]
        line = line.split(",")
        # print(line)
        dic_ParB_alleles[line[0]] = line[1]
  
dic_alleles = {**dic_ParB_alleles, **dic_ParA_alleles}


dic_paralog = {}
list_paralog_already_processed = []

stop = 0
with open("../Results/2_Best_hits/"+str(hybrid)+"-"+str(hybrid)+".csv", "r") as hyb:
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
            

nb = 0
total = 0
list_paralog = []
with open("../Results/3_Orthologs_Paralogs/homologs_paralogs_"+str(hybrid)+".csv", "w") as output_paralog:
    output_paralog.write("Homologs_list"+"\t"+str(parentB)+"-like content"+"\t"+str(hybrid)+" content"+"\t"+str(parentA)+"-like content"+"\n") 
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
                
               