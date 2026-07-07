""" 
The King is at position (1,1) on a 4×4 grid and needs to reach (4,4). The King can move one step in any of 8 directions. Model this as a BFS problem: (i) Write the BFS algorithm in Python using a queue to find the shortest path for the King. (ii) Trace the BFS showing queue state at each step on the 4×4 grid. (iii) What is the minimum number of moves required and what is the path?   """

from collections import deque

def bfs(start, target, size):
    queue = deque()

    queue.append((start, [start]))

    visited = set()
    visited.add(start)

    while queue:
        (row,col), path = queue.popleft()

        if (row, col) == target:
            return path
        
        for r,c in moves:
            new_r = row + r
            new_c = col + c

            if 1 <= new_r <= size and 1 <= new_c <= size and (new_r, new_c) not in visited:
                queue.append(((new_r, new_c), path + [(new_r, new_c)]))

moves = [
    (1,0), (0,1),
    (-1,0), (0,-1),
    (1,1), (1,-1),
    (-1,1), (-1,-1)
]

path = bfs((1,1), (4,4), 4)
print(path)