# https://jungol.co.kr/problem/12370

n = int(input())
a = list(map(int, input().split()))

cnt = {}

for c in a:
    if c not in cnt:
        cnt[c] = 0
    cnt[c] += 1

for x in cnt:
    if cnt[x] > 2:
        print("No")
        break
else:
    print("Yes")