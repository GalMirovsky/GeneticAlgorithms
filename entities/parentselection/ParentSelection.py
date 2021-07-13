import importlib
from abc import ABC, abstractmethod


# An abstract class that implements and declares common functionality to all parent selection methods
class ParentSelection(ABC):

    @abstractmethod
    def getCandidates(self, citizens):
        raise NotImplementedError

    @staticmethod
    def factory(parentSelectionName):
        module = importlib.import_module('entities.parentselection.' + parentSelectionName)
        parentSelection = getattr(module, parentSelectionName)
        return parentSelection()
