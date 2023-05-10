import sys
N, M = map(int, sys.stdin.readline().split())
card = list(map(int, input().split()))

max_card = 0
for i in range(len(card)-2):
    for j in range(i+1, len(card)-1):
        for k in range(j+1, len(card)):
            add_card =  card[i] + card[j] + card[k]
            if add_card <= M and add_card > max_card :
                max_card = add_card


print(max_card)