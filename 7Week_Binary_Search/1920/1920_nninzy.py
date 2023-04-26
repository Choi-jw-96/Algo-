n = int(input())
a_list = set(map(int, input().split()))
m = int(input())
x_list = [*map(int, input().split())]

answer = []
for x in x_list:
    if x in a_list:
        answer.append(1)
    else:
        answer.append(0)
print(*answer, sep="\n")