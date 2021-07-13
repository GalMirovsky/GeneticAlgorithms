import random

import numpy as np

from entities.crossovers.Crossover import Crossover
from entities.GeneticEntity import GeneticEntity


class UniformCrossover(Crossover):

    def makeNewChild(self, parent1, parent2):
        childVec = np.array([parent1.getVec()[i] if random.random() < 0.5 else parent2.getVec()[i]
                             for i in range(len(parent1.getVec()))])

        return GeneticEntity(childVec)
