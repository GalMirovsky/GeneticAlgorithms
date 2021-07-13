import random

import numpy as np

from entities.GeneticEntity import GeneticEntity
from entities.crossovers.Crossover import Crossover


class OrderedCrossover(Crossover):

    def makeNewChild(self, parent1, parent2):

        vecSize = len(parent1.getVec())
        newChildVec = []

        parent2List = parent2.getVec().tolist()

        for i in range(vecSize):
            if random.random() < 0.5:
                newChildVec.append(parent1.getVec()[i])
                if parent1.getVec()[i] in parent2List:
                    parent2List.remove(parent1.getVec()[i])
            else:
                newChildVec.append(parent2List[0])
                parent2List.pop(0)

        return GeneticEntity(np.array(newChildVec))
