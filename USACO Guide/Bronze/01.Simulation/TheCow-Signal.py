# https://usaco.org/index.php?page=viewproblem2&cpid=665


import sys

sys.stdin = open('cowsignal.in', 'r')
sys.stdout = open('cowsignal.out', 'w')

m, n, k = map(int, input().split())

for i in range(m):
    line = input()
    row = ''

    for c in line:
        row += c * k

    for j in range(k):
        print(row)