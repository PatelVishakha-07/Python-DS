from collections import deque

graph = {}

def add_vertex(v):
    if v not in graph:
        graph[v] = []

def add_edge(v, u):
    add_vertex(v)
    add_vertex(u)

    graph[v].append(u)
    graph[u].append(v)

def bfs(v):
    visited = set()
    queue = deque([v])
    
    visited.add(v)

    while queue:
        val = queue.popleft()
        print(val, end = " ")

        for i in graph[val]:
            if i not in visited:
                queue.append(i)
                visited.add(i)

while True:
    ch = int(input("""\n0. Exit
1. Create Edge
2. BFS
Enter your choice: """))
    
    if ch == 0:
        break
    elif ch == 1:
        v = int(input("enter vertex: "))
        u = int(input("enter neighbour: "))
        add_edge(v,u)
    elif ch == 2:        
        v = int(input("enter starting node: "))
        bfs(v)    
    else:
        print("Invalid Choice...")

