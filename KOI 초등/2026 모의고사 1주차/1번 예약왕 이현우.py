# https://jungol.co.kr/contest/4229/problem/1

n, m = map(int, input().split())
room = [0] * 200001

for i in range(m):
    k, s, e = map(int, input().split())
    if room[k] <= s:
        room[k] = e
        print("YES")
    else:
        print("NO")