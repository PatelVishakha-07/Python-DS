""" 
H3) You're climbing a staircase. You can take 1 step or 2 steps at a time. How many distinct ways can you reach the Nth stair? """

def stairs(n):
    if n <= 1:
        return 1
    
    return stairs(n-1) + stairs(n-2)

n = int(input("enter a no: "))

print(stairs(n))