# 13417 카드 문자열
import sys

T = int(input())
for t in range(T):
    n = int(input())
    ls = sys.stdin.readline().split()
    string = ls[0]
    for i in range(1, n):
        if ls[i] <= string[0]:
            string = ls[i] + string
        else:
            string = string + ls[i]
    print(string)