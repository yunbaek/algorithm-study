import sys
sys.stdin = open("input.txt", "r")

def count(len):
    cnt = 0
    for x in lines:
        cnt += (x // len)
    return cnt

k, n = map(int, input().split())
lines = []
result = 0
largest = 0

for i in range(k):
    tmp = int(input())
    lines.append(tmp)
    largest = max(largest, tmp)

lt = 1
rt = largest

while lt <= rt:
    mid = (lt + rt) // 2
    if count(mid) >= n:
        result = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(result)
