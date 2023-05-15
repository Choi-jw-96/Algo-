# https://docs.python.org/3/howto/sorting.html
# 입력
i_n = int(input())
ls_serial = [input() for _ in range(i_n)]
# 우선 순위를 역으로 정렬하면 원하는 조건대로 정렬 가능
# 사전 순으로 정렬
ls_serial.sort()
# 자리의 숫자의 합으로 정렬
# 문자열의 각 자리의 정수의 합을 구하는 함수 정의
def digitsum(string):
    sum = 0
    for string_1 in string:
        #  isdecimal int로 변환 가능한지 확인해주는 method
         if string_1.isdecimal():
              sum += int(string_1)
    return sum
ls_serial.sort(key=digitsum)
# 문자열의 길이로 정렬
ls_serial.sort(key=len)
# 출력
for serial in ls_serial:
    print(serial)