import importlib
from abc import ABC, abstractmethod


# An abstract class that implements and declares common functionality to all problems
class Problem(ABC):

    def __init__(self, fitnessFunction, target):
        self._target = target
        self._fitnessFunction = fitnessFunction

    @abstractmethod
    def getTargetSize(self):
        raise NotImplementedError

    @abstractmethod
    def translateVec(self, vec):
        raise NotImplementedError

    @abstractmethod
    def generateRandomVec(self):
        raise NotImplementedError

    def calculateFitness(self, newVec):
        return self._fitnessFunction(self, newVec)

    @staticmethod
    def factory(problemName, fitnessFunction, target):
        module = importlib.import_module('problems.' + problemName)
        problem = getattr(module, problemName)

        if problemName == 'StringMatching':
            return problem(fitnessFunction, target)

        if problemName == 'NQueens':
            return problem(fitnessFunction, target)

        if problemName == 'Knapsack':
            return problem(fitnessFunction, target)
