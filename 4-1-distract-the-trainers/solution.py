def solution(bananaList):
    #Your code here
    graph = createGraph(bananaList)
    maxPairedTrainers = getMaxPairedTrainers(graph)
    unpairedTrainers = len(bananaList) - maxPairedTrainers
    return unpairedTrainers

def createGraph(bananaList):
    graph = {i: [] for i in range(len(bananaList))}
    for i in range(len(bananaList)):
        for j in range(i+1, len(bananaList)):
            if isInfiniteLoop(bananaList[i], bananaList[j]):
                graph[i].append(j)
                graph[j].append(i)
    return graph

def isInfiniteLoop(x,y):
    base = (x+y)//gcd(x,y)
    return bool(base & (base - 1))

def gcd(a,b):
    while b:
        a, b = b, a % b
    return a

def getMaxPairedTrainers(graph):
    paired = 0
    maxDegreeNode = max(graph, key=lambda key: len(graph[key]))
    maxDegreeGraph = len(graph[maxDegreeNode])
    while len(graph) > 1 and maxDegreeGraph >= 1:
        minDegreeNode = min(graph, key=lambda key: len(graph[key]))
        if (len(graph[minDegreeNode])) < 1 :
            del graph[minDegreeNode]
        else:
            secondMinDegreeNode =  graph[minDegreeNode][0]
            for neighbourNode in graph[minDegreeNode]:
                if len(graph[neighbourNode]) < len(graph[secondMinDegreeNode]):
                    secondMinDegreeNode = neighbourNode
                for i in range(len(graph[neighbourNode])):
                    if graph[neighbourNode][i] == minDegreeNode:
                        del graph[neighbourNode][i]
                        break
            for neighbourNode in graph[secondMinDegreeNode]:
                for i in range(len(graph[neighbourNode])):
                    if graph[neighbourNode][i] == secondMinDegreeNode:
                        del graph[neighbourNode][i]
                        break
            del graph[minDegreeNode]
            del graph[secondMinDegreeNode]
            paired += 2
        if len(graph) > 1:
            maxDegreeNode = max(graph, key=lambda key: len(graph[key]))
            maxDegreeGraph = len(graph[maxDegreeNode])
    return paired

bananaList = [1, 7, 3, 21, 13, 19]
#bananaList = [1,1]

print(solution(bananaList))