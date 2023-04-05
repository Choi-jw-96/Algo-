formula = input().split('-')
result = 0
for i in formula[0].split('+'):
    result += int(i)
for i in formula[1:]:
    for j in i.split('+'):
        result -= int(j)
print(result)