T = int(input())
for t in range(T):
    n = int(input())
    note1 = set(map(int, input().split()))
    m = int(input())
    note2 = [*map(int, input().split())]
    answer = []
    for i in note2:
        if i in note1:
            answer.append(1)
        else:
            answer.append(0)
    print(*answer, sep='\n')