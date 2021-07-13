from fitness.FitnessFunction import FitnessFunction


class AsciiDistance(FitnessFunction):

    def calculate(self, problem, vector):
        fitness = 0
        targetVec = problem.getTargetVec()

        # sum all distances
        for newVal, targetElement in zip(vector, targetVec):
            fitness += abs(newVal - targetElement)

        return fitness
