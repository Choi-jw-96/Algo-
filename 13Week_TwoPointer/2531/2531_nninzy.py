n, d, k, c = map(int, input().split())
sushi = []
for _ in range(n):
  sushi.append(int(input()))
sushi = sushi + sushi[:k-1]

selected = set()
answer = 0

for start in range(len(sushi)):
    end = start + k
    selected = set(sushi[start: end])
    s = len(selected)
    if c not in selected:
        s += 1
    if s > answer:
        answer = s
print(answer)