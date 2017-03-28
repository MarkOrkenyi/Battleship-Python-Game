import os
import time
import prints
import settings
import attack
import boardhandle
import shipboard_setup

#p1ship = []
#p2ship = []
#p1attack = []
#p2attack = []
#shipcord0 = []


# boardhandle.empty_board(p1ship)
# boardhandle.empty_board(p2ship)
# boardhandle.empty_board(p1attack)
# boardhandle.empty_board(p2attack)

ships = 2


def main():
    os.system('clear')
    prints.startscreen()
    start = input("")
    prints.selecthelp(ships)
    start = input("")
    currentboard = boardhandle.p1ship
    shipboard_setup.select_ships(1, ships, currentboard)
    os.system('clear')
    print()
    print()
    boardhandle.print_board(boardhandle.p1ship)
    confirm = input("Press enter to continue")
    currentboard = boardhandle.p2ship
    shipcord = []
    shipboard_setup.select_ships(2, ships, currentboard)
    os.system('clear')
    print()
    print()
    boardhandle.print_board(boardhandle.p2ship)
    confirm = input("Press enter to continue")
    os.system('clear')
    # END OF SHIP SELECTION
    playernumber = 1
    while True:
        alivep1 = 0
        alivep2 = 0
        attack.nextplayer(playernumber)
        attack.attack(playernumber, currentboard)
        if playernumber == 1:
            playernumber = 2
        else:
            playernumber = 1
        for i in range(10):
            if "O" in boardhandle.p1ship[i]:
                alivep1 += 1
        for i in range(10):
            if "O" in boardhandle.p2ship[i]:
                alivep2 += 1
        if alivep1 < 1:
            break
        if alivep2 < 1:
            break
    if alivep1 == 0:
        os.system('clear')
        prints.player2won()
    elif alivep2 == 0:
        os.system('clear')
        prints.player1won()
    time.sleep(5)


if __name__ == '__main__':
    main()
