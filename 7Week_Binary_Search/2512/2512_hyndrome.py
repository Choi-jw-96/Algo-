# 분류: 7주차 이분탐색
# 문제: 백준 2512 예산
# 문제 주소: https://www.acmicpc.net/problem/2512
# 푼 사람: 진홍엽
# 설명: 이분탐색

# 입력 받기
i_n = int(input())
ls_city_budget = list(map(int, input().split()))
i_total_budget = int(input())

# 예산 배정함수 (예산 배정 리스트, 총 예산) 입력 받음
def city_budget_divider(budgets, total_budget):
    # 이진탐색을 위한 정렬
    budgets.sort()
    # 결과값 저장을 위한 빈 리스트
    ls_result = []

    # 목표 금액을 받아서 예산 배정 리스트에 처리 후 총예산 값과 비교하는 함수
    # 배정 금액이 총 예산 보다 작을 경우 True, 아닐 경우 False 반환
    def budget_allocator(target):
        nonlocal budgets
        nonlocal total_budget
        budget_sum = 0
        for budget in budgets:
            if budget <= target:
                budget_sum += budget
            else:
                budget_sum += target
        if budget_sum <= total_budget:
            return True
        else:
            return False
    
    # 이진탐색 함수
    def bi_search(start, end):
        if start <= end:
            mid = (start + end) // 2
            if budget_allocator(mid):
                ls_result.append(mid)
                bi_search(mid + 1, end)
            else:
                bi_search(start, mid - 1)
    # 이진탐색함수 실행 (전체예산을 예산을 할당 받아야하는 도시만큼 나눈 값을 min으로 
    # 예산 할당 받은 도시 중 가장 큰 요청 값을 max로 받음)
    bi_search(total_budget // len(budgets), budgets[-1])
    # 저장된 결과 값 중 가장 큰 값 출력
    return max(ls_result)

if sum(ls_city_budget) <= i_total_budget:
    print(max(ls_city_budget))
else:
    print(city_budget_divider(ls_city_budget, i_total_budget))