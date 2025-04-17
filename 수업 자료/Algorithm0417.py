import random

class Graph:
    def __init__(self, nodeNum : int):
        self.nodeNum = nodeNum
        self.list = [[]for _ in range(nodeNum)]

    def AddNode(self, A , B ):
        
        self.list[A].append(B)
        self.list[B].append(A)

        
    def print(self):
        for i in range(self.nodeNum):
            print(f"{i} -> {self.list[i]}")

        

# 교수님 코드
class Graph:
    def __init__(self, lst: list[str]):
        self.city2idx = {city: idx for idx, city in enumerate(lst)}
        self.idx2city = {idx: city for city, idx in self.city2idx.items()}
        self.size = len(lst)
        self.adj_matrix = [[0 for _ in range(self.size)] for _ in range(self.size)]

    def add_edge(self, city1: str, city2: str, weight : int):
        i, j = self.city2idx[city1], self.city2idx[city2]
        self.adj_matrix[i][j] += 1
        self.adj_matrix[j][i] += 1  # 양방향 그래프일 경우

    def show(self):
        for i in range(self.size):
            city_name = self.idx2city[i]
            connections = self.adj_matrix[i]
            print(f"{city_name} → {connections}")



if __name__ == "__main__":

    cities = ["서울", "용인", "세종", "청주", "대전"]
    g = Graph(cities)

    g.add_edge("서울", "용인", 5)
    g.add_edge("서울", "세종", 15)
    g.add_edge("용인", "세종", 7)
    g.add_edge("용인", "청주", 5)

    g.show()
    
