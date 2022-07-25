try:
    tc = input().split()  #testcase
    #lis = tc.split()
    X = float(tc[0]) # amount for withdrawal should be a multiple of 5
    Y = float(tc[1])  # the current balance
    if X%5 == 0 and (X + 0.50) <= Y:
        bal = Y - (X + 0.50)   # balance
        print(bal)
    else:
        print(Y)# incase of insufficient funds or incorrect amount
except EOFError:
    pass
            
