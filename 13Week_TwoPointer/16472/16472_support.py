import sys

input = sys.stdin.readline
n = int(input())
string = input().rstrip()
d = {}
answer = front = 0
for rear in range(len(string)):
    # rear를 1씩 증가시키며 딕셔너리의 크기를 계속 확인한다.
    d.setdefault(string[rear], 0)
    d[string[rear]] += 1
    # 만약 딕셔너리 크기가 n보다 크면 딕셔너리에서 front 값을 -1해주며 n을 맞춘다.
    while len(d) > n:
        d[string[front]] -= 1
        # 딕셔너리에서 제거
        if d[string[front]] == 0:
            del d[string[front]]
        front += 1
    answer = max(answer, rear - front + 1)
print(answer)