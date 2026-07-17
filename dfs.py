def add_vertex(v):
    graph[v] = []

def add_edge(u,v):
    add_vertex(u)
    add_vertex(v)

    graph[v].append(u)
    graph[u].append(v)

def dfs(node, visited):
    visited.add(node)
    print(node, end = " ")

    for n in graph[node]:
        if n not in visited:
            dfs(n, visited)

graph = {}

while True:
    ch = int(input("""\n0. Exit
1. Create Edge
2. DFS
Enter your choice: """))
    
    if ch == 0:
        break
    elif ch == 1:
        v = int(input("enter vertex: "))
        u = int(input("enter neighbour: "))
        add_edge(v,u)
    elif ch == 2:        
        v = int(input("enter starting node: "))
        visited = set()
        dfs(v,visited)
    else:
        print("Invalid Choice...")