n = int(input())
ran = n if n < 100 else 54
answer = 0
for i in range(n) :
    i_sum = sum(map(int, str(i)))
    if (i + i_sum) == n :
        answer = i;
        break;
print(answer)
