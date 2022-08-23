# 10 3
# 13 15 34 23 45 65 33 11 26 42
import sys
sys.stdin = open("input.txt", "rt")

n, k = map(int, input().split())
a = list(map(int, input().split()))

result = set()

for i in range(n):
    for j in range(i + 1, n):
        for m in range(j + 1, n):
            result.add(a[i] + a[j] + a[m])

result = list(result).sort(reverse = True)

print(result[k])