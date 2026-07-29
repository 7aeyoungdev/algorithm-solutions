# https://jungol.co.kr/problem/12380

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

even = False
odd = False

for i in range(k):
    r, c = map(int, input().split())

    if (r + c) % 2 == 0:
        even = True
    else:
        odd = True

if even and odd:
    print("NO")
else:
    print("YES")