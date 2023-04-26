# 2776 암기왕

import sys
input = sys.stdin.readline

def bs(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1
    return 0


t = int(input())
for _ in range(t):
    n = int(input()) 
    array = sorted(list(map(int, input().split()))) 
    m = int(input())
    array2 = list(map(int, input().split()))
    for target in array2:
        print(bs(array, target, 0, n - 1))