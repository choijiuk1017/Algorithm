import random
import heapq


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

# AdjacencyArray
AdjA = [ [] for _ in range(len(V))]
for row, col in E:
    AdjA[row-1].append(col)
    AdjA[col-1].append(row)

# print(3 < math.inf)
# print(3 < -math.inf)

# 프림 알고리즘
# 1. 시작 정점을 선택함
# 2. 연결된 정점 중 가장 가중치가 작은 정점 선택
# 3. 해당 간선으로 연결된 정점에서 다시 가중치가 작은 정점 선택
# 4. 위 과정을 모든 정점이 연결될 때까지 반복
# 간선 정보, 인접 배열, 시작 정점에 대한 정보 필요
def Prim(E : dict, AdjA : list, start : int):
    visited = [] # 최소 값의 간선을 연결한 결과를 보여줄 리스트
    q = [] # 힙큐로 저장할 리스트

    visited.append(start) # 시작 지점 저장

    prevCost = 11 # 이전의 간선 가중치를 확인할 변수, 10이 최대 가중치이기 때문에 시작은 11로 시작

    totalCost = 0 # 총 가중치의 합을 저장할 변수
    
    # 시작 정점의 이웃 정점에 대한 반복
    for neighbor in AdjA[start-1]:
        cost = E[(start,neighbor)] # 이웃 정점과의 간선의 가중치를 구함
        if(cost < prevCost): # 이웃 정점과의 가중치가 이전보다 작다면
            neighborNode = neighbor # 최종 이웃 정점으로 지정
            prevCost = cost # 현재 가중치를 이전 가중치로 설정하고 다음으로 넘어감

    # 반복이 끝나고 나온 최종 이웃 정점은 시작 정점에서 연결할 수 있는 가장 최소의 가중치를 가진 정점임
    # 이 정점에 대한 가중치와 정점 정보를 우선 순위 큐에 저장
    heapq.heappush(q, (prevCost, neighborNode))

    # 우선 순위 큐가 빌 때까지 반복함
    while(q):
        # 가중치와 정점 정보를 우선 순위 큐에서 꺼냄
        cost, node = heapq.heappop(q) 

        # 정점이 방문한 적이 있는 정점이면 넘어감
        if(node in visited):
            continue
        
        # 정점이 방문한 적 없다면 추가
        visited.append(node)
        totalCost += cost
        
        # 현재 처리하고 있는 정점의 이웃 정점 확인
        for neighbor in AdjA[node-1]:

            # 이웃 정점이 방문한 적이 없다면
            if neighbor not in visited:
                # 해당 정점에 대한 가중치를 받아서 우선 순위 큐에 저장함
                edgeCost = E[(min(node, neighbor), max(node, neighbor))]
                heapq.heappush(q, (edgeCost, neighbor))

    print(visited)
    print(f"총 비용{totalCost}")


if __name__ == "__main__":
    print(V)
    print(E)
    print(AdjA)

    Prim(E, AdjA, 1)
