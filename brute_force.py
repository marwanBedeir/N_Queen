def checkSafety(board, row, col, N):
    # check same column
    for i in range(row, -1, -1):
        if board[i][col] == 1:
            return False

    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def trySolve(board, row, col, N):
    # Base Case
    if row == N:
        row = 0
        col += 1
    if col == N:
        return True

    for j in range(col, N):
        for i in range(row, N):
            if checkSafety(board, i, j, N):
                board[i][j] = 1
                if trySolve(board, i + 1, j, N):
                    return True
                board[i][j] = 0
        flag = 0
        for n in range(N):  # check all column if it already have a queen placed
            if board[n][j] == 1:
                flag = 1
                row = 0
                break

        if flag == 0:  # if the column has no placed queen back track
            return False
    return True


def brute_force(N):
    board = [0] * N
    for i in range(N):
        board[i] = [0] * N

    trySolve(board, 0, 0, N)
    return board