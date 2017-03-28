
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
    '''
    prints startscreen
    '''
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
    print('\x1b[1;32;40m' + "Select your ships!" + '\x1b[0m')
    print("In this game, you have to place", ships, "ships on your board")
    print("You can do this, by first entering H for Horizontal or V for Vertical placement of your ship")
    print("Next, you shall enter a coordinate, where the origin of your ship will be")
    print("The origin point of any ship is the top or the left endpoint")
    print("For example, if you enter A1, your ship will be on the A1, A2 and A3 coordinates")
    print()
    print('\x1b[1;31;40m' + "Press enter to select ships!" + '\x1b[0m')
