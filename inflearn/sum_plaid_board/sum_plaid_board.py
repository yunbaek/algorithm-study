import sys
sys.stdin = open("input.txt", "r")
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

largest = -2147000000

for i in range(n):
    row_sum = column_sum = 0
    for j in range(n):
        row_sum += a[i][j]
        column_sum += a[j][i]
    if row_sum > largest:
        largest = row_sum
    if column_sum > largest:
        largest = column_sum

x_sum = y_sum = 0
for i in range(n):
    x_sum += a[i][i]
    y_sum += a[i][n - i - 1]
if x_sum > largest:
    largest = x_sum
if x_sum > largest:
    largest = y_sum

print(largest)