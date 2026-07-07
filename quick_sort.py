def quickSort(l, start, end):
    if start < end:
        pos = partition(l, start, end)
        quickSort(l, start, pos-1)
        quickSort(l, pos+1, end)

def partition(l ,start, end):
    pivot = l[start]
    lb = start

    while start <= end:
        while start <= end and l[start] <= pivot:
            start += 1

        while start <= end and l[end] > pivot:
            end -= 1

        if start < end:
            l[start], l[end] = l[end], l[start]

    l[lb], l[end] = l[end], pivot
    return end


l = [27, 38, 4, 3, 43, 82, 10, 14, 5]

print("List before sorting:")
print(l)

print("list after sorting:")
quickSort(l, 0, len(l) - 1)
print(l)