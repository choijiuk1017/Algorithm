import math
import heapq

# 교수님의 프림 알고리즘

def G(V, E): 
    AdjM = [ [ math.inf for _ in range(len(V))] for _ in range(len(V)) ]
    for (row, col), weight in E:    
        AdjM[row-1][col-1] = weight
        AdjM[col-1][row-1] = weight
    return AdjM

# Prim's algorithm
def Prim( V, E, r):
    AdjM = G(V, E)
    
    S = [ 0 for _ in range(len(V))]
    P = [ None for _ in range(len(V))]
    W = [ math.inf for _ in range(len(V))]
    W[r-1] = 0
    Q = []
    for col in range(len(W)):
        if col != r-1 and AdjM[r-1][col] != math.inf:
            W[col] = AdjM[r-1][col]
            P[col] = r
    for i in range(len(W)):
        if i+1 == r: continue
        heapq.heappush( Q, (W[i], i+1) )
    S[r-1] = 1
    while len(Q) > 0:
        weight, u = heapq.heappop(Q)
        print(f"extract {u} with weight {weight}")
        S[u-1] = 1
        for v in range(len(V)):
            if v == r-1: continue
            print(f"adj {v+1} with weight {AdjM[u-1][v]} comparing {W[v]}")
            if S[v] == 0 and AdjM[u-1][v] < W[v]:  
                Q.remove( (W[v], v+1))
                W[v] = AdjM[u-1][v]
                heapq.heappush(Q, (W[v], v+1))
                P[v] = u
    print(W)
    print(P)
    

def make1(x : int):
    print(x)
    if x < 0:
        return math.inf
    if x== 1:
        return 0
    if x == 2 or x == 3:
        return 1
    if int(x) != x:
        return math.inf
    return min(make1(x-1), make1(x/2), make1(x/3)) +1    
    
    
if __name__ == "__main__":
    V = [ i+1 for i in range(7)]
    print(V)

    E = [ ((1, 2), 8), ((2, 3), 10), ((1, 4), 9), ((4, 3),5), ((1, 5), 11), ((5, 4), 13), ((4,7), 12), ((5, 6), 8), ((6, 7), 7) ]
    
    Prim(V, E, 1)
    
    print(make1(200))



    
    
