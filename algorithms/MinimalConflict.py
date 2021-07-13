import itertools
import random

import numpy as np

from algorithms.Algorithm import Algorithm


class MinimalConflict(Algorithm):

    def __init__(self, problem, popSize):
        super().__init__(problem, popSize)

        size = self._problem.getTargetSize()
        queensPositions = []

        # get all pairs in range
        availPos = [[i, j] for i, j in itertools.product(range(size), range(size))]

        # init the queens position
        for i in range(size):
            pos = random.choice(availPos)
            queensPositions.append(pos)
            availPos.remove(pos)

        self._queensPositions = queensPositions

    def findSolution(self, maxIter):

        size = self._problem.getTargetSize()

        # iterative improvement
        iterCounter = 0
        while not self._solutionFound() and iterCounter < maxIter:

            # want to minimize this variable
            minAttacks = size + 1

            # get a random queen
            pickedQueenIndex = random.randrange(size)

            # get all possible positions the queen can move into
            availPositions = [[i, j] for i, j in itertools.product(range(size), range(size)) if
                              [i, j] not in self._queensPositions]
            minConflictPosition = (-1, -1)

            # get the minimal conflict position
            for pos in availPositions:

                # move queen to pos
                priorPosition = self._queensPositions[pickedQueenIndex]
                self._queensPositions[pickedQueenIndex] = pos

                # calculate the conflict in this position and save the pos if it's the current minimum
                newNumberOfConflicts = self._specificQueenConflicts(pos)
                if newNumberOfConflicts < minAttacks:
                    minConflictPosition = pos
                    minAttacks = newNumberOfConflicts

                # return the queen to prev place
                self._queensPositions[pickedQueenIndex] = priorPosition

            # move the queen to the minimal conflict position
            self._queensPositions[pickedQueenIndex] = minConflictPosition
            iterCounter += 1

        # convert the solution to a vector
        solution = np.zeros(size, dtype=int)
        for pos in self._queensPositions:
            solution[pos[0]] = pos[1]

        print(f'num of iter = {iterCounter}')
        return solution

    def _solutionFound(self):

        tempQueensPos = np.array(self._queensPositions)

        # check rows conflicts
        rows = tempQueensPos[:, 0]
        cols = tempQueensPos[:, 1]

        # if unique rows are less then the rows we have it means we have at least 2 queens on the same row
        # (same for col)
        if len(rows) != len(set(rows)) or len(cols) != len(set(cols)):
            return False

        size = self._problem.getTargetSize()

        # check diagonal conflicts
        i = 0
        while i < size:
            j = i + 1
            while j < size:
                if abs(rows[i] - rows[j]) == abs(cols[i] - cols[j]):
                    return False
                j += 1
            i += 1

        return True

    def _specificQueenConflicts(self, pos):

        conflicts = 0

        tempQueensPos = np.copy(self._queensPositions)
        rows = tempQueensPos[:, 0]
        cols = tempQueensPos[:, 1]

        # row conflicts
        num, count = np.unique(rows, return_counts=True)
        for i in range(len(num)):
            if num[i] == pos[0]:
                conflicts += count[i] - 1

        # col conflicts
        num, count = np.unique(cols, return_counts=True)
        for i in range(len(num)):
            if num[i] == pos[1]:
                conflicts += count[i] - 1

        # dia conflicts
        for queenPos in tempQueensPos:
            if (queenPos[0] != pos[0] or queenPos[1] != pos[1]) and abs(queenPos[0] - pos[0]) == abs(
                    queenPos[1] - pos[1]):
                conflicts += 1

        return conflicts
