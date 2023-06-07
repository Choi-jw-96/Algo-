n = int(input())
arr = list(map(int, input().split(' ')))
arr.sort()

start = 0
end = n-1

answer = abs(arr[start] + arr[end])
final = [arr[start], arr[end]]


while start < end:
    start_val = arr[start]
    end_val = arr[end]
    sum = start_val + end_val

    if abs(sum) < answer:
        answer = abs(sum)
        final = [start_val, end_val]
        if answer == 0:
          break
    if sum < 0:
        start += 1
    else:
        end -= 1

print(final[0], final[1])