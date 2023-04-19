n = int(input())
grape = [0] + [int(input()) for _ in range(n)]
drink = [0] * (n+1)
drink[1] = grape[1]
# n==1이면 drink[2]가 없으니 인덱스 에러가 남
if n != 1:
  drink[2] = sum(grape[1:3])

for i in range(3, n+1):
    # 연속을 마시지 않을 때 - drink[i-1]
    # drink[i-2]을 마실 때
    # drink[i-2]을 마시지 않을 때
    drink[i] = max(drink[i-1], drink[i-2] + grape[i], drink[i-3] + grape[i-1] + grape[i])
print(drink[n])