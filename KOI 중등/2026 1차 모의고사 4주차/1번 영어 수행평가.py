# https://jungol.co.kr/contest/4097/problem/1

n = int(input())
s = input()

first = [] # 모두 연속하다고 가정할 때, 첫 번째 학생의 의자 번호
std = 0
for i in range(n):
    if s[i] == '1':
        first.append(i - std)
        std += 1
        
ans = 0
if std > 1:
    target = first[std // 2] # 가운데 학생이 기준

    for f in first:
        ans += abs(target - f)
else:
    ans = 0

print(ans)