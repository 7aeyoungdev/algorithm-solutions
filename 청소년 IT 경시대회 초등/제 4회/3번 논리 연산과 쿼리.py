# https://jungol.co.kr/problem/12367

n, q = map(int, input().split())
l = list(input())
k = list(map(int, input().split()))

block = [0] * (2 * n - 1)
zero = []

b = 0
z = 0

for i in range(2 * n - 1):
    block[i] = b # 블록 번호

    if l[i] == '0': # 0 의 개수 증가
        z += 1

    if l[i] == '|': # 해당 블록의 0 의 개수 저장, 블록 번호 증가
        zero.append(z)
        z = 0
        b += 1
zero.append(z) # 마지막 블록의 0 의 개수 저장

ans = []
true_block = zero.count(0) # 참인 블록의 개수 = 0 이 없는 블록의 개수

for x in k:
    i = 2 * x - 2 # 쿼리의 인덱스
    b = block[i] # 쿼리의 블록 번호

    if l[i] == '0':
        l[i] = '1' # 동작
        zero[b] -= 1 # 0 의 개수 감소
        if zero[b] == 0: # 0 이 없다면 참인 블록의 개수 증가
            true_block += 1
    else: # l[i] == '1'
        l[i] = '0' # 동작
        if zero[b] == 0: # 0 이 없었다면 참인 블록의 개수 감소
            true_block -= 1
        zero[b] += 1 # 0 의 개수 증가

    if true_block > 0: # 하나라도 참이면
        ans.append('1')
    else:
        ans.append('0')

print(*ans, sep = '')