num = input()

num_1 = int(num[0])

n = (len(num)-1) * 9 + num_1

for i in range(n, 0, -1):
    J = 0
    for j in str(int(num) - i):
        J += int(j)
    if J + int(num) - i == int(num):
        print(int(num) - i)
        break

    if i == 1:
        print(0)