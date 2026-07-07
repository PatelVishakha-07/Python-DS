# using adjancency matrix
def add_edge(mat, i, j):
    mat[i][j] = 1
    mat[j][i] = 1

def display(mat):
    for m in mat:
        print(" ".join(map(str, m)))

mat = [[0] * 4 for _ in range(4)]

add_edge(mat, 0,1)
add_edge(mat, 0,2)
add_edge(mat, 1,2)
add_edge(mat, 2,3)

display(mat)