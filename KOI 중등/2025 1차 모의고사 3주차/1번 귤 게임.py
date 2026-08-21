# https://jungol.co.kr/contest/2496/problem/2

n = int(input())
a = input().split()

for i in range(n):
    if a[i] != '1':
        break

if i == n:
    if i % 2 == 1:
        print("J")
    else:
        print("H")
else:
    if i % 2 == 0:
        print("J")
    else:
        print("H")