class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []

    def add_edge(self, v, u):
        self.add_vertex(v)
        self.add_vertex(u)

        self.graph[v].append(u)
        self.graph[u].append(v)

    def display(self):
        for vertex in self.graph:
            print(f"{vertex} --> {self.graph[vertex]}")


g = Graph()
while True:
    ch = int(input("""0. Exit
1. Create Edge
2. Display
Enter your choice: """))
    
    if ch == 0:
        break
    elif ch == 1:
        v = input("enter vertex: ")
        u = input("enter neighbour: ")
        g.add_edge(v,u)
    elif ch == 2:
        g.display()
    else:
        print("Invalid Choice...")
    