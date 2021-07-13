import os

import numpy as np

from problems.Problem import Problem


class Knapsack(Problem):

    def __init__(self, fitnessFunction, target):
        super().__init__(fitnessFunction, target)

        # set path params
        dirPath = os.getcwd() + '\\util\\knapsackfiles\\' + str(target) + '\\'
        filePrefix = 'p0' + str(target) + '_'
        fileSuffix = '.txt'

        # get c
        cFile = open(dirPath + filePrefix + 'c' + fileSuffix, 'r')
        self._c = int(cFile.readline())

        # get p (gain) vector
        pFile = open(dirPath + filePrefix + 'p' + fileSuffix, 'r')
        gainVec = []
        for line in pFile:
            gainVec.append(int(line))
        self._gainVec = np.array(gainVec)

        # get w (weights) vector
        wFile = open(dirPath + filePrefix + 'w' + fileSuffix, 'r')
        weightsVec = []
        for line in wFile:
            weightsVec.append(int(line))
        self._weightsVec = np.array(weightsVec)

        # get optimal solution
        sFile = open(dirPath + filePrefix + 's' + fileSuffix, 'r')
        optimalSolution = []
        for line in sFile:
            optimalSolution.append(int(line))
        self._target = np.array(optimalSolution)
        self._targetSize = len(self._target)

        optimalCost = 0
        for i in range(self._targetSize):
            if self._target[i] == 1:
                optimalCost += self._gainVec[i]
        self._optimalCost = optimalCost

    def getTargetSize(self):
        return self._targetSize

    def translateVec(self, vec):
        gain = self.calculateGain(vec)
        return gain

    def generateRandomVec(self):
        return np.random.choice([0, 1], size=self._targetSize)

    def calculateGain(self, vec):
        gain = 0
        for i in range(self._targetSize):
            if vec[i] == 1:
                gain += self._gainVec[i]
        return gain

    def getC(self):
        return self._c

    def getOptimalCost(self):
        return self._optimalCost

    def getWeight(self, vec):
        weight = 0
        for i in range(self._targetSize):
            if vec[i] == 1:
                weight += self._weightsVec[i]

        return weight
