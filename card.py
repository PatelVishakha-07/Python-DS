def lowerBound():
    l = [1,5,6,6,8,10,10,11,11,15,17,18]

    start = 0
    end = len(l)-1
    tar = 10

    while start <= end:
        mid = start + (end-start)//2

        if l[mid] >= tar:
            ans = mid
            end = mid-1
        else:
            start = mid+1

    print(ans)

def upperBound():
    l = [1,5,6,6,8,10,10,11,11,15,17,18]

    start = 0
    end = len(l)-1
    tar = 10

    while start <= end:
        mid = start + (end-start)//2

        if l[mid] <= tar:
            start = mid + 1
            
        else:
            end = mid 

    print(l[start])

upperBound()