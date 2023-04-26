# 2776번 암기왕
'''
연종이 하루 동안 본 정수들을 모두 '수첩1'에 적어 놓았다
동규는 연종에게 M개의 질문을 던졌다. 질문의 내용은 “X라는 정수를 오늘 본 적이 있는가?” 이다.
동규는 연종이 봤다고 주장하는 수 들을 '수첩2'에 적어 두었다. 
동규를 도와주기 위해 '수첩2'에 적혀있는 순서대로,
각각의 수에 대하여, '수첩1'에 있으면 1을, 없으면 0을 출력하는 프로그램을 작성
'''
import sys
input = sys.stdin.readline

def bs(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1
    return 0

t = int(input())
for _ in range(t):
    n = int(input()) 
    arr = sorted(list(map(int, input().split()))) #수첩1(arr)
    m = int(input()) #수첩2(targets)
    targets = list(map(int, input().split()))
    for target in targets:
        print(bs(arr, target, 0, n - 1))