#input 받기
n,m = map(int, input().split())
j = int(input())

basket_l = 1
basket_r = m
result = 0

for _ in range(j):
    drop = int(input())
    # 바구니 범위 내에서 떨어질 경우 => 이동 X
    if basket_l <= drop <= basket_r:
        result += 0
    # 바구니 범위 왼쪽에서 떨어질 경우 => 바구니 왼쪽값이 drop 위치가 될때까지 이동
    elif drop < basket_l:
        cnt = basket_l - drop
        basket_l -= cnt
        basket_r -= cnt
        result += cnt
    # 바구니 범위 오른쪽에서 떨어질 경우 => 바구니 오른쪽 값이 drop 위치가 될때까지 이동
    else:
        cnt = drop - basket_r
        basket_r += cnt
        basket_l += cnt
        result += cnt
print(result)