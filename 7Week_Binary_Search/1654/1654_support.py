# 랜선의 개수와 자르고자 하는 길이 입력
n, cnt = map(int, input().split())
Lan = []
# 랜선에 대한 정보 입력
for i in range(n):
    Lan.append(int(input()))

# 이진탐색을 위한 시작점과 끝점 설정
start, end = 1, max(Lan)

# 이진탐색
while start <= end:
    cut = (start + end) // 2
    line = 0
    # 잘렸을때 랜선의 개수를 계산
    for i in Lan:
        line += i // cut
    # 랜선이 적은 경우 더 많이 잘려야하니(짧게 잘라야하니) 왼쪽 부분을 탐색
    if line < cnt:
        end = cut -1
    # 랜선의 양이 너무 많은 경우 덜 잘려야하니 오른쪽부분 탐색
    else:
        start = cut + 1
# 정답 출력
print(end)
        
