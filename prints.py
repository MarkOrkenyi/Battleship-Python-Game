
def player2won():
    '''Displays that player number 2 won the game'''
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
    '''Displays that player number 1 won the game'''
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
    '''prints startscreen'''
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


def selecthelp(ships):
    '''Displays game information'''
    print('\x1b[1;32;40m' + "Select your ships!" + '\x1b[0m')
    print("In this game, you have to place", ships, "ships on your board")
    print("You can do this, by first entering H for Horizontal or V for Vertical placement of your ship")
    print("Next, you shall enter a coordinate, where the origin of your ship will be")
    print("The origin point of any ship is the top or the left endpoint")
    print("For example, if you enter A1, your ship will be on the A1, A2 and A3 coordinates")
    print()
    print('\x1b[1;31;40m' + "Press enter to select ships!" + '\x1b[0m')


def ai_or_player():
    '''Ask if you want to play against AI, or another human'''
    print()
    print("Would like to play against AI or another human player?")
    print()
    validanswer = 0
    while validanswer == 0:
        AI = input('Enter "AI" to play against a computer, or enter "HUMAN" to play against another player: ')
        if AI.lower() == "ai":
            validanswer = 1
            return 1
        elif AI.lower() == "human":
            validanswer = 1
            return 0
        else:
            print("Not a valid option!")
