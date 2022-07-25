T =  int(input()) # number of test cases 
# total distanmce walked in a day = 2 * X
# total dist walked in a week = 10 * X
lis = []
out = []
for i in range(T):
    tc = input() # test cases 
    lis.append(tc.split())
for i in lis:
    X = int(i[0])
    total_dist = 10 * X
    out.append(total_dist)
for i in out:
    print(i)
