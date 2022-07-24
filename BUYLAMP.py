# red and blue lamps, cost of Red is X and Cost of Blue is Y
# buy N lamps, K lamps are Red
T = int(input()) # number of test cases 
lis = []
out = []
for i in range(T):
    tc = input()  # test cases
    lis.append(tc.split())
for i in lis:
    #if int(i[2]<=int(i[3])):    # price of blue is more
    price1 = int(i[0]) * int(i[2])
    #if int(i[2]>int(i[3])):    # price of red is more
    price2 = (int(i[1]) * int(i[2])) + (int(i[0]) - int(i[1])) * int(i[3])
    final_price = min(price1, price2)
    out.append(final_price)
for i in out:
    print(i)
