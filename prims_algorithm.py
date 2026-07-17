def add_vertex(v):
    if v not in graph:
        graph[v] = []

def add_edge(v,u,w):
    add_vertex(v)
    add_vertex(u)

    graph[v].append((u,w))
    graph[u].append((v,w))

def display():
    for v in graph:
        print(v, " --> ", graph[v])

def prims(st):
    mst = []
    visited = {st}

    total_cost = 0

    while len(visited) < len(graph):
        u = None
        v = None
        min_weight = float('inf')
        for vertex in visited:
            for neighbour, weight in graph[vertex]:
                if neighbour not in visited and weight < min_weight:
                    min_weight = weight
                    u = vertex
                    v = neighbour

        total_cost += min_weight
        visited.add(v)
        mst.append((u,v,min_weight))

    print("\nMinimum Spanning Tree:")
    for u, v, w in mst:
        print(f"{u} --- {v} = {w}")

    print("\nTotal Cost: ", total_cost)



graph = {}

while True:
    ch = int(input("""
0. Exit
1. Add Edge
2. Display Graph
3. Prim's Algorithm
Enter choice: """))
    
    if ch == 0:
        break

    elif ch == 1:
        u = input("Enter source vertex: ")
        v = input("Enter destination vertex: ")
        w = int(input("Enter weight: "))
        add_edge(u, v, w)

    elif ch == 2:
        print("\nGraph:")
        display()

    elif ch == 3:
        start = input("Enter starting vertex: ")
        if start in graph:
            prims(start)
        else: 
            print("Vertex not found.")

    else:
        print("Invalid Choice")