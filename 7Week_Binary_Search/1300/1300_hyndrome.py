# 분류: 7주차 이분탐색
# 문제: 백준 1300 k번째
# 문제 주소: https://www.acmicpc.net/problem/1300
# 푼 사람: 진홍엽
# 설명: 이분탐색


i_n = int(input()) # 배열의 크기 N
i_k = int(input()) # 배열을 flatten했을 때, 출력해야할 인덱스
 
start, end = 1, i_n * i_n # 이분탐색 시작 1~N*N (시작인덱스가 1부터)
while start <= end:
    mid = (start + end) // 2 # B[k]값으로 찾아야할 타겟 값
    # 핵심 부분 각 행에서 trg_value이하인 값들의 개수 → 추정 인덱스
    search = sum(min(mid // i, i_n) for i in range(1, i_n+1))
    if result == i_k:
        result = search
    elif result > i_k: # 추정 인덱스가 찾는 인덱스보다 크거나 같으면
        end = mid - 1 # 더 작은쪽(왼쪽)을 봐야되서 end를 땡겨온다.
    else: # 추정 인덱스가 찾는 인덱스(k)보다 작으면 
        start = mid + 1 # 오른쪽(큰쪽) 보기
        
print(result)

# i_n = int(input())
# i_k = int(input())

# i_row = 0
# i_select = 1
# for i in range(1, i_n + 1):
#     i_row += i
#     i_select += 1
#     if (i % 2 == 1) and (i_row > i_k):
#         break
# else:
#     for i in range(i_n - 1, 0):
#         i_row += i
#         i_select += 1
#         if (i % 2 == 1) and (i_row > i_k):
#             break
#     else:
#         print('last')

# ls_final = []
# if i_select < i_n:
#     for i in range(1,  i_select - 1):
#         ls_final.append(i * (i_select-2 - i))
#     for i in range(1,  i_select):
#         ls_final.append(i * (i_select - i))
# else:
#     for i in range(2*i_n - i_select, i_select):
#         ls_final.append(i * (i_select - i + 1))
#     for i in range(2*i_n - i_select + 1, i_select):
#         ls_final.append(i * (i_select - i + 2))
# # i_select - 3
# print(i_select)
# ls_final.sort()
# print(ls_final)
# print(ls_final[i_k - i_row])