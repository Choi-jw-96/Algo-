# 2470번 두 용액
'''
산성 용액의 특성값은 1부터 1,000,000,000까지의 양의 정수로 나타내고,
알칼리성 용액의 특성값은 -1부터 -1,000,000,000까지의 음의 정수로 나타낸다.

같은 양의 두 용액을 혼합한 용액의 특성값은 혼합에 사용된 각 용액의 특성값의 합으로 정의한다.
같은 양의 두 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들려고 한다.

참고로, 두 종류의 알칼리성 용액만으로나
혹은 두 종류의 산성 용액만으로 특성값이 0에 가장 가까운 혼합 용액을 만드는 경우도 존재할 수 있다.
'''
'''
첫 리스트를 순서대로 탐색할 필요가 없다.
'''
import sys
input = sys.stdin.readline

n = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

start = 0
end = n - 1
ans = abs(liquid[start] + liquid[end])
res = [liquid[start], liquid[end]]

while start < end:
    temp_start = liquid[start]
    temp_end = liquid[end]
    temp_sum = temp_start + temp_end

    if abs(temp_sum) < ans:
        ans = abs(temp_sum)
        res = [temp_start, temp_end]
        if ans == 0:
            break
    
    if temp_sum < 0:
        start += 1
    else:
        end -= 1
print(res[0], res[1])