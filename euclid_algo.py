a = int(input("Enter no 1: "))
b = int(input("Enter no 2: "))

while a > 0 and b > 0:
    if a>b:
        a = a%b
    else:
        b = b%a

print(max(a,b))