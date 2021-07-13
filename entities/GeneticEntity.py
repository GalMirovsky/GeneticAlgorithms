import random

from entities.IndividualEntity import IndividualEntity
from util.Consts import AGE_DIE


class GeneticEntity(IndividualEntity):

    def __init__(self, stringVal):
        super().__init__(stringVal)

        self._age = random.randrange(AGE_DIE)

    def increaseAge(self):
        self._age += 1

    def getAge(self):
        return self._age
