T = int(input()) # number of test cases
li=[]
out = [] # list of output
for i in range(T):
    tc = input() # test case
    li.append(tc.split())
for i in li:
    s1 = int(i[0]) + int(i[1]) # price for style 1
    s2 = int(i[2]) + int(i[3]) # price for style 2
    if s1>= s2:
        out.append(s2)
    else:
        out.append(s1)
for i in out:
    print(i)
