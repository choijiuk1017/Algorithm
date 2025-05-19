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
def Dijkstra(AdjA: list, E: dict, start: int):
    distanceList = [INF for _ in range(len(AdjA))]
    distanceList[start - 1] = 0  # 시작 노드의 거리 = 0

    q = []
    heapq.heappush(q, (0, start))  # (거리, 노드 번호)

    while q:
        currentCost, node = heapq.heappop(q)

        if distanceList[node - 1] < currentCost:
            continue

        for neighbor in AdjA[node - 1]:
            # 간선의 가중치는 (작은 번호, 큰 번호) 형식으로 찾기
            edge_key = (min(node, neighbor), max(node, neighbor))
            cost = E[edge_key]

            newCost = currentCost + cost

            if newCost < distanceList[neighbor - 1]:
                distanceList[neighbor - 1] = newCost
                heapq.heappush(q, (newCost, neighbor))

    print(f"최단 거리 리스트: {distanceList}")
            
    




if __name__ == "__main__":
    print(V)
    print(E)
    print(AdjA)

    Dijkstra(AdjA, E, 1)

    