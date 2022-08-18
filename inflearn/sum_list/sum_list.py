import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

result = a + b
result.sort()

for x in result:
    print(x, end = ' ')
