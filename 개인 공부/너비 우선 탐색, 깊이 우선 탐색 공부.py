from collections import deque # 파이썬에서 자주 사용하는 큐 모듈
# 너비 우선 탐색
# 큐를 사용하는 것이 가장 효과적
# 시작 정점에서 가장 가까운 정점부터 탐색함
# 정점을 큐에 저장하며 경로로 지정
def BFS(graph : list, start : str):
    queue = deque([start]) # 시작 정점을 큐에 넣음
    visited = set([start]) # 방문한 정점을 기록함
    print(start, end=' ')   # 시작 정점 표시
    while(queue): # 큐가 비어있지 않은 동안 반복
        current = queue.popleft() # 큐의 맨 앞 노드를 꺼냄
        for next in graph[current]: # 꺼낸 노드의 이웃 정점들 순회
            if(next not in visited): # 방문하지 않은 이웃 정점만 처리
                visited.add(next) # 방문한 이웃 정점 기록
                queue.append(next) # 큐에 추가해서 다음에 탐색
                print(next, end=' ') 

# 깊이 우선 탐색
# 스택, 재귀를 이용하여 구현
# 시작 정점에서 가장 깊은 정점부터 탐색함
def DFS(graph, node, visited=None):
    if visited is None: # 처음 호출 시 visited가 없다면 새로 생성
        visited = set()

    visited.add(node) # 현재 노드를 방문 처리
    print(node, end=' ') # 방문한 노드 출력
    
    for neighbor in graph[node]: # 현재 노드의 이웃들을 순회
        if neighbor not in visited: # 아직 방문하지 않은 노드만 처리
            DFS(graph, neighbor, visited) # 재귀 호출로 깊이 탐색

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['E'],
        'D': [],
        'E': []
    }

    BFS(graph, 'A')
    print('')
    DFS(graph, 'A')
