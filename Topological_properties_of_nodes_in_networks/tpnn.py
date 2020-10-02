#!/usr/bin/env python
def BFS(searchNodes,graph_dict,color_dict,path_dict):
    graph_dict1=graph_dict.copy()
    color_dict1=color_dict.copy()
    path_dict1=path_dict.copy()
    
    myqueue=[]
    start=searchNodes[0]
    color_dict1[start]='g'
    path_dict1[start]=path_dict1.get(start)+[['start']]
    end=searchNodes[1]
    
    myqueue.extend(graph_dict1.get(start))
    for i in myqueue:
        color_dict1[i]='g'
    for i in myqueue:
        path_dict1[i]=path_dict1.get(i)+[[start]]
    while len(myqueue)!=0:
        current=myqueue.pop(0)
        color_dict1[current]='b'
        for i in graph_dict1.get(current):
            if color_dict1.get(i) =='w':
                myqueue.append(i)
                color_dict1[i]='g'
                for j in path_dict1.get(current):
                    path=j
                    path=path+[current]
                    path_dict1[i]=path_dict1.get(i)+[path]
            
            elif color_dict1.get(i)=='g'or color_dict1.get(i)=='b' and path_dict1.get(i)!=[['start']]:
                for j in path_dict1.get(current):
                    path=j
                    path=path+[current]
                    path2=path_dict1.get(i)
                    path2=path2[0]
                    if len(path) == len(path2):
                        path_dict1[i]=(path_dict1.get(i))+[path]
                       
    finalPath=path_dict1.get(end)
    
    if len(finalPath) > 1:
        print ("(",start,",",end,"):","MORE THAN ONE SHORTEST PATH")
    elif len(finalPath) == 0:
        print("(",start,",",end,"):","NO PATH")

def check_paths(input_1):
    graph_dict={}
    f=open(input_1,"r")
    readfile=f.readlines()
    adj_matrix=[]
    for i,j in zip(readfile,range(len(readfile))):
        new=[]
        adj_matrix.append(new)
        i=i.rstrip()
        i=i.split(",")
        adj_matrix[j].extend(i)
        
    adj_matrix[0][0]=0
        
             
    color_dict={}
    for i in adj_matrix[0]:
        if i !=0:
            color_dict[i]="w"
    path_dict={}
    for i in adj_matrix[0]:
        if i !=0:
            path_dict[i]=[]
        
    for i in range(len(adj_matrix)):
        if adj_matrix[i][0] != 0:
            graph_dict[adj_matrix[i][0]]=[]
            for j in range(len(adj_matrix[i])):
                if adj_matrix[i][j]=='1':
                    graph_dict[adj_matrix[i][0]]=(graph_dict.get(adj_matrix[i][0])) +[adj_matrix[0][j]]
    explored_paths=[]
    print("PART 1:")
    for i in color_dict:
        for j in color_dict: 
            if [i,j] not in explored_paths and [j,i] not in explored_paths:
                explored_paths.append([i,j])
                searchNodes=[i,j]
                BFS(searchNodes,graph_dict,color_dict,path_dict)

def make_adj_matrix(input_2):
    INF =1000000
    f=open(input_2,"r")
    readfile=f.readlines()
    adj_matrix=[]

    for i,j in zip(readfile,range(len(readfile))):
        new=[]
        adj_matrix.append(new)
        i=i.rstrip()
        i=i.split(",")
        adj_matrix[j].extend(i)
        
    for row in range(len(adj_matrix)):
        for col in range(len(adj_matrix)):
            if row!=0 and col!=0:
                if adj_matrix[row][col]=='0':
                    adj_matrix[row][col]=INF
      
    adj_matrix[0][0]=0
    nodes=[]
    for line in adj_matrix[0]:
        if line != 0:
            nodes.append(line) 
    for k in range(len(nodes)):
        for i in range(len(nodes)):
            for j in range(len(nodes)):
                if adj_matrix[i+1][0]==adj_matrix[0][j+1]:
                    adj_matrix[i+1][j+1]=0
                else:
                    adj_matrix[i+1][j+1] = min(int(adj_matrix[i+1][j+1]), int(adj_matrix[i+1][k+1])+int(adj_matrix[k+1][j+1]))
    return(adj_matrix)
def closeness_centrality(adj_matrix):
    
    add=0
    central={}
    for i in range(len(adj_matrix)):
        if i != 0:
            for j in range(len(adj_matrix[i])):
                if j != 0:
                    add = add + adj_matrix[i][j]
            centrality = 1/add
            add = 0
            if centrality in central:
                central[centrality] = (central.get(centrality)) + [adj_matrix[i][0]]
            else:
                central[centrality] = [adj_matrix[i][0]]
    max_central = max(k for k, v in central.items()) 
    print("PART 2:")
    print("Nodes with highest closeness centrality value of",max_central,":")
    for i in central.get(max_central):
        print (i)

def compute_eccentricity(adj_matrix):

    max_ec=0
    ecentricity={}
    for i in range(len(adj_matrix)):
        if i!=0:
            for j in range(len(adj_matrix[i])):
                if j!=0:
                    if max_ec < adj_matrix[i][j]:
                        max_ec=adj_matrix[i][j]
            if max_ec in ecentricity:
                ecentricity[max_ec]=(ecentricity.get(max_ec))+[adj_matrix[i][0]]
            else:
                ecentricity[max_ec]=[adj_matrix[i][0]]
            max_ec=0
          
    min_ec=min(k for k, v in ecentricity.items())
    print("PART 3:")
    print ("Nodes with minimum ecentricity",min_ec,":")
    for i in ecentricity.get(min_ec):
        print(i)

def main():

    #FILE PATH FOR PART 1
    input_1 = "./data/testCSV.csv"
    #FILE PATH FOR PART 2 AND 3
    input_2 = "./data/testCSV2.csv"
    check_paths(input_1)
    adj_matrix = make_adj_matrix(input_2)
    closeness_centrality(adj_matrix)
    compute_eccentricity(adj_matrix)

if __name__=='__main__':
    main()
