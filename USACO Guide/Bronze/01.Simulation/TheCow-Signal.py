# https://usaco.org/index.php?page=viewproblem2&cpid=665

# M * N 크기로 주어진 문자열 신호를 가로, 세로 각각 K 배 확대한다.

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