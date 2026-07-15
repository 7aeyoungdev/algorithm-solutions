# https://jungol.co.kr/contest/4243/problem/1

n = int(input())
a = list(map(int, input().split()))

line = [0] * (n + 1)
last = [0, 0, 0]
high, low = 0, 0

for x in a:
    if last[1] > last[2]:
        high, low = 1, 2
    else:
        high, low = 2, 1
    
    if x > last[high]:
        last[high], line[x] = x, high
    elif x > last[low]:
        last[low], line[x] = x, low
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