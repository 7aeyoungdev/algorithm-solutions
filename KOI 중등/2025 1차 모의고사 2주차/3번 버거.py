# https://jungol.co.kr/contest/2491/problem/3

n = int(input())
x = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def check(mid):
    need, limit = 0, mid

    for i in range(n): # 모든 재료에 대해
        x_left = x[i] - (a[i] * mid) # a 레시피로만 만들었을 때 남는 개수
        diff = abs(a[i] - b[i]) # 개수 차이

        if a[i] < b[i]: # a 재료가 적게 드는 경우
            limit = min(limit, x_left // diff)
        elif a[i] > b[i]: # b 재료가 적게 드는 경우 
            if x_left < 0:
                need = max(need, -(x_left // diff))
        else: # 재료가 똑같이 드는 경우
            if x_left < 0:
                return False

        if need > limit:
            return False

    return True

l, r = 0, 10**9
ans = 0

while l <= r:
    mid = (l + r) // 2

    if check(mid):
        ans = mid
        l = mid + 1
    else:
        r = mid - 1

print(ans)