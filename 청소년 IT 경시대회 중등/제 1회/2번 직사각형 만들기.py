# https://jungol.co.kr/problem/12347

n = int(input())
l = list(map(int, input().split()))

cnt = {} # 길이가 x 인 나무젓가락의 개수
for x in l:
    if x in cnt:
        cnt[x] += 1
    else:
        cnt[x] = 1

u = list(cnt.keys())
area = {} # 길이의 합이 x 인 직사각형 넓이의 합

def sum_area(a, b):
    if a == b:
        pair = cnt[a] // 2
    else:
        pair = min(cnt[a], cnt[b])

    if pair == 0:
        return

    s = a * b * pair
    if a + b in area:
        area[a + b] += s
    else:
        area[a + b] = s

for i in range(len(u)):
    for j in range(i, len(u)):
        sum_area(u[i], u[j])

print(max(area.values()))