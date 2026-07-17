def add_vertex(v):
    if v not in graph:
        graph[v] = []

def add_edge(u,v):
    add_vertex(u)
    add_vertex(v)

    graph[u].append(v)
    graph[v].append(u)

def get_path(v, tar, path, visibility):
    if v == tar:
        print(path)
        return
    
    for n in graph[v]:
        if n not in visibility:
            visibility.append(n)
            get_path(n, tar, path + " -> " +n, visibility)
            visibility.pop()

graph = {}

while True:
    ch = int(input("""0. Exit
1. Create Edge
2. Get Path
Enter your choice: """))
    
    if ch == 0:
        break
    elif ch == 1:
        v = input("enter vertex: ")
        u = input("enter neighbour: ")
        add_edge(v,u)
    elif ch == 2:
        v = input("enter vertex: ")
        tar = input("enter vertex: ")
        get_path(v, tar, v, [v])
    else:
        print("Invalid Choice...")