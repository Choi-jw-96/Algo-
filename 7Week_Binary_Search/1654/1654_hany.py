# 1654번 랜선 자르기
## 문제
'''
박성원이 캠프 때 쓸 N개의 랜선을 만들어야 하는데 너무 바빠서 영식이에게 도움을 청했다.
이미 오영식은 자체적으로 K개의 랜선을 가지고 있다. 그러나 K개의 랜선은 길이가 제각각이다.
성원은 랜선을 모두 N개의 같은 길이의 랜선으로 만들고 싶었기 때문에 K개의 랜선을 잘라서 만들어야 한다.
(이미 자른 랜선은 붙일 수 없다.)


1. 편의를 위해 랜선을 자르거나 만들 때 손실되는 길이는 없음
2. 기존의 K개의 랜선으로 N개의 랜선을 만들 수 없는 경우는 없음
3. 자를 때는 항상 센티미터 단위로 정수길이만큼 자름
4. N개보다 많이 만드는 것도 N개를 만드는 것에 포함

이때 만들 수 있는 최대 랜선의 길이를 구하는 프로그램 작성
'''

## 접근방법
'''
- 같은 랜선 길이(최대 랜선 길이)
- 이분 탐색 활용
- 종료조건
1. end < start
- cnt 구하는 법
1. 각 랜선 // mid
2. 더한다.  
'''
import sys
input = sys.stdin.readline
k, n = map(int, input().split()) # k: 기존 랜선 개수, n: 필요 랜선 개수 (k<=n)
cables = [int(input()) for _ in range(k)]

start = 1
end = max(cables)

while True:
    if end < start:
        break
    mid = (start + end) // 2
    cnt = 0
    for cable in cables:
        cnt += cable // mid
        
    # 만약 cnt의 개수가 n보다 작다면, end를 왼쪽으로 옮기고
    if cnt < n:
        end = mid - 1
    # cnt의 개수가 n보다 크거나 같으면 start를 오른쪽으로 옮긴다.
    else:
        start = mid + 1
print(end)