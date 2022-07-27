for i in range(int(input())):
    AB = input().split()
    A = int(AB[0])
    B = int(AB[1])
    if A > B:
        print('>')
    elif A == B:
        print('=')
    else: 
        print('<')
