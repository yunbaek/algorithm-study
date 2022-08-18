import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
result = 0
for i in range(n):
    tmp = input().split()
    tmp.sort()
    a, b, c = map(int, tmp)
    if a == b and a == c:
        result = a * 1000 + 10000
    elif a == b or a == c:
        result = a * 100 + 1000
    elif b == c:
        result = b * 100 + 1000
    else:
        reulst = a * 100
print(result)