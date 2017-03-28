#define listsss
p1ship = []
p2ship= []
p1attack = []
p2attack = []

shipcord0 = []
shipcord = []
pshipcord = []

# Function to creat empty field
def empty_board(matrix):
    for i in range (11):
        matrix.append([])
        for j in range (11):
            matrix[i].append(' ')
    # set initial values for the column and row indexes
    matrix[0] = [' ','A','B','C','D','E','F','G','H','I','J']
    for i in range(1,len(matrix)):
        matrix [i][0] = i

#print out given board
def print_board(matrix): 
    for i in range(len(matrix)):
        if i==0:
            for j in range(len(matrix[i])):
                if j==0:
                    print ('\x1b[31m{:2}\x1b[0m '.format(matrix[i][j]), end='')
                else:
                    print ('\x1b[4m{}\x1b[0m '.format(matrix[i][j]), end='')
            print()
        else:
            print ('\x1b[0m{:2}\x1b[0m|'.format(matrix[i][0]), end='')
            for j in range(1,len(matrix[i])):
                print ('\x1b[4;1m{}\x1b[0m|'.format(matrix[i][j]), end='')
            print()
    print()


# Puts a ship onto the current player's board
def addship(length,currentboard,ships):
    shipcord0=[]
    validrow = [1,2,3,4,5,6,7,8,9,10]
    validcolumn = ['A','B','C','D','E','F','G','H','I','J']
    print("Current ship length:",length)
    orient = input("Enter H or V: ")
    while True:
        if orient == "V":
            break
        elif orient == "H":
            break
        else:
            print("Please enter H for Horizontal, or V for Vertical")
            orient = input("Enter H or V: ")
    
    while True:
        c = input("Enter the origin of your ship (ex. A4): ")
    
        try:
            int(c[1])
        except IndexError:
            print ('Enter a valid coordinate!')
            continue  
        except ValueError:
            print ('Enter a valid coordinate!')
            continue
        
        if len(c) == 2:
            if  c[0] in validcolumn and int(c[1]) in validrow:
                print("")
            else:
                print ('Enter a valid coordinate!')
                continue
        elif len(c) == 3:
            if  c[0] in validcolumn and int(c[1]+c[2]) in validrow:
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
            y = int(c[1]+c[2])
        shipparameter = [orient,length,x,y]   
        
        # check is on board
        if orient == 'H' and int(int(x)+int(length)) > 11:
            print ('Ship out of board! Enter another coordinate!')
            continue
        if orient == 'V' and int(int(y)+int(length)) > 11:
            print ('Ship out of board! Enter another coordinate!')
            continue        
        
        # check ship overlap
        if orient == 'H':
            q = 0
            for p in range(length):
                if currentboard [y][x+p] == "O":
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
                if currentboard [y+p][x] == "O":
                    q = q + 1
            if q == 0:
                break
            else:
                print ('Ship overlaps with other ships on board! Enter another coordinate!')
                print()
                continue
                
    if shipparameter[0] == "H":
        for i in range(length):            
            currentboard[y][x+i] = "O"
            sc = str(y) + str(x+i)
            shipcord0.append(sc)
        shipcord.append(shipcord0)
    else:
        for i in range(length):            
            currentboard[y+i][x] = "O"
            sc = str(y+i) + str(x)
            shipcord0.append(sc)
        shipcord.append(shipcord0)

def select_ships(playernumber):
    for a in range(ships):
        os.system('clear')
        if playernumber == 1:
            print('\x1b[6;30;42m' + 'Player ' + str(playernumber) + '\x1b[0m')
        else:
            print('\x1b[6;30;43m' + 'Player ' + str(playernumber) + '\x1b[0m')
        print()
        print_board(currentboard)    
        addship(shiplength[a],currentboard,ships)
    pshipcord.append(shipcord)
    
def attack(playernumber):
    validrow = [1,2,3,4,5,6,7,8,9,10]
    validcolumn = ['A','B','C','D','E','F','G','H','I','J']
    os.system('clear')
    if playernumber == 1:
        attackboard = p1attack
        shipboard = p2ship
        print('\x1b[6;30;42m' + 'Player ' + str(playernumber) + '\x1b[0m')
        print('\x1b[1;31;40m' + "Attackboard" + '\x1b[0m')
        print_board(attackboard)
        print('\x1b[1;34;40m' + "Shipboard" + '\x1b[0m')
        print_board(p1ship)
    else:
        attackboard = p2attack
        shipboard = p1ship
        print('\x1b[6;30;43m' + 'Player ' + str(playernumber) + '\x1b[0m')
        print('\x1b[1;31;40m' + "Attackboard" + '\x1b[0m')
        print_board(attackboard)
        print('\x1b[1;34;40m' + "Shipboard" + '\x1b[0m')
        print_board(p2ship)
    
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
            if  attackcord[0] in validcolumn and int(attackcord[1]) in validrow:
                print("")
            else:
                print ('Enter a valid coordinate!')
                continue
        elif len(attackcord) == 3:
            if  attackcord[0] in validcolumn and int(attackcord[1]+attackcord[2]) in validrow:
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
            y = int(attackcord[1]+attackcord[2])

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
        print_board(attackboard)
        print('\x1b[1;34;40m' + "Shipboard" + '\x1b[0m')
        print_board(p1ship)
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
        print_board(attackboard)
        print('\x1b[1;34;40m' + "Shipboard" + '\x1b[0m')
        print_board(p1ship)
        time.sleep(1)


def player2won():
    print()
    print()
    print()
    print("                                      ██╗    ██╗██╗███╗   ██╗███╗   ██╗███████╗██████╗ ")
    print("                                      ██║    ██║██║████╗  ██║████╗  ██║██╔════╝██╔══██╗")
    print("                                      ██║ █╗ ██║██║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝")
    print("                                      ██║███╗██║██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗")
    print("                                      ╚███╔███╔╝██║██║ ╚████║██║ ╚████║███████╗██║  ██║")
    print("                                       ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝")
    print("                                                                                       ")
    print("  ██████╗ ██╗      █████╗ ██╗   ██╗███████╗██████╗     ██████╗                         ")
    print("  ██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗    ╚════██╗                        ")
    print("  ██████╔╝██║     ███████║ ╚████╔╝ █████╗  ██████╔╝     █████╔╝                        ")
    print("  ██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗    ██╔═══╝                         ")
    print("  ██║     ███████╗██║  ██║   ██║   ███████╗██║  ██║    ███████╗                        ")
    print("  ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝    ╚══════╝                        ")
    print("                                                                                       ")

def player1won():
    print()
    print()
    print()
    print("                                      ██╗    ██╗██╗███╗   ██╗███╗   ██╗███████╗██████╗ ")
    print("                                      ██║    ██║██║████╗  ██║████╗  ██║██╔════╝██╔══██╗")
    print("                                      ██║ █╗ ██║██║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝")
    print("                                      ██║███╗██║██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗")
    print("                                      ╚███╔███╔╝██║██║ ╚████║██║ ╚████║███████╗██║  ██║")
    print("                                       ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝")
    print("                                                                                       ")
    print("  ██████╗ ██╗      █████╗ ██╗   ██╗███████╗██████╗      ██╗                            ")
    print("  ██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗    ███║                            ")
    print("  ██████╔╝██║     ███████║ ╚████╔╝ █████╗  ██████╔╝    ╚██║                            ")
    print("  ██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗     ██║                            ")
    print("  ██║     ███████╗██║  ██║   ██║   ███████╗██║  ██║     ██║                            ")
    print("  ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝     ╚═╝                            ")
    print("                                                                                       ")
    
def startscreen():
    print()
    print()
    print("  ██████╗  █████╗ ████████╗████████╗██╗     ███████╗███████╗██╗  ██╗██╗██████╗ ")
    print("  ██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║     ██╔════╝██╔════╝██║  ██║██║██╔══██╗")
    print("  ██████╔╝███████║   ██║      ██║   ██║     █████╗  ███████╗███████║██║██████╔╝")
    print("  ██╔══██╗██╔══██║   ██║      ██║   ██║     ██╔══╝  ╚════██║██╔══██║██║██╔═══╝ ")
    print("  ██████╔╝██║  ██║   ██║      ██║   ███████╗███████╗███████║██║  ██║██║██║     ")
    print("  ╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝     ")
    print("                                         Created by Peter Olle and Mark Orkenyi")
    print() 
    print('\x1b[1;31;40m' + "Press enter to START!" + '\x1b[0m')                                                                             

def selecthelp():
    print('\x1b[1;32;40m' + "Select your ships!" + '\x1b[0m')
    print("In this game, you have to place",ships,"ships on your board")
    print("You can do this, by first entering H for Horizontal or V for Vertical placement of your ship")
    print("Next, you shall enter a coordinate, where the origin of your ship will be")
    print("The origin point of any ship is the top or the left endpoint")
    print("For example, if you enter A1, your ship will be on the A1, A2 and A3 coordinates")
    print()
    print('\x1b[1;31;40m' + "Press enter to select ships!" + '\x1b[0m')

def nextplayer():
    os.system('clear')
    waittimer = 1
    print('\x1b[1;31;40m' + "Player",playernumber,"'s turn will begin in",waittimer," seconds!" + '\x1b[0m')
    time.sleep(waittimer)

import os
import time
empty_board(p1ship)
empty_board(p2ship)
empty_board(p1attack)
empty_board(p2attack)
ships = 2
shiplength = [2,3,3,2,1]
os.system('clear')
startscreen()
start = input("")
selecthelp()
start = input("")
currentboard = p1ship
shipcord=[]
select_ships(1)
os.system('clear')
print()
print()
print_board(p1ship)
confirm = input("Press enter to continue")
currentboard = p2ship
shipcord=[]
select_ships(2)
os.system('clear')
print()
print()
print_board(p2ship)
confirm = input("Press enter to continue")
os.system('clear')
#END OF SHIP SELECTION
playernumber = 1
while True:
    alivep1 = 0
    alivep2 = 0
    nextplayer()
    attack(playernumber)
    if playernumber == 1:
        playernumber = 2
    else:        
        playernumber = 1
    for i in range(10):
            if "O" in p1ship[i]:
                alivep1 += 1
    for i in range(10):
            if "O" in p2ship[i]:
                alivep2 += 1
    if alivep1<1:
        break
    if alivep2<1:
        break
if alivep1 == 0:
    os.system('clear')
    player2won()
elif alivep2 == 0:
    os.system('clear')
    player1won()
time.sleep(5)