# 틀린 풀이

def n_sum(inputs):
    result = 0
    for i in inputs:
        if i.isdigit():
            result += int(i)
        return result

n = int(input())
n_list = []
for _ in range(n):
    n_list.append(input())

n_list.sort(key=lambda x: (len(x), n_sum(x), x))

for i in n_list:
    print(i)