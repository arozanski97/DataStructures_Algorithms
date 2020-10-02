#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 09:24:16 2019

"""


import random
def MakeSif(csv_matrix,number):
    output1=open("/Users/queenalli/class/output{}.sif".format(number),"w+")
    #for i in csv_matrix:
        #print(i)
    for i in range(len(csv_matrix)):
        for j in range(len(csv_matrix)):
            if csv_matrix[i][j]==1:
                coordinates=("{}\t1.0\t{}\n".format(csv_matrix[i][0],csv_matrix[0][j]))
                output1.write(coordinates)
    output1.close()
def Degree(gene_matrix):
    print("\nDegree")
    degree_dict={}
    for i in range(len(gene_matrix)):
        degree=len(gene_matrix[i])-1
        if degree in degree_dict:
            degree_dict[degree]=degree_dict.get(degree)+1
        elif i != 0:
            degree_dict[degree]=1
    for i in degree_dict:
        print("k=",i, "p",i,"=",degree_dict.get(i))

 
def Neighbors(gene_matrix):
    print("\nNum Neighbors:")
    neighbor_list=[]
    neighbor_dict={}
    neighbor_dict2={}
    for i in gene_matrix:
        for j in gene_matrix:
            if i[0] !=  j[0] and j[0] in i:
                for x in j:
                    if x not in neighbor_list and x != i[0] and x not in i:
                        neighbor_list.append(x)
        if i[0] != "\ufeffgene_symbol":
            if len(neighbor_list) in neighbor_dict:
                neighbor_dict[len(neighbor_list)].append(i[0])
            else:
                neighbor_dict[len(neighbor_list)]=[i[0]]
            neighbor_dict2[i[0]]=neighbor_list
        neighbor_list=[]          
                
    max_neigh=(max(k for k,v in neighbor_dict.items()))            
    if len(neighbor_dict.get(max_neigh)) > 1:
        for i in neighbor_dict.get(max_neigh):
            mylist=neighbor_dict2.get(i)
            s=" "
            mylist=s.join(mylist)
            print("Node",i,"has the largest neighborhood T2 and the size of T2 is",max_neigh,"T2 consists of the following nodes",  mylist)
    else:
        mylist=neighbor_dict.get(max_neigh)
        mylist2=(neighbor_dict2.get(mylist[0]))
        s=' '
        mylist2=s.join(mylist2)
        print("Node",mylist[0],"has the largest neighborhood T2 and size of T2 is",max_neigh, "T2 consists of the following nodes",mylist2)
        
def Clique(gene_matrix):
    print("\nCliques of 3")
    cliq_dict={}   
    for i in gene_matrix:
        for j in gene_matrix:
            if i[0] != j[0] and j[0] in i:
                for x in i:
                    if x in j and x !=j[0] and x !=i[0]:
                        mylist=[i[0],j[0],x]
                        mylist=sorted(mylist)
                        s=','
                        mylist=s.join(mylist)
                        if mylist not in cliq_dict:
                            cliq_dict[mylist]='3'
    for i in cliq_dict:
        print(i,end="; ")
    
def Random(csv_matrix,prob,gene_list):
    gene_matrix=[]
    
    for i in range(len(csv_matrix)):
        
        new3=[]
        gene_matrix.append(new3)
        gene_matrix[i].append(csv_matrix[i][0])
        
        for j in range(len(csv_matrix[i])):
            if i!=0 and j!=0:
                if csv_matrix[0][j]==csv_matrix[i][0]:
                    csv_matrix[i][j]=0
                elif  random.random() > prob:
                    csv_matrix[i][j]=0
                else:
                    csv_matrix[i][j]=1
                    gene_matrix[i].append(gene_list[j-1])
    MakeSif(csv_matrix,prob)
    return(gene_matrix)

def main():
    #Open file and read to a matrix
    f=open("./data/Co-ex_matrix.csv","r")
    readfile=f.readlines()
    csv_matrix=[]
    for i,j in zip(readfile,range(len(readfile))):
        new=[]
        csv_matrix.append(new)
        i=i.rstrip()
        i=i.split(",")
        csv_matrix[j].extend(i)
        
    gene_matrix=[]
    
    #Save all the gene names to a list
    gene_list=csv_matrix[0][1:]

    for i in range(len(csv_matrix)):
        new2=[]
        gene_matrix.append(new2)
        gene_matrix[i].append(csv_matrix[i][0])
        for j in range(len(csv_matrix[i])):
            if j!=0 and i!=0:
                if float(csv_matrix[i][j]) < 0.5 or csv_matrix[0][j] == csv_matrix[i][0]:
                    csv_matrix[i][j]=0
                elif csv_matrix[0][j] != csv_matrix[i][0]:
                    csv_matrix[i][j]=1
                    gene_matrix[i].append(gene_list[j-1])
    
    print("part1")
    MakeSif(csv_matrix,1) 
    Degree(gene_matrix)
    Clique(gene_matrix)
    Neighbors(gene_matrix)
    print("\nprob 0.1")
    prob1=Random(csv_matrix,0.1,gene_list)
    Degree(prob1)
    Clique(prob1)
    Neighbors(prob1)
    print("\nprob 0.5")
    prob2=Random(csv_matrix,0.5,gene_list)
    Degree(prob2)
    Clique(prob2)
    Neighbors(prob2)
    print("\nprob 0.8")
    prob3=Random(csv_matrix,0.8,gene_list)
    Degree(prob3)
    Clique(prob3)
    Neighbors(prob3)
main()
