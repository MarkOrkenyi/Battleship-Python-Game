import os
import time
import prints
import settings
import attack
import boardhandle
import shipboard_setup
from copy import deepcopy
import sound
p1shipcord = []
p2shipcord = []
ships = 5


def main():
    # start screens and game informations
    os.system('clear')
    prints.startscreen()
    start = input("")
    prints.selecthelp(ships)
    start = input("")
    AI = prints.ai_or_player()
    sound.play_sound("start")
    # ship selection beginning
    currentboard = boardhandle.p1ship
    p1shipcord = deepcopy(shipboard_setup.select_ships(1, ships, currentboard, AI))
    os.system('clear')
    print()
    print()
    boardhandle.print_board(boardhandle.p1ship)
    confirm = input("Press enter to continue")
    currentboard = boardhandle.p2ship
    p2shipcord = deepcopy(shipboard_setup.select_ships(2, ships, currentboard, AI))
    os.system('clear')
    print()
    print()
    if AI == 1:
        pass
    else:
        boardhandle.print_board(boardhandle.p2ship)
        confirm = input("Press enter to continue")
        os.system('clear')
    # attack phase beginning
    playernumber = 1
    while True:
        alivep1 = 0
        alivep2 = 0
        attack.nextplayer(playernumber, AI)
        attack.attack(playernumber, currentboard, AI, p1shipcord, p2shipcord)
        if playernumber == 1:
            playernumber = 2
        else:
            playernumber = 1
        for i in range(1, 11):
            if "O" in boardhandle.p1ship[i]:
                alivep1 += 1
        for i in range(1, 11):
            if "O" in boardhandle.p2ship[i]:
                alivep2 += 1
        if alivep1 < 1:
            break
        if alivep2 < 1:
            break
    if alivep1 == 0:
        os.system('clear')
        prints.player2won()
        sound.play_sound("clap")
    elif alivep2 == 0:
        os.system('clear')
        prints.player1won()
        sound.play_sound("clap")
    time.sleep(5)


if __name__ == '__main__':
    main()
