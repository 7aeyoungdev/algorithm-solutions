# https://jungol.co.kr/problem/21026

n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(1, 4):
    x = a.count(i)
    y = a.count(7 - i)
    
    if x != 0 or y != 0:
        ans += max(1, abs(x - y))

print(ans)