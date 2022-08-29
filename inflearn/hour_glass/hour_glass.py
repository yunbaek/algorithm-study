import sys
sys.stdin = open("input.txt", "r")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = 3
b = [list(map(int, input().split())) for _ in range(m)]


