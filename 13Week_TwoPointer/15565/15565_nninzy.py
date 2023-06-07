n, k = map(int, input().split())
dolls = list(map(int, input().split()))

start = 0
end = k - 1
answer = int(1e9)

lion = []
for i in range(len(dolls)) :
    if dolls[i] == 1 :
        lion.append(i)

if len(lion) < k :
    print(-1)
    exit(0)
while end < len(lion) :
    length = lion[end] - lion[start] + 1
    answer = min(length, answer)
    start += 1
    end += 1
print(answer)