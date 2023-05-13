# 분류: 10주차 정렬
# 문제: 백준 2751 수정렬하기2
# 문제 주소: https://www.acmicpc.net/problem/2751
# 푼 사람: 진홍엽
# 설명: 정렬
# 평점: 3/5 
# 이전에 풀어봤던 건데 메모리를 희생하고 정렬 연산을 덜 가져가는 방법
# 전체 입력 받는 수의 범위 만큼 빈 리스트를 만들고 입력 받은 수를 체크하여 순서대로 출력
import sys


i_n = int(sys.stdin.readline())
# 문제에서 입력 받는 수는 1000000보다 절댓값이 작거나 같은 정수
ls_number = [0] * 2000001
for i in range(i_n):
    ls_number[int(sys.stdin.readline()) + 1000000] = 1
for i in range(2000001):
    if ls_number[i]:
        print(i - 1000000)
# 메모리 46880 KB / 시간 1196 ms




# 일반 sort 남의 풀이 그냥 가져옴 
import sys

n = int(input())
num = []
for _ in range(n):
    num.append(int(sys.stdin.readline()))

num.sort()

for i in num:
    print(i)
# 메모리 77108 KB / 시간 1404 ms

# 위의 풀이가 메모리도 적게 먹고 시간도 적게 소요됨
# 숫자의 범위에 따라서 정렬 방법을 고민