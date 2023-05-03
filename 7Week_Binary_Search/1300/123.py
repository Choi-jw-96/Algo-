from bisect import bisect_left, bisect_right

nums = [1,2,3,4,5]
n = 2
print(bisect_left(nums, n))
print(bisect_right(nums, n))

# nums = [1,2,3,4,5]
# nums = [5,4,3,2,1]