import sys
sys.stdin = open("input.txt", "rt")

s = input()
result = 0
for x in s:
    if x.isdecimal():
        result = result * 10 + int(x)
print(result)

count = 0
for i in range(1, result + 1):
    if result % i == 0:
        count += 1
print(count)
