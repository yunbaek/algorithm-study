import sys
sys.stdin = open("input.txt", "r")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

for i in ragne(m):
    h, t, k = map(int, input().split())