import sys
sys.stdin = open("input.txt", "rt")

li = [i + 1 for i in range(20)]

for _ in range(10):
    a, b = map(int, input().split())
    li = li[:a - 1] + li[a - 1:b][::-1] + li[b:]

for x in li:
    print(x, end = ' ')
