n = int(input())
r_len = [*map(int, input().split())]
price = [*map(int, input().split())]
result = 0
cheap = price[0]
for i in range(n-1):
    if price[i] < cheap:
        cheap = price[i]
    result += cheap * r_len[i]
print(result)