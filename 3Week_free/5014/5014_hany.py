# 5014번 스타트링크
'''
스타트링크는 총 F층으로 이루어진 고층 건물에 사무실이 있고, 
스타트링크가 있는 곳의 위치는 G층이다.
강호가 지금 있는 곳은 S층이고, 이제 엘리베이터를 타고 G층으로 이동하려고 한다.

U버튼은 위로 U층을 가는 버튼, D버튼은 아래로 D층을 가는 버튼이다.
(만약, U층 위, 또는 D층 아래에 해당하는 층이 없을 때는, 엘리베이터는 움직이지 않는다)

강호가 G층에 도착하려면, 버튼을 적어도 몇 번 눌러야 하는지 구하는 프로그램을 작성하시오.
만약, 엘리베이터를 이용해서 G층에 갈 수 없다면, "use the stairs"를 출력한다.
'''
# 0. 초기값 설정
f, s, g, u, d = map(int, input().split())
s = s - 1
g = g - 1
check = [False] * f
floors = [-1 for _ in range(f)]
moving = [u, -d]
floors[s] = 0



# 1. bfs 함수 만들기
# 주의점: 최소값 cnt하기

from collections import deque

def bfs(i):
    q = deque()
    q.append(i)
    check[i] = True

    while q:
       cur = q.popleft()
       for n in range(2):
          new_cur = cur + moving[n]
          ## 범위 확인
          if 0<= new_cur < f and not check[new_cur]:
             q.append(new_cur)
             floors[new_cur] = floors[cur] + 1 # 1씩 더해나가서 최소값구하기
             check[new_cur] = True 

bfs(s)

# 절대 도달 불가한 경우 (print('use the stairs'))
if floors[g] == -1:
   print('use the stairs')
else:
   print(floors[g])  
