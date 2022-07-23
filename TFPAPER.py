T = int(input()) # number of test cases
lis = []
out = []
for i in range(T):
    tc = input() # test cases
    lis.append(tc.split())
for i in lis:
    res = int(i[0]) - int(i[1])
    out.append(res)
    res = 0
for i in out:
    print(i)
