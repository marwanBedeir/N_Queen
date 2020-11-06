def check(board, row, column, n):
    for i in range(n):
        if board[row][i] == 1:
            return False

    for i in range(n):
        if board[i][column] == 1:
            return False

    r = row
    c = column
    while r < n and c < n:
        if board[r][c] == 1:
            return False
        r = r + 1
        c = c + 1

    r = row
    c = column
    while r >= 0 and c >= 0:
        if board[r][c] == 1:
            return False
        r = r - 1
        c = c - 1

    r = row
    c = column
    while r >= 0 and c < n:
        if board[r][c] == 1:
            return False
        r = r - 1
        c = c + 1

    r = row
    c = column
    while r < n and c >= 0:
        if board[r][c] == 1:
            return False
        r = r + 1
        c = c - 1

    return True


def solve(board, column, n):
    if column >= n:
        return True

    for i in range(n):
        if check(board, i, column, n):
            board[i][column] = 1
            if solve(board, column + 1, n):
                return True
            board[i][column] = 0
    return False


def backtracking(n):
    board = [0] * n
    for i in range(n):
        board[i] = [0] * n

    solve(board, 0, n)
    return board

# End of Backtracking algorithm
