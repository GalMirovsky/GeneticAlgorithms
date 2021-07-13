import importlib
from abc import abstractmethod


# An abstract class that implements and declares common functionality to all fitness functions
class FitnessFunction:

    @abstractmethod
    def calculate(self, problem, vector):
        raise NotImplementedError

    @staticmethod
    def factory(fitnessName):
        module = importlib.import_module('fitness.' + fitnessName)
        fitness = getattr(module, fitnessName)
        return fitness()
