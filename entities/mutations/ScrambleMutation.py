import random

import numpy as np

from entities.mutations.Mutation import Mutation
from util.Util import getValidIndexes


class ScrambleMutation(Mutation):

    def mutate(self, vec):
        vecSize = len(vec)
        # get two random indexes and shuffle their range
        index1, index2 = getValidIndexes(vecSize)

        elementsToShuffle = vec[index1:index2 + 1]
        random.shuffle(elementsToShuffle)

        return np.concatenate((vec[:index1], elementsToShuffle, vec[index2 + 1:]))
