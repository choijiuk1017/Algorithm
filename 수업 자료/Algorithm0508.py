'''
from collections import deque
import math
INF = math.inf

class AdjacencyMatrix:
    def __init__(self, lst : list[int]):
        self.node2idx = {node : idx for idx, node in enumerate(lst)}
        self.idx2node = {idx : node for node, idx in self.node2idx.items()}
        self.size = len(lst)
        self.adj_matrix = [[INF for _ in range(self.size)] for _ in range(self.size)]

    def add_edge(self, node : int, neighbor : int):
        i, j = self.node2idx[node], self.node2idx[neighbor]
        self.adj_matrix[i][j] = 1
        self.adj_matrix[j][i] = 1

    def show(self):
        for i in range(self.size):
            nodeNum = self.idx2node[i]
            connections = self.adj_matrix[i]
            print(f"{nodeNum} -> {connections}")
            

class AdjacencyList:
    def __init__(self, lst : list[int]):
        self.lst = lst
        self.size = len(lst)
        self.adj_List = [[] for _ in range(self.size)]

    def add_edge(self, nodeNum : int, neighbor : int):
        self.adj_List[nodeNum-1].append(neighbor)
        self.adj_List[neighbor-1].append(nodeNum)

    def BFS(self, start : int):
        queue = deque([start])
        visited = set([start])

        while(queue):
            currentNode = queue.popleft()
            for nextNode in self.adj_List[currentNode-1]:
                if(nextNode not in visited):
                    visited.add(nextNode)
                    queue.append(nextNode)
                    print(nextNode, end=' ')


    def show(self):
        for i in range(self.size):
            print(f"{self.lst[i]} -> {self.adj_List[i]}")

        
        
if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5, 6, 7, 8]

    adj_m = AdjacencyMatrix(lst)

    adj_m.add_edge(1, 2)
    adj_m.add_edge(2, 1)
    adj_m.add_edge(1, 4)
    adj_m.add_edge(4, 7)
    adj_m.show()
    
    print(' ')

    adj_l = AdjacencyList(lst)

    adj_l.add_edge(1, 2)
    adj_l.add_edge(1, 3)
    adj_l.add_edge(1, 4)
    adj_l.add_edge(3, 5)
    adj_l.add_edge(4, 6)
    adj_l.add_edge(4, 7)
    adj_l.add_edge(6, 8)

    adj_l.show()

    adj_l.BFS(1)

'''

import math
 # adjacenyMatrix
V = [ i+1 for i in range(8)]

E = [ (1, 2), (1, 3), (1, 4), (2, 3), (3, 4),(3,5), (4, 6), (4, 7),(6,7), (6, 8), (7, 8)]

print(V)

AdjM = [ [ math.inf for _ in range(len(V))] for _ in range(len(V)) ]
for row, col in E:    
    AdjM[row-1][col-1] = 1
    AdjM[col-1][row-1] = 1
    
print(AdjM)

# AdjacencyArray

AdjA = [ [] for _ in range(len(V))]
for row, col in E:
    AdjA[row-1].append(col)
    AdjA[col-1].append(row)

print(AdjA)

print(3 < math.inf)
print(3 < -math.inf)

def BFS(lst : list, start : int):
    nodelist = []
    nodelist.append(start)
    visited = set([start]) 

    while(nodelist):
        currentNode = nodelist.pop(0)
        for nextNode in lst[currentNode - 1]:        
            if(nextNode not in visited):               
                visited.add(nextNode)
                nodelist.append(nextNode)
                print(f"정점 {currentNode}와 연결된 노드{nextNode}")

def BFS2(lst :list, start : int, goal : int):
    nodeList = []
    nodeList.append(start)
    path = []
    path.append(start)
    visited = set([start])

    while(nodeList):
        currentNode = nodeList.pop(0)
        for nextNode in lst[currentNode -1]:
            if(nextNode not in visited):
                if(nextNode == goal):
                    visited.add(nextNode)
                    print(f"목적지 {goal} 도착, {currentNode}와 연결되었음")
                    print(path)
                    return
                visited.add(nextNode)
                nodeList.append(nextNode)
                path.append(nextNode)
                print(f"목적지까지 탐색을 위해 정점{currentNode}부터 {nextNode}까지 탐색")

# buildPath
def buildPath(parent: list, dest):
    path = [dest]
    current = dest
    while parent[current-1] != -1:
        path.append(parent[current-1])
        current = parent[current-1]
    path.reverse()
    return path
    
#교수님 코드
def BFS3(V, AdjA, s, d: int = None):
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
                print(path)
    if d:
        return None
    return Tree

def DFS(V, AdjA, s, d: int = None, visited = None, Tree = None, parent = None):
    if(visited == None):
        visited = []
    if(Tree == None):
        Tree = [ [] for _ in range(len(V))]
    # if(parent == None):
         # parent = [ -1 for _ in range(len(V))]
    
    visited.append(s)
    
    for neighbor in AdjA[s-1]:
        if (neighbor != d and neighbor not in visited):
            print(f"visited {s}->{neighbor}")
            Tree[s-1].append(neighbor)
            found = DFS(V, AdjA, neighbor, d, visited, Tree, parent)
            if found:
                return True
            
        if neighbor == d:  
            visited.append(neighbor)
            print(f"visited {s}->{neighbor}")
            # path = buildPath(parent, d)
            print(Tree)     
            print(visited)
            # print(path)   
            return True

    return False

if __name__ == "__main__":
    '''
    BFS(AdjA, 1)
    BFS2(AdjA, 1, 4)
        
    '''
    # BFS3(V, AdjA, 1, 5)  
    # print(' ')
    DFS(V, AdjA, 1, 8)