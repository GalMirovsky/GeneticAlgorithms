from fitness.FitnessFunction import FitnessFunction


# for N queens
class DiagonalConflicts(FitnessFunction):

    def calculate(self, problem, vector):

        fitness = 0
        for i in range(problem.getTargetSize() - 1):
            for j in range(i + 1, len(vector)):
                rowDelta = abs(i - j)
                colDelta = abs(vector[i] - vector[j])
                if rowDelta == colDelta:
                    fitness += 1

            # second part for pso
            if vector[i] < 0:
                fitness += -vector[i]
            if vector[i] >= len(vector):
                fitness += vector[i] - len(vector) + 1
            if vector[i] in vector[i + 1:]:
                fitness += 2

        return fitness
