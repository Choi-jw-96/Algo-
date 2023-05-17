# 13164번 행복 유치원
'''
N명의 원생들을 키 순서대로 일렬로 줄 세우고, 총 K개의 조로 나누려고 한다.
각 조에는 원생이 적어도 한 명 있어야 하며, 같은 조에 속한 원생들은 서로 인접해 있어야 한다.
조별로 인원수가 같을 필요는 없다.
조마다 티셔츠를 맞추는 비용은 조에서 가장 키가 큰 원생과 가장 키가 작은 원생의 키 차이만큼 든다.
최대한 비용을 아끼고 싶어 하는 태양이는 K개의 조에 대해 티셔츠 만드는 비용의 합을 최소로 하고 싶어한다. 
'''
'''
최소비용 -> 그리디?
최소비용이려면 가장 키가 큰 원생과 가장 키가 작은 원생의 차이가 적어야 한다(즉 비슷한 애들끼리 묶는다.)
혼자인 조는 최대한 키가 커야 한다(키큰 원생 - 키작원생 = 0 이니까)

태양이는 원생들을 키 순서대로 줄 세웠으므로, 왼쪽에 있는 원생이 오른쪽에 있는 원생보다 크지 않다. 
'''
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
children = list(map(int, input().split()))
cost = []
for i in range(1, n):
    cost.append(children[i] - children[i - 1])
cost.sort(reverse=True)
# print(cost)
print(sum(cost[k - 1:]))
