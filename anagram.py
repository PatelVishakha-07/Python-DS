def isAnagram(s1, s2):
    l = [0] * 26

    for i in s1:
        if i.isalpha():
            l[abs(ord('a') - ord(i))] += 1

    for i in s2:
        if i.isalpha():
            l[abs(ord('a') - ord(i))] -= 1

    for i in l:
        if i != 0:
            return False
    return True


s1 = input("enter string 1: ")
s2 = input("enter string 2: ")

print(f"Is {s1} and {s2} anagram? ", isAnagram(s1,s2))