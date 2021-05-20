n = int(input())

for _ in range(n):
    ox_list = input()
    score = 0
    total = 0
    for ox in ox_list:
        if ox == 'O':
            score += 1
            total += score
        else:
            score = 0
    print(total)