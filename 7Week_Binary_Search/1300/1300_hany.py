# 1300번 K번째 수
## 문제
'''
세준이는 크기가 N*N인 배열 A를 만들었다. 
배열에 들어있는 수 A[i][j] = i*j 이다. 
이 수를 일차원 배열 B에 넣으면 B의 크기는 N*N이 된다.

B를 오름차순 정렬했을 때, B[k]를 구해보자.
배열 A와 B의 인덱스는 1부터 시작한다.
'''

## 접근 방법
'''
1부터 n**2까지의 오름차순 배열 중 B[k]를 출력하라.
1. k번째 숫자(인덱스)는 절대 k보다 클 수 없다.
2. k번째 숫자 밑으로 개수를 구한다.
3. min(임의의 수 // 각 행, n) -> 임의의 수 // 각행 혹은 n개를 모두 더한 cnt
4. 이 cnt가 타겟과 동일한지 여부 따지기 (이분탐색)
'''
## 추후에 다시 풀어볼 것

n = int(input())
k = int(input())

start, end = 1, k
while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for i in range(1, n + 1):
        cnt += min(mid // i, n)
    
    if cnt >= k:
        res = mid
        end = mid - 1
    else:
        start = mid + 1
print(res)