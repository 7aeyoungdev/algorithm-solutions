# https://jungol.co.kr/problem/12379

n = int(input())
a = [0] + list(map(int, input().split()))

ans = []
pos = {}

for i in range(1, n + 1):
    num = a[i]

    if num == 0:
        continue

    if num not in pos:
        pos[num] = [0, 0]

    bit = i % 2

    if pos[num][bit] == 0:
        pos[num][bit] = i
    else:
        l = pos[num][bit]
        pos[num][bit] = 0
        ans.append( (l, (l + i) // 2, i) )

print(len(ans))
for r in ans:
    print(*r)