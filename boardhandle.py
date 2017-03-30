

# Function to creat empty field
def empty_board(matrix):
    '''Creates empty gameboards'''
    for i in range(11):
        matrix.append([])
        for j in range(11):
            matrix[i].append(' ')
    # set initial values for the column and row indexes
    matrix[0] = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for i in range(1, len(matrix)):
        matrix[i][0] = i

# print out given board


def print_board(matrix):
    '''Prints out given board'''
    for i in range(len(matrix)):
        if i == 0:
            for j in range(len(matrix[i])):
                if j == 0:
                    print ('\x1b[31m{:2}\x1b[0m '.format(matrix[i][j]), end='')
                else:
                    print ('\x1b[4m{}\x1b[0m '.format(matrix[i][j]), end='')
            print()
        else:
            print ('\x1b[0m{:2}\x1b[0m|'.format(matrix[i][0]), end='')
            for j in range(1, len(matrix[i])):
                print ('\x1b[4;1m{}\x1b[0m|'.format(matrix[i][j]), end='')
            print()
    print()


p1ship = []
p2ship = []
p1attack = []
p2attack = []

empty_board(p1ship)
empty_board(p2ship)
empty_board(p1attack)
empty_board(p2attack)
