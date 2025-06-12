import math
import heapq
from heapdict import heapdict

def G(V, E): 
    AdjM = [ [ math.inf for _ in range(len(V))] for _ in range(len(V)) ]
    for (row, col), weight in E:    
        AdjM[row-1][col-1] = weight
        AdjM[col-1][row-1] = weight
    return AdjM

# buildPath
def buildPath(parent: list, dest):
    path = [dest]
    current = dest
    while parent[current-1] != -1:
        path.append(parent[current-1])
        current = parent[current-1]
    path.reverse()
    return path

# BFS
def BFS(V, AdjA, s, d: int = None):
    parent = [ -1 for _ in range(len(V))]
    Tree = [ [] for _ in range(len(V))]
    visited = [ False for _ in range(len(V))]
    Q = [s]
    visited[s-1] = True
    while len(Q) > 0:
        current = Q.pop(0)
        for neighbor in AdjA[current-1]:
            if visited[neighbor-1] == False:
                visited[neighbor-1] = True
                Q.append(neighbor)
                if d: 
                    parent[neighbor-1] = current
                print(f"visited {current}->{neighbor}")
                Tree[current-1].append(neighbor)
            if neighbor == d:
                path = buildPath(parent, d)
                return path
    if d:
        return None
    return Tree


# DFS
def DFS(visited, AdjA, node, source):
    if visited[node-1] == False:
        print(f"visiting {node} from {source}")
        visited[node-1] = True
        for neighbor in AdjA[node-1]:
            DFS(visited, AdjA, neighbor, node)
    else:
        #print(f"visited already {node} from {source}")
        pass

# DFSMain
def DFSMain(V, AdjA, s):
    visited = [ False for _ in range(len(V))]
    DFS(visited, AdjA, s, None)
    
# Prim's algorithm
def Prim( V, E, r):
    AdjM = G(V, E)
    
    S = [False] * len(V)
    P = [None] * len(V)
    W = [math.inf] * len(V)
    W[r-1] = 0
    Q = heapdict()
    for i in range(len(V)):
        Q[i] = W[i]
    
    S[r-1] = True
    
    while len(Q) > 0:
        u, weight = Q.popitem()
        print(f"extract {u+1} with weight {weight}")
        S[u] = True
        for v in range(len(V)):
            if v == r-1: continue
            print(f"adj {v+1} with weight {AdjM[u][v]} comparing {W[v]}")
            if S[v] == False and AdjM[u][v] < W[v]:  
                W[v] = AdjM[u][v]
                Q[v] = W[v]
                P[v] = u+1
    print(W)
    print(P)
    

memo = None

def make1(x):
    global memo
    if x < 0 or int(x) != x: return math.inf
    x = int(x)
    if x == 1: return 0
    if x == 2 or x == 3: return 1
    if memo[x-1] != math.inf:
        return memo[x-1]
    values = [make1(x-1), make1(x/3), make1(x/2)]
    value = min(values)
    memo[x-1] = value + 1
    if value == values[0]:
        print(x, x-1)
    elif value == values[1]:
        print(x, x/3)
    else:
        print(x, x/2)
    return memo[x-1]
    
    
    
if __name__ == "__main__":
    V = [ i+1 for i in range(7)]
    print(V)

    E = [ ((1, 2), 8), ((2, 3), 10), ((1, 4), 9), ((4, 3),5), ((1, 5), 11), ((5, 4), 13), ((4,7), 12), ((5, 6), 8), ((6, 7), 7) ]
    
    sortedE = sorted(E, key=lambda el: el[1])
    
    P = [ i+1 for i in range(len(V))]
    D = [0] * len(V)
    
    def find(x):
        if P[x-1] == x: return P[x-1]
        return find(P[x-1])
    
    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX == rootY: return
        if D[rootX-1] < D[rootY-1]:
            P[rootX-1] = rootY
            return    
        P[rootY-1] = rootX
        if D[rootX-1] == D[rootY -1]:
            D[rootX-1] += 1
    
    for (x, y), w in sortedE:
        union(x,y)

    
    #Prim(V, E, 1)
    
    memo = [math.inf]*1000
    print(make1(1000))

    
    
