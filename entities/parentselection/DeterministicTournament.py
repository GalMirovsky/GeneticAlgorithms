import random
from math import sqrt

import numpy as np

from entities.parentselection.ParentSelection import ParentSelection


class DeterministicTournament(ParentSelection):

    def getCandidates(self, citizens):

        candidates = []
        citizensSize = len(citizens)

        for j in range(citizensSize):

            # get a random k (within allowed range)
            k = random.randrange(1, int(sqrt(citizensSize)))
            tournamentParticipants = []

            for i in range(k):
                tournamentParticipants.append((citizens[random.randrange(len(citizens))]))

            # get best gene
            winner = min(tournamentParticipants)
            candidates.append(winner)

        return np.array(candidates)
