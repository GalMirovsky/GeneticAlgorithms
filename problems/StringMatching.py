import random

import numpy as np

from problems.Problem import Problem
from util.Consts import ALLOWED_CHARS


class StringMatching(Problem):

    def getTargetSize(self):
        return len(self._target)

    def __init__(self, fitnessFunction, target):
        super().__init__(fitnessFunction, target)
        self._targetVec = np.array([ord(c) for c in self._target])

    def generateRandomVec(self):
        randomString = ''.join(random.choice(ALLOWED_CHARS) for _ in range(len(self._targetVec)))
        return np.array([ord(c) for c in randomString])

    def translateVec(self, vec):
        return ''.join([chr(c) if 32 <= c <= 120 else '_' for c in vec])

    def getTargetVec(self):
        return np.copy(self._targetVec)
