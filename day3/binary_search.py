""" C2) Binary search using recursion
 """

def binarySearch(l, start, end, tar):

    if start <= end:
        mid = start + (end-start)//2

        if l[mid] == tar:
            return mid
        
        elif l[mid] > tar:
            return binarySearch(l, start, mid-1, tar)
        
        else:
            return binarySearch(l, mid+1, end, tar)
        
    return -1
        
l = [10,13,14,16,17,20,25]
n = int(input("enter element to search: "))

pos = binarySearch(l, 0, len(l)-1, n)

if pos == -1:
    print("not found")
else:
    print(f"{n} found at {pos} position")