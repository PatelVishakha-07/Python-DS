# nums = [2,3,1]
# nums = [-1,-3,-2]
# nums = [1,2,3,4]
nums = [0,0,0,0]

m1 = float('-inf')
m2 = float('-inf')
m3 = float('-inf')

min1 = float('inf')
min2 = float('inf')

for i in nums:
    if i >= m1:
        m3 = m2
        m2 = m1
        m1 = i
    elif i >= m2:
        m3 = m2
        m2 = i
    elif i >= m3:
        m3 = i

    if i <= min1:
        min2 = min1
        min1 = i
    elif i <= min2:
        min2 = i

prd1 = m1 * m2 * m3
prd2 = m1 * min1 * min2

print("Product: ", max(prd1, prd2))