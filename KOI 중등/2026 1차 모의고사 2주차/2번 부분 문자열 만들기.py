# https://jungol.co.kr/contest/4084/problem/2

an, bn = map(int, input().split())
a = input()
b = input()

d = [ [10**20] * (bn + 1) for _ in range(an + 1) ]

for i in range(an + 1):
    d[i][0] = 0

for i in range(1, an + 1):
    for j in range(1, bn + 1):
        if a[i - 1] == b[j - 1]:
            c = 0
        else:
            c = 1
        d[i][j] = min(d[i - 1][j], d[i - 1][j - 1] + c)

print(d[an][bn])