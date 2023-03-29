# 1914번 하노이 탑
'''
세 개의 장대가 있고 첫 번째 장대에는 반경이 서로 다른 n개의 원판이 쌓여 있다.
각 원판은 반경이 큰 순서대로 쌓여있다
다음 규칙에 따라 첫 번째 장대에서 세 번째 장대로 옮기려 한다.

1. 한 번에 한 개의 원판만을 다른 탑으로 옮길 수 있다.
2. 쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.

이 작업을 수행하는데 필요한 이동 순서를 출력하는 프로그램을 작성하라.
단, 이동 횟수는 최소가 되어야 한다.
'''

def hanoi(n, a, b, c):
    if n == 1:
        print(a, c)
        return
    hanoi(n - 1, a, c, b) # n-1개의 원판은 b로 이동
    # 맨 아래 마지막으로 남은 원판은 c로 이동
    print(a, c)
    # b에 있는 원반 n - 1개를 c로 이동시켜라
    hanoi(n - 1, b, a, c)

n = int(input())
result = 2**n -1
print(result)
if n <= 20:
    hanoi(n, 1, 2, 3)


# 원판의 개수가 1개가 될 때, start와 end를 출력하고 반환
# start: 현 위치
# end: 옮긴 위치
# def hanoi(n, start, end):
#     if n == 1:
#         print(start, end)
#         return
#     # 1개를 제외한 나머지 (n-1) 원판은 2번으로 옮겨야 한다.
#     # 처음엔 1에서 시작해서 
#     hanoi(n - 1, start, 6-start-end) 
#     print(start, end)
#     hanoi(n - 1, 6-start-end, end)


## 다르게 풀 방법은 없을까? 후에 고민해보자
# n = int(input())
# '''
# result = 2**n -1
# print(result)
# '''
# first = [i for i in range(n, 0, -1)]
# # print(first)
# second = []
# third = []

# 후입 선출(스택)
# 목표: third = [5, 4, 3, 2, 1]
# 재귀를 이용해야 한다.
# 가장 마지막에 있는 원판이 3번 위치에 가면 재귀한다.
# 탈출 조건 : n in third
# dfs
# dfs(n-1) / n-1 = 1 까지
# 작은 것위에 큰게 오지는 못한다.(if문으로 제어)

