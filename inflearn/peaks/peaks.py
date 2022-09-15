import sys
sys.stdin = open("input.txt", "r")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
count = 0

a.insert(0, [0] * n)
a.append([0] * n)

for x in a:
    x.insert(0, 0)
    x.append(0)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if all(a[i][j] > a[i + dx[k]][j + dy[k]] for k in range(4)):
            count += 1

print(count)

reason: no instance(s) of type variable(s) exist so that PrecedeSubjectItemValidateDTO conforms to BatchCourseRunBaseDTO
