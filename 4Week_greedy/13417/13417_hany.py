# 13417번 카드 문자열
'''
N장의 카드가 일렬로 놓여있다. 각 카드에는 알파벳이 하나씩 적혀있다.
태욱이는 가장 왼쪽에 있는 카드부터 차례대로 한 장씩 가져올 수 있다.

가장 처음에 가져온 카드는 자신의 앞에 놓는다.
그다음부터는 가져온 카드를 자신의 앞에 놓인 카드들의 가장 왼쪽, 또는 가장 오른쪽에 놓는다.

태욱이는 모든 카드를 다 가져온 후에 자신의 앞에 놓인 카드를 순서대로 이어 붙여 카드 문자열을 만들려고 한다.

태욱이가 만들 수 있는 문자열 중 사전 순으로 가장 빠른 문자열은 “KMU”이다.

태욱이가 만들 수 있는 카드 문자열 중 사전 순으로 가장 빠른 문자열을 출력하는 프로그램을 작성하시오.

'''

# 사전 순으로 가장 빠른은? 오름차순
# 가장 처음 뽑은 알파벳이 기준
# 뽑은 알파벳이 기준 알파벳보다 아스키코드가 작은가?
    # yes -> 왼쪽에 배치한다.
    # no -> 오른쪽에 배치한다.
# 만약 같다면?
# 그 순간 선택이 정답을 좌지우지 하기 때문에 그리디다.
from collections import deque

T = int(input())
for _ in range(T):
    n = int(input())
    cards = list(input().split())
    # print(ord('A'))

    standard = cards.pop(0)
    ans = deque()
    ans.append(standard)
    # print(cards)
    for card in cards:
        # 뽑은 카드의 아스키 코드가 크다면
        if ord(standard) < ord(card):
            ans.append(card)
        elif ord(standard) >= ord(card):
            ans.appendleft(card)
            standard = card
    ans = list(ans)
    for a in ans:
        print(a, end="")
    print()
