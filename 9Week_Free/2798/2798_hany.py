# 2798번 블랙잭
'''
카드의 합이 21을 넘지 않는 한도 내에서, 카드의 합을 최대한 크게 만드는 게임
딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓는다. 그런 후에 딜러는 숫자 M을 크게 외친다.
N장의 카드 중에서 3장의 카드를 골라야 한다. 
플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.
N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력
'''

N, M = list(map(int, input().split()))

# 1. 카드덱을 만든다.
card = list(map(int, input().split()))

# 2. 모든 경우의 수로 3개를 뽑아내서 21과 가장 가까운 숫자를 뽑아 낸다(합 <= 21, min(len(21 - 합)) )
# 2-1 모든 경우의 수 만들기.
max_card = 0 # 큰 값 초기설정

for x in range(N - 2):
    for y in range(x + 1 , N - 1):
        for z in range(y + 1, N):
            sum_card = card[x] + card[y] + card[z]
            
            # 2-2 card 총합이 M보다 작거나 같아야 하며, 그 합이 가장 커야함. (MAX 구현)
            if max_card < sum_card <= M:
                max_card = sum_card

            if max_card == M:
                break

print(max_card)