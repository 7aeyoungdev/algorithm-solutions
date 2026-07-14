# https://jungol.co.kr/contest/4230/problem/1

n = int(input())
d = list(map(int, input().split()))

from collections import deque

ls = deque(d)
rs = deque()

ans = []

def take(h, s):
    ans.append(f'take {h} {s}')
    if s == 'L':
        return ls.popleft()
    else:
        return rs.popleft()

def put(h, s, v):
    ans.append(f'put {h} {s}')
    if s == 'L':
        ls.appendleft(v)
    else:
        rs.appendleft(v)

while len(ls) > 0:
    lh = take('L', 'L')

    while len(rs) > 0 and rs[0] > lh:
        rh = take('R', 'R')
        put('R', 'L', rh)
    
    put('L', 'R', lh)

while len(rs) > 0:
    lh = take('L', 'R')
    put('L', 'L', lh)

print(len(ans))
print(*ans, sep = '\n')