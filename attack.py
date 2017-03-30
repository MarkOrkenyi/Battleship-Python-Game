import os
import time
import boardhandle
import prints
import random
p1attack = []
p2attack = []


def attack(playernumber, currentboard, AI, p1shipcord, p2shipcord):
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
        if (playernumber == 2) and (AI == 1):
            attackboard = boardhandle.p2attack
            shipboard = boardhandle.p1ship
        else:
            attackboard = boardhandle.p2attack
            shipboard = boardhandle.p1ship
            print('\x1b[6;30;43m' + 'Player ' + str(playernumber) + '\x1b[0m')
            print('\x1b[1;31;40m' + "Attackboard" + '\x1b[0m')
            boardhandle.print_board(attackboard)
            print('\x1b[1;34;40m' + "Shipboard" + '\x1b[0m')
            boardhandle.print_board(boardhandle.p2ship)

    while True:
        if (playernumber == 2) and (AI == 1):
            x_ai = str(random.choice(validcolumn))
            y_ai = str(random.choice(validrow))
            attackcord = x_ai + y_ai
        else:
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

    elif shipboard[y][x] == 'O':
        attackboard[y][x] = '\x1b[1;32;40m' + "V" + '\x1b[0m'
        shipboard[y][x] = '\x1b[1;31;40m' + "V" + '\x1b[0m'

    if playernumber == 1:
        os.system('clear')
        print('\x1b[6;30;42m' + 'Player ' + str(playernumber) + '\x1b[0m')
        print('\x1b[1;31;40m' + "Attackboard" + '\x1b[0m')
        boardhandle.print_board(boardhandle.p1attack)
        print('\x1b[1;34;40m' + "Shipboard" + '\x1b[0m')
        boardhandle.print_board(boardhandle.p1ship)
        time.sleep(1)

    elif playernumber == 2:
        os.system('clear')
        print('\x1b[6;30;43m' + 'Player ' + str(playernumber) + '\x1b[0m')
        print('\x1b[1;31;40m' + "Attackboard" + '\x1b[0m')
        boardhandle.print_board(boardhandle.p2attack)
        print('\x1b[1;34;40m' + "Shipboard" + '\x1b[0m')
        boardhandle.print_board(boardhandle.p2ship)
        time.sleep(1)

        if playernumber == 1:
            for i in range(len(p2shipcord)):
                for j in range(len(p2shipcord[i])):
                    if attackcord in p2shipcord[i][j]:
                        p2shipcord[i][j] = attackcord + "-"
        elif playernumber == 2:
            for i in range(len(p1shipcord)):
                for j in range(len(p1shipcord[i])):
                    if attackcord in p1shipcord[i][j]:
                        p1shipcord[i][j] = attackcord + "-"
        if playernumber == 1:
            for i in range(len(p2shipcord)):
                count = 0
                for j in range(len(p2shipcord[i])):
                    if p2shipcord[i][j].count("-"):
                        count += 1
                        if count == len(p2shipcord[i]):
                            for cord in range(len(p2shipcord[i])):
                                x = int(currentboard[0].index(p2shipcord[i][cord][0]))
                                if len(p2shipcord[i][cord]) == 3:
                                    y = int(p2shipcord[i][cord][1])
                                elif len(p2shipcord[i][cord]) == 4:
                                    y = int(p2shipcord[i][cord][1] + p2shipcord[i][cord][2])
                                attackboard[y][x] = '\x1b[1;32;45m' + "Y" + '\x1b[0m'
                                shipboard[y][x] = '\x1b[1;31;45m' + "Y" + '\x1b[0m'
        elif playernumber == 2:
            for i in range(len(p1shipcord)):
                count = 0
                for j in range(len(p1shipcord[i])):
                    if p1shipcord[i][j].count("-"):
                        count += 1
                        if count == len(p1shipcord[i]):
                            for cord in range(len(p1shipcord[i])):
                                x = int(currentboard[0].index(p1shipcord[i][cord][0]))
                                if len(p1shipcord[i][cord]) == 3:
                                    y = int(p1shipcord[i][cord][1])
                                elif len(p1shipcord[i][cord]) == 4:
                                    y = int(p1shipcord[i][cord][1] + p1shipcord[i][cord][2])
                                attackboard[y][x] = '\x1b[1;32;45m' + "Y" + '\x1b[0m'
                                shipboard[y][x] = '\x1b[1;31;45m' + "Y" + '\x1b[0m'


def nextplayer(playernumber, AI):
    os.system('clear')
    waittimer = 1
    print('\x1b[1;31;40m' + "Player", playernumber, "'s turn will begin in", waittimer, " seconds!" + '\x1b[0m')
    time.sleep(waittimer)
