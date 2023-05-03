T = int(input())
for t in range(T):
    # 수첩 1은 비교군이기에 set으로 정리
    n = int(input())
    note1 = set(map(int, input().split()))
    # 수첩 2는 기준으로 비교해야함
    m = int(input())
    note2 = [*map(int, input().split())]
    answer = []
    # 잡기술 : answer을 문자열로 받는 방법
    for i in note2:
        if i in note1:
            answer.append(1)
            # answer += '1' +'\n'
        else:
            answer.append(0)
    print(*answer, sep='\n')