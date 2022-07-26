try:
    FL_sum = 0 #first and last digit sum
    for i in range(int(input())):
        N = input()
        FL_sum = int(N[0]) + int(N[-1])
        print(FL_sum)
except EOFError:
    pass
    
