import random


def genetic(N):
    for i in range(15):  # sometimes we can't reach the correct result from the first time
        board, flag = tryGenetic(N)  # So we will try again and again and again
        if flag:
            break
    return board


def tryGenetic(N):
    populationSize = 160
    numberOfGeneration = int((N * N) / 2)

    board = []  # create an empty board
    for i in range(N):
        board.append([0] * N)

    population = initialParentRandomly(N, populationSize)  # initialize first population

    fitnessPopulation = []
    for i in range(populationSize):  # calculate fitness function for each parent
        fitnessPopulation.append((fitness(population[i]), population[i]))
    fitnessPopulation.sort(reverse=True)  # sort parents according to fitness values

    for generation in range(numberOfGeneration):
        fitnessValue, chromosome = fitnessPopulation[0]  # look for the best parent
        if fitnessValue == N:  # find a correct result
            c = 0
            for r in chromosome:  # put queens in there places on board
                board[r][c] = 1
                c = c + 1
            return board, True  # return correct board

        for i in range(int(populationSize / 10)):  # remove bad parents (KILL THEM ALL HA HA HA HA)
            fitnessPopulation.pop(-1)

        for x in range(int((populationSize / 10) / 2)):
            i = random.randint(0, int((populationSize / 10) - 1))
            ii = random.randint(0, int((populationSize / 10) - 1))
            _, parent1 = fitnessPopulation[i]
            _, parent2 = fitnessPopulation[ii]
            child1, child2 = crossOver(parent1, parent2)
            child1 = mutate(child1)
            child2 = mutate(child2)
            fitnessPopulation.append((fitness(child1), child1))
            fitnessPopulation.append((fitness(child2), child2))
        fitnessPopulation.sort(reverse=True)  # sort parents according to fitness values
    return board, False  # can't find correct result


def initialParentRandomly(N, populationSize):
    parents = []
    for i in range(populationSize):
        chromosome = []
        for ii in range(N):
            chromosome.append(random.randint(0, N - 1))
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
    child1 = parent1[0:int(N / 2)] + parent2[int(N / 2):]
    child2 = parent2[0:int(N / 2)] + parent1[int(N / 2):]
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
        x = random.randint(0, N - 1)
        y = random.randint(0, N - 1)
        swapStore = chromosome[x]
        chromosome[x] = chromosome[y]
        chromosome[y] = swapStore
    return chromosome
# End of Genetic algorithm