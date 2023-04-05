n = int(input())

load = list(map(int, input().split()))
city = list(map(int, input().split()))

dic = {}
m = int(10e9)

for i in range(len(load)):
    if not dic:
        m = city[i]
        dic[m] = load[i]
    else:
        if m > city[i]:
            m = city[i]
            dic[m] = load[i]
        else:
            dic[m] += load[i]

total = 0
for key, value in dic.items():
    total += key * value

print(total)