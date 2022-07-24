T = int(input())  # number of test cases 
lis = []
out = []
for i in range(T):
    tc = input()  # test cases 
    lis.append(tc.split())
for i in lis:
    N = int(i[0])
    M = int(i[1])
    if N%2 == 0 and M%2 == 0:
        single_cell = 0            # the number of 1 * 1 tiles
        out.append(single_cell)
    elif N%2 != 0 and M%2 == 0:
        single_cell = M
        out.append(single_cell)
    elif N%2 == 0 and M%2 != 0:
        single_cell = N
        out.append(single_cell)
    elif N%2 != 0 and M%2 != 0:
        single_cell = N + (M - 1) 
        out.append(single_cell)
        
for i in out:
    print(i)
