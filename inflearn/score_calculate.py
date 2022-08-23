import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))

result = 0
count = 0

for i in a:
    if i == 1:
        count += 1
        result += count
    else:
        count = 0

print(result)