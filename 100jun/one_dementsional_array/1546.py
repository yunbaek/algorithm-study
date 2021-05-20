n = int(input())
scores = list(map(int, input().split()))

max_score = int(max(scores))
fake_list = []
for score in scores:
    fake_list.append(score / max_score * 100)

print(sum(fake_list) / n)

