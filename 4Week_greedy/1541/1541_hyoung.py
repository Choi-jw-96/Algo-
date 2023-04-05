# 1541 잃어버린 괄호
import re

expr = input()
nums = list(map(int, re.split(r'[+, -]', expr)))
operation = ''
result = 0

for elem in expr:
    if elem in ['+', '-']:
        operation += elem

minus = operation.find('-')

if minus == -1:
    for num in nums:
        result += num
else:
    for i in range(minus + 1):
        result += nums[i]
    for j in range(minus + 1, len(nums)):
        result -= nums[j]
print(result)

