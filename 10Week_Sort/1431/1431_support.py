# 문자열 판별 - isalpha( )
# 숫자 + 문자열 판별 isalnum( )
def sum_num(x):
    result = 0
    for i in x:
      # 숫자인지 판별하는 방법
      # isdecimal( ): 어떤 문자열이 int형으로 변환이 가능하면 True를 반환
      # isdigit( ): 어떤 문자열이 숫자의 형태면 True를 반환
      # isnumeric( ): 숫자값 표현에 해당하는 문자열이면 True를 반환
      if i.isdigit():
        result += int(i)
    return result


n = int(input())
num = []

for i in range(n):
    num.append(input())

num.sort(key=lambda x:(len(x), sum_num(x), x))
print(*[i for i in num])