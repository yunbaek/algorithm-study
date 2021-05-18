a = int(input())
b = int(input())
c = int(input())

numbers = list(str(a * b * c))
for i in range(10):
    print(numbers.count(str(i)))
