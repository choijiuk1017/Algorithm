import random
import heapq
import math

INF = math.inf 
random.seed(10)
V = [i+1 for i in range(0, 8)]

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
print(E)
AdjA = [[] for _ in range(len(V))]

for row, col in E:
    AdjA[row-1].append(col)
    AdjA[col-1].append(row)

print(AdjA)

def buildPath(parent:list, dest):
    path = [dest]
    current = dest
    while parent[current -1] != -1:
        path.append(parent[current -1])
        current = parent[current -1]
    path.reverse()
    return path

def BFS(V, AdjA, s, d : int = None):
    parent = [-1 for _ in range(len(V))]
    Tree = [[] for _ in range(len(V))]
    visited = [False for _ in range(len(V))]

    Q = [s]
    visited[s-1] = True

    while(len(Q) > 0):
        current = Q.pop(0)
        for neighbor in AdjA[current-1]:
            if visited[neighbor-1] == False:
                visited[neighbor-1] = True
                Q.append(neighbor)
                if d:
                    parent[neighbor-1] = current

                Tree[current-1] = neighbor
            
            if neighbor == d:
                path = buildPath(parent, d)
                return path
    if d:
        return None
    return Tree

def DFS(visited, AdjA, node, resource, path:list):
    if visited[node-1] == False:
        visited[node-1] = True
        path.append(node)
        for neighbor in AdjA[node-1]:
            DFS(visited, AdjA, neighbor, node, path)
    else:
        pass

def DFSMain(V, AdjA, start):
    visited = [False for _ in range(len(V))]
    path = []
    DFS(visited, AdjA, start, None, path)
    return path

def Prim(E : dict, AdjA, start):
    visited = []
    q = []
    visited.append(start)

    prevCost = max(E.values()) + 1
    totalCost = 0

    for i in AdjA[start-1]:
        cost = E[(start, i)]
        if cost < prevCost:
            neighbor = i
            prevCost = cost
    heapq.heappush(q, (prevCost, neighbor))

    while(q):
        cost, node = heapq.heappop(q)
        if node in visited:
            continue
        visited.append(node)
        totalCost += cost
        for neighbor in AdjA[node-1]:
            if neighbor not in visited:
                edgeCost = E[(min(neighbor, node) , max(neighbor, node))]
                heapq.heappush(q, (edgeCost, neighbor))

    print(visited, totalCost)

def Find(parent, x):
    if parent[x] != x:
        parent[x] = Find(parent, parent[x])
    return parent[x]

def Union(parent, x, y):
    x_root = Find(parent, x)
    y_root = Find(parent, y)

    if x_root == y_root:
        return False
    
    parent[y_root] = x_root
    return True

def Kruskal(V, E:dict):
    edgeList = [(u,v,w) for (u,v), w in E.items()]
    edgeList.sort(key=lambda x : x[2])

    mst = []
    parent = {v : v for v in V}
    totalCost = 0
    for (u,v,w) in edgeList:
        if Union(parent, u,v):
            mst.append((u,v))
            totalCost += w
        if len(mst) == len(V)-1:
            break
    print(mst, totalCost)

def Dijkstra(AdjA, E :dict, start):
    distanceList= [INF for _ in range(len(AdjA))]
    distanceList[start -1] = 0

    q = []
    heapq.heappush(q, (0, start))
    while(q):
        currentCost, node = heapq.heappop(q)
        if distanceList[node -1] < currentCost:
            continue
        for neighbor in AdjA[node-1]:
            edgeCost = E[(min(neighbor, node), max(neighbor, node))]
            newCost = currentCost + edgeCost
            if newCost < distanceList[neighbor-1]:
                distanceList[neighbor-1] = newCost
                heapq.heappush(q, (newCost, neighbor))
    print(distanceList)

def BellmanFord(AdjA, E:dict, start):
    distanceList= [INF for _ in range(len(AdjA))]
    distanceList[start -1] = 0
    for _ in range(len(AdjA) -1 ):
        for (node, neighbor) , cost in E.items():
            if distanceList[node-1] != INF and distanceList[node-1] + cost < distanceList[neighbor-1]:
                distanceList[neighbor-1] = distanceList[node-1] + cost

    print(distanceList)

if __name__ == "__main__":
    
    print(BFS(V, AdjA, 1, 8))
    path = DFSMain(V, AdjA, 1)
    print(path)

    Prim(E, AdjA, 1)
    Kruskal(V, E)

    Dijkstra(AdjA, E, 1)
    BellmanFord(AdjA, E, 1)

