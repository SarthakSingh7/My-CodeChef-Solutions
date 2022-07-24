T = int(input())  # number of test cases
out = []
lis = []
for i in range(T):
    tc = input()
    lis.append(tc.split())
# N is number of candies, K is number of pockets in the bag and M is capacity of a pockets
for i in lis:
    if int(i[0]) <= int(i[1])*int(i[2]):
        bags = 1
        out.append(bags)
    elif int(i[0]) > int(i[1])*int(i[2]) and int(i[0])/(int(i[1])*int(i[2])) == int(int(i[0])/(int(i[1])*int(i[2]))):
        bags = int(i[0])//(int(i[1])*int(i[2]))
        out.append(bags)
    elif int(i[0]) > int(i[1])*int(i[2]) and int(i[0])/(int(i[1])*int(i[2])) != int(int(i[0])/(int(i[1])*int(i[2]))):
        bags = (int(i[0])//(int(i[1])*int(i[2]))) + 1
        out.append(bags)
for i in out:
    print(i)
# NOTE: this problem can be solved easily if we import the math library and use the ceil function
