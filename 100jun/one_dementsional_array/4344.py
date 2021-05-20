n = int(input())

for _ in range(n):
    input_data = list(map(int, input().split(' ')))
    cnt = 0
    avg = sum(input_data[1:])/input_data[0]
    for score in input_data[1:]:
        if score > avg:
            cnt += 1
        rate = cnt/input_data[0] * 100
    print(f'{rate:.3f}%')
