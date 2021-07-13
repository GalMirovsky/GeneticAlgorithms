import numpy as np

from entities.crossovers.Crossover import Crossover
from entities.GeneticEntity import GeneticEntity
from util.Util import getValidIndexes


class TwoPointCrossover(Crossover):

    def makeNewChild(self, parent1, parent2):
        matingIndex1, matingIndex2 = getValidIndexes(len(parent1.getVec()))
        childVec = np.concatenate(
            (parent1.getVec()[:matingIndex1], parent2.getVec()[matingIndex1:matingIndex2],
             parent1.getVec()[matingIndex2:]))
        return GeneticEntity(childVec)
