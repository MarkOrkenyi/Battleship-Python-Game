import os
import boardhandle
import random
import copy
import sound
shiplength = [5, 3, 3, 2, 1]
shipcord = []


# Puts a ship onto the current player's board


def addship(length, currentboard, playernumber, AI):
    shipcord0 = []
    validrow = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    validcolumn = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    HV = ["H", "V"]
    print("Current ship length:", length)
    if (playernumber == 2) and (AI == 1):
        orient = random.choice(HV)
    else:
        orient = input("Enter H or V: ")
        orient = orient.upper()
        while True:
            if orient == "V":
                break
            elif orient == "H":
                break
            else:
                print("Please enter H for Horizontal, or V for Vertical")
                orient = input("Enter H or V: ")
    while True:
        if (playernumber == 2) and (AI == 1):
            x_ai = str(random.choice(validcolumn))
            y_ai = str(random.choice(validrow))
            c = x_ai + y_ai
        else:
            c = input("Enter the origin of your ship (ex. A4): ")
            c = c.upper()
            try:
                int(c[1])
            except IndexError:
                print ('Enter a valid coordinate!')
                continue
            except ValueError:
                print ('Enter a valid coordinate!')
                continue

            if len(c) == 2:
                if c[0] in validcolumn and int(c[1]) in validrow:
                    print("")
                else:
                    print ('Enter a valid coordinate!')
                    continue
            elif len(c) == 3:
                if c[0] in validcolumn and int(c[1] + c[2]) in validrow:
                    print("")
                else:
                    print ('Enter a valid coordinate!')
                    continue
            else:
                print ('Enter a valid coordinate!')
                continue
        x = int(currentboard[0].index(c[0]))
        if len(c) == 2:
            y = int(c[1])
        elif len(c) == 3:
            y = int(c[1] + c[2])
        shipparameter = [orient, length, x, y]

        # check is on board
        if orient == 'H' and int(int(x) + int(length)) > 11:
            print ('Ship out of board! Enter another coordinate!')
            continue
        if orient == 'V' and int(int(y) + int(length)) > 11:
            print ('Ship out of board! Enter another coordinate!')
            continue

        # check ship overlap
        if orient == 'H':
            q = 0
            for p in range(length):
                if currentboard[y][x + p] == "O":
                    q = q + 1
            if q == 0:
                break
            else:
                print ('Ship overlaps with other ships on board! Enter another coordinate!')
                print()
                continue
        if orient == 'V':
            q = 0
            for p in range(length):
                if currentboard[y + p][x] == "O":
                    q = q + 1
            if q == 0:
                break
            else:
                print ('Ship overlaps with other ships on board! Enter another coordinate!')
                print()
                continue

    if shipparameter[0] == "H":
        for i in range(length):
            currentboard[y][x + i] = "O"
            sc = str(validcolumn[x - 1 + i]) + str(y) + "+"  # "+" added as switcher character
            shipcord0.append(sc)
        shipcord.append(shipcord0)
    else:
        for i in range(length):
            currentboard[y + i][x] = "O"
            sc = str(validcolumn[x - 1]) + str(y + i) + "+"  # "+" added as switcher character
            shipcord0.append(sc)
        shipcord.append(shipcord0)


def select_ships(playernumber, ships, currentboard, AI):
    '''Adds a ship with the given length to the current players shipboard'''
    del shipcord[:]
    for a in range(ships):
        os.system('clear')
        if playernumber == 1:
            print('\x1b[6;30;42m' + 'Player ' + str(playernumber) + '\x1b[0m')
        elif playernumber == 2:
            if AI == 1:
                print('\x1b[6;30;43m' + "Computer" + '\x1b[0m')
            else:
                print('\x1b[6;30;43m' + 'Player ' + str(playernumber) + '\x1b[0m')
        print()
        boardhandle.print_board(currentboard)
        addship(shiplength[a], currentboard, playernumber, AI)
        sound.play_sound("placement")
    return shipcord
