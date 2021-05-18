array = []
for i in range(10):
    n = int(input())
    array.append(n % 42)
print(len(set(array)))
