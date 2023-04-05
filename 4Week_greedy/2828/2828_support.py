n, m = map(int, input().split())
start = 0
end = start + m - 1
move = 0
for _ in range(int(input())):
    apple = int(input()) - 1
    if apple in range(start, end+1):
        continue
    else:
        if apple > end:
            c = apple - end
            start += c
            end += c
            move += c
        else:
            c = start - apple
            start -= c
            end -= c
            move += c
print(move)
