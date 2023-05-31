from collections import deque

n = int(input())
cards = deque(list(range(1, n+1)))

while len(cards) > 1:
    cards.popleft()
    card = cards.popleft()
    cards.append(card)

print(cards[0])