for t in range(int(input())):
    # 오늘 본 숫자를 입력받고 이진탐색으로 풀기 위해 오름차순 정렬해준다
    see_n = int(input())
    see = sorted(list(map(int, input().split())))
    write_n = int(input())
    write = list(map(int, input().split()))
    
    # 적은 숫자만큼 반복한다
    for n in write:
        # 시작과 끝을 정해준다
        start, end = 0, see_n-1
        while True:
            mid = (start + end) // 2
            # 같은 숫자가 나오면 1
            if see[mid] == n:
                print(1)
                break
            # 아님 0
            if start >= end:
                print(0)
                breaㅏ
            # 적어논 숫자가 본 숫자보다 크면 start를 조정
            if see[mid] < n:
                start = mid + 1
            else:
                end = mid - 1