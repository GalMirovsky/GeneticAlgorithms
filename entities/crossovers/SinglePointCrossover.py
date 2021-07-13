import random

import numpy as np

from entities.crossovers.Crossover import Crossover
from entities.GeneticEntity import GeneticEntity


class SinglePointCrossover(Crossover):

    def makeNewChild(self, parent1, parent2):
        matingIndex = random.randrange(len(parent1.getVec()))
        childVec = np.concatenate((parent1.getVec()[:matingIndex], parent2.getVec()[matingIndex:]))

        return GeneticEntity(childVec)
