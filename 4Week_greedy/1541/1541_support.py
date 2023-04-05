n = input().split("-")
li = []

for i in n:
    num = ""
    if "+" in i:
        m = i.split("+")
        num = 0
        for j in m:
            num += int(j)
        li.append(num)
    else:
        li.append(int(i))

if len(li) > 1:
  num = li[0]
  for i in li[1:]:
      num += -i
  print(num)
else:
    print(*li)