import importlib
from abc import ABC, abstractmethod


# An abstract class that implements and declares common functionality to all continuation rules
class ContinuationRule(ABC):

    # need to return 2 lists/arrays:
    # 1 - The genes that moves directly to the next generation
    # 2 - The genes that can be parents
    @abstractmethod
    def getNextGenAndPotentialParents(self, citizens, eliteRate):
        raise NotImplementedError

    @staticmethod
    def factory(continuationRuleName):
        module = importlib.import_module('entities.continuationrule.' + continuationRuleName)
        continuationRule = getattr(module, continuationRuleName)
        return continuationRule()
