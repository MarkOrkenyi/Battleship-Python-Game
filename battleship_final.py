'''
#define listsss
p1ship = []
p2ship= []
p1attack = []
p2attack = []

shipcord0 = []
shipcord = []
pshipcord = []

import os
import time
empty_board(p1ship)
empty_board(p2ship)
empty_board(p1attack)
empty_board(p2attack)
ships = 2
shiplength = [2,3,3,2,1]

import prints, attack, shipboard_setup, boardhandle
#import settings
'''
import prints


def main():
    os.system('clear')
    prints.startscreen()
    start = input("")
    prints.selecthelp()
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

    if __name__ == "__main__":
        main()