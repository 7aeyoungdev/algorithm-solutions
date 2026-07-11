# https://usaco.org/index.php?page=viewproblem2&cpid=1565

n, q = map(int, input().split())
a = list(map(int, input().split()))
x = [ int(input()) for _ in range(q) ]

for i in range(1, n):
    a[i] = min(a[i], a[i - 1] * 2)

m = min(n - 1, 30)
INF = 10**20

def query(target):
    ans = INF
    curr = 0
    
    for i in range(m, -1, -1):
        if target == 0:
            ans = min(ans, curr)
            break
            
        power = 2 ** i
        cnt = target // power
        
        ans = min(ans, curr + (cnt + 1) * a[i])
        
        curr += cnt * a[i]
        target %= power
        
    if target == 0:
        ans = min(ans, curr)
        
    print(ans)


for i in x:
    query(i)