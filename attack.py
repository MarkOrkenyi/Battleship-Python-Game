import os
import time
import boardhandle
p1attack = []
p2attack = []


def attack(playernumber, currentboard):
    validrow = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    validcolumn = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    os.system('clear')
    if playernumber == 1:
        attackboard = boardhandle.p1attack
        shipboard = boardhandle.p2ship
        print('\x1b[6;30;42m' + 'Player ' + str(playernumber) + '\x1b[0m')
        print('\x1b[1;31;40m' + "Attackboard" + '\x1b[0m')
        boardhandle.print_board(attackboard)
        print('\x1b[1;34;40m' + "Shipboard" + '\x1b[0m')
        boardhandle.print_board(boardhandle.p1ship)
    else:
        attackboard = boardhandle.p2attack
        shipboard = boardhandle.p1ship
        print('\x1b[6;30;43m' + 'Player ' + str(playernumber) + '\x1b[0m')
        print('\x1b[1;31;40m' + "Attackboard" + '\x1b[0m')
        boardhandle.print_board(attackboard)
        print('\x1b[1;34;40m' + "Shipboard" + '\x1b[0m')
        boardhandle.print_board(boardhandle.p2ship)

    while True:
        attackcord = input("Enter a coordinate to attack (ex. A4): ")

        try:
            int(attackcord[1])
        except IndexError:
            print ('Enter a valid coordinate!')
            continue
        except ValueError:
            print ('Enter a valid coordinate!')
            continue

        if len(attackcord) == 2:
            if attackcord[0] in validcolumn and int(attackcord[1]) in validrow:
                print("")
            else:
                print ('Enter a valid coordinate!')
                continue
        elif len(attackcord) == 3:
            if attackcord[0] in validcolumn and int(attackcord[1] + attackcord[2]) in validrow:
                print("")
            else:
                print ('Enter a valid coordinate!')
                continue
        else:
            print ('Enter a valid coordinate!')
            continue

        x = int(currentboard[0].index(attackcord[0]))
        if len(attackcord) == 2:
            y = int(attackcord[1])
        elif len(attackcord) == 3:
            y = int(attackcord[1] + attackcord[2])

        break
    if shipboard[y][x] == ' ':
        attackboard[y][x] = "X"
        shipboard[y][x] = "X"
        os.system('clear')
        if playernumber == 1:
            print('\x1b[6;30;42m' + 'Player ' + str(playernumber) + '\x1b[0m')
        else:
            print('\x1b[6;30;43m' + 'Player ' + str(playernumber) + '\x1b[0m')
        print('\x1b[1;31;40m' + "Attackboard" + '\x1b[0m')
        boardhandle.print_board(attackboard)
        print('\x1b[1;34;40m' + "Shipboard" + '\x1b[0m')
        boardhandle.print_board(boardhandle.p1ship)
        time.sleep(1)
    elif shipboard[y][x] == 'O':
        print('\x1b[1;31;40m' + "Attackboard" + '\x1b[0m')
        attackboard[y][x] = '\x1b[1;32;40m' + "V" + '\x1b[0m'
        shipboard[y][x] = '\x1b[1;31;40m' + "V" + '\x1b[0m'
        os.system('clear')
        if playernumber == 1:
            print('\x1b[6;30;42m' + 'Player ' + str(playernumber) + '\x1b[0m')
        else:
            print('\x1b[6;30;43m' + 'Player ' + str(playernumber) + '\x1b[0m')
        print('\x1b[1;31;40m' + "Attackboard" + '\x1b[0m')
        boardhandle.print_board(attackboard)
        print('\x1b[1;34;40m' + "Shipboard" + '\x1b[0m')
        boardhandle.print_board(boardhandle.p1ship)
        time.sleep(1)


def nextplayer(playernumber):
    os.system('clear')
    waittimer = 1
    print('\x1b[1;31;40m' + "Player", playernumber, "'s turn will begin in", waittimer, " seconds!" + '\x1b[0m')
    time.sleep(waittimer)
