""" C2) Multiplication as a series of addition
 """

def multiply(n,c, ans):
    if c==n:
        return ans
    return multiply(n,c+1, ans+n)

n = int(input("enter a no: "))
print(multiply(n, 0, 0))