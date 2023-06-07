import sys
n, k = list(map(int, sys.stdin.readline().split()))
doll = list(map(int, sys.stdin.readline().split()))

answer = 10e6
left = 0
right = 0

# 라이언 인형의 개수
lion = 0

if doll[left] == 1:
    lion += 1

# 왼쪽 / 오른쪽 중 하나가 끝에 도달할 때까지 반복한다.
while left < len(doll) and right < len(doll):
    # 라이언 인형의 개수가 부족하다면, 오른쪽 포인터를 옮겨 본다.
    if lion < k:
        right += 1
        if right < len(doll) and doll[right] == 1:
            lion += 1
    # 라이언 인형의 개수가 충분하다면, 왼쪽 포인터를 옮겨 본다.
    else:
        # 딱 맞게 되있다면, 사이즈를 찾아 놓는다.
        if lion == k:
            answer = min(answer, right - left + 1)

        if left < len(doll) and doll[left] == 1:
            lion -= 1
        left += 1

if answer == 10e6:
    print(-1)
else:
    print(answer)