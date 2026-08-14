# https://jungol.co.kr/problem/12499

n = int(input())
a = input()

first = {'S' : n, 'R' : n, 'P' : n}
last = {'S' : -1, 'R' : -1, 'P' : -1}

win = {'S' : 'P', 'R' : 'S', 'P' : 'R'}
lose = {'S' : 'R', 'R' : 'P', 'P' : 'S'}

ans = []

for i in range(n):
    card = a[i]
    if first[card] == n:
        first[card] = i
    last[card] = i

for i in range(n):
    card = a[i]

    left = first[lose[card]] > i or first[win[card]] < i
    right = last[lose[card]] < i or last[win[card]] > i

    if left and right:
        ans.append(1)
    else:
        ans.append(0)

print(*ans, sep = '')