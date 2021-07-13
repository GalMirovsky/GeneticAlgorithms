import numpy as np

from problems.Problem import Problem


class NQueens(Problem):

    def __init__(self, fitnessFunction, target):
        super().__init__(fitnessFunction, target)
        self._target = int(self._target)

    def getTargetSize(self):
        return self._target

    def translateVec(self, vec):
        return vec

    def generateRandomVec(self):
        return np.random.permutation(self._target)
