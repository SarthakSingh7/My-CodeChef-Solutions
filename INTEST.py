T = input().split()  # N,k
count = 0
t = int(T[0])  # number of test cases
for i in range(t):
    N = int(input())
    if N%int(T[1]) == 0:
        count = count + 1
print(count)    
    
    
