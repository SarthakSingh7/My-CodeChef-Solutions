for i in range(int(input())):
    N = input()
    a = ''
    for j in range(1,len(N)+1):
        a = a + N[-j]
    print(int(a))    
