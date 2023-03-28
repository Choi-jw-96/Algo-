def hanoi(n, start, goal, side):
    # 1일 경우(가장 작다) 골로 보내줘
    if n == 1:
        return print(start, goal)
    
    # 아니라면 n-1하면주고 goal, side 위치를 바꿔줘
    # 짝 = goal, side 위치 변경
    hanoi(n-1, start, side, goal)
    # 재귀하고 나오면(작은 수가 빠졌다.) 움직일 수 있다
    # 1일 경우와 다른 축에 넣어줘야함
    print(start, goal)
    # 
    hanoi(n-1, side, goal, start)

n = int(input())

# 큰 수를 끝으로 옮기는 것 2**n 마지막 -1
# 20초과하는 수도 나와줘야함
print((2**n) - 1)

if n <= 20:
    hanoi(n, 1, 3, 2)