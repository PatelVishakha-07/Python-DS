""" H1) A security researcher is testing a 3-digit lock (digits 1-3 only, no repeats). They need to generate every possible combination - a classic backtracking/permutation problem asked in Google and Microsoft interviews.
 """

def permutation(n, idx):  
    if idx == len(str(n)):
        ans.append(n)  

    s = list(str(n))

    for i in range(idx, len(s)):
        s[i], s[idx] = s[idx], s[i]

        permutation(int("".join(s)), idx+1)

        s[i], s[idx] = s[idx], s[i]

ans = []
permutation(123, 0)
print(ans)