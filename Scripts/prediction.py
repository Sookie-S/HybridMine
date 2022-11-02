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


import argparse

parser = argparse.ArgumentParser(description='nb')
parser.add_argument('--nb', required=True)
parser.add_argument('--fH', required=True)
parser.add_argument('--fA', required=True)
parser.add_argument('--fB', required=True)
parser.add_argument('--fC', required=False)
parser.add_argument('--fD', required=False)
parser.add_argument('--hyb', required=True)
parser.add_argument('--pA', required=True)
parser.add_argument('--pB', required=True)
parser.add_argument('--pC', required=False)
parser.add_argument('--pD', required=False)

args = parser.parse_args()
nb = args.nb
total_hyb_genes = args.hyb
total_pA_genes = args.pA
total_pB_genes = args.pB
global number
number = nb



if nb == "2":
    
    hybrid = args.fH
    parentA = args.fA
    parentB = args.fB

    identity_file_ParentA = "../Results/2_Best_hits/"+str(hybrid)+"-"+str(parentA)+".csv"
    identity_file_ParentB = "../Results/2_Best_hits/"+str(hybrid)+"-"+str(parentB)+".csv"
    identity_file_ParentA_bis = "../Results/2_Best_hits/"+str(parentA)+"-"+str(hybrid)+".csv"
    identity_file_ParentB_bis = "../Results/2_Best_hits/"+str(parentB)+"-"+str(hybrid)+".csv"
    orthoParentA = "../Results/3_Orthologs_Paralogs/"+str(hybrid)+"_"+str(parentA)+"_orthologies.csv"
    orthoParentB = "../Results/3_Orthologs_Paralogs/"+str(hybrid)+"_"+str(parentB)+"_orthologies.csv"

    dic_ortho_ParentA = {}
    dic_ortho_ParentB = {}
    dic_identities_ParentA = {}
    dic_identities_ParentB = {}
    
    x = 0
    with open(orthoParentA, "r") as orthoParentA, open(orthoParentB, "r") as orthoParentB:
        linePA = orthoParentA.readline().rstrip() #Line 0 = title
        linePB = orthoParentB.readline().rstrip() #Line 0 = title
        linePA = orthoParentA.readline().rstrip() #Line 1
        linePB = orthoParentB.readline().rstrip() #Line 1
        
        while(linePA):
            p_parentA = linePA.split(',')
            p1_ParentA = p_parentA[0]
            p2_ParentA = p_parentA[1]
            dic_ortho_ParentA[p1_ParentA] = p2_ParentA
            x+=1
            linePA = orthoParentA.readline().rstrip() #Line 1  
    
        while(linePB):
            p_parentB = linePB.split(',')
            p1_ParentB = p_parentB[0]
            p2_ParentB = p_parentB[1]
            dic_ortho_ParentB[p1_ParentB] = p2_ParentB
            linePB = orthoParentB.readline().rstrip() #Line 1
    
    
    with open(identity_file_ParentA, "r") as identity_file_ParentA, open(identity_file_ParentB, "r") as identity_file_ParentB, open(identity_file_ParentA_bis, "r") as identity_file_ParentA_bis, open(identity_file_ParentB_bis, "r") as identity_file_ParentB_bis:
        line_id_parentA = identity_file_ParentA.readline().rstrip() #Line 0 = title
        line_id_parentA = identity_file_ParentA.readline().rstrip() #Line 1
        line_id_parentB = identity_file_ParentB.readline().rstrip() #Line 0 = title
        line_id_parentB = identity_file_ParentB.readline().rstrip() #Line 1    
        line_id_parentA_bis = identity_file_ParentA_bis.readline().rstrip() #Line 0 = title
        line_id_parentA_bis = identity_file_ParentA_bis.readline().rstrip() #Line 1
        line_id_parentB_bis = identity_file_ParentB_bis.readline().rstrip() #Line 0 = title
        line_id_parentB_bis = identity_file_ParentB_bis.readline().rstrip() #Line 1
        
        while(line_id_parentA):
            line_id_parentA = line_id_parentA.split(',')
            name_ParentA = line_id_parentA[0].split(".")[1]
            ortho_ParentA = line_id_parentA[1].split(".")[1]
            id_parentA = int(line_id_parentA[3])
            gap_parentA = int(line_id_parentA[4])
            dic_identities_ParentA[name_ParentA] = {"Ortholog" :ortho_ParentA, "identities" : id_parentA, "gaps" : gap_parentA }
            line_id_parentA = identity_file_ParentA.readline().rstrip() 
        
        while(line_id_parentB):
            line_id_parentB = line_id_parentB.split(',')
            name_ParentB = line_id_parentB[0].split(".")[1]
            ortho_ParentB = line_id_parentB[1].split(".",1)[1]
            id_parentB = int(line_id_parentB[3])
            gap_parentB = int(line_id_parentB[4])
            dic_identities_ParentB[name_ParentB] = {"Ortholog" :ortho_ParentB, "identities" : id_parentB, "gaps" : gap_parentB }
            line_id_parentB = identity_file_ParentB.readline().rstrip() 
            
        while(line_id_parentA_bis):
            line_id_parentA_bis = line_id_parentA_bis.split(',')
            name_ParentA_bis = line_id_parentA_bis[0].split(".")[1]
            ortho_ParentA_bis = line_id_parentA_bis[1].split(".")[1]
            id_parentA_bis = int(line_id_parentA_bis[3])
            gap_parentA_bis = int(line_id_parentA_bis[4])
            dic_identities_ParentA[name_ParentA_bis] = {"Ortholog" :ortho_ParentA_bis, "identities" : id_parentA_bis, "gaps" : gap_parentA_bis }
            line_id_parentA_bis = identity_file_ParentA_bis.readline().rstrip() 
        
        while(line_id_parentB_bis):
            line_id_parentB_bis = line_id_parentB_bis.split(',')
            name_ParentB_bis = line_id_parentB_bis[0].split(".")[1]
            ortho_ParentB_bis = line_id_parentB_bis[1].split(".",1)[1]
            id_parentB_bis = int(line_id_parentB_bis[3])
            gap_parentB_bis = int(line_id_parentB_bis[4])
            dic_identities_ParentB[name_ParentB_bis] = {"Ortholog" :ortho_ParentB_bis, "identities" : id_parentB_bis, "gaps" : gap_parentB_bis }
            line_id_parentB_bis = identity_file_ParentB_bis.readline().rstrip() 
        
    
    x = 0
    liste_p_hybrid = []
    threshold = 80

    with open("../Results/4_Parental_alleles_prediction/genes_inherited_from_"+str(parentA)+".csv","w") as output_ParentA,  open("../Results/4_Parental_alleles_prediction/genes_inherited_from_"+str(parentB)+".csv","w") as output_ParentB,  open("../Results/4_Parental_alleles_prediction/identical_alleles_in_"+str(parentA)+"_AND_"+str(parentB)+".csv","w") as output_ParentAParentB, open("../Results/4_Parental_alleles_prediction/potential_parental_alleles_less_80_percent_identity.csv","w") as output_dodgy:   
        output_ParentA.write("Hybrid" + ',' + str(parentA)+"_ortholog" + ',' + "gene_identities" + ',' + "gene_gaps" + '\n')
        output_ParentB.write("Hybrid" + ',' + str(parentB)+"_ortholog" + ',' + "gene_identities" + ',' + "gene_gaps" + '\n')
        output_ParentAParentB.write("Hybrid" + ',' + "Ortholog_ID" + ',' + "gene_identities" + ',' + "gene_gaps" + '\n')
        output_dodgy.write("Hybrid" + ',' + "Ortholog_ID" + ',' + "gene_identities" + ',' + "gene_gaps" + '\n')
       
        for k,v in dic_ortho_ParentA.items():
            if k in dic_ortho_ParentB.keys():

                if int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentB[k]['identities']):
                    if int(dic_identities_ParentA[k]['identities']) >= int(threshold):
                        output_ParentA.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                        ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                        x+=1
                    else:
                        output_dodgy.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                        ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                        x+=1
                        
                elif int(dic_identities_ParentA[k]['identities']) < int(dic_identities_ParentB[k]['identities']):
                    if int(dic_identities_ParentB[k]['identities']) >= int(threshold):
                        output_ParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                        ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                        x+=1
                    else:
                        output_dodgy.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                        ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                        x+=1
                   
                else:
                    output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                    ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                    output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                    ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                      
                    x+=1
                    
                
            else: # if key not in dic Se
                if int(dic_identities_ParentA[k]['identities']) >= int(threshold):
                    output_ParentA.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                    ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                    x+=1
                else:
                    output_dodgy.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                    ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                    x+=1
                        
            liste_p_hybrid.append(k)
    #    
    #    
        for k,v in dic_ortho_ParentB.items():
            if k not in liste_p_hybrid:
                if k in dic_ortho_ParentA.keys():

                    if int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentB[k]['identities']):
                        
                        if int(dic_identities_ParentA[k]['identities']) >= int(threshold):
                            output_ParentA.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                            ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                            ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                            x+=1
                            
                    elif int(dic_identities_ParentA[k]['identities']) < int(dic_identities_ParentB[k]['identities']):
                        if int(dic_identities_ParentB[k]['identities']) >= threshold:
                            output_ParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                            ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                            ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                            x+=1
                       
                    else:
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                        ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                        ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                          
                        x+=1
                    
                else: # key not in Sc
                    if int(dic_identities_ParentB[k]['identities']) >= threshold:
                        output_ParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                        ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                        x+=1
                        
                    else:
                        output_dodgy.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                        ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                        x+=1    

                liste_p_hybrid.append(k)    

    
    ###########      GROUPING PARALOGS ###############
    
    dic_ParB_alleles = {}
    dic_ParA_alleles = {}
    
    count_alleleA = 0
    count_alleleB = 0

    with open("../Results/4_Parental_alleles_prediction/genes_inherited_from_"+str(parentA)+".csv", "r") as parentalA:
        for line in parentalA:
            line = line.split("\n")[0]
            line = line.split(",")
            dic_ParA_alleles[line[0]] = line[1]
            count_alleleA+=1
    
    with open("../Results/4_Parental_alleles_prediction/genes_inherited_from_"+str(parentB)+".csv", "r") as parentalB:
        next(parentalB)
        for line in parentalB:
            line = line.split("\n")[0]
            line = line.split(",")
            dic_ParB_alleles[line[0]] = line[1]
            count_alleleB+=1
    dic_alleles = {**dic_ParB_alleles, **dic_ParA_alleles}
    
    
    with open("../Results/4_Parental_alleles_prediction/rank.txt", "w") as out:
        out.write("Total number of genes in the hybrid genome: "+str(total_hyb_genes))
        out.write("\nTotal number of genes in the Parent A genome: "+str(total_pA_genes))
        out.write("\nTotal number of genes in the Parent B genome: "+str(total_pB_genes))
        out.write("\nPredicted ParentA-like genes in the hybrid genome: "+str(count_alleleA)+" (~"+str((float(count_alleleA)*100)/float(total_hyb_genes))+"% of the hybrid genome)")
        out.write("\nPredicted ParentB-like genes in the hybrid genome: "+str(count_alleleB)+" (~"+str((float(count_alleleB)*100)/float(total_hyb_genes))+"% of the hybrid genome)")
    
    dic_paralog = {}
    list_paralog_already_processed = []
    
    stop = 0
    with open("../Results/1_Raw_Blast_output/output_blastn_hybrid_vs_hybrid.txt", "r") as hyb:
        next(hyb)
        list_done = []
        for line in hyb:
            stop+=1
            line = line.split("\n")[0]
            line = line.split("\t")
            id1 = line[0]
            id2 = line[1]
            
            
            if id1 == id2:
                continue
            elif id1 in list_done:
                continue
            else:
                list_done.append(id1)
                if (id1 not in list_paralog_already_processed) and (id2 not in list_paralog_already_processed): # new dict[id1] = id2
                    dic_paralog[id1] = [id2]
                    list_paralog_already_processed.append(id1)
                    list_paralog_already_processed.append(id2)

                          
                elif (id1 in list_paralog_already_processed) and (id2 not in list_paralog_already_processed): # dict[id1] = append id2
                    try:
                        dic_paralog[id1].append(id2)
                        list_paralog_already_processed.append(id2)
                        
                    except:
                        try: 
                            for elm in dic_paralog:
                                for val in dic_paralog[elm]:
                                    if val == str(id1):
                                        dic_paralog[elm].append(id2)
                                        list_paralog_already_processed.append(id2)                            
                        except:
                            pass
                            
                elif id1 not in list_paralog_already_processed and id2 in list_paralog_already_processed: # dict[id1] = append id2
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
                            
                elif id1 in list_paralog_already_processed and id2 in list_paralog_already_processed:
                    pass                    
        
                else:
                    pass
                    
    
    nb = 0
    total = 0
    list_paralog = []
    with open("../Results/3_Orthologs_Paralogs/homologs_paralogs_"+str(hybrid)+".csv", "w") as output_paralog:
        output_paralog.write("Homologs_list"+"\t"+str(parentB)+"-like content"+"\t"+str(hybrid)+" content"+"\t"+str(parentA)+"-like content"+"\n") 
        for elm in dic_paralog:
            total += 1
            list_paralog = []
            hyb = []
            ParA = []
            ParB = []
            try:
                list_paralog.append(dic_alleles[elm])
                try:
                    temp = dic_ParB_alleles[elm]
                    ParB.append(dic_alleles[elm])
                except:
                    ParA.append(dic_alleles[elm])      
            except:
                list_paralog.append(elm)
                hyb.append(elm)
            for val in dic_paralog[elm]:
                nb+=1
                try:
                    list_paralog.append(dic_alleles[val])
                    try:
                        temp = dic_ParB_alleles[val]
                        ParB.append(dic_alleles[val])                    
                    except:
                        ParA.append(dic_alleles[val]) 
                except:
                    list_paralog.append(val)
                    hyb.append(val)
            output_paralog.write("; ".join(list_paralog)+"\t"+ "; ".join(ParB) + "\t" + "; ".join(hyb) + "\t" + "; ".join(ParA) + "\n")        
                    



elif nb == "3":
    total_pC_genes = args.pC
    
    hybrid = args.fH
    parentA = args.fA
    parentB = args.fB
    parentC = args.fC
    
    identity_file_ParentA = "../Results/2_Best_hits/"+str(hybrid)+"-"+str(parentA)+".csv"
    identity_file_ParentB = "../Results/2_Best_hits/"+str(hybrid)+"-"+str(parentB)+".csv"
    identity_file_ParentC = "../Results/2_Best_hits/"+str(hybrid)+"-"+str(parentC)+".csv"
    identity_file_ParentA_bis = "../Results/2_Best_hits/"+str(parentA)+"-"+str(hybrid)+".csv"
    identity_file_ParentB_bis = "../Results/2_Best_hits/"+str(parentB)+"-"+str(hybrid)+".csv"
    identity_file_ParentC_bis = "../Results/2_Best_hits/"+str(parentC)+"-"+str(hybrid)+".csv"
    orthoParentA = "../Results/3_Orthologs_Paralogs/"+str(hybrid)+"_"+str(parentA)+"_orthologies.csv"
    orthoParentB = "../Results/3_Orthologs_Paralogs/"+str(hybrid)+"_"+str(parentB)+"_orthologies.csv"
    orthoParentC = "../Results/3_Orthologs_Paralogs/"+str(hybrid)+"_"+str(parentC)+"_orthologies.csv"
    
    
    dic_ortho_ParentA = {}
    dic_ortho_ParentB = {}
    dic_ortho_ParentC = {}
    dic_identities_ParentA = {}
    dic_identities_ParentB = {}
    dic_identities_ParentC = {}
 
    x = 0
    with open(orthoParentA, "r") as orthoParentA, open(orthoParentB, "r") as orthoParentB, open(orthoParentC, "r") as orthoParentC:
        linePA = orthoParentA.readline().rstrip() #Line 0 = title
        linePB = orthoParentB.readline().rstrip() #Line 0 = title
        linePC = orthoParentC.readline().rstrip() #Line 0 = title
        
        linePA = orthoParentA.readline().rstrip() #Line 1
        linePB = orthoParentB.readline().rstrip() #Line 1
        linePC = orthoParentC.readline().rstrip() #Line 1
        
        while(linePA):
            p_parentA = linePA.split(',')
            p1_ParentA = p_parentA[0]
            p2_ParentA = p_parentA[1]
            dic_ortho_ParentA[p1_ParentA] = p2_ParentA
            x+=1
            linePA = orthoParentA.readline().rstrip() #Line 1  
    
        while(linePB):
            p_parentB = linePB.split(',')
            p1_ParentB = p_parentB[0]
            p2_ParentB = p_parentB[1]
            dic_ortho_ParentB[p1_ParentB] = p2_ParentB
            linePB = orthoParentB.readline().rstrip() #Line 1
            
        while(linePC):
            p_parentC = linePC.split(',')
            p1_ParentC = p_parentC[0]
            p2_ParentC = p_parentC[1]
            dic_ortho_ParentC[p1_ParentC] = p2_ParentC
            linePC = orthoParentC.readline().rstrip() #Line 1
        
    
    with open(identity_file_ParentA, "r") as identity_file_ParentA, open(identity_file_ParentB, "r") as identity_file_ParentB, open(identity_file_ParentC, "r") as identity_file_ParentC, open(identity_file_ParentA_bis, "r") as identity_file_ParentA_bis, open(identity_file_ParentB_bis, "r") as identity_file_ParentB_bis, open(identity_file_ParentC_bis, "r") as identity_file_ParentC_bis:
        line_id_parentA = identity_file_ParentA.readline().rstrip() #Line 0 = title
        line_id_parentA = identity_file_ParentA.readline().rstrip() #Line 1
        line_id_parentB = identity_file_ParentB.readline().rstrip() #Line 0 = title
        line_id_parentB = identity_file_ParentB.readline().rstrip() #Line 1
        line_id_parentC = identity_file_ParentC.readline().rstrip() #Line 0 = title
        line_id_parentC = identity_file_ParentC.readline().rstrip() #Line 1
        line_id_parentA_bis = identity_file_ParentA_bis.readline().rstrip() #Line 0 = title
        line_id_parentA_bis = identity_file_ParentA_bis.readline().rstrip() #Line 1
        line_id_parentB_bis = identity_file_ParentB_bis.readline().rstrip() #Line 0 = title
        line_id_parentB_bis = identity_file_ParentB_bis.readline().rstrip() #Line 1
        line_id_parentC_bis = identity_file_ParentC_bis.readline().rstrip() #Line 0 = title
        line_id_parentC_bis = identity_file_ParentC_bis.readline().rstrip() #Line 1

        
        while(line_id_parentA):
            line_id_parentA = line_id_parentA.split(',')
            name_ParentA = line_id_parentA[0].split(".")[1]
            ortho_ParentA = line_id_parentA[1].split(".")[1]
            id_parentA = int(line_id_parentA[3])
            gap_parentA = int(line_id_parentA[4])            
            dic_identities_ParentA[name_ParentA] = {"Ortholog" :ortho_ParentA, "identities" : id_parentA, "gaps" : gap_parentA }
            line_id_parentA = identity_file_ParentA.readline().rstrip() 
        
        while(line_id_parentB):
            line_id_parentB = line_id_parentB.split(',')
            name_ParentB = line_id_parentB[0].split(".")[1]
            ortho_ParentB = line_id_parentB[1].split(".",1)[1]
            id_parentB = int(line_id_parentB[3])
            gap_parentB = int(line_id_parentB[4])
            dic_identities_ParentB[name_ParentB] = {"Ortholog" :ortho_ParentB, "identities" : id_parentB, "gaps" : gap_parentB }
            line_id_parentB = identity_file_ParentB.readline().rstrip() 
            
        while(line_id_parentC):
            line_id_parentC = line_id_parentC.split(',')
            name_ParentC = line_id_parentC[0].split(".")[1]
            ortho_ParentC = line_id_parentC[1].split(".",1)[1]
            id_parentC = int(line_id_parentC[3])
            gap_parentC = int(line_id_parentC[4])
            dic_identities_ParentC[name_ParentC] = {"Ortholog" :ortho_ParentC, "identities" : id_parentC, "gaps" : gap_parentC }
            line_id_parentC = identity_file_ParentC.readline().rstrip() 
                        
            
        while(line_id_parentA_bis):
            line_id_parentA_bis = line_id_parentA_bis.split(',')
            name_ParentA_bis = line_id_parentA_bis[0].split(".")[1]
            ortho_ParentA_bis = line_id_parentA_bis[1].split(".")[1]
            id_parentA_bis = int(line_id_parentA_bis[3])
            gap_parentA_bis = int(line_id_parentA_bis[4])            
            dic_identities_ParentA[name_ParentA_bis] = {"Ortholog" :ortho_ParentA_bis, "identities" : id_parentA_bis, "gaps" : gap_parentA_bis }
            line_id_parentA_bis = identity_file_ParentA_bis.readline().rstrip() 
        
        while(line_id_parentB_bis):
            line_id_parentB_bis = line_id_parentB_bis.split(',')
            name_ParentB_bis = line_id_parentB_bis[0].split(".")[1]
            ortho_ParentB_bis = line_id_parentB_bis[1].split(".",1)[1]
            id_parentB_bis = int(line_id_parentB_bis[3])
            gap_parentB_bis = int(line_id_parentB_bis[4])
            dic_identities_ParentB[name_ParentB_bis] = {"Ortholog" :ortho_ParentB_bis, "identities" : id_parentB_bis, "gaps" : gap_parentB_bis }
            line_id_parentB_bis = identity_file_ParentB_bis.readline().rstrip() 
            
        while(line_id_parentC_bis):
            line_id_parentC_bis = line_id_parentC_bis.split(',')
            name_ParentC_bis = line_id_parentC_bis[0].split(".")[1]
            ortho_ParentC_bis = line_id_parentC_bis[1].split(".",1)[1]
            id_parentC_bis = int(line_id_parentC_bis[3])
            gap_parentC_bis = int(line_id_parentC_bis[4])
            dic_identities_ParentC[name_ParentC_bis] = {"Ortholog" :ortho_ParentC_bis, "identities" : id_parentC_bis, "gaps" : gap_parentC_bis }
            line_id_parentC_bis = identity_file_ParentC_bis.readline().rstrip() 
                
    
    x = 0
    liste_p_hybrid = []
    
    threshold = 80
    
    
    with open("../Results/4_Parental_alleles_prediction/genes_inherited_from_"+str(parentA)+".csv","w") as output_ParentA,  open("../Results/4_Parental_alleles_prediction/genes_inherited_from_"+str(parentB)+".csv","w") as output_ParentB,  open("../Results/4_Parental_alleles_prediction/genes_inherited_from_"+str(parentC)+".csv","w") as output_ParentC,  open("../Results/4_Parental_alleles_prediction/identical_alleles_in_"+str(parentA)+"_AND_"+str(parentB)+"_AND_"+str(parentC)+".csv","w") as output_ParentAParentB, open("../Results/4_Parental_alleles_prediction/potential_parental_alleles_less_80_percent_identity.csv","w") as output_dodgy:   
        output_ParentA.write("Hybrid" + ',' + str(parentA)+"_ortholog" + ',' + "gene_identities" + ',' + "gene_gaps" + '\n')
        output_ParentB.write("Hybrid" + ',' + str(parentB)+"_ortholog" + ',' + "gene_identities" + ',' + "gene_gaps" + '\n')
        output_ParentC.write("Hybrid" + ',' + str(parentC)+"_ortholog" + ',' + "gene_identities" + ',' + "gene_gaps" + '\n')
        output_ParentAParentB.write("Hybrid" + ',' + "Ortholog_ID" + ',' + "gene_identities" + ',' + "gene_gaps" + '\n')
        output_dodgy.write("Hybrid" + ',' + "Ortholog_ID" + ',' + "gene_identities" + ',' + "gene_gaps" + '\n')
        
        for k,v in dic_ortho_ParentA.items():
            
            if (k in dic_ortho_ParentB.keys()) and (k in dic_ortho_ParentC.keys()):  ## if in parent A and B and C
                if (int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentB[k]['identities'])) and (int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentC[k]['identities'])):
                    if int(dic_identities_ParentA[k]['identities']) >= int(threshold):
                        output_ParentA.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                        ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                        x+=1
                    else:
                        output_dodgy.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                        ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                        x+=1
                        
                elif (int(dic_identities_ParentB[k]['identities']) > int(dic_identities_ParentA[k]['identities'])) and (int(dic_identities_ParentB[k]['identities']) > int(dic_identities_ParentC[k]['identities'])):
                    if int(dic_identities_ParentB[k]['identities']) >= int(threshold):
                        output_ParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                        ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                        x+=1
                    else:
                        output_dodgy.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                        ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                        x+=1
                        
                elif (int(dic_identities_ParentC[k]['identities']) > int(dic_identities_ParentA[k]['identities'])) and (int(dic_identities_ParentC[k]['identities']) > int(dic_identities_ParentB[k]['identities'])):
                    if int(dic_identities_ParentC[k]['identities']) >= int(threshold):
                        output_ParentC.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                        ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                        x+=1
                    else:
                        output_dodgy.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                        ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                        x+=1
                   
                else:
                    # print("Same copy in Parent A and Parent B")
                    output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                    ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                    output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                    ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                    output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                    ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')                   
                    x+=1

            elif (k in dic_ortho_ParentB.keys()) and (k not in dic_ortho_ParentC.keys()):  ## if in parent A and B NOT C
                    
                if int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentB[k]['identities']):
                    if int(dic_identities_ParentA[k]['identities']) >= int(threshold):
                        output_ParentA.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                        ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                        x+=1
                    else:
                        output_dodgy.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                        ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                        x+=1
                        
                elif int(dic_identities_ParentA[k]['identities']) < int(dic_identities_ParentB[k]['identities']):
                    if int(dic_identities_ParentB[k]['identities']) >= int(threshold):
                        output_ParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                        ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                        x+=1
                    else:
                        output_dodgy.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                        ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                        x+=1
                   
                else:
                    # print("Same copy in Parent A and Parent B")
                    output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                    ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                    output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                    ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                      
                    x+=1       
                    
            elif (k in dic_ortho_ParentC.keys()) and (k not in dic_ortho_ParentB.keys()):  ## if in parent A and C NOT B
                    
                if int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentC[k]['identities']):
                    if int(dic_identities_ParentA[k]['identities']) >= int(threshold):
                        output_ParentA.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                        ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                        x+=1
                    else:
                        output_dodgy.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                        ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                        x+=1
                        
                elif int(dic_identities_ParentA[k]['identities']) < int(dic_identities_ParentC[k]['identities']):
                    if int(dic_identities_ParentC[k]['identities']) >= int(threshold):
                        output_ParentC.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                        ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                        x+=1
                    else:
                        output_dodgy.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                        ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                        x+=1
                   
                else:
                    # print("Same copy in Parent A and Parent C")
                    output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                    ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                    output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                    ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                      
                    x+=1                      
                    
            else: # if in Parent A not in B and not in C
                if int(dic_identities_ParentA[k]['identities']) >= int(threshold):
                    output_ParentA.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                    ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                    x+=1
                else:
                    output_dodgy.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                    ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                    x+=1
                        
            liste_p_hybrid.append(k)
            
            #############################################################
        for k,v in dic_ortho_ParentB.items():
            if k not in liste_p_hybrid:
                   
                if (k in dic_ortho_ParentA.keys()) and (k in dic_ortho_ParentC.keys()):  ## if in parent A and B and C:

                    if (int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentB[k]['identities'])) and (int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentC[k]['identities'])):
                        if int(dic_identities_ParentA[k]['identities']) >= int(threshold):
                            output_ParentA.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                            ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                            ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                            x+=1
                            
                    elif (int(dic_identities_ParentB[k]['identities']) > int(dic_identities_ParentA[k]['identities'])) and (int(dic_identities_ParentB[k]['identities']) > int(dic_identities_ParentC[k]['identities'])):
                        if int(dic_identities_ParentB[k]['identities']) >= int(threshold):
                            output_ParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                            ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                            ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                            x+=1
                            
                    elif (int(dic_identities_ParentC[k]['identities']) > int(dic_identities_ParentA[k]['identities'])) and (int(dic_identities_ParentC[k]['identities']) > int(dic_identities_ParentB[k]['identities'])):
                        if int(dic_identities_ParentC[k]['identities']) >= int(threshold):
                            output_ParentC.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                            ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                            ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                            x+=1
                       
                    else:
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                        ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                        ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                        ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')                   
                        x+=1
    
                elif (k in dic_ortho_ParentA.keys()) and (k not in dic_ortho_ParentC.keys()):  ## if in parent A and B NOT C
                        
                    if int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentB[k]['identities']):
                        if int(dic_identities_ParentA[k]['identities']) >= int(threshold):
                            output_ParentA.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                            ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                            ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                            x+=1
                            
                    elif int(dic_identities_ParentA[k]['identities']) < int(dic_identities_ParentB[k]['identities']):
                        if int(dic_identities_ParentB[k]['identities']) >= int(threshold):
                            output_ParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                            ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                            ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                            x+=1
                       
                    else:
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                        ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                        ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                          
                        x+=1       
                        
                elif (k in dic_ortho_ParentC.keys()) and (k not in dic_ortho_ParentA.keys()):  ## if in parent B and C NOT A
                        
                    if int(dic_identities_ParentB[k]['identities']) > int(dic_identities_ParentC[k]['identities']):
                        if int(dic_identities_ParentB[k]['identities']) >= int(threshold):
                            output_ParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                            ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                            ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                            x+=1
                            
                    elif int(dic_identities_ParentB[k]['identities']) < int(dic_identities_ParentC[k]['identities']):
                        if int(dic_identities_ParentC[k]['identities']) >= int(threshold):
                            output_ParentC.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                            ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                            ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                            x+=1
                       
                    else:
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                        ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                        ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                          
                        x+=1                      
                        
                else: # if in Parent B not in A and not in C
                    if int(dic_identities_ParentB[k]['identities']) >= int(threshold):
                        output_ParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                        ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                        x+=1
                    else:
                        output_dodgy.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                        ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                        x+=1

                liste_p_hybrid.append(k)   
                
                
        ############################################################
        for k,v in dic_ortho_ParentC.items():
            if k not in liste_p_hybrid:
                   
                if (k in dic_ortho_ParentA.keys()) and (k in dic_ortho_ParentB.keys()):  ## if in parent A and B and C:

                    if (int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentB[k]['identities'])) and (int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentC[k]['identities'])):
                        if int(dic_identities_ParentA[k]['identities']) >= int(threshold):
                            output_ParentA.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                            ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                            ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                            x+=1
                            
                    elif (int(dic_identities_ParentB[k]['identities']) > int(dic_identities_ParentA[k]['identities'])) and (int(dic_identities_ParentB[k]['identities']) > int(dic_identities_ParentC[k]['identities'])):
                        if int(dic_identities_ParentB[k]['identities']) >= int(threshold):
                            output_ParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                            ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                            ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                            x+=1
                            
                    elif (int(dic_identities_ParentC[k]['identities']) > int(dic_identities_ParentA[k]['identities'])) and (int(dic_identities_ParentC[k]['identities']) > int(dic_identities_ParentB[k]['identities'])):
                        if int(dic_identities_ParentC[k]['identities']) >= int(threshold):
                            output_ParentC.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                            ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                            ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                            x+=1
                       
                    else:
                        # print("Same copy in Parent A and Parent B")
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                        ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                        ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                        ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')                   
                        x+=1
    
                elif (k in dic_ortho_ParentA.keys()) and (k not in dic_ortho_ParentB.keys()):  ## if in parent A and C NOT B
                        
                    if int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentC[k]['identities']):
                        if int(dic_identities_ParentA[k]['identities']) >= int(threshold):
                            output_ParentA.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                            ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                            ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                            x+=1
                            
                    elif int(dic_identities_ParentA[k]['identities']) < int(dic_identities_ParentC[k]['identities']):
                        if int(dic_identities_ParentC[k]['identities']) >= int(threshold):
                            output_ParentC.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                            ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                            ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                            x+=1
                       
                    else:
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                        ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                        ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                          
                        x+=1       
                        
                elif (k in dic_ortho_ParentB.keys()) and (k not in dic_ortho_ParentA.keys()):  ## if in parent B and C NOT A
                        
                    if int(dic_identities_ParentB[k]['identities']) > int(dic_identities_ParentC[k]['identities']):
                        if int(dic_identities_ParentB[k]['identities']) >= int(threshold):
                            output_ParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                            ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                            ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                            x+=1
                            
                    elif int(dic_identities_ParentB[k]['identities']) < int(dic_identities_ParentC[k]['identities']):
                        if int(dic_identities_ParentC[k]['identities']) >= int(threshold):
                            output_ParentC.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                            ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                            ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                            x+=1
                       
                    else:
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                        ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                        ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                          
                        x+=1                      
                        
                else: # if in Parent C not in A and not in B
                    if int(dic_identities_ParentC[k]['identities']) >= int(threshold):
                        output_ParentC.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                        ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                        x+=1
                    else:
                        output_dodgy.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                        ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                        x+=1

                liste_p_hybrid.append(k)    

    #############################################################            
    
    
    #############################################################
    
    #      GROUPING PARALOGS      
    
    dic_ParA_alleles = {}
    dic_ParB_alleles = {}
    dic_ParC_alleles = {}
    
    count_alleleA = 0
    count_alleleB = 0
    count_alleleC = 0
    
    with open("../Results/4_Parental_alleles_prediction/genes_inherited_from_"+str(parentA)+".csv", "r") as parentalA:
        for line in parentalA:
            line = line.split("\n")[0]
            line = line.split(",")
            # print(line)
            dic_ParA_alleles[line[0]] = line[1]
            count_alleleA+=1
    
    with open("../Results/4_Parental_alleles_prediction/genes_inherited_from_"+str(parentB)+".csv", "r") as parentalB:
        next(parentalB)
        for line in parentalB:
            line = line.split("\n")[0]
            line = line.split(",")
            dic_ParB_alleles[line[0]] = line[1]
            count_alleleB+=1

    with open("../Results/4_Parental_alleles_prediction/genes_inherited_from_"+str(parentC)+".csv", "r") as parentalC:
        next(parentalC)
        for line in parentalC:
            line = line.split("\n")[0]
            line = line.split(",")
            dic_ParC_alleles[line[0]] = line[1]
            count_alleleC+=1
            
            
            
    with open("../Results/4_Parental_alleles_prediction/rank.txt", "w") as out:
        out.write("Total number of genes in the hybrid genome: "+str(total_hyb_genes))
        out.write("\nTotal number of genes in the Parent A genome: "+str(total_pA_genes))
        out.write("\nTotal number of genes in the Parent B genome: "+str(total_pB_genes))
        out.write("\nTotal number of genes in the Parent C genome: "+str(total_pC_genes))
        out.write("\nPredicted ParentA-like genes in the hybrid genome: "+str(count_alleleA)+" (~"+str((float(count_alleleA)*100)/float(total_hyb_genes))+"% of the hybrid genome)")
        out.write("\nPredicted ParentB-like genes in the hybrid genome: "+str(count_alleleB)+" (~"+str((float(count_alleleB)*100)/float(total_hyb_genes))+"% of the hybrid genome)")
        out.write("\nPredicted ParentC-like genes in the hybrid genome: "+str(count_alleleC)+" (~"+str((float(count_alleleC)*100)/float(total_hyb_genes))+"% of the hybrid genome)")
            
    dic_alleles = {**dic_ParB_alleles, **dic_ParA_alleles, **dic_ParC_alleles}
    
    
    dic_paralog = {}
    list_paralog_already_processed = []
    
    stop = 0
    with open("../Results/1_Raw_Blast_output/output_blastn_hybrid_vs_hybrid.txt", "r") as hyb:
        next(hyb)
        list_done = []
        for line in hyb:
            stop+=1
            line = line.split("\n")[0]
            line = line.split("\t")
            id1 = line[0]
            id2 = line[1]
            
            
            if id1 == id2:
                continue
            elif id1 in list_done:
                continue
            else:
                list_done.append(id1)
                if (id1 not in list_paralog_already_processed) and (id2 not in list_paralog_already_processed): # new dict[id1] = id2
                    dic_paralog[id1] = [id2]
                    list_paralog_already_processed.append(id1)
                    list_paralog_already_processed.append(id2)

                          
                elif (id1 in list_paralog_already_processed) and (id2 not in list_paralog_already_processed): # dict[id1] = append id2
                    try:
                        dic_paralog[id1].append(id2)
                        list_paralog_already_processed.append(id2)
                        
                    except:
                        try: 
                            for elm in dic_paralog:
                                for val in dic_paralog[elm]:
                                    if val == str(id1):
                                        dic_paralog[elm].append(id2)
                                        list_paralog_already_processed.append(id2)                            
                        except:
                            pass
                            
                elif id1 not in list_paralog_already_processed and id2 in list_paralog_already_processed: # dict[id1] = append id2
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
                            
                elif id1 in list_paralog_already_processed and id2 in list_paralog_already_processed:
                    pass                    
        
                else:
                    pass
                    
    
    nb = 0
    total = 0
    list_paralog = []
    with open("../Results/3_Orthologs_Paralogs/homologs_paralogs_"+str(hybrid)+".csv", "w") as output_paralog:
        output_paralog.write("Homologs_list"+"\t"+str(hybrid)+" content"+"\t"+str(parentA)+"-like content"+"\t"+str(parentB)+"-like content"+"\t"+str(parentC)+"-like content"+"\n") 
        for elm in dic_paralog:
            total += 1
    #        nb = 0
            list_paralog = []
            hyb = []
            ParA = []
            ParB = []
            ParC = []
            
            try:
                list_paralog.append(dic_alleles[elm])
                try:
                    ParB.append(dic_ParB_alleles[elm])
                except:
                    try:
                        ParA.append(dic_ParA_alleles[elm])   
                    except:
                        ParC.append(dic_ParC_alleles[elm])   
                        
            except:
                list_paralog.append(elm)
                hyb.append(elm)
            
            for val in dic_paralog[elm]:
                nb+=1
                try:
                    list_paralog.append(dic_alleles[val])
                    try:
                        ParB.append(dic_ParB_alleles[val])                    
                    except:
                        try:
                            ParA.append(dic_ParA_alleles[val]) 
                        except:
                            ParC.append(dic_ParC_alleles[val]) 
                except:
                    list_paralog.append(val)
                    hyb.append(val)
                    
            output_paralog.write("; ".join(list_paralog)+"\t"+ "; ".join(hyb) + "\t" + "; ".join(ParA) + "\t" + "; ".join(ParB) + "\t" + "; ".join(ParC) + "\n")        
                    



######

elif nb == "4":
    total_pC_genes = args.pC
    total_pD_genes = args.pD

    hybrid = args.fH
    parentA = args.fA
    parentB = args.fB
    parentC = args.fC
    parentD = args.fD
    
    identity_file_ParentA = "../Results/2_Best_hits/"+str(hybrid)+"-"+str(parentA)+".csv"
    identity_file_ParentB = "../Results/2_Best_hits/"+str(hybrid)+"-"+str(parentB)+".csv"
    identity_file_ParentC = "../Results/2_Best_hits/"+str(hybrid)+"-"+str(parentC)+".csv"
    identity_file_ParentD = "../Results/2_Best_hits/"+str(hybrid)+"-"+str(parentD)+".csv"
    identity_file_ParentA_bis = "../Results/2_Best_hits/"+str(parentA)+"-"+str(hybrid)+".csv"
    identity_file_ParentB_bis = "../Results/2_Best_hits/"+str(parentB)+"-"+str(hybrid)+".csv"
    identity_file_ParentC_bis = "../Results/2_Best_hits/"+str(parentC)+"-"+str(hybrid)+".csv"
    identity_file_ParentD_bis = "../Results/2_Best_hits/"+str(parentD)+"-"+str(hybrid)+".csv"

    orthoParentA = "../Results/3_Orthologs_Paralogs/"+str(hybrid)+"_"+str(parentA)+"_orthologies.csv"
    orthoParentB = "../Results/3_Orthologs_Paralogs/"+str(hybrid)+"_"+str(parentB)+"_orthologies.csv"
    orthoParentC = "../Results/3_Orthologs_Paralogs/"+str(hybrid)+"_"+str(parentC)+"_orthologies.csv"
    orthoParentD = "../Results/3_Orthologs_Paralogs/"+str(hybrid)+"_"+str(parentD)+"_orthologies.csv"
    
    
    dic_ortho_ParentA = {}
    dic_ortho_ParentB = {}
    dic_ortho_ParentC = {}
    dic_ortho_ParentD = {}
    dic_identities_ParentA = {}
    dic_identities_ParentB = {}
    dic_identities_ParentC = {}
    dic_identities_ParentD = {}

 
    x = 0
    with open(orthoParentA, "r") as orthoParentA, open(orthoParentB, "r") as orthoParentB, open(orthoParentC, "r") as orthoParentC, open(orthoParentD, "r") as orthoParentD:
        linePA = orthoParentA.readline().rstrip() #Line 0 = title
        linePB = orthoParentB.readline().rstrip() #Line 0 = title
        linePC = orthoParentC.readline().rstrip() #Line 0 = title
        linePD = orthoParentD.readline().rstrip() #Line 0 = title
        linePA = orthoParentA.readline().rstrip() #Line 1
        linePB = orthoParentB.readline().rstrip() #Line 1
        linePC = orthoParentC.readline().rstrip() #Line 1
        linePD = orthoParentD.readline().rstrip() #Line 1
        
        while(linePA):
            p_parentA = linePA.split(',')
            p1_ParentA = p_parentA[0]
            p2_ParentA = p_parentA[1]
            dic_ortho_ParentA[p1_ParentA] = p2_ParentA
            x+=1
            linePA = orthoParentA.readline().rstrip() #Line 1  
    
        while(linePB):
            p_parentB = linePB.split(',')
            p1_ParentB = p_parentB[0]
            p2_ParentB = p_parentB[1]
            dic_ortho_ParentB[p1_ParentB] = p2_ParentB
            linePB = orthoParentB.readline().rstrip() #Line 1
            
        while(linePC):
            p_parentC = linePC.split(',')
            p1_ParentC = p_parentC[0]
            p2_ParentC = p_parentC[1]
            dic_ortho_ParentC[p1_ParentC] = p2_ParentC
            linePC = orthoParentC.readline().rstrip() #Line 1
        
        while(linePD):
            p_parentD = linePD.split(',')
            p1_ParentD = p_parentD[0]
            p2_ParentD = p_parentD[1]
            dic_ortho_ParentD[p1_ParentD] = p2_ParentD
            linePD = orthoParentD.readline().rstrip() #Line 1
        
        
    with open(identity_file_ParentA, "r") as identity_file_ParentA, open(identity_file_ParentB, "r") as identity_file_ParentB, open(identity_file_ParentC, "r") as identity_file_ParentC, open(identity_file_ParentD, "r") as identity_file_ParentD, open(identity_file_ParentA_bis, "r") as identity_file_ParentA_bis, open(identity_file_ParentB_bis, "r") as identity_file_ParentB_bis, open(identity_file_ParentC_bis, "r") as identity_file_ParentC_bis, open(identity_file_ParentD_bis, "r") as identity_file_ParentD_bis:
        line_id_parentA = identity_file_ParentA.readline().rstrip() #Line 0 = title
        line_id_parentA = identity_file_ParentA.readline().rstrip() #Line 1
        line_id_parentB = identity_file_ParentB.readline().rstrip() #Line 0 = title
        line_id_parentB = identity_file_ParentB.readline().rstrip() #Line 1
        line_id_parentC = identity_file_ParentC.readline().rstrip() #Line 0 = title
        line_id_parentC = identity_file_ParentC.readline().rstrip() #Line 1
        line_id_parentD = identity_file_ParentD.readline().rstrip() #Line 0 = title
        line_id_parentD = identity_file_ParentD.readline().rstrip() #Line 1
        line_id_parentA_bis = identity_file_ParentA_bis.readline().rstrip() #Line 0 = title
        line_id_parentA_bis = identity_file_ParentA_bis.readline().rstrip() #Line 1
        line_id_parentB_bis = identity_file_ParentB_bis.readline().rstrip() #Line 0 = title
        line_id_parentB_bis = identity_file_ParentB_bis.readline().rstrip() #Line 1
        line_id_parentC_bis = identity_file_ParentC_bis.readline().rstrip() #Line 0 = title
        line_id_parentC_bis = identity_file_ParentC_bis.readline().rstrip() #Line 1
        line_id_parentD_bis = identity_file_ParentD_bis.readline().rstrip() #Line 0 = title
        line_id_parentD_bis = identity_file_ParentD_bis.readline().rstrip() #Line 1

        
        while(line_id_parentA):
            line_id_parentA = line_id_parentA.split(',')
            name_ParentA = line_id_parentA[0].split(".")[1]
            ortho_ParentA = line_id_parentA[1].split(".")[1]
            id_parentA = int(line_id_parentA[3])
            gap_parentA = int(line_id_parentA[4])            
            dic_identities_ParentA[name_ParentA] = {"Ortholog" :ortho_ParentA, "identities" : id_parentA, "gaps" : gap_parentA }
            line_id_parentA = identity_file_ParentA.readline().rstrip() 
        
        while(line_id_parentB):
            line_id_parentB = line_id_parentB.split(',')
            name_ParentB = line_id_parentB[0].split(".")[1]
            ortho_ParentB = line_id_parentB[1].split(".",1)[1]
            id_parentB = int(line_id_parentB[3])
            gap_parentB = int(line_id_parentB[4])
            dic_identities_ParentB[name_ParentB] = {"Ortholog" :ortho_ParentB, "identities" : id_parentB, "gaps" : gap_parentB }
            line_id_parentB = identity_file_ParentB.readline().rstrip() 
            
        while(line_id_parentC):
            line_id_parentC = line_id_parentC.split(',')
            name_ParentC = line_id_parentC[0].split(".")[1]
            ortho_ParentC = line_id_parentC[1].split(".",1)[1]
            id_parentC = int(line_id_parentC[3])
            gap_parentC = int(line_id_parentC[4])
            dic_identities_ParentC[name_ParentC] = {"Ortholog" :ortho_ParentC, "identities" : id_parentC, "gaps" : gap_parentC }
            line_id_parentC = identity_file_ParentC.readline().rstrip() 
                        
        while(line_id_parentD):
            line_id_parentD = line_id_parentD.split(',')
            name_ParentD = line_id_parentD[0].split(".")[1]
            ortho_ParentD = line_id_parentD[1].split(".",1)[1]
            id_parentD = int(line_id_parentD[3])
            gap_parentD = int(line_id_parentD[4])
            dic_identities_ParentD[name_ParentD] = {"Ortholog" :ortho_ParentD, "identities" : id_parentD, "gaps" : gap_parentD }
            line_id_parentD = identity_file_ParentD.readline().rstrip() 
                        
            
        while(line_id_parentA_bis):
            line_id_parentA_bis = line_id_parentA_bis.split(',')
            name_ParentA_bis = line_id_parentA_bis[0].split(".")[1]
            ortho_ParentA_bis = line_id_parentA_bis[1].split(".")[1]
            id_parentA_bis = int(line_id_parentA_bis[3])
            gap_parentA_bis = int(line_id_parentA_bis[4])            
            dic_identities_ParentA[name_ParentA_bis] = {"Ortholog" :ortho_ParentA_bis, "identities" : id_parentA_bis, "gaps" : gap_parentA_bis }
            line_id_parentA_bis = identity_file_ParentA_bis.readline().rstrip() 
        
        while(line_id_parentB_bis):
            line_id_parentB_bis = line_id_parentB_bis.split(',')
            name_ParentB_bis = line_id_parentB_bis[0].split(".")[1]
            ortho_ParentB_bis = line_id_parentB_bis[1].split(".",1)[1]
            id_parentB_bis = int(line_id_parentB_bis[3])
            gap_parentB_bis = int(line_id_parentB_bis[4])
            dic_identities_ParentB[name_ParentB_bis] = {"Ortholog" :ortho_ParentB_bis, "identities" : id_parentB_bis, "gaps" : gap_parentB_bis }
            line_id_parentB_bis = identity_file_ParentB_bis.readline().rstrip() 
            
        while(line_id_parentC_bis):
            line_id_parentC_bis = line_id_parentC_bis.split(',')
            name_ParentC_bis = line_id_parentC_bis[0].split(".")[1]
            ortho_ParentC_bis = line_id_parentC_bis[1].split(".",1)[1]
            id_parentC_bis = int(line_id_parentC_bis[3])
            gap_parentC_bis = int(line_id_parentC_bis[4])
            dic_identities_ParentC[name_ParentC_bis] = {"Ortholog" :ortho_ParentC_bis, "identities" : id_parentC_bis, "gaps" : gap_parentC_bis }
            line_id_parentC_bis = identity_file_ParentC_bis.readline().rstrip() 
                
        while(line_id_parentD_bis):
            line_id_parentD_bis = line_id_parentD_bis.split(',')
            name_ParentD_bis = line_id_parentD_bis[0].split(".")[1]
            ortho_ParentD_bis = line_id_parentD_bis[1].split(".",1)[1]
            id_parentD_bis = int(line_id_parentD_bis[3])
            gap_parentD_bis = int(line_id_parentD_bis[4])
            dic_identities_ParentD[name_ParentD_bis] = {"Ortholog" :ortho_ParentD_bis, "identities" : id_parentD_bis, "gaps" : gap_parentD_bis }
            line_id_parentD_bis = identity_file_ParentD_bis.readline().rstrip() 
                
    x = 0
    liste_p_hybrid = []
    
    threshold = 80
    
    
    with open("../Results/4_Parental_alleles_prediction/genes_inherited_from_"+str(parentA)+".csv","w") as output_ParentA,  open("../Results/4_Parental_alleles_prediction/genes_inherited_from_"+str(parentB)+".csv","w") as output_ParentB,  open("../Results/4_Parental_alleles_prediction/genes_inherited_from_"+str(parentC)+".csv","w") as output_ParentC,  open("../Results/4_Parental_alleles_prediction/genes_inherited_from_"+str(parentD)+".csv","w") as output_ParentD,  open("../Results/4_Parental_alleles_prediction/identical_alleles_in_"+str(parentA)+"_AND_"+str(parentB)+"_AND_"+str(parentC)+"_AND_"+str(parentD)+".csv","w") as output_ParentAParentB, open("../Results/4_Parental_alleles_prediction/potential_parental_alleles_less_80_percent_identity.csv","w") as output_dodgy:   
        output_ParentA.write("Hybrid" + ',' + str(parentA)+"_ortholog" + ',' + "gene_identities" + ',' + "gene_gaps" + '\n')
        output_ParentB.write("Hybrid" + ',' + str(parentB)+"_ortholog" + ',' + "gene_identities" + ',' + "gene_gaps" + '\n')
        output_ParentC.write("Hybrid" + ',' + str(parentC)+"_ortholog" + ',' + "gene_identities" + ',' + "gene_gaps" + '\n')
        output_ParentD.write("Hybrid" + ',' + str(parentD)+"_ortholog" + ',' + "gene_identities" + ',' + "gene_gaps" + '\n')

        output_ParentAParentB.write("Hybrid" + ',' + "Ortholog_ID" + ',' + "gene_identities" + ',' + "gene_gaps" + '\n')
        output_dodgy.write("Hybrid" + ',' + "Ortholog_ID" + ',' + "gene_identities" + ',' + "gene_gaps" + '\n')
       
        
        for k,v in dic_ortho_ParentA.items():
            
            if (k in dic_ortho_ParentB.keys()) and (k in dic_ortho_ParentC.keys()) and (k in dic_ortho_ParentD.keys()):  ## if in parent A and B and C and D
                   
                if (int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentB[k]['identities'])) and (int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentC[k]['identities'])) and (int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentD[k]['identities'])):
                    if int(dic_identities_ParentA[k]['identities']) >= int(threshold):
                        output_ParentA.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                        ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                        x+=1
                    else:
                        output_dodgy.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                        ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                        x+=1
                        
                elif (int(dic_identities_ParentB[k]['identities']) > int(dic_identities_ParentA[k]['identities'])) and (int(dic_identities_ParentB[k]['identities']) > int(dic_identities_ParentC[k]['identities'])) and (int(dic_identities_ParentB[k]['identities']) > int(dic_identities_ParentD[k]['identities'])):
                    if int(dic_identities_ParentB[k]['identities']) >= int(threshold):
                        output_ParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                        ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                        x+=1
                    else:
                        output_dodgy.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                        ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                        x+=1
                        
                elif (int(dic_identities_ParentC[k]['identities']) > int(dic_identities_ParentA[k]['identities'])) and (int(dic_identities_ParentC[k]['identities']) > int(dic_identities_ParentB[k]['identities'])) and (int(dic_identities_ParentC[k]['identities']) > int(dic_identities_ParentD[k]['identities'])):
                    if int(dic_identities_ParentC[k]['identities']) >= int(threshold):
                        output_ParentC.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                        ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                        x+=1
                    else:
                        output_dodgy.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                        ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                        x+=1
                        
                        
                elif (int(dic_identities_ParentD[k]['identities']) > int(dic_identities_ParentA[k]['identities'])) and (int(dic_identities_ParentD[k]['identities']) > int(dic_identities_ParentB[k]['identities'])) and (int(dic_identities_ParentD[k]['identities']) > int(dic_identities_ParentC[k]['identities'])):
                    if int(dic_identities_ParentD[k]['identities']) >= int(threshold):
                        output_ParentD.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                        ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                        x+=1
                    else:
                        output_dodgy.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                        ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                        x+=1                   
                else:
                    # print("Same copy in Parent A and Parent B")
                    output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                    ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                    output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                    ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                    output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                    ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')   
                    output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                    ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                    x+=1


            elif (k in dic_ortho_ParentB.keys()) and (k not in dic_ortho_ParentC.keys()) and (k not in dic_ortho_ParentD.keys()):  ## if in parent A and B, NOT C, NOT D
                    
                if int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentB[k]['identities']):
                    if int(dic_identities_ParentA[k]['identities']) >= int(threshold):
                        output_ParentA.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                        ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                        x+=1
                    else:
                        output_dodgy.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                        ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                        x+=1
                        
                elif int(dic_identities_ParentA[k]['identities']) < int(dic_identities_ParentB[k]['identities']):
                    if int(dic_identities_ParentB[k]['identities']) >= int(threshold):
                        output_ParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                        ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                        x+=1
                    else:
                        output_dodgy.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                        ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                        x+=1
                   
                else:
                    # print("Same copy in Parent A and Parent B")
                    output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                    ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                    output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                    ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                      
                    x+=1       
                    
                    
            elif (k in dic_ortho_ParentC.keys()) and (k not in dic_ortho_ParentB.keys()) and (k not in dic_ortho_ParentD.keys()):  ## if in parent A and C, NOT B, NOT D
                    
                if int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentC[k]['identities']):
                    if int(dic_identities_ParentA[k]['identities']) >= int(threshold):
                        output_ParentA.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                        ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                        x+=1
                    else:
                        output_dodgy.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                        ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                        x+=1
                        
                elif int(dic_identities_ParentA[k]['identities']) < int(dic_identities_ParentC[k]['identities']):
                    if int(dic_identities_ParentC[k]['identities']) >= int(threshold):
                        output_ParentC.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                        ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                        x+=1
                    else:
                        output_dodgy.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                        ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                        x+=1
                   
                else:
                    output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                    ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                    output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                    ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                      
                    x+=1                      


            elif (k in dic_ortho_ParentD.keys()) and (k not in dic_ortho_ParentB.keys()) and (k not in dic_ortho_ParentC.keys()):  ## if in parent A and D, NOT B, NOT C
                    
                if int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentD[k]['identities']):
                    if int(dic_identities_ParentA[k]['identities']) >= int(threshold):
                        output_ParentA.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                        ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                        x+=1
                    else:
                        output_dodgy.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                        ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                        x+=1
                        
                elif int(dic_identities_ParentA[k]['identities']) < int(dic_identities_ParentD[k]['identities']):
                    if int(dic_identities_ParentD[k]['identities']) >= int(threshold):
                        output_ParentD.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                        ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                        x+=1
                    else:
                        output_dodgy.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                        ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                        x+=1
                   
                else:
                    output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                    ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                    output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                    ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                      
                    x+=1                  
                
            ##### CASE ABC/D    
            elif (k in dic_ortho_ParentB.keys()) and (k in dic_ortho_ParentC.keys()) and (k not in dic_ortho_ParentD.keys()):
                    
                if (int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentB[k]['identities'])) and (int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentC[k]['identities'])):
                    if int(dic_identities_ParentA[k]['identities']) >= int(threshold):
                        output_ParentA.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                        ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                        x+=1
                    else:
                        output_dodgy.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                        ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                        x+=1
                        
                elif (int(dic_identities_ParentB[k]['identities']) > int(dic_identities_ParentA[k]['identities'])) and (int(dic_identities_ParentB[k]['identities']) > int(dic_identities_ParentC[k]['identities'])):
                    if int(dic_identities_ParentB[k]['identities']) >= int(threshold):
                        output_ParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                        ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                        x+=1
                    else:
                        output_dodgy.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                        ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                        x+=1
          
                elif (int(dic_identities_ParentC[k]['identities']) > int(dic_identities_ParentA[k]['identities'])) and (int(dic_identities_ParentC[k]['identities']) > int(dic_identities_ParentB[k]['identities'])):
                    if int(dic_identities_ParentC[k]['identities']) >= int(threshold):
                        output_ParentC.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                        ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                        x+=1
                    else:
                        output_dodgy.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                        ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                        x+=1
                        
                else:
                    output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                    ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                    output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                    ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                    output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                    ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                      
                    x+=1                  

            ##### CASE ACD/B    
            elif (k in dic_ortho_ParentC.keys()) and (k in dic_ortho_ParentD.keys()) and (k not in dic_ortho_ParentB.keys()):
                    
                if (int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentC[k]['identities'])) and (int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentD[k]['identities'])):
                    if int(dic_identities_ParentA[k]['identities']) >= int(threshold):
                        output_ParentA.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                        ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                        x+=1
                    else:
                        output_dodgy.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                        ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                        x+=1
                        
                elif (int(dic_identities_ParentC[k]['identities']) > int(dic_identities_ParentA[k]['identities'])) and (int(dic_identities_ParentC[k]['identities']) > int(dic_identities_ParentD[k]['identities'])):
                    if int(dic_identities_ParentC[k]['identities']) >= int(threshold):
                        output_ParentC.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                        ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                        x+=1
                    else:
                        output_dodgy.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                        ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                        x+=1
          
                elif (int(dic_identities_ParentD[k]['identities']) > int(dic_identities_ParentA[k]['identities'])) and (int(dic_identities_ParentD[k]['identities']) > int(dic_identities_ParentC[k]['identities'])):
                    if int(dic_identities_ParentD[k]['identities']) >= int(threshold):
                        output_ParentD.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                        ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                        x+=1
                    else:
                        output_dodgy.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                        ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                        x+=1
                        
            
                else:
                    output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                    ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')

                    output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                    ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                    output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                    ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')

                    x+=1                  
                              

                             
            ##### CASE ABD/C
            elif (k in dic_ortho_ParentB.keys()) and (k in dic_ortho_ParentD.keys()) and (k not in dic_ortho_ParentC.keys()):
                    
                if (int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentB[k]['identities'])) and (int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentD[k]['identities'])):
                    if int(dic_identities_ParentA[k]['identities']) >= int(threshold):
                        output_ParentA.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                        ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                        x+=1
                    else:
                        output_dodgy.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                        ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                        x+=1
                        
                elif (int(dic_identities_ParentB[k]['identities']) > int(dic_identities_ParentA[k]['identities'])) and (int(dic_identities_ParentB[k]['identities']) > int(dic_identities_ParentD[k]['identities'])):
                    if int(dic_identities_ParentB[k]['identities']) >= int(threshold):
                        output_ParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                        ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                        x+=1
                    else:
                        output_dodgy.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                        ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                        x+=1
          
                elif (int(dic_identities_ParentD[k]['identities']) > int(dic_identities_ParentA[k]['identities'])) and (int(dic_identities_ParentD[k]['identities']) > int(dic_identities_ParentB[k]['identities'])):
                    if int(dic_identities_ParentD[k]['identities']) >= int(threshold):
                        output_ParentD.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                        ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                        x+=1
                    else:
                        output_dodgy.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                        ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                        x+=1
                        
            
                else:
                    output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                    ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')

                    output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                    ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                    output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                    ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')

                    x+=1                  
                                      
                
            else: # if in Parent A not in B and not in C, and not D
                if int(dic_identities_ParentA[k]['identities']) >= int(threshold):
                    output_ParentA.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                    ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                    x+=1
                else:
                    output_dodgy.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                    ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                    x+=1
                        
            liste_p_hybrid.append(k)
            
            
            
            #############################################################
        for k,v in dic_ortho_ParentB.items():
            if k not in liste_p_hybrid:

                if (k in dic_ortho_ParentA.keys()) and (k in dic_ortho_ParentC.keys()) and (k in dic_ortho_ParentD.keys()):  ## if in parent A and B and C and D
                       
                    if (int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentB[k]['identities'])) and (int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentC[k]['identities'])) and (int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentD[k]['identities'])):
                        if int(dic_identities_ParentA[k]['identities']) >= int(threshold):
                            output_ParentA.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                            ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                            ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                            x+=1
                            
                    elif (int(dic_identities_ParentB[k]['identities']) > int(dic_identities_ParentA[k]['identities'])) and (int(dic_identities_ParentB[k]['identities']) > int(dic_identities_ParentC[k]['identities'])) and (int(dic_identities_ParentB[k]['identities']) > int(dic_identities_ParentD[k]['identities'])):
                        if int(dic_identities_ParentB[k]['identities']) >= int(threshold):
                            output_ParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                            ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                            ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                            x+=1
                            
                    elif (int(dic_identities_ParentC[k]['identities']) > int(dic_identities_ParentA[k]['identities'])) and (int(dic_identities_ParentC[k]['identities']) > int(dic_identities_ParentB[k]['identities'])) and (int(dic_identities_ParentC[k]['identities']) > int(dic_identities_ParentD[k]['identities'])):
                        if int(dic_identities_ParentC[k]['identities']) >= int(threshold):
                            output_ParentC.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                            ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                            ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                            x+=1
                            
                            
                    elif (int(dic_identities_ParentD[k]['identities']) > int(dic_identities_ParentA[k]['identities'])) and (int(dic_identities_ParentD[k]['identities']) > int(dic_identities_ParentB[k]['identities'])) and (int(dic_identities_ParentD[k]['identities']) > int(dic_identities_ParentC[k]['identities'])):
                        if int(dic_identities_ParentD[k]['identities']) >= int(threshold):
                            output_ParentD.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                            ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                            ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                            x+=1                   
                    else:
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                        ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                        ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                        ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')   
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                        ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                        x+=1
    
    
                elif (k in dic_ortho_ParentA.keys()) and (k not in dic_ortho_ParentC.keys()) and (k not in dic_ortho_ParentD.keys()):  ## if in parent A and B, NOT C, NOT D
                        
                    if int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentB[k]['identities']):
                        if int(dic_identities_ParentA[k]['identities']) >= int(threshold):
                            output_ParentA.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                            ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                            ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                            x+=1
                            
                    elif int(dic_identities_ParentA[k]['identities']) < int(dic_identities_ParentB[k]['identities']):
                        if int(dic_identities_ParentB[k]['identities']) >= int(threshold):
                            output_ParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                            ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                            ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                            x+=1
                       
                    else:
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                        ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                        ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                          
                        x+=1       
                        
                        
                elif (k in dic_ortho_ParentC.keys()) and (k not in dic_ortho_ParentA.keys()) and (k not in dic_ortho_ParentD.keys()):  ## if in parent B and C, NOT A, NOT D
                        
                    if int(dic_identities_ParentB[k]['identities']) > int(dic_identities_ParentC[k]['identities']):
                        if int(dic_identities_ParentB[k]['identities']) >= int(threshold):
                            output_ParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                            ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                            ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                            x+=1
                            
                    elif int(dic_identities_ParentB[k]['identities']) < int(dic_identities_ParentC[k]['identities']):
                        if int(dic_identities_ParentC[k]['identities']) >= int(threshold):
                            output_ParentC.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                            ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                            ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                            x+=1
                       
                    else:
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                        ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                        ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                          
                        x+=1                      
    
    
                elif (k in dic_ortho_ParentD.keys()) and (k not in dic_ortho_ParentA.keys()) and (k not in dic_ortho_ParentC.keys()):  ## if in parent B and D, NOT A, NOT C
                        
                    if int(dic_identities_ParentB[k]['identities']) > int(dic_identities_ParentD[k]['identities']):
                        if int(dic_identities_ParentB[k]['identities']) >= int(threshold):
                            output_ParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                            ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                            ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                            x+=1
                            
                    elif int(dic_identities_ParentB[k]['identities']) < int(dic_identities_ParentD[k]['identities']):
                        if int(dic_identities_ParentD[k]['identities']) >= int(threshold):
                            output_ParentD.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                            ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                            ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                            x+=1
                       
                    else:
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                        ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                        ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                          
                        x+=1              
                        
                        
                ##### CASE ABC/D    
                elif (k in dic_ortho_ParentA.keys()) and (k in dic_ortho_ParentC.keys()) and (k not in dic_ortho_ParentD.keys()):
                        
                    if (int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentB[k]['identities'])) and (int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentC[k]['identities'])):
                        if int(dic_identities_ParentA[k]['identities']) >= int(threshold):
                            output_ParentA.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                            ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                            ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                            x+=1
                            
                    elif (int(dic_identities_ParentB[k]['identities']) > int(dic_identities_ParentA[k]['identities'])) and (int(dic_identities_ParentB[k]['identities']) > int(dic_identities_ParentC[k]['identities'])):
                        if int(dic_identities_ParentB[k]['identities']) >= int(threshold):
                            output_ParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                            ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                            ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                            x+=1
              
                    elif (int(dic_identities_ParentC[k]['identities']) > int(dic_identities_ParentA[k]['identities'])) and (int(dic_identities_ParentC[k]['identities']) > int(dic_identities_ParentB[k]['identities'])):
                        if int(dic_identities_ParentC[k]['identities']) >= int(threshold):
                            output_ParentC.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                            ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                            ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                            x+=1
                            
                    else:
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                        ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                        ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                        ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                          
                        x+=1                  
    
                ##### CASE BCD/A  
                elif (k in dic_ortho_ParentC.keys()) and (k in dic_ortho_ParentD.keys()) and (k not in dic_ortho_ParentA.keys()):
                        
                    if (int(dic_identities_ParentB[k]['identities']) > int(dic_identities_ParentC[k]['identities'])) and (int(dic_identities_ParentB[k]['identities']) > int(dic_identities_ParentD[k]['identities'])):
                        if int(dic_identities_ParentB[k]['identities']) >= int(threshold):
                            output_ParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                            ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                            ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                            x+=1
                            
                    elif (int(dic_identities_ParentC[k]['identities']) > int(dic_identities_ParentB[k]['identities'])) and (int(dic_identities_ParentC[k]['identities']) > int(dic_identities_ParentD[k]['identities'])):
                        if int(dic_identities_ParentC[k]['identities']) >= int(threshold):
                            output_ParentC.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                            ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                            ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                            x+=1
              
                    elif (int(dic_identities_ParentD[k]['identities']) > int(dic_identities_ParentB[k]['identities'])) and (int(dic_identities_ParentD[k]['identities']) > int(dic_identities_ParentC[k]['identities'])):
                        if int(dic_identities_ParentD[k]['identities']) >= int(threshold):
                            output_ParentD.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                            ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                            ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                            x+=1
                            
                
                    else:
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                        ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
    
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                        ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                        ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
    
                        x+=1                  
                                  
    
                                 
                ##### CASE ABD/C
                elif (k in dic_ortho_ParentA.keys()) and (k in dic_ortho_ParentD.keys()) and (k not in dic_ortho_ParentC.keys()):
                        
                    if (int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentB[k]['identities'])) and (int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentD[k]['identities'])):
                        if int(dic_identities_ParentA[k]['identities']) >= int(threshold):
                            output_ParentA.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                            ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                            ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                            x+=1
                            
                    elif (int(dic_identities_ParentB[k]['identities']) > int(dic_identities_ParentA[k]['identities'])) and (int(dic_identities_ParentB[k]['identities']) > int(dic_identities_ParentD[k]['identities'])):
                        if int(dic_identities_ParentB[k]['identities']) >= int(threshold):
                            output_ParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                            ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                            ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                            x+=1
              
                    elif (int(dic_identities_ParentD[k]['identities']) > int(dic_identities_ParentA[k]['identities'])) and (int(dic_identities_ParentD[k]['identities']) > int(dic_identities_ParentB[k]['identities'])):
                        if int(dic_identities_ParentD[k]['identities']) >= int(threshold):
                            output_ParentD.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                            ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                            ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                            x+=1
                            
                
                    else:
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                        ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
    
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                        ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                        ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
    
                        x+=1                  
                                  
                    
                else: # if in Parent B not in A and not in C, and not D
                    if int(dic_identities_ParentB[k]['identities']) >= int(threshold):
                        output_ParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                        ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                        x+=1
                    else:
                        output_dodgy.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                        ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                        x+=1
                            
                liste_p_hybrid.append(k)



                ##
            #############################################################
            
        for k,v in dic_ortho_ParentC.items():
            if k not in liste_p_hybrid:

                if (k in dic_ortho_ParentA.keys()) and (k in dic_ortho_ParentB.keys()) and (k in dic_ortho_ParentD.keys()):  ## if in parent A and B and C and D
                       
                    if (int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentB[k]['identities'])) and (int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentC[k]['identities'])) and (int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentD[k]['identities'])):
                        if int(dic_identities_ParentA[k]['identities']) >= int(threshold):
                            output_ParentA.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                            ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                            ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                            x+=1
                            
                    elif (int(dic_identities_ParentB[k]['identities']) > int(dic_identities_ParentA[k]['identities'])) and (int(dic_identities_ParentB[k]['identities']) > int(dic_identities_ParentC[k]['identities'])) and (int(dic_identities_ParentB[k]['identities']) > int(dic_identities_ParentD[k]['identities'])):
                        if int(dic_identities_ParentB[k]['identities']) >= int(threshold):
                            output_ParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                            ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                            ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                            x+=1
                            
                    elif (int(dic_identities_ParentC[k]['identities']) > int(dic_identities_ParentA[k]['identities'])) and (int(dic_identities_ParentC[k]['identities']) > int(dic_identities_ParentB[k]['identities'])) and (int(dic_identities_ParentC[k]['identities']) > int(dic_identities_ParentD[k]['identities'])):
                        if int(dic_identities_ParentC[k]['identities']) >= int(threshold):
                            output_ParentC.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                            ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                            ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                            x+=1
                            
                            
                    elif (int(dic_identities_ParentD[k]['identities']) > int(dic_identities_ParentA[k]['identities'])) and (int(dic_identities_ParentD[k]['identities']) > int(dic_identities_ParentB[k]['identities'])) and (int(dic_identities_ParentD[k]['identities']) > int(dic_identities_ParentC[k]['identities'])):
                        if int(dic_identities_ParentD[k]['identities']) >= int(threshold):
                            output_ParentD.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                            ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                            ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                            x+=1                   
                    else:
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                        ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                        ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                        ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')   
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                        ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                        x+=1
    
    
                elif (k in dic_ortho_ParentA.keys()) and (k not in dic_ortho_ParentB.keys()) and (k not in dic_ortho_ParentD.keys()):  ## if in parent A and C, NOT B, NOT D
                        
                    if int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentC[k]['identities']):
                        if int(dic_identities_ParentA[k]['identities']) >= int(threshold):
                            output_ParentA.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                            ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                            ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                            x+=1
                            
                    elif int(dic_identities_ParentA[k]['identities']) < int(dic_identities_ParentC[k]['identities']):
                        if int(dic_identities_ParentC[k]['identities']) >= int(threshold):
                            output_ParentC.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                            ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                            ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                            x+=1
                       
                    else:
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                        ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                        ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                          
                        x+=1       
                        
                        
                elif (k in dic_ortho_ParentB.keys()) and (k not in dic_ortho_ParentA.keys()) and (k not in dic_ortho_ParentD.keys()):  ## if in parent B and C, NOT A, NOT D
                        
                    if int(dic_identities_ParentB[k]['identities']) > int(dic_identities_ParentC[k]['identities']):
                        if int(dic_identities_ParentB[k]['identities']) >= int(threshold):
                            output_ParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                            ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                            ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                            x+=1
                            
                    elif int(dic_identities_ParentB[k]['identities']) < int(dic_identities_ParentC[k]['identities']):
                        if int(dic_identities_ParentC[k]['identities']) >= int(threshold):
                            output_ParentC.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                            ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                            ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                            x+=1
                       
                    else:
                        # print("Same copy in Parent B and Parent C")
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                        ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                        ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                          
                        x+=1                      
    
    
                elif (k in dic_ortho_ParentD.keys()) and (k not in dic_ortho_ParentA.keys()) and (k not in dic_ortho_ParentD.keys()):  ## if in parent C and D, NOT A, NOT B
                        
                    if int(dic_identities_ParentC[k]['identities']) > int(dic_identities_ParentD[k]['identities']):
                        if int(dic_identities_ParentC[k]['identities']) >= int(threshold):
                            output_ParentC.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                            ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                            ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                            x+=1
                            
                    elif int(dic_identities_ParentC[k]['identities']) < int(dic_identities_ParentD[k]['identities']):
                        if int(dic_identities_ParentD[k]['identities']) >= int(threshold):
                            output_ParentD.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                            ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                            ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                            x+=1
                       
                    else:
                        # print("Same copy in Parent C and Parent D")
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                        ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                        ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                          
                        x+=1               
                        
                        
                ##### CASE ABC/D    
                elif (k in dic_ortho_ParentA.keys()) and (k in dic_ortho_ParentB.keys()) and (k not in dic_ortho_ParentD.keys()):
                        
                    if (int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentB[k]['identities'])) and (int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentC[k]['identities'])):
                        if int(dic_identities_ParentA[k]['identities']) >= int(threshold):
                            output_ParentA.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                            ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                            ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                            x+=1
                            
                    elif (int(dic_identities_ParentB[k]['identities']) > int(dic_identities_ParentA[k]['identities'])) and (int(dic_identities_ParentB[k]['identities']) > int(dic_identities_ParentC[k]['identities'])):
                        if int(dic_identities_ParentB[k]['identities']) >= int(threshold):
                            output_ParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                            ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                            ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                            x+=1
              
                    elif (int(dic_identities_ParentC[k]['identities']) > int(dic_identities_ParentA[k]['identities'])) and (int(dic_identities_ParentC[k]['identities']) > int(dic_identities_ParentB[k]['identities'])):
                        if int(dic_identities_ParentC[k]['identities']) >= int(threshold):
                            output_ParentC.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                            ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                            ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                            x+=1
                            
                    else:
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                        ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                        ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                        ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                          
                        x+=1                  
    
                ##### CASE BCD/A  
                elif (k in dic_ortho_ParentB.keys()) and (k in dic_ortho_ParentD.keys()) and (k not in dic_ortho_ParentA.keys()):
                        
                    if (int(dic_identities_ParentB[k]['identities']) > int(dic_identities_ParentC[k]['identities'])) and (int(dic_identities_ParentB[k]['identities']) > int(dic_identities_ParentD[k]['identities'])):
                        if int(dic_identities_ParentB[k]['identities']) >= int(threshold):
                            output_ParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                            ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                            ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                            x+=1
                            
                    elif (int(dic_identities_ParentC[k]['identities']) > int(dic_identities_ParentB[k]['identities'])) and (int(dic_identities_ParentC[k]['identities']) > int(dic_identities_ParentD[k]['identities'])):
                        if int(dic_identities_ParentC[k]['identities']) >= int(threshold):
                            output_ParentC.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                            ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                            ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                            x+=1
              
                    elif (int(dic_identities_ParentD[k]['identities']) > int(dic_identities_ParentB[k]['identities'])) and (int(dic_identities_ParentD[k]['identities']) > int(dic_identities_ParentC[k]['identities'])):
                        if int(dic_identities_ParentD[k]['identities']) >= int(threshold):
                            output_ParentD.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                            ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                            ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                            x+=1
                            
                
                    else:
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                        ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
    
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                        ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                        ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
    
                        x+=1                  

                ##### CASE ACD/B    
                elif (k in dic_ortho_ParentA.keys()) and (k in dic_ortho_ParentD.keys()) and (k not in dic_ortho_ParentB.keys()):
                        
                    if (int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentC[k]['identities'])) and (int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentD[k]['identities'])):
                        if int(dic_identities_ParentA[k]['identities']) >= int(threshold):
                            output_ParentA.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                            ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                            ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                            x+=1
                            
                    elif (int(dic_identities_ParentC[k]['identities']) > int(dic_identities_ParentA[k]['identities'])) and (int(dic_identities_ParentC[k]['identities']) > int(dic_identities_ParentD[k]['identities'])):
                        if int(dic_identities_ParentC[k]['identities']) >= int(threshold):
                            output_ParentC.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                            ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                            ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                            x+=1
              
                    elif (int(dic_identities_ParentD[k]['identities']) > int(dic_identities_ParentA[k]['identities'])) and (int(dic_identities_ParentD[k]['identities']) > int(dic_identities_ParentC[k]['identities'])):
                        if int(dic_identities_ParentD[k]['identities']) >= int(threshold):
                            output_ParentD.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                            ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                            ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                            x+=1
                            
                
                    else:
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                        ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
    
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                        ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                        ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
    
                        x+=1                  
                                  

                    
                else: # if in Parent C not in A and not in B, and not D
                    if int(dic_identities_ParentC[k]['identities']) >= int(threshold):
                        output_ParentC.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                        ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                        x+=1
                    else:
                        output_dodgy.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                        ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                        x+=1
                            
                liste_p_hybrid.append(k)


            #############################################################
            
        for k,v in dic_ortho_ParentD.items():
            if k not in liste_p_hybrid:

                if (k in dic_ortho_ParentA.keys()) and (k in dic_ortho_ParentB.keys()) and (k in dic_ortho_ParentC.keys()):  ## if in parent A and B and C and D
                       
                    if (int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentB[k]['identities'])) and (int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentC[k]['identities'])) and (int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentD[k]['identities'])):
                        if int(dic_identities_ParentA[k]['identities']) >= int(threshold):
                            output_ParentA.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                            ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                            ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                            x+=1
                            
                    elif (int(dic_identities_ParentB[k]['identities']) > int(dic_identities_ParentA[k]['identities'])) and (int(dic_identities_ParentB[k]['identities']) > int(dic_identities_ParentC[k]['identities'])) and (int(dic_identities_ParentB[k]['identities']) > int(dic_identities_ParentD[k]['identities'])):
                        if int(dic_identities_ParentB[k]['identities']) >= int(threshold):
                            output_ParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                            ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                            ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                            x+=1
                            
                    elif (int(dic_identities_ParentC[k]['identities']) > int(dic_identities_ParentA[k]['identities'])) and (int(dic_identities_ParentC[k]['identities']) > int(dic_identities_ParentB[k]['identities'])) and (int(dic_identities_ParentC[k]['identities']) > int(dic_identities_ParentD[k]['identities'])):
                        if int(dic_identities_ParentC[k]['identities']) >= int(threshold):
                            output_ParentC.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                            ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                            ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                            x+=1
                            
                            
                    elif (int(dic_identities_ParentD[k]['identities']) > int(dic_identities_ParentA[k]['identities'])) and (int(dic_identities_ParentD[k]['identities']) > int(dic_identities_ParentB[k]['identities'])) and (int(dic_identities_ParentD[k]['identities']) > int(dic_identities_ParentC[k]['identities'])):
                        if int(dic_identities_ParentD[k]['identities']) >= int(threshold):
                            output_ParentD.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                            ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                            ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                            x+=1                   
                    else:
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                        ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                        ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                        ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')   
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                        ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                        x+=1
    
    
                elif (k in dic_ortho_ParentA.keys()) and (k not in dic_ortho_ParentB.keys()) and (k not in dic_ortho_ParentC.keys()):  ## if in parent A and D, NOT B, NOT C
                        
                    if int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentD[k]['identities']):
                        if int(dic_identities_ParentA[k]['identities']) >= int(threshold):
                            output_ParentA.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                            ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                            ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                            x+=1
                            
                    elif int(dic_identities_ParentA[k]['identities']) < int(dic_identities_ParentD[k]['identities']):
                        if int(dic_identities_ParentD[k]['identities']) >= int(threshold):
                            output_ParentD.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                            ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                            ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                            x+=1
                       
                    else:
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                        ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                        ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                          
                        x+=1       
                        
                        
                elif (k in dic_ortho_ParentB.keys()) and (k not in dic_ortho_ParentA.keys()) and (k not in dic_ortho_ParentC.keys()):  ## if in parent B and D, NOT A, NOT C
                        
                    if int(dic_identities_ParentB[k]['identities']) > int(dic_identities_ParentD[k]['identities']):
                        if int(dic_identities_ParentB[k]['identities']) >= int(threshold):
                            output_ParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                            ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                            ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                            x+=1
                            
                    elif int(dic_identities_ParentB[k]['identities']) < int(dic_identities_ParentD[k]['identities']):
                        if int(dic_identities_ParentD[k]['identities']) >= int(threshold):
                            output_ParentD.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                            ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                            ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                            x+=1
                       
                    else:
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                        ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                        ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                          
                        x+=1                      
    
    
                elif (k in dic_ortho_ParentC.keys()) and (k not in dic_ortho_ParentA.keys()) and (k not in dic_ortho_ParentB.keys()):  ## if in parent C and D, NOT A, NOT B
                        
                    if int(dic_identities_ParentC[k]['identities']) > int(dic_identities_ParentD[k]['identities']):
                        if int(dic_identities_ParentC[k]['identities']) >= int(threshold):
                            output_ParentC.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                            ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                            ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                            x+=1
                            
                    elif int(dic_identities_ParentC[k]['identities']) < int(dic_identities_ParentD[k]['identities']):
                        if int(dic_identities_ParentD[k]['identities']) >= int(threshold):
                            output_ParentD.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                            ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                            ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                            x+=1
                       
                    else:
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                        ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                        ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                          
                        x+=1          
                        

                ##### CASE BCD/A  
                elif (k in dic_ortho_ParentB.keys()) and (k in dic_ortho_ParentC.keys()) and (k not in dic_ortho_ParentA.keys()):
                        
                    if (int(dic_identities_ParentB[k]['identities']) > int(dic_identities_ParentC[k]['identities'])) and (int(dic_identities_ParentB[k]['identities']) > int(dic_identities_ParentD[k]['identities'])):
                        if int(dic_identities_ParentB[k]['identities']) >= int(threshold):
                            output_ParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                            ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                            ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                            x+=1
                            
                    elif (int(dic_identities_ParentC[k]['identities']) > int(dic_identities_ParentB[k]['identities'])) and (int(dic_identities_ParentC[k]['identities']) > int(dic_identities_ParentD[k]['identities'])):
                        if int(dic_identities_ParentC[k]['identities']) >= int(threshold):
                            output_ParentC.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                            ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                            ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                            x+=1
              
                    elif (int(dic_identities_ParentD[k]['identities']) > int(dic_identities_ParentB[k]['identities'])) and (int(dic_identities_ParentD[k]['identities']) > int(dic_identities_ParentC[k]['identities'])):
                        if int(dic_identities_ParentD[k]['identities']) >= int(threshold):
                            output_ParentD.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                            ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                            ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                            x+=1
                            
                
                    else:
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                        ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
    
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                        ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                        ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
    
                        x+=1                  

                ##### CASE ACD/B    
                elif (k in dic_ortho_ParentA.keys()) and (k in dic_ortho_ParentC.keys()) and (k not in dic_ortho_ParentB.keys()):
                        
                    if (int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentC[k]['identities'])) and (int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentD[k]['identities'])):
                        if int(dic_identities_ParentA[k]['identities']) >= int(threshold):
                            output_ParentA.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                            ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                            ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                            x+=1
                            
                    elif (int(dic_identities_ParentC[k]['identities']) > int(dic_identities_ParentA[k]['identities'])) and (int(dic_identities_ParentC[k]['identities']) > int(dic_identities_ParentD[k]['identities'])):
                        if int(dic_identities_ParentC[k]['identities']) >= int(threshold):
                            output_ParentC.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                            ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                            ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                            x+=1
              
                    elif (int(dic_identities_ParentD[k]['identities']) > int(dic_identities_ParentA[k]['identities'])) and (int(dic_identities_ParentD[k]['identities']) > int(dic_identities_ParentC[k]['identities'])):
                        if int(dic_identities_ParentD[k]['identities']) >= int(threshold):
                            output_ParentD.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                            ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                            ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                            x+=1
                            
                
                    else:
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                        ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
    
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentC[k]['Ortholog']) + ',' + str(dic_identities_ParentC[k]['identities']) + 
                                        ','  + str(dic_identities_ParentC[k]['gaps']) + '\n')
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                        ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
    
                        x+=1    
                        
                        
                        
                ##### CASE ABD/C
                elif (k in dic_ortho_ParentB.keys()) and (k in dic_ortho_ParentA.keys()) and (k not in dic_ortho_ParentC.keys()):
                        
                    if (int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentB[k]['identities'])) and (int(dic_identities_ParentA[k]['identities']) > int(dic_identities_ParentD[k]['identities'])):
                        if int(dic_identities_ParentA[k]['identities']) >= int(threshold):
                            output_ParentA.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                            ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                            ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
                            x+=1
                            
                    elif (int(dic_identities_ParentB[k]['identities']) > int(dic_identities_ParentA[k]['identities'])) and (int(dic_identities_ParentB[k]['identities']) > int(dic_identities_ParentD[k]['identities'])):
                        if int(dic_identities_ParentB[k]['identities']) >= int(threshold):
                            output_ParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                            ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                            ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                            x+=1
              
                    elif (int(dic_identities_ParentD[k]['identities']) > int(dic_identities_ParentA[k]['identities'])) and (int(dic_identities_ParentD[k]['identities']) > int(dic_identities_ParentB[k]['identities'])):
                        if int(dic_identities_ParentD[k]['identities']) >= int(threshold):
                            output_ParentD.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                            ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                            x+=1
                        else:
                            output_dodgy.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                            ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                            x+=1
                            
                
                    else:
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentA[k]['Ortholog']) + ',' + str(dic_identities_ParentA[k]['identities']) + 
                                        ','  + str(dic_identities_ParentA[k]['gaps']) + '\n')
    
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentB[k]['Ortholog']) + ',' + str(dic_identities_ParentB[k]['identities']) + 
                                        ','  + str(dic_identities_ParentB[k]['gaps']) + '\n')
                        output_ParentAParentB.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                        ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
    
                        x+=1                  
                                     
                    
                else: # if in Parent D not in A and not in B, and not C
                    if int(dic_identities_ParentD[k]['identities']) >= int(threshold):
                        output_ParentD.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                        ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                        x+=1
                    else:
                        output_dodgy.write(str(k) + ',' + str(dic_identities_ParentD[k]['Ortholog']) + ',' + str(dic_identities_ParentD[k]['identities']) + 
                                        ','  + str(dic_identities_ParentD[k]['gaps']) + '\n')
                        x+=1
                            
                liste_p_hybrid.append(k)



    #############################################################            
    
    
    #############################################################
    
    #      GROUPING PARALOGS      
    
    dic_ParA_alleles = {}
    dic_ParB_alleles = {}
    dic_ParC_alleles = {}
    dic_ParD_alleles = {}
    
    count_alleleA = 0
    count_alleleB = 0
    count_alleleC = 0
    count_alleleD = 0
    
    with open("../Results/4_Parental_alleles_prediction/genes_inherited_from_"+str(parentA)+".csv", "r") as parentalA:
        for line in parentalA:
            line = line.split("\n")[0]
            line = line.split(",")
            # print(line)
            dic_ParA_alleles[line[0]] = line[1]
            count_alleleA+=1
            
    with open("../Results/4_Parental_alleles_prediction/genes_inherited_from_"+str(parentB)+".csv", "r") as parentalB:
        next(parentalB)
        for line in parentalB:
            line = line.split("\n")[0]
            line = line.split(",")
            dic_ParB_alleles[line[0]] = line[1]
            count_alleleB+=1

    with open("../Results/4_Parental_alleles_prediction/genes_inherited_from_"+str(parentC)+".csv", "r") as parentalC:
        next(parentalC)
        for line in parentalC:
            line = line.split("\n")[0]
            line = line.split(",")
            dic_ParC_alleles[line[0]] = line[1]
            count_alleleC+=1
         
    with open("../Results/4_Parental_alleles_prediction/genes_inherited_from_"+str(parentD)+".csv", "r") as parentalD:
        next(parentalD)
        for line in parentalD:
            line = line.split("\n")[0]
            line = line.split(",")
            dic_ParD_alleles[line[0]] = line[1]
            count_alleleD+=1
         
                        
            
    with open("../Results/4_Parental_alleles_prediction/rank.txt", "w") as out:
        out.write("Total number of genes in the hybrid genome: "+str(total_hyb_genes))
        out.write("\nTotal number of genes in the Parent A genome: "+str(total_pA_genes))
        out.write("\nTotal number of genes in the Parent B genome: "+str(total_pB_genes))
        out.write("\nTotal number of genes in the Parent C genome: "+str(total_pC_genes))
        out.write("\nTotal number of genes in the Parent D genome: "+str(total_pD_genes))
        out.write("\nPredicted ParentA-like genes in the hybrid genome: "+str(count_alleleA)+" (~"+str((float(count_alleleA)*100)/float(total_hyb_genes))+"% of the hybrid genome)")
        out.write("\nPredicted ParentB-like genes in the hybrid genome: "+str(count_alleleB)+" (~"+str((float(count_alleleB)*100)/float(total_hyb_genes))+"% of the hybrid genome)")
        out.write("\nPredicted ParentC-like genes in the hybrid genome: "+str(count_alleleC)+" (~"+str((float(count_alleleC)*100)/float(total_hyb_genes))+"% of the hybrid genome)")
        out.write("\nPredicted ParentD-like genes in the hybrid genome: "+str(count_alleleD)+" (~"+str((float(count_alleleD)*100)/float(total_hyb_genes))+"% of the hybrid genome)")

            
    dic_alleles = {**dic_ParB_alleles, **dic_ParA_alleles, **dic_ParC_alleles, **dic_ParD_alleles}
    
    
    dic_paralog = {}
    list_paralog_already_processed = []
    
    stop = 0
    with open("../Results/1_Raw_Blast_output/output_blastn_hybrid_vs_hybrid.txt", "r") as hyb:
        next(hyb)
        list_done = []
        for line in hyb:
            stop+=1
            line = line.split("\n")[0]
            line = line.split("\t")
            id1 = line[0]
            id2 = line[1]
            
            
            if id1 == id2:
                continue
            elif id1 in list_done:
                continue
            else:
                list_done.append(id1)
                if (id1 not in list_paralog_already_processed) and (id2 not in list_paralog_already_processed): # new dict[id1] = id2
                    # print("############CASE 1")
                    dic_paralog[id1] = [id2]
                    list_paralog_already_processed.append(id1)
                    list_paralog_already_processed.append(id2)

                          
                elif (id1 in list_paralog_already_processed) and (id2 not in list_paralog_already_processed): # dict[id1] = append id2
                    try:
                        dic_paralog[id1].append(id2)
                        list_paralog_already_processed.append(id2)
                        
                    except:
                        try: 
                            for elm in dic_paralog:
                                for val in dic_paralog[elm]:
                                    if val == str(id1):
                                        dic_paralog[elm].append(id2)
                                        list_paralog_already_processed.append(id2)                            
                        except:
                            pass
                            
                elif id1 not in list_paralog_already_processed and id2 in list_paralog_already_processed: # dict[id1] = append id2
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
                            
                elif id1 in list_paralog_already_processed and id2 in list_paralog_already_processed:
                    pass                    
        
                else:
                    pass
                    
    
    nb = 0
    total = 0
    list_paralog = []
    with open("../Results/3_Orthologs_Paralogs/homologs_paralogs_"+str(hybrid)+".csv", "w") as output_paralog:
        output_paralog.write("Homologs_list"+"\t"+str(hybrid)+" content"+"\t"+str(parentA)+"-like content"+"\t"+str(parentB)+"-like content"+"\t"+str(parentC)+"-like content"+"\t"+str(parentD)+"-like content"+"\n") 
        for elm in dic_paralog:
            total += 1
    #        nb = 0
            list_paralog = []
            hyb = []
            ParA = []
            ParB = []
            ParC = []
            ParD = []
            
            # print("\n------ELM is: "+str(elm))
            try:
                # print("TRY 1")
                list_paralog.append(dic_alleles[elm])
                try:
                    ParB.append(dic_ParB_alleles[elm])
                except:
                    try:
                        ParA.append(dic_ParA_alleles[elm])   
                    except:
                        try:
                            ParC.append(dic_ParC_alleles[elm])
                        except:
                            ParD.append(dic_ParD_alleles[elm])
                        
            except:
                list_paralog.append(elm)
                hyb.append(elm)
            
            for val in dic_paralog[elm]:
                nb+=1
                try:
                    list_paralog.append(dic_alleles[val])
                    try:
                        ParB.append(dic_ParB_alleles[val])                    
                    except:
                        try:
                            ParA.append(dic_ParA_alleles[val]) 
                        except:
                            try:
                                ParC.append(dic_ParC_alleles[val]) 
                            except:
                                ParD.append(dic_ParD_alleles[val]) 
                except:
                    list_paralog.append(val)
                    hyb.append(val)
                    
            output_paralog.write("; ".join(list_paralog)+"\t"+ "; ".join(hyb) + "\t" + "; ".join(ParA) + "\t" + "; ".join(ParB) + "\t" + "; ".join(ParC) +  "\t" + "; ".join(ParD) + "\n")        
                    


                                     