import math
import random
import numpy as np
from entities.parentselection.ParentSelection import ParentSelection


class RWS(ParentSelection):

    def getCandidates(self, citizens):

        candidates = []
        fitnessSum = 0

        # calculate sum of fitness of all genes.
        for i in range(len(citizens)):
            fitnessSum += math.sqrt(citizens[i].getFitness())  # scaling with sqrt

        # calculate a proportional fitness for each gene.
        fitnessRate = []
        for i in range(len(citizens)):
            fitnessRate.append(math.sqrt(citizens[i].getFitness()) / fitnessSum)  # scaling with sqrt

        # at index i we sum up the fitnesses until index i.
        # flip the list - the lower the fitness, the better the solution.
        cumFitnessRate = list(np.cumsum(np.flip(fitnessRate)))

        # N(pop size) spins
        for j in range(len(cumFitnessRate)):
            r = random.random()

            i = 0
            found = False

            # find the index that matching to r and append it to candidates list.
            while i < len(cumFitnessRate) and not found:
                if r < cumFitnessRate[i]:
                    candidates.append(citizens[i])
                    found = True
                i += 1

        return np.array(candidates)
