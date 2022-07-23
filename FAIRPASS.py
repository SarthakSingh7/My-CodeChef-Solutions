T = int(input()) # number of test cases 
test_case = []
for i in range(T):
    tc = input() # test cases
    test_case.append(tc.split())
for i in test_case:
    if int(i[0])< int(i[1]):
        print('YES')
    else:
        print('NO')
# note: if chef has 2 passes and he wants to enter with 
# his 2 friends then he can't enter, for that he needs 3 passes
        
