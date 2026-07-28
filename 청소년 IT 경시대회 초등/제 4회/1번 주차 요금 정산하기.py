# https://jungol.co.kr/problem/12363

a, b, c = map(int, input().split())
t = int(input())

ans = a

if t > 30:
    t -= 30
    t += b - 1
    ans += t // b * c

print(ans)