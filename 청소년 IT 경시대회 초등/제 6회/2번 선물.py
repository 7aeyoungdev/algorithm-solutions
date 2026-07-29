# https://jungol.co.kr/problem/12378

import sys
input = sys.stdin.readline

n = int(input())
g = [ list(map(int, input().split())) for _ in range(2 * n - 1) ]

give = [0] * (n + 1)
take = [0] * (n + 1)
prev = [0] * (n + 1)

ans = "YES"

for a, b in g:
    if a == b or prev[a] == b or give[a] > 1 or take[b] > 1:
        ans = "NO"
        break

    give[a] += 1
    take[b] += 1
    prev[a] = b
else:
    x = give.index(1)
    y = take.index(1)

    if x == y or prev[x] == y:
        ans = "NO"

print(ans)
if ans == "YES":
    print(x, y)