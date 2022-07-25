# X = number of weeks classes attended 
# Y =  fee for 1 week 
T = int(input())  # number of test cases 
lis = []
out = []
for i in range(T):
    tc = input() # test cases 
    lis.append(tc.split())
for i in lis:
    X = int(i[0])  # number of weeks 
    Y = int(i[1])  # fee for 1 week 
    total_fee = X*Y
    out.append(total_fee)
for i in out:
    print(i)
