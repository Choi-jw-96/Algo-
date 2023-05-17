# 1431번 시리얼 번호
'''
기타를 시리얼 번호 순서대로 정렬하고자 한다.
모든 시리얼 번호는 알파벳 대문자 (A-Z)와 숫자 (0-9)로 이루어져 있다.

시리얼번호 A가 시리얼번호 B의 앞에 오는 경우는 다음과 같다.

1. A와 B의 길이가 다르면, 짧은 것이 먼저 온다.
2. 만약 서로 길이가 같다면, A의 모든 자리수의 합과 B의 모든 자리수의 합을 비교해서 작은 합을 가지는 것이 먼저온다. (숫자인 것만 더한다)
3. 만약 1,2번 둘 조건으로도 비교할 수 없으면, 사전순으로 비교한다. 숫자가 알파벳보다 사전순으로 작다.
시리얼이 주어졌을 때, 정렬해서 출력하는 프로그램을 작성하시오.

1. 짧은 것 먼저
2. 숫자 합 적은 것 먼저
3. 사전 순
'''
import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    x = input().rstrip()
    arr.append(x)

for i in range(n - 1):
    for j in range(i + 1, n):
        # 짧은 게 먼저
        if len(arr[i]) > len(arr[j]):
            arr[i], arr[j] = arr[j], arr[i]
        # 같다면
        elif len(arr[i]) == len(arr[j]):
            sum_x = 0
            sum_y = 0
            # print(list(zip(arr[i], arr[j])))
            for x, y in zip(arr[i], arr[j]):
                if x.isdigit():
                    sum_x += int(x)
                if y.isdigit():
                    sum_y += int(y)
            if sum_x > sum_y:
                arr[i], arr[j] = arr[j], arr[i]        
            elif sum_x == sum_y:
                for x, y in zip(arr[i], arr[j]):
                    if x > y:
                        arr[i], arr[j] = arr[j], arr[i]
                        break
                    elif x < y:
                        break
for a in arr:
    print(a)