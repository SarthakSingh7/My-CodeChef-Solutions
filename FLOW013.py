try:    
    for i in range(int(input())):
        deg = input().split() # angles of a triangle
        s = int(deg[0]) + int(deg[1]) + int(deg[2])
        if s == 180:
            print('YES')
        else:
            print('NO')
except EOFError:
    pass
