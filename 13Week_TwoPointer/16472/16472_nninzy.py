n = int(input())
text = input()
if len(text) == 1:
    print(1)
elif len(set(text)) <= n:
    print(len(text))
else:
    start = 0
    end = 1
    sets = set([text[start]])
    answer = 0
    while start < len(text)-1:
        if end == len(text):
            answer = max(answer, end-start)
            break
        sets.add(text[end])
        if len(sets) == n:
            answer = max(answer, end-start+1)
            end += 1
        elif len(sets) > n:
            sets.clear()
            start += 1
            sets.add(text[start])
            end = start + 1
        else:
            end += 1
    print(answer)