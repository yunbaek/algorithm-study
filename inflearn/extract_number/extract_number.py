import re
import sys
sys.stdin = open("input.txt", "rt")

inputString = input()
extractNumber = int(re.sub(r'[^0-9]', '', inputString))

count = 0
for i in range(1, extractNumber + 1):
    if extractNumber % i == 0:
        count += 1
print(extractNumber)
print(count)