# 14720 우유 축제

n = int(input())

milk_list = list(map(int, input().split()))
count = 0

for i in range(n):
   # 우유 가게에서 파는 우유 종류가 내가 이번에 마실 우유 종류와 같다면, count 1 증가
   if milk_list[i] == count % 3:
        count += 1

print(count)