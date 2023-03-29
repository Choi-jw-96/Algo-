# 구글링......

n = int(input())

def Hanoi(n, a, b, c):
    if n == 1:
        print(a, c)
        return

    # 원반 n-1 b로 이동
    Hanoi(n-1, a, c, b)
    # 가장 큰 원반을 c 로 이동
    print(a, c)
    # b 에 있는 원반 n-1 개를 c로 이동
    Hanoi(n-1, b, a, c)

print(2 ** n - 1) 
if n <= 20: Hanoi(n, 1, 2, 3)