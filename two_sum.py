l = [5,2,7,9,10,13,1]
tar = int(input("enter target value: "))

d = {}

for i in l:
    v = tar - i
    
    if i in d:
        print("Values are:", i, "and", d[i])
        break
    d[v] = i
    