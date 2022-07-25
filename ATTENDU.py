T = int(input())  
N_lis = []
B_lis = []
out = []
for i in range(T):
    N = input()
    B = input()
    N_lis.append(N)
    B_lis.append(B)
    for k in N_lis:
        days_left = 120 - int(k)
    for b in B_lis:
        count1 = b.count('1')  # present
    if ((count1 + days_left)/120)*100 >= 75:
        out.append('YES')
    else:
        out.append("NO")
for i in out:
    print(i)
