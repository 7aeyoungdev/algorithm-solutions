# https://jungol.co.kr/contest/4242/problem/2

n = int(input())
a = list(map(int, input().split()))

line = [0] * (n + 1)
last = [0, 0, 0]
i, j = 0, 0

for x in a:
    if last[1] > last[2]:
        i, j = 1, 2
    else:
        i, j = 2, 1
    
    if last[i] < x:
        last[i], line[x] = x, i
    elif last[j] < x:
        last[j], line[x] = x, j
    else:
        print('NO')
        exit()

ans = []
num = 1

for x in a:
    while num <= x:
        ans.append(f'IN {line[num]}')
        num += 1
    
    ans.append(f'OUT {line[x]}')

print('YES', len(ans), *ans, sep = '\n')