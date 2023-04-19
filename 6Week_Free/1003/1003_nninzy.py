t = int(input())
 
for _ in range(t):
    cnt0 = [1,0]
    cnt1 = [0,1]
    n = int(input())
    if n>1:
        for i in range(n-1):
            cnt0.append(cnt1[-1])
            cnt1.append(cnt0[-2]+cnt1[-1]) 
 
    print(cnt0[n], cnt1[n])