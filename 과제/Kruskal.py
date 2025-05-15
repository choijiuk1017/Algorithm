import random
import heapq


V = [ i+1 for i in range(8) ]

E = { 
     (1, 2) : random.randint(1, 10), 
     (1, 3) : random.randint(1, 10), 
     (1, 4) : random.randint(1, 10),
     (2, 3) : random.randint(1, 10),
     (3, 4) : random.randint(1, 10),
     (3, 5) : random.randint(1, 10),
     (4, 6) : random.randint(1, 10),
     (4, 7) : random.randint(1, 10),
     (6, 7) : random.randint(1, 10),
     (6, 8) : random.randint(1, 10),
     (7, 8) : random.randint(1, 10)
       } 

AdjA = [ [] for _ in range(len(V))]
for row, col in E:
    AdjA[row-1].append(col)
    AdjA[col-1].append(row)

def Kruskal(E : dict, AdjA : list):
    visited = []
    sortEdge = dict(sorted(E.items(), key= lambda item: item[1]))
    vertexList = list(sortEdge.keys())

    print(sortEdge)
    print(vertexList)
    first, edge = vertexList[0]
    
    visited.append(first)
    visited.append(edge)

    vertexList.pop(0)
    while(vertexList):
        first, edge = vertexList[0]
        if(first in visited and edge not in visited):
            visited.append(edge)
            vertexList.pop(0)
            continue
        elif(first not in visited and edge in visited):
            visited.append(first)
            vertexList.pop(0)
            continue
        elif(first in visited and edge in visited):
            vertexList.pop(0)
            continue

        visited.append(first)
        visited.append(edge)

        vertexList.pop(0)
        
    print(visited)


if __name__ == "__main__":
    print(V)
    print(E)
    print(AdjA)

    Kruskal(E, AdjA)
    
