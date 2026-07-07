def split(start, end, l):
    if start < end:
        mid = start + (end-start)//2
        split(start, mid, l)
        split(mid+1, end, l)
        merge(l, start, end, mid)

def merge(l, start, end, mid):
    i=start
    j=mid+1
    lb=start
    new_l = []

    while i <= mid and j <= end:
        if l[i] <= l[j]:
            new_l.append(l[i])
            i += 1
        else:
            new_l.append(l[j])
            j += 1
    
    while i <= mid:
        new_l.append(l[i])
        i += 1

    while j <= end:
        new_l.append(l[j])
        j += 1

    l[start:end+1] = new_l
    

l = [27, 38, 4, 3, 43, 82, 10, 14, 5]
print("List before sorting:")
print(l)

print("list after sorting:")
split(0, len(l)-1, l)
print(l)