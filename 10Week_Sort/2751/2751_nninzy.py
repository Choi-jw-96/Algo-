import sys
n = int(sys.stdin.readline())
num_list = []
for _ in range(n) :
    num_list.append(int(sys.stdin.readline()))
print(*sorted(num_list), sep = '\n')