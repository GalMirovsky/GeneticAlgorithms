import random

import numpy as np

from entities.mutations.Mutation import Mutation
from util.Consts import ALLOWED_CHARS


class FlipMutation(Mutation):
    def mutate(self, vec):
        # choose a random index and flip it
        indexToMutate = random.randrange(len(vec))
        mutation = ord(random.choice(ALLOWED_CHARS))
        vec = np.concatenate((vec[:indexToMutate], [mutation], vec[indexToMutate + 1:]))

        return vec
