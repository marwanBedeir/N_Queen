import random
import time

#make arandom board to be solve
#.................................................................
def create_board_randomly(n):
    board = []
    for _ in range(n):
        board.append(random.randint(0, n - 1))
    return board
#..................................................................

#hill_climping algorithm
#..................................................................
def my_hill_climpin_algorithm_Implementation(n):
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
    if (currentBestThreats == 0):
        for c, r in enumerate(currentBestSolution):
              my_final_board[c][r]=1

    return my_final_board
#..................................................................

#here i want to know posible each state in board
#..................................................................
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
#..................................................................

# my heuristic 2 functions
#...................................................................
def numOfThreatenedQueens(board):
    threatenedQueens = 0
    for column, row in enumerate(board):
        if isQueenThreatened(board, column, row):
            threatenedQueens = threatenedQueens + 1

    return threatenedQueens
#...................................................................

#...................................................................
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
#...................................................................

# Start of Backtracking algorithm
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
    board = []
    for i in range(n):
        board.append([0] * n)

    solve(board, 0, n)
    return board
# End of Backtracking algorithm

# Start of Genetic algorithm
def genetic(N):
    for i in range(15):             # sometimes we can't reach the correct result from the first time
        print(i)
        board, flag = tryGenetic(N) # So we will try again and again and again
        if flag:
            break
    return board

def tryGenetic(N):
    populationSize = 160
    numberOfGeneration = int((N * N)/2)

    board = []          # create an empty board
    for i in range(N):
        board.append([0] * N)

    population = initialParentRandomly(N, populationSize)   # initialize first population

    fitnessPopulation = []
    for i in range(populationSize):     # calculate fitness function for each parent
        fitnessPopulation.append((fitness(population[i]), population[i]))
    fitnessPopulation.sort(reverse=True)    # sort parents according to fitness values

    for generation in range(numberOfGeneration):
        fitnessValue, chromosome = fitnessPopulation[0]  # look for the best parent
        if fitnessValue == N:   # find a correct result
            c = 0
            for r in chromosome:    # put queens in there places on board
                board[r][c] = 1
                c = c + 1
            return board, True    # return correct board

        for i in range(int(populationSize/10)):  # remove bad parents (KILL THEM ALL HA HA HA HA)
            fitnessPopulation.pop(-1)

        for x in range(int((populationSize/10)/2)):
            i = random.randint(0, int((populationSize/10)-1))
            ii = random.randint(0, int((populationSize/10)-1))
            _, parent1 = fitnessPopulation[i]
            _, parent2 = fitnessPopulation[ii]
            child1, child2 = crossOver(parent1, parent2)
            child1 = mutate(child1)
            child2 = mutate(child2)
            fitnessPopulation.append((fitness(child1), child1))
            fitnessPopulation.append((fitness(child2), child2))
        fitnessPopulation.sort(reverse=True)    # sort parents according to fitness values
    return board, False    # can't find correct result

def initialParentRandomly(N, populationSize):
    parents = []
    for i in range(populationSize):
        chromosome = []
        for ii in range(N):
            chromosome.append(random.randint(0, N-1))
        parents.append(chromosome)
    return parents

def fitness(chromosome):
    N = len(chromosome)
    fitnessValue = N

    D1 = []
    for i in range(N):
        D1.append([0] * N)

    D2 = []
    for i in range(N):
        D2.append([0] * N)

    c = 0
    for r in chromosome:
        D1[r - min(r, c)][c - min(r, c)] = D1[r - min(r, c)][c - min(r, c)] + 1
        D2[r - min(r, N - 1 - c)][c + min(r, N - 1 - c)] = D2[r - min(r, N - 1 - c)][c + min(r, N - 1 - c)] + 1
        c = c + 1

    c = 0
    for r in chromosome:
        if chromosome.count(r) > 1:
            fitnessValue = fitnessValue - 1
        elif D1[r - min(r, c)][c - min(r, c)] > 1 or D2[r - min(r, N - 1 - c)][c + min(r, N - 1 - c)] > 1:
            fitnessValue = fitnessValue - 1
        c = c + 1

    return fitnessValue

def crossOver(parent1, parent2):
    N = len(parent1)
    if N % 2 != 0:
        N = N + 1
    child1 = parent1[0:int(N/2)] + parent2[int(N/2):]
    child2 = parent2[0:int(N/2)] + parent1[int(N/2):]
    return child1, child2

def mutate(chromosome):
    N = len(chromosome)
    flag = 0
    for i in range(N):
        if i not in chromosome:
            iii = 0
            for ii in chromosome:
                if chromosome.count(ii) > 1:
                    chromosome[iii] = i
                    flag = 1
                if flag == 1:
                    break
                iii = iii + 1
        if flag == 1:
                break
    if flag == 1:
        return chromosome
    else:
        x = random.randint(0, N-1)
        y = random.randint(0, N-1)
        swapStore = chromosome[x]
        chromosome[x] = chromosome[y]
        chromosome[y] = swapStore
    return chromosome
# End of Genetic algorithm


def main():
    N = int(input("Enter number of queens : "))
    a = time.time()
    board = genetic(N)
    b = time.time()
    print(b-a)
    #board = backtracking(N)
    #board = my_hill_climpin_algorithm_Implementation(N)
    print(board)
    #input("Enter any key to close : ")

if __name__ == '__main__':
    main()