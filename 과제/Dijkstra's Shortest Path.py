import random
import math
import heapq

INF = math.inf

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

# 다익스트라 알고리즘
# 하나의 시작 정점을 중심으로 다른 모든 정점까지의 최단 거리를 구하는 알고리즘
# 간선의 가중치는 0 아니면 양수여야 함, 음수가 있다면 사용 불가능

# 1. 시작 정점의 거리는 0, 나머지 정점은 무한대로 설정
# 2. 최소 거리부터 탐색을 위한 우선 순위 큐 사용
# 3. 현재 최단 거리가 가장 짧은 정점을 우선 순위 큐에서 꺼냄
# 4. 해당 정점과 연결된 이웃 정점들 검사
# 5. 현재 거리에 이웃 정점까지의 가중치를 더한 값이 기존 거리보다 크다면 거리 갱신
# 6. 갱신된 정점을 다시 우선 순위 큐에 넣음
# 7. 모든 정점이 처리될 때까지 반복
def Dijkstra(AdjA: list, E: dict, start: int):

    # 거리를 저장할 리스트, 모든 정점까지의 거리를 무한대로 설정
    distanceList = [INF for _ in range(len(AdjA))]

    distanceList[start - 1] = 0  # 시작 노드의 거리를 0으로 설정

    # 우선 순위 큐에 사용할 리스트
    q = []

    # 거리, 정점을 우선 순위 큐에 넣음
    heapq.heappush(q, (0, start)) 

    while q:
        # 현재 가장 작은 가중치, 정점를 우선 순위 큐에서 꺼냄
        currentCost, node = heapq.heappop(q)

        # 이미 더 짧은 거리가 있다면 넘어감
        if distanceList[node - 1] < currentCost:
            continue
        
        # 현재 정점에 연결된 모든 이웃 정점 탐색
        for neighbor in AdjA[node - 1]:
            # 간선 가중치를 얻기 위해 현재 정점과 이웃 정점을 (작은 것, 큰 것)으로 받아옴
            edge = (min(node, neighbor), max(node, neighbor))

            # 간선 가중치 조회
            cost = E[edge]

            # 현재 거리에 간선의 가중치를 더함
            newCost = currentCost + cost

            # 위 값이 기존 거리보다 작다면
            if newCost < distanceList[neighbor - 1]:
                # 새로 거리로 갱신
                distanceList[neighbor - 1] = newCost
                heapq.heappush(q, (newCost, neighbor))

    print(f"시작 정점 {start} 최단 거리 리스트: {distanceList}")
            
    
if __name__ == "__main__":
    print(V)
    print(E)
    print(AdjA)

    Dijkstra(AdjA, E, 1)
    Dijkstra(AdjA, E, 2)
    Dijkstra(AdjA, E, 3)
    Dijkstra(AdjA, E, 4)
    Dijkstra(AdjA, E, 5)
    Dijkstra(AdjA, E, 6)
    Dijkstra(AdjA, E, 7)
    Dijkstra(AdjA, E, 8)

    