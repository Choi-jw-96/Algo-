# 1946번 신입사원
'''
서류심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발한다는 원칙을 세웠다.
이러한 조건을 만족시키면서, 진영 주식회사가 이번 신규 사원 채용에서 선발할 수 있는 신입사원의 최대 인원수를 구하는 프로그램
'''
'''
적어도 하나가 1위이면 붙는다.
1위가 없고 꼴지만 있을 경우, 무조건 떨어진다.
1위의 다른 순위보다 낮으면 무조건 떨어진다.
1위의 다른 순위보다 높으면, 1위 대신 기준이된다.
대신 기준이 된 순의보다 낮으면 떨어진다. 높으면 붙는다. 그리고 또다시 기준이된다.
'''
import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    test = []
    n = int(input())
    for _ in range(n):
        paper, review = map(int, input().split())
        test.append((paper, review))

    test.sort()
    # print(test)

    win = test[0][1]
    cnt = 1
    for i in range(1, n):
        if test[i][1] < win:
            win = test[i][1]
            cnt += 1
    print(cnt)