import math
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

# AdjacencyArray

AdjA = [ [] for _ in range(len(V))]
for row, col in E:
    AdjA[row-1].append(col)
    AdjA[col-1].append(row)

# print(3 < math.inf)
# print(3 < -math.inf)


def Prim(E : dict, AdjA : list, start : int):
    visited = []
    q = []

    visited.append(start)

    prevCost = 11

    totalCost = 0
    
    for neighbor in AdjA[start-1]:
        cost = E[(start,neighbor)]
        if(cost < prevCost):
            neighborNode = neighbor
            prevCost = cost
  
    heapq.heappush(q, (prevCost, neighborNode))

    while(q):
        cost, node = heapq.heappop(q)


        if(node in visited):
            continue

        visited.append(node)
        totalCost += cost
        
        for neighbor in AdjA[node-1]:
            if neighbor not in visited:
                edgeCost = E[(min(node, neighbor), max(node, neighbor))]
                heapq.heappush(q, (edgeCost, neighbor))

    print(visited)
    print(f"총 비용{totalCost}")


if __name__ == "__main__":
    print(V)
    print(E)
    print(AdjA)

    Prim(E, AdjA, 1)
