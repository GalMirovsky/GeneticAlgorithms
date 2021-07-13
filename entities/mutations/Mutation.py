import importlib
from abc import ABC, abstractmethod


# An abstract class that implements and declares common functionality to all mutation functions
class Mutation(ABC):

    @abstractmethod
    def mutate(self, vec):
        raise NotImplementedError

    @staticmethod
    def factory(mutationName):
        module = importlib.import_module('entities.mutations.' + mutationName)
        cross = getattr(module, mutationName)
        return cross()
