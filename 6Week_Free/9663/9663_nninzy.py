n = int(input())
arr = [0] * n
cnt = 0

def check(num): # 해당 자리에 놓아도 되는지 여부 확인
    for v in range(num):
        if arr[num] == arr[v] or abs(arr[num] - arr[v]) == num - v: # 세로의 경우와 대각선이 하나라도 겹친다면 유효 X
            return False
    return True
    
def func(num):
    global cnt
    if num == n : # 퀸을 n행까지 조건에 맞게 다 채워 넣은 경우
        cnt += 1 # 여기까지 도달하게 되면 cnt += 1을 통해 경우의 수를 더하기
        return
    
    for i in range(n):
        arr[num] = i
        if check(num): # 놓아도 되는 자리라면 다음행도 가능한지 확인
            func(num + 1)
func(0)
print(cnt)