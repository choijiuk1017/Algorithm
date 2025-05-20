import random
import math
import heapq

INF = math.inf

V = [ i+1 for i in range(8) ]

# 간선의 정보
# 연결된 간선 + 가중치
E = { 
     (1, 2) : random.randint(-10, 10), 
     (1, 3) : random.randint(-10, 10), 
     (1, 4) : random.randint(-10, 10),
     (2, 3) : random.randint(-10, 10),
     (3, 4) : random.randint(-10, 10),
     (3, 5) : random.randint(-10, 10),
     (4, 6) : random.randint(-10, 10),
     (4, 7) : random.randint(-10, 10),
     (6, 7) : random.randint(-10, 10),
     (6, 8) : random.randint(-10, 10),
     (7, 8) : random.randint(-10, 10)
    } 

AdjA = [ [] for _ in range(len(V))]
for row, col in E:
    AdjA[row-1].append(col)
    AdjA[col-1].append(row)
# 벨만 포드 알고리즘
# 모든 간선을 반복하고 검사하며 거리를 완화하여 점점 더 짧은 거리로 갱신함

# 1. 시작 정점의 거리는 0, 나머지는 무한대로 설정
# 2. 매 반복마다 모든 간선을 순회하며 검사함
# 3. 더 짧은 거리의 간선이 발견되면 최단 거리 값 갱신
def BellmanFord(AdjA: list, E: dict, start: int):
    # 거리를 저장할 리스트, 모든 정점까지의 거리를 무한대로 설정
    distanceList = [INF for _ in range(len(AdjA))]

    distanceList[start - 1] = 0  # 시작 노드의 거리를 0으로 설정

    # 정점의 수 - 1까지 반복
    for _ in range(len(AdjA) - 1):
        # 한 정점과 그 정점의 이웃에 대한 모든 간선 검사
        for (node, neighbor), cost in E.items():
            # 만약 이웃 정점까지 가는 간선 중 더 비용이 적은 간선이 있다면 갱신
            if distanceList[node - 1] != INF and distanceList[node - 1] + cost < distanceList[neighbor - 1]:
                distanceList[neighbor - 1] = distanceList[node - 1] + cost

    print(f"시작 정점 {start} 최단 거리 리스트 : {distanceList}")


if __name__ == "__main__":
    print(V)
    print(E)
    print(AdjA)
    BellmanFord(AdjA, E, 1)
    BellmanFord(AdjA, E, 2)
    BellmanFord(AdjA, E, 3)
    BellmanFord(AdjA, E, 4)
    BellmanFord(AdjA, E, 5)
    BellmanFord(AdjA, E, 6)
    BellmanFord(AdjA, E, 7)
    BellmanFord(AdjA, E, 8)

