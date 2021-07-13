import random
from math import sqrt
import numpy as np
from entities.parentselection.ParentSelection import ParentSelection


class StochasticTournament(ParentSelection):

    def getCandidates(self, citizens):

        candidates = []
        citizensSize = len(citizens)

        for j in range(citizensSize):

            # get a random k (within allowed range)
            k = random.randrange(1, int(sqrt(citizensSize)))
            tournamentParticipants = []

            for i in range(k):
                tournamentParticipants.append((citizens[random.randrange(len(citizens))]))
            tournamentParticipants.sort()

            # set the weight array based on fitness
            fitnessSum = 0
            for i in range(len(tournamentParticipants)):
                fitnessSum += tournamentParticipants[i].getFitness()

            weights = []
            # normalize the weights
            for i in range(len(tournamentParticipants)):
                weights.append(tournamentParticipants[i].getFitness() / fitnessSum)

            adjustedWeights = np.flip(weights)

            cumFitnessRate = list(np.cumsum(adjustedWeights))

            r = random.random()
            i = 0
            found = False
            while i < len(cumFitnessRate) and not found:
                if r < cumFitnessRate[i]:
                    candidates.append(tournamentParticipants[i])
                    found = True
                i += 1

        return np.array(candidates)
