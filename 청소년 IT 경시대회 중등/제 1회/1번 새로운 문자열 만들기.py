# https://jungol.co.kr/problem/12345

t = int(input())

for _ in range(t):
    s = input()
    
    for i in range(len(s)):
        front = s[:i]
        back = front[::-1]

        new = s + back

        if new == new[::-1]:
            print(new)
            break