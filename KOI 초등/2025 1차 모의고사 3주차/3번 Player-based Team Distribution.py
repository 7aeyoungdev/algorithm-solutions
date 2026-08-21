# https://jungol.co.kr/contest/2496/problem/3

n = int(input())
a = list(map(int, input().split()))

p = [ x for x in a if x > 0 ]

print(sum(p) * len(p) + sum(a) - sum(p))