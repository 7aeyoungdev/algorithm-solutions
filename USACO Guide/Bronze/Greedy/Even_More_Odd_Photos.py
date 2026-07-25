# https://usaco.org/index.php?page=viewproblem2&cpid=1084

n = int(input())
id = list(map(int, input().split()))

even = 0
odd = 0

for i in id:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

while even < odd:
    even += 1
    odd -= 2

if even > odd:
    print(2 * odd + 1)
else:
    print(2 * even)