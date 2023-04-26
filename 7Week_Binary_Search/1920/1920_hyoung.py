# 1920 수 찾기

import sys
input = sys.stdin.readline
n = int(input())
array = sorted(list(map(int, input().split())))
m = int(input())
targets= list(map(int, input().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for target in targets:
    print(binary_search(array, target, 0, n - 1))