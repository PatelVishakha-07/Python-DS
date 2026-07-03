""" C2) Multiplication as a series of addition
 """

def multiply(n1, n2, c, ans):
    if c==n2:
        return ans
    return multiply(n1, n2, c+1, ans+n1)

n1 = int(input("enter a no 1: "))
n2 = int(input("enter a no 2: "))
print(multiply(n1,n2, 0, 0))