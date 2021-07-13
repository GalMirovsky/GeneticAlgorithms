import numpy as np

from entities.parentselection.ParentSelection import ParentSelection


class NaiveParentSelection(ParentSelection):

    def getCandidates(self, citizens):
        sizeCitizens = len(citizens)
        candidates = []

        # get half the population
        for i in range(int(sizeCitizens / 2)):
            candidates.append(citizens[i])

        return np.array(candidates)
