#method 1 
T = int(input())
for i in range(T):
    A,B = map(int, input().split())
    print(A%B)
    
# Method 2 (long)
# T = int(input())  # number of tet cases 
# lis = []
# out = []
# for i in range(T):
#     tc = input()  # test cases 
#     lis.append(tc.split())
# for i in lis:
#     mod = int(i[0])%int(i[1]) 
#     out.append(mod)
# for i in out:
#     print(i)    
    
