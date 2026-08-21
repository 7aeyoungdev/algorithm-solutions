# https://jungol.co.kr/contest/2490/problem/3

n = int(input())
a = list(map(int, input().split()))

left, right = 0, 1

total_left = 0
for i in range(n):
    if a[i] > 0: # 오른쪽 비둘기
        total_left = i + a[i]
        break

def check(face):
    ans = []
    left_count = 0

    for i in range(n):
        is_left = i - left_count == a[i]
        is_right = total_left - left_count == a[i]

        if is_left and is_right:
            result = face
        elif is_left:
            result = left
        elif is_right:
            result = right
        else:
            return False

        ans.append(result)
        if result == left:
            left_count += 1

    if left_count == total_left:
        print(*ans)
        return True
    else:
        return False

if not check(left) and not check(right):
    print(-1)