n = int(input("enter a no: "))
center = n
n = 2*center-1

for i in range(n):
    for j in range(n):
        top=i
        left=j
        bottom = n-1-i
        right = n-1-j

        val = min(top,right,bottom,left)
        print(center-val, end=" ")
    print()