# 3253번 트램
'''
In every intersection there is a switch pointing to the one of the rails going out of the intersection. 
When the tram enters the intersection it can leave only in the direction the switch is pointing. 
If the driver wants to go some other way, he/she has to manually change the switch.

When a driver has do drive from intersection A to the intersection B
he/she tries to choose the route that will minimize the number of times
he/she will have to change the switches manually.

calculate the minimal number of switch changes necessary to travel from intersection A to intersection B.

<입력>
The first line of the input file contains integers N, A and B, separated by a single blank
첫째줄 : n(네트워크 인터섹션 개수), a -> b
첫 번째 숫자: i번째 교차지점에서 나가는 레일의 수
두 번째 숫자: i번째 교차지점에서 스위치가 가르키고 있는 연결된 교차지점 
세 번쨰 숫자: 해당 교차지점에서 스위치가 가르키고 있지 않은 연결된 다른 교차지점을 나타냅니다. (스위치를 수동으로 변경하여 변경가능)

<출력>
A지점부터 B지점으로 도착할 수 있는 최소 스위치 변경 횟수를 출력해야합니다.\
A지점부터 B지점에 도달할 수 없으면 '-1'를 출력합니다.
'''
## 접근 방법
'''
최대한 수동 변겅 없이 출발지에서 목적지로 향해야 함
'''
n, s, e = map(int, input().split())
rail = [[] for _ in range(n + 1)]
rail[0] = (0, 0)
print(rail)
INF = 1e9
distance = [INF] * (n + 1)

# 직접갈 수 있는 곳은 가중치 0을 주고,
# 수동으로 바꿔야하는 곳은 가중치 1을 주자.
for _ in range(1, n + 1):
    route = map(int, input().split)
    if route[0] == 1:
        rail[_].append(route[1], 0)
    if route[0] >= 2:
        rail[_].append(route[1, 0])
        pass


