import sys
sys.stdin = open("input.txt", "r")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

mid = n // 2
s = e = mid
result = 0
for i in range(n):
    for j in range(s, e + 1):
        result += a[i][j]
    if i < mid:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1

print(result)