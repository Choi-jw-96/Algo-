import sys
input = sys.stdin.readline

num = []
for _ in range(int(input())):
    s = input().rstrip()
    
    # 자리수의 합
    summ = 0
    for i in s:
        if i.isdigit():
            summ += int(i)
    num.append((s,summ))
    
num.sort(key=lambda x:(len(x[0]),x[1],x[0]))

for i in num:
    print(i[0])


# isdigit( ): 문자열이 숫자의 형태인지