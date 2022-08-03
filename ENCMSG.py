L = []
fi = []
import string
al = string.ascii_lowercase  
for i in range(int(input())):
    N = int(input())
    S = input()
    for i in range(N):
        L.append(S[i])
    C = L    
    for i in range(N-1):
        if i%2 == 0: 
            C[i], C[i+1] = C[i+1], C[i]
    fi= []
    for i in C:
        for k in range(len(al)):
            if i == al[k]:
                fi.append(al[25-k])
    final = ''            
    for i in fi:
        final = final + i  
    print(final)
    C = []
    L = []
    
