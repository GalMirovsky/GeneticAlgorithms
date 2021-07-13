from abc import ABC

from entities.continuationrule.ContinuationRule import ContinuationRule


class EliteRule(ContinuationRule, ABC):

    def getNextGenAndPotentialParents(self, citizens, eliteRate):
        elite = []

        eliteSize = int(len(citizens) * eliteRate)

        # get elite genes
        for i in range(eliteSize):
            citizens[i].increaseAge()
            elite.append(citizens[i])

        return elite, citizens
