import random

import numpy as np

from entities.IndividualEntity import IndividualEntity
from util.Consts import LOWER_BOUND, UPPER_BOUND


class PsoParticle(IndividualEntity):

    def __init__(self, vec):
        super().__init__(vec)

        self._pBestVec = np.copy(self._vec)
        self._velocity = np.array(
            [random.randint(-abs(LOWER_BOUND - UPPER_BOUND), abs(LOWER_BOUND - UPPER_BOUND)) for _ in
             vec])

    def getVelocity(self):
        return self._velocity

    def getPBestVec(self):
        return self._pBestVec

    def updatePosition(self, newVelocity):
        # update velocity
        self._velocity = newVelocity

        # updatePosition
        self._vec += newVelocity.astype(int)

    def updateFitness(self, fitness):
        # update pBest if needed
        if fitness < self._fitness:
            self._pBestVec = np.copy(self._vec)

        self.setFitness(fitness)
