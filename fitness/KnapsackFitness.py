from fitness.FitnessFunction import FitnessFunction


class KnapsackFitness(FitnessFunction):

    def calculate(self, problem, vector):
        gain = problem.calculateGain(vector)

        # if exceeded c, give max fitness
        if problem.getWeight(vector) > problem.getC():
            return problem.getOptimalCost()

        # return delta to optimal
        return problem.getOptimalCost() - gain
