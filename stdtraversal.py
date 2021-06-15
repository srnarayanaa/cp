from queue import deque
visitedDfs = set()
visitedBfs = set()
visitedLevel = set()

dfsArr = []
bfsArr = []
levelOrderArr  =[]

def dfs(src, children):
    if src in visitedDfs:
        return 
    visitedDfs.add(src)
    dfsArr.append(src)
    for i in G[src]:
        children.append(i)
    while children:
        i = children.pop()
        if i not in visitedDfs:
            dfs(i, children)
    return dfsArr
    
def levelOrder(src):
    q = deque()
    q.append(src)
    q.append(None)
    temp = []
    while q:
        node = q.popleft()
        if node is None:
            if temp: levelOrderArr.append(temp)
            temp = []
        else:
            temp.append(node)
            for i in G[node]:
                if i not in visitedLevel:
                    q.append(i)
                    visitedLevel.add(i)
            q.append(None)
    return levelOrderArr

def bfs(src):
    q = deque()
    q.append(src)
    while q:
        node = q.popleft()
        bfsArr.append(node)
        for i in G[node]:
            if i not in visitedBfs:
                q.append(i)
                visitedBfs.add(i)
    return bfsArr

N = int(input())
G = {}
for i in range(1, N+1, 1):
    G[i] = []

for i in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)

dfs(1, [])
print(dfsArr)
bfs(1)
print(bfsArr)
levelOrder(1)
print(levelOrderArr)
