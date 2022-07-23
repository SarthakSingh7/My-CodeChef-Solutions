T = int(input())  # number of test cases
lis = []
out = []
for i in range(T):
    tc = input()   # test cases
# X levels remaining, Y minutes to complete each level, Z min break after 3 levels
    lis.append(tc.split())
for i in lis:
    if int(i[0]) <= 3:
        a = int(i[0])*int(i[1])
        out.append(a)
    elif int(i[0])%3 == 0:
        a1 = int(i[0])*int(i[1]) + ((int(i[0])//3)-1)*int(i[2])
        out.append(a1)
    elif int(i[0])%3 != 0:
        a2 = int(i[0])*int(i[1]) + (int(i[0])//3)*int(i[2])
        out.append(a2)
for i in out:
    print(i)
