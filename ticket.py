tid = [101, 102, 105, 101, 103, 103, 102, 106]
duplicate = []
def bruteForce():
    for i in range(len(tid)):
        for j in range(i+1, len(tid)):
            if tid[i] == tid[j] and tid[i] not in duplicate:
                duplicate.append(tid[i])

    print(duplicate)

# bruteForce()

def sortingTech():
    tid.sort()

    i=0
    while i < len(tid)-1:
        if tid[i] == tid[i+1] and tid[i] not in duplicate:
            duplicate.append(tid[i])
        i += 1

    print(duplicate)

# sortingTech()

def hasingTech():
    d = {}
    for i in tid:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    
    for i in d:
        if d[i] > 1:
            duplicate.append(i)

    print(duplicate)

hasingTech()