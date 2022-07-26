try:
    for i in range(int(input())):      # T is directly taken
        tc = input()
        dig_sum = 0   # sum of digits 
        for i in tc :
            dig_sum = dig_sum + int(i)
        print(dig_sum)
except EOFError:
    pass
