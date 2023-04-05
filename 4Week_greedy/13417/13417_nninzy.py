t = int(input())
for i in range(t):
    n = int(input())
    alp = input().split()
    result = [alp[0]]
    for i in range(1, len(alp)):
        left = result[0]
        if alp[i] <= left:
            result = [alp[i]] + result
        else:
            result.append(alp[i])
    print(*result, sep='')