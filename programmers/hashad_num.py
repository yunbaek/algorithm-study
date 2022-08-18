def solution(x):
    return x % sum([int(c) for c in str(x)]) == 0

def collatz(num):
    answer = 0
    if num == 1:
        return 0
    while True:
        num = num / 2 if num % 2 == 0 else (num * 3) + 1
        answer += 1
        if num == 1:
            return answer
        elif answer == 500:
            return -1
    return answer

print(collatz(6))
