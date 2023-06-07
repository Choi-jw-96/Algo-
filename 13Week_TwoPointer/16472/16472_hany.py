# 16472번 고냥이
'''
문자열을 주면 그 중에서 최대 N개의 종류의 알파벳을 가진 연속된 문자열밖에 인식하지 못한다. 
문자열이 주어졌을 때 이 번역기가 인식할 수 있는 최대 문자열의 길이는 얼마인지가 궁금해졌다.
'''
n = int(input())
string = list(input())
dict = {}
result = [0, 0]
start = 0
end = 0

while start < len(string) and end < len(string):

    if string[end] not in dict:
        dict[string[end]] = 1
    else:
        dict[string[end]] += 1

    if len(dict) > n:
        while start <= end and len(dict) > n:
            if dict[string[start]] == 1:
                dict.pop(string[start])
            else:
                dict[string[start]] -= 1
            start += 1

    if len(dict) <= n:
        if result[1] - result[0] < end - start:
            result[0] = start
            result[1] = end
    end += 1
 
print(result[1] - result[0] + 1)