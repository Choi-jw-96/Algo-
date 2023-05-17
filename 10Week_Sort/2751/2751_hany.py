# 2751번 수 정렬하기 2
'''
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 
'''
## 접근방법
'''
단순한 sort
'''
import sys
input = sys.stdin.readline
sort_lst = []
n = int(input())
for _ in range(n):
    sort_lst.append(int(input()))
sort_lst.sort()
for i in sort_lst:
    print(i)