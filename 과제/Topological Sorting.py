import random
import heapq

V = ["물 붇기", "점화", "수프 넣기", "라면 넣기", "봉지 뜯기", "계란 풀기"]

# E = [ (1, 2), (1, 3), (1, 4), (2, 3), (2, 8), (3, 4), (3, 5), (4, 6), (4, 7), (6, 7), (6, 8), (7, 8), (8 , 3), (8, 2)]
E = [("물 붇기", "점화"),
    ("점화", "수프 넣기"),
    ("점화", "라면 넣기"),
    ("점화", "계란 풀기"),
    ("봉지 뜯기", "라면 넣기"),
    ("봉지 뜯기", "수프 넣기"),
    ("라면 넣기", "계란 풀기"),
    ("수프 넣기", "계란 풀기")
    ]
     
AdjA = { v : [] for v in V}

for row, col in E:
    AdjA[row].append(col)


# 위상 정렬 알고리즘
# 1. 진입 차수, 즉 해당 정점으로 향하는 간선의 개수가 0인 정점들을 꺼냄
# 2. 정점을 하나씩 꺼내고 결과 리스트에 추가함
# 3. 꺼낸 정점과 연결된 모든 간선을 제거함
# 4. 모든 정점을 처리할 때까지 반복
def TopologicalSort(V : list, AdjA : dict):
    indegreeList = []
    i = 0
    lastVertex = 0

    # 다음 정점으로 연결되는 간선이 없는 정점, 즉 끝 정점을 찾음
    # 아래 과정에서는 간선이 없으면 끝내기 때문
    for last in AdjA.values():
        if last == []:
            lastVertex = V[i]
            i = 0
        i += 1

    # 진입 차수가 0인 정점들 우선으로 정렬
    while(any(AdjA.values())):
        isLinked = False 
        # 정점의 연결 간선과 비교
        for j in AdjA.values():
            # 연결되어 있으면 반복 안함
            if isLinked == True:
                break
            # 현재 정점이 어떠한 다른 정점의 연결 간선에 존재한다면 진입 차수가 0이 아님
            if V[i] in j:
                isLinked = True
                continue   
        # 현재 정점이 어떠한 정점의 연결 간선이 없고 이미 저장되지도 않았다면     
        if(isLinked == False and V[i] not in indegreeList):
            # 현재 정점은 진입 차수가 0 이므로 저장
            indegreeList.append(V[i])

            # 현재 정점의 모든 연결 간선을 지움
            AdjA[V[i]] = []

        # 한 번씩 인접 배열을 둘러봤고 아직 정점이 남아 있다면
        if(i == len(AdjA) - 1):
            # 처음부터 다시 확인
            i = 0 
        else:
            # 아니면 다음으로 넘어감
            i += 1
    # 맨 끝 정점, 즉 진입 차수가 가장 큰 정점 추가
    indegreeList.append(lastVertex)
    print(indegreeList)

if __name__ == "__main__":
    print(V)
    print(E)
    print(AdjA)

    TopologicalSort(V, AdjA)
