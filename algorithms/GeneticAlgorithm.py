import random
import time

import numpy as np

from algorithms.Algorithm import Algorithm
from entities.GeneticEntity import GeneticEntity

from util.Consts import BEST, CLOCK_RATE


# implements the genetic algorithm
class GeneticAlgorithm(Algorithm):

    def __init__(self, problem, popSize, eliteRate, crossoverFunc, mutationRate,
                 mutationFunction, parentSelectionFunction, continuationRuleFunction):
        super().__init__(problem, popSize)

        self._citizens = np.array(
            [GeneticEntity(problem.generateRandomVec()) for _ in
             range(popSize)])

        self._mean = None
        self._standardDeviation = None
        self._eliteRate = eliteRate
        self._crossoverFunc = crossoverFunc
        self._mutationFunction = mutationFunction
        self._mutationRate = mutationRate
        self._parentSelectionFunction = parentSelectionFunction
        self._continuationRuleFunction = continuationRuleFunction
        self._problem = problem

    def findSolution(self, maxIter):

        # measure time
        totalRunTime = time.time()

        # init the fitness of the citizens
        self.updateFitness()
        best = self._citizens[BEST]

        # iterative improvement
        iterCounter = 0
        while best.getFitness() != 0 and iterCounter < maxIter:
            startTime = time.time()

            self._mate()

            self.updateFitness()
            best = self._citizens[BEST]
            iterCounter += 1

            elapsedTime = time.time() - startTime
            print(f'Best: {self._problem.translateVec(best.getVec())} ({best.getFitness()}). Mean: {self._mean:.2f},'
                  f' STD: {self._standardDeviation:.2f}. Time in secs: {elapsedTime}. '
                  f'CPU clicks: {elapsedTime * CLOCK_RATE}')

        totalElapsedTime = time.time() - totalRunTime
        print(f'Total: Iterations: {iterCounter}. Elapsed Time in secs: {totalElapsedTime}.'
              f' CPU clicks: {totalElapsedTime * CLOCK_RATE}\n')

        return best.getVec()

    def _mate(self):

        # get who continue directly and who's allowed to be a parent
        tempPopulation, secList = self._continuationRuleFunction(self._citizens, self._eliteRate)

        # get the candidates to be parents based on the function that was passed
        candidates = self._parentSelectionFunction(secList)
        candidatesSize = len(candidates)

        # fill in the rest of the population
        while len(tempPopulation) < self._popSize:

            # choose parents and make child
            parent1 = candidates[random.randrange(candidatesSize)]
            parent2 = candidates[random.randrange(candidatesSize)]
            newChild = self._crossoverFunc(parent1, parent2)

            # mutation factor
            if random.random() < self._mutationRate:
                newChild.setVec(self._mutationFunction(newChild.getVec()))

            tempPopulation.append(newChild)

        self._citizens = np.array(tempPopulation)

    def updateFitness(self):
        fitnessValues = []
        for citizen in self._citizens:
            fitnessVal = self._problem.calculateFitness(citizen.getVec())
            citizen.setFitness(fitnessVal)
            fitnessValues.append(fitnessVal)

        # calculate mean and std of fitness function across all genes
        self._citizens.sort()
        self._mean = np.mean(fitnessValues)
        self._standardDeviation = np.std(fitnessValues)
