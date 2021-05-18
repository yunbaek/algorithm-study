num = int(input())
check = num
count = 0
new_num = 0
while True:
    temp = num // 10 + num % 10
    num = (num % 10) * 10 + temp % 10
    count += 1
    if num == check:
        break

print(count)
