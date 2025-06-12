import math

# adjacenyMatrix

V = [ i+1 for i in range(8)]

E = [ (1, 2), (1, 3), (1, 4), (2, 3), (3, 4), (3, 5), (4, 6), (4, 7), (6,7), (6, 8), (7, 8)]

print(V)
'''
AdjM = [ [ math.inf for _ in range(len(V))] for _ in range(len(V)) ]
for row, col in E:    
    AdjM[row-1][col-1] = 1
    AdjM[col-1][row-1] = 1
    
print(AdjM)
'''

# AdjacencyArray
AdjA = [ [] for _ in range(len(V))]
for row, col in E:
    AdjA[row-1].append(col)
    AdjA[col-1].append(row)

print(AdjA)

# buildPath
# 경로 생성 함수
# parent: 각 정점의 부모를 담은 리스트, dest: 경로의 도착 정점
def buildPath(parent: list, dest):
    path = [dest] # 도착 정점을 경로 리스트에 먼저 추가
    current = dest # 현재 위치를 도착 정점으로 초기화
    while parent[current-1] != -1: # 시작 정점에 도달할 때까지 반복
        path.append(parent[current-1]) # 현재 노드의 부모를 경로에 추가
        current = parent[current-1] # 현재 노드를 그 부모로 갱신
    path.reverse() # 다 반복 후 결과 뒤집음
    return path # 경로 반환

# BFS
def BFS(V, AdjA, s, d: int = None): 
    parent = [ -1 for _ in range(len(V))] # 각 노드의 부모를 저장할 리스트
    Tree = [ [] for _ in range(len(V))] # BFS 트리 구조를 저장할 리스트
    visited = [ False for _ in range(len(V))] # 노드 방문 여부를 저장하는 리스트

    Q = [s] # BFS 탐색을 위한 큐, 시작 정점을 먼저 삽입
    visited[s-1] = True # 시작 정점 방문 처리

    while len(Q) > 0: #큐가 빌 때까지 반복
        current = Q.pop(0) # 큐에서 현재 정점을 꺼냄
        for neighbor in AdjA[current-1]: # 현재 정점에 인접한 모든 이웃에 대해 반복
            if visited[neighbor-1] == False: # 방문하지 않은 이웃이라면
                visited[neighbor-1] = True # 방문 처리
                Q.append(neighbor) # 이웃을 큐에 삽입하여 다음에 방문하도록 함
                if d: 
                    parent[neighbor-1] = current # 경로 추적을 위해 부모를 기록
                print(f"visited {current}->{neighbor}") # 방문 경로 출력
                Tree[current-1].append(neighbor) #트리에 자식으로 추가
            if neighbor == d: # 목적지 도달 시
                path = buildPath(parent, d) # 경로 구성
                return path # 경로 반환
    if d: # 목적지를 못찾았다면
        return None #반환 안함
    return Tree # 트리 구조 반환


# DFS
def DFS(visited, AdjA, node, source):
    if visited[node-1] == False: # 현재 노드가 아직 방문되지 않았다면
        print(f"visiting {node} from {source}") # 어디서 방문했는지 출력
        visited[node-1] = True # 현재 노드를 방문 처리
        for neighbor in AdjA[node-1]: # 현재 노드에 인접한 이웃에 대해 반복
            DFS(visited, AdjA, neighbor, node) # 재귀 호출로 이웃 노드 방문 (현재 노드는 부모가 됨)
    else:
        #print(f"visited already {node} from {source}")
        pass

# DFSMain
def DFSMain(V, AdjA, s):
    visited = [ False for _ in range(len(V))]
    DFS(visited, AdjA, s, None)
    
    
if __name__ == "__main__":
    print(AdjA)
    print(BFS(V, AdjA, 2, 7))
    path = DFSMain(V, AdjA, 1)
    print(path)
    
    
    
