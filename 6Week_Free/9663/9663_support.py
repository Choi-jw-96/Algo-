def dfs(x):
    global Queen
    # 맨 끝 행까지 온 경우 모두 놓을 수 있는 자리이니 += 1
    if x == n:
        Queen += 1
        return
    
    # 행 기준으로 돈다(행이 겹치지 않도록)
    for y in range(n):
        # 열과 좌우 대각선에 겹치는 부분이 없는지 본다
        if not visited_1[y] and not visited_2[x+y] and not visited_3[x-y]:
            # 돌았다면 체크 후 다음 행으로 넘어간다
            visited_1[y] = visited_2[x+y] = visited_3[x-y] = 1
            dfs(x+1)
            # 재귀가 풀릴때 체크를 풀어준다
            visited_1[y] = visited_2[x+y] = visited_3[x-y] = 0
    

n = int(input())

# 같은 열에 있는 지 체크하는 visited
visited_1 = [0] * n
# 우측에서 내려오는 대각선에 있는지 체크하는 visited
# x+y가 같은 값을 나타내기때문에 최대 n+n을 체크 할수 있게 (2 * n)
visited_2 = [0] * (2 * n)
# 좌측에서 내려오는 대각선이 있는지 체크하는 visited
# x-y가 같은 값을 나타내기때문에 최대 n+n을 체크 할수 있게 (2 * n)
visited_3 = [0] * (2 * n)
Queen = 0
dfs(0)
print(Queen)