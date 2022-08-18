import sys
sys.stdin = open("input.txt", "rt")

T = int(input())
for t in range(T):
    m, s, e, k = map(int, input().split())
    b = list(map(int, input().split()))
    b = b[s - 1: e]
    b.sort()
    print("#%d %d" % (t + 1, b[k - 1]))
