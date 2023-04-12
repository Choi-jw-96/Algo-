n = int(input())
stair = [0]
score = [0] * (n+1)
for i in range(n):
  stair.append(int(input()))
  # 한칸에서 두번째 칸은 점화식에서 이용되는 수이자 max값이 바뀔일이 없으니 먼저 설정한다.
  if i < 2:
    score[i+1] = sum(stair[0:i+2])

# 설정이 인된 3부터 돌아준다
for i in range(3, n+1):
    # score[i-2]+stair[i] : 1칸 2칸 가는경우
    # score[i-3]+stair[i-1]+stair[i] : 2칸 1칸 가는경우
    score[i] = max(score[i-2]+stair[i], score[i-3]+stair[i-1]+stair[i])
print(score[-1])