def create(v):
    for i in range(v):
        for j in range(v):
            if  i != j:
                graph[i][j] = int(input(f"Is {i} neighbour of {j} [1/0]: "))
    

def readGraph(v):
    print("Vertex    In-Degree    Out-Degree    Total")
    
    for i in range(v):
        od = 0
        id = 0
        for j in range(v):
            if graph[i][j]:
                od += 1
            if graph[j][i]:
                id += 1
        print(f"   {i}          {id}             {od}            {id + od}")

v = int(input("enter no of vertex: "))
graph = [[0]*v for i in range(v)]

create(v)
readGraph(v)