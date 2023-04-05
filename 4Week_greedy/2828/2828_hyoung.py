# 2828 사과 담기 게임
import sys

n, m = list(map(int, input().split()))
j = int(input())
apple = []
cnt = 0

for _ in range(j):
    position = int(sys.stdin.readline())
    apple.append(position)

left = 1
right = m

for i in apple:
    if i >= left and i <= right:
        continue
    elif right < i:
        cnt += i - right
        left += i - right
        right += i - right
    elif left > i:
        cnt += left - i
        right -= left - i
        left -= left - i
print(cnt)


# 2828 사과 담기 게임 - 왜 안될까
import sys

# 어차피 바구니의 길이가 몇이든 움직이는 한 칸 씩임. 시작 위치가 다를뿐
# (다음 위치 - 전 위치) - (바구니의 길이 - 1)

n, m = list(map(int, input().split()))
j = int(input())
apple = []

for _ in range(j):
    position = int(sys.stdin.readline())
    apple.append(position)

cnt = 0
for i in range(j-1):
    if abs(apple[i+1] - apple[i]) - (m-1) < 0:
        cnt += 0
    else:
        cnt += abs(apple[i+1] - apple[i]) - (m-1)
print(cnt)



