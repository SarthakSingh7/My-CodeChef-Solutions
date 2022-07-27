try:
    for i in range(int(input())):
        l = input()
        if l in ['b','B']:
            print('BattleShip')
        elif l in ['c','C']:
            print('Cruiser')
        elif l in ['d','D']:
            print('Destroyer')
        elif l in ['f','F']:
            print('Frigate')
except EOFError:
    pass
