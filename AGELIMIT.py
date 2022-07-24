# X Y A where age >= X, age < Y, Current age  A
T = int(input())   # number of test cases
out = []
lis = []
for i in range(T):
    tc = input()   # test cases
    lis.append(tc.split())
for i in lis:
    X = int(i[0])
    Y = int(i[1])
    A = int(i[2])
    if X <= A < Y:
        print("YES")
    else:
        print("NO")
