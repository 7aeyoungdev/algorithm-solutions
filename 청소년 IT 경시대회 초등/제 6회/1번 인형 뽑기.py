# https://jungol.co.kr/problem/12377

n, a1, a2, b, c1, c2 = map(int, input().split())

def normal(coin):
    if coin < b:
        return 0
    return (coin - b) // c1 * c2

ans = normal(n)

if a1 <= n:
    ans = max(ans, a2 + normal(n - a1))

print(ans)