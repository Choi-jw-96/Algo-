import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

length = 0
jump = 0

for n in range(N):
    if length == N:
        break
    for i in range(A[length],-1,-1):
        if length + i <= N:
            length += i       
            jump += 1      
            break

if length < N:
    print(-1)
else:
    print(jump)
    
        
# ls = [A[0]]
# length = 0

# for i in range(A[length],0,-1):
#     if length + i > N:
#         for elem in range(i):

# graph = [list(range(A[n],-1,-1)) for n in range(N)]
# visited = [False] * N
# # print(graph)
# length = 0
# cnt = 0

# def bfs(v,cnt):
#     cnt += 1
#     visited[v] = True
#     for i in graph[v]:
#         if length + i > 10:
#             return False
#         elif length + i < 10:
#             bfs(length + i,cnt)

# ls = [A[0]]
# length = A[0]
# for n in range(N):
#     for i in range(A[ls[-1]],-1,-1):
#         if length + i <= 10:
#             length += i
#             ls.append(length)
#             print(n,ls)
#             break