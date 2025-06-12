V = [i+1 for i in range(0, 8)]

E = [(1, 2), (1, 3), (1, 4), (2, 3), (3, 4), (3, 5), (4, 6), (4, 7), (6,7), (6, 8), (7, 8)]

AdjA = [[] for _ in range(len(V))]

for row, col in E:
    AdjA[row-1].append(col)
    AdjA[col-1].append(row)

print(AdjA)

def buildPath(parent : list, dest):
    path = [dest]
    current = dest
    while parent[current-1] != -1:
        path.append(parent[current-1])
        current = parent[current-1]
    path.reverse()
    return path


def BFS(V, AdjA, s, d : int = None):
    parent = [-1 for _ in range(len(V))]
    Tree = [[] for _ in range(len(V))]
    visited = [False for _ in range(len(V))]

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
                Tree[current-1].append(neighbor)

            if neighbor == d:
                path =buildPath(parent, d)
                return path
    if d:
        return None
    return Tree 

def DFS(visited, AdjA, node, resource, path : list):
    if visited[node-1] == False:
        visited[node-1] = True
        path.append(node)
        for neighbor in AdjA[node-1]:
            DFS(visited, AdjA, neighbor, node, path)
    else:
        pass

def DFSMain(V, AdjA, start):
    visited = [False for _ in range(len(V))]
    path = []
    DFS(visited, AdjA, 1, None, path)
    return path

if __name__ == "__main__":
    print(BFS(V, AdjA, 2, 7))
    path = DFSMain(V, AdjA, 1)
    print(path)
    