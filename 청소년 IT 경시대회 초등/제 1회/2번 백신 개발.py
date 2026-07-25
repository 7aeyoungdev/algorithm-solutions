# https://jungol.co.kr/problem/12346

from itertools import permutations

n = int(input())
s = [ input() for _ in range(n) ]

ans = 10**20

def merge(a, b):
    l = min(len(a), len(b))

    for i in range(l, 0, -1):
        if a[-i:] == b[:i]:
            return a + b[i:]

    return None

for p in permutations(s):
    vac = p[0]
    
    for i in range(1, n):
        vac = merge(vac, p[i])
        
        if vac is None:
            break
    
    if vac is not None:
        if len(vac) < ans:
            ans = len(vac)

print(ans)