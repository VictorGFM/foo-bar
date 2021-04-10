from Queue import Queue
import copy

class Node:
    def __init__(self, row, col, dist):
        self.row = row
        self.col = col
        self.dist = dist

def findShortestPath(map, N, M):
    start = Node(0, 0, 1) 
    visited = copy.deepcopy(map)
    visited[start.row][start.col] = 1
    
    queue = Queue()
    queue.put(start)
    
    while(not queue.empty()):
        item = queue.get()
        if((item.row == N-1) and (item.col == M-1)):
            return item.dist
        if((item.row - 1 >= 0) and visited[item.row-1][item.col] == 0):
            queue.put(Node(item.row-1, item.col, item.dist+1))
            visited[item.row-1][item.col] = 1
        if((item.row + 1 < N) and visited[item.row+1][item.col] == 0):
            queue.put(Node(item.row+1, item.col, item.dist+1))
            visited[item.row+1][item.col] = 1
        if((item.col - 1 >= 0) and visited[item.row][item.col-1] == 0):
            queue.put(Node(item.row, item.col-1, item.dist+1))
            visited[item.row][item.col-1] = 1
        if((item.col + 1 < M) and visited[item.row][item.col+1] == 0):
            queue.put(Node(item.row, item.col+1, item.dist+1))
            visited[item.row][item.col+1] = 1

    return float('inf')

def solution(map):
    # Your code here
    N = len(map)
    M = len(map[0])
    shortestPath = findShortestPath(map, N, M)
    for i in range(N):
        for j in range(M):
            if(map[i][j]):
                modifiedMap = copy.deepcopy(map)
                modifiedMap[i][j] = 0
                shortestPathModified = findShortestPath(modifiedMap, N, M)
                if(shortestPathModified < shortestPath):
                    shortestPath = shortestPathModified
    return shortestPath

map = [[0, 1], 
       [1, 0]]

""" map = [[0, 1, 1, 0], 
       [0, 0, 0, 1], 
       [1, 1, 0, 0], 
       [1, 1, 1, 0]] """

""" map = [[0, 0, 0, 0, 0, 0],
       [1, 1, 1, 1, 1, 0],
       [0, 0, 0, 0, 0, 0],
       [0, 1, 1, 1, 1, 1],
       [0, 1, 1, 1, 1, 1],
       [0, 0, 0, 0, 0, 0]] """

print(solution(map))