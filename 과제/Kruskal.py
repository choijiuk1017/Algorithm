import random

V = [ i+1 for i in range(8) ]

# 간선의 정보
# 연결된 간선 + 가중치
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


# 크루스칼 알고리즘
# 1. 모든 간선을 가중치 순으로 오름차순으로 정렬함
# 2. 하나씩 꺼내면서 간선의 사이클이 생기지 않게 저장
# 3. 위 과정을 거치며 간선이 모든 정점을 연결할 때까지 반복
# 간선의 정보를 받아서 처리
def Kruskal(E : dict):
    visited = [] # 방문한 정점의 순서를 저장할 리스트
    edgeList = [] # 연결할 간선을 저장할 리스트

    # 간선의 가중치 기준으로 오름차순 정렬
    sortEdge = dict(sorted(E.items(), key= lambda item: item[1]))

    # 정렬된 딕셔너리를 리스트로 저장
    vertexList = list(sortEdge.keys())

    print(f"가중치 기준 정렬 : {sortEdge}")
    print(f"정렬된 간선 리스트 : {vertexList}")

    # 간선 리스트가 빌 때까지 반복
    while(vertexList):

        # 첫 번째 간선의 정점들을 받아옴
        first, edge = vertexList[0]
        
        # 간선의 이웃 정점이 방문한 적이 없다면
        if(edge not in visited):

            # 해당 정점 방문 처리
            visited.append(edge)

            # 해당 간선 저장
            edgeList.append((first, edge))

            # 리스트에서 삭제하고 넘어감
            vertexList.pop(0)
            continue
        
        # 간선의 시작 정점과 이웃 정점이 이미 방문한 적이 있는 경우, 즉 이미 연결되어 있는 경우
        if(first in visited or edge in visited):
            # 리스트에서 삭제하고 넘어감
            vertexList.pop(0)
            continue

        # 위 조건을 모두 충족하지 않을 경우

        # 해당 간선 및 정점들 저장
        visited.append(first)
        visited.append(edge)
        edgeList.append((first, edge))

        # 리스트에서 삭제함
        vertexList.pop(0)
        
    print(f"방문한 정점 순서 : {visited}")
    print(f"연결할 간선 : {edgeList}")

# 인터넷 검색 및 지피티를 참고한 크루스칼 알고리즘

# 특정 노드 x의 부모를 찾는 함수
def Find(parent, x):
    if parent[x] != x:
        # 최상위 부모를 찾을 때까지 재귀
        parent[x] = Find(parent, parent[x])
    return parent[x]

# 두 집합을 합치는 함수, x y가 서로 다른 집합일 때만 병합함
def Union(parent, x, y):
    x_root = Find(parent, x)
    y_root = Find(parent, y)

    if x_root == y_root:
        return False
    
    parent[y_root] = x_root
    return True

# 크루스칼 알고리즘 함수
def Kruskal2(V : list, E : dict):
    # 간선 딕셔너리, 리스트 [(u, v , 가중치)] 형태로 변환
    edge_list = [(u, v, w) for (u, v), w in E.items()]

     # 가중치 기준으로 간선 정렬
    edge_list.sort(key=lambda x: x[2])

    # Union, Find 함수를 사용하기 위한 초기화
    parent = {v: v for v in V}

    # 최소 신장 트리에 포함될 간선들
    mst = []

    # 최소 신장 트리의 총 가중치
    total_cost  = 0

    # 간선을 하나씩 확인하며 MST 구성
    for u, v, w in edge_list:
        if Union(parent, u, v):  # 두 정점이 서로 다른 집합일 경우
            mst.append((u, v, w)) # 해당 간선 MST에 추가
            total_cost += w # 비용 누적
        # MST의 간선 수가 정점-1 이면 종료
        if len(mst) == len(V) - 1:
            break

    print(f"선택된 간선들 (MST): {mst}")

    print("총 비용:", total_cost)

if __name__ == "__main__":
    print(V)
    print(E)
    print(AdjA)

    Kruskal(E)
    Kruskal2(V, E)
    
