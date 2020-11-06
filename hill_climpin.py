import random

# Heuristic Algorithm

# make a random board to be solve
# .................................................................
def create_board_randomly(n):
    board = []
    for _ in range(n):
        board.append(random.randint(0, n - 1))
    return board


# ..................................................................

# hill_climping algorithm
# ..................................................................
def hill_climpin(n):
    currentBestSolution = []
    currentBestThreats = n

    for _ in range(500):

        my_current_Board = create_board_randomly(n)

        while True:

            moved = False

            neighbours = generate_state_of_all_neighbours(my_current_Board)
            for neighbour in neighbours:

                if numOfThreatenedQueens(neighbour) < numOfThreatenedQueens(my_current_Board):
                    my_current_Board = neighbour
                    moved = True

            if numOfThreatenedQueens(my_current_Board) == 0:
                break

            if moved != True:
                break

        if numOfThreatenedQueens(my_current_Board) < currentBestThreats:
            currentBestThreats = numOfThreatenedQueens(my_current_Board)
            currentBestSolution = list(my_current_Board)

            if currentBestThreats == 0:
                break

    my_final_board = [0] * n
    for i in range(n):
        my_final_board[i] = [0] * n
    if currentBestThreats == 0:
        for c, r in enumerate(currentBestSolution):
            my_final_board[c][r] = 1

    return my_final_board


# ..................................................................

# here i want to know posible each state in board
# ..................................................................
def generate_state_of_all_neighbours(board):
    neighbours = []
    for c, r in enumerate(board):
        neighbour = list(board)

        for x in range(0, len(board)):
            if x != r:
                neighbour[c] = x
                neighbours.append(neighbour)
                neighbour = list(board)

    return neighbours


# ..................................................................

# my heuristic 2 functions
# ...................................................................
def numOfThreatenedQueens(board):
    threatenedQueens = 0
    for column, row in enumerate(board):
        if isQueenThreatened(board, column, row):
            threatenedQueens = threatenedQueens + 1

    return threatenedQueens


# ...................................................................

# ...................................................................
def isQueenThreatened(board, queenColumn, queenRow):
    queenOnRow = 0
    queenOnLeftDiag = 0
    queenOnRightDiag = 0

    for column, row in enumerate(board):

        if row == queenRow:
            queenOnRow = queenOnRow + 1

        if queenOnRow > 1:
            return True

        if (column - queenColumn) == (row - queenRow):
            queenOnLeftDiag = queenOnLeftDiag + 1

        if queenOnLeftDiag > 1:
            return True

        if (queenColumn - column) == -(queenRow - row):
            queenOnRightDiag = queenOnRightDiag + 1

        if queenOnRightDiag > 1:
            return True
    return False


# ...................................................................