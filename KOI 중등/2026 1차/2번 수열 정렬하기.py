# https://jungol.co.kr/problem/12494

n = int(input())
a = list(map(int, input().split()))

first = [-1] * (n + 1)
last = [-1] * (n + 1)

for i in range(n):
    x = a[i]

    if first[x] == -1:
        first[x] = i
    last[x] = i

ans = 0
past = 0

for i in range(1, n + 1):
    if first[i] == -1:
        continue

    if past != 0 and first[i] < last[past]:
        ans += 1

    past = i

print(ans)