import time

import argparse
import traceback

from algorithms.Algorithm import Algorithm
from entities.continuationrule.ContinuationRule import ContinuationRule
from entities.crossovers.Crossover import Crossover
from entities.mutations.Mutation import Mutation
from entities.parentselection.ParentSelection import ParentSelection
from fitness.FitnessFunction import FitnessFunction
from problems.Problem import Problem
from util.Consts import *


# returns default and allowed dicts
def getParamsDict(problemName):
    if problemName == 'StringMatching':
        return STRING_MATCHING_DEF_PRAMS, STRING_MATCHING_ALLOWED_PARAMS

    if problemName == 'NQueens':
        return N_QUEENS_DEF_PRAMS, N_QUEENS_ALLOWED_PARAMS

    if problemName == 'Knapsack':
        return KNAPSACK_DEF_PRAMS, KNAPSACK_ALLOWED_PARAMS

    print('Unknown problem!')
    exit(1)


def validateTarget(problemName, target):
    if problemName == 'NQueens':
        if not target.isdigit():
            print(f'Invalid input {target} for N-Queens')
            exit(1)

    elif problemName == 'StringMatching':
        if type(target) != str or target == '':
            print(f'Invalid input {target} for String Matching')
            exit(1)

    elif problemName == 'Knapsack':
        if not target.isdigit():
            print(f'Invalid input {target} for Knapsack')
            exit(1)


def main():
    startTime = time.time()

    parser = argparse.ArgumentParser()

    # set cmd flags
    parser.add_argument('-p', '--problem', default=DEFAULT_PROBLEM)
    parser.add_argument('-ps', '--popsize', default=GA_POP_SIZE)
    parser.add_argument('-c', '--cross')
    parser.add_argument('-f', '--fitness')
    parser.add_argument('-m', '--mutation')
    parser.add_argument('-a', '--algo', default=DEFAULT_ALGORITHM)
    parser.add_argument('-s', '--parentSelection', default=DEFAULT_PARENT_SELECTION_FUNC)
    parser.add_argument('-r', '--continuationRule', default=DEFAULT_CONTINUATION_RULE)
    parser.add_argument('-t', '--target')

    args = parser.parse_args()

    # validate input
    if args.problem not in ALLOWED_PROBLEM_NAMES:
        print("invalid problem!\n")
        exit(1)

    paramsDict, allowedDict = getParamsDict(args.problem)

    if args.fitness:
        if args.fitness in allowedDict[FITNESS]:
            paramsDict[FITNESS] = args.fitness
        else:
            print("Input Error: This problem can't work with this fitness function")
            exit(1)

    if args.cross:
        if args.cross in allowedDict[CROSSOVER]:
            paramsDict[CROSSOVER] = args.cross
        else:
            print("Input Error: This problem can't work with this crossover")
            exit(1)

    if args.mutation:
        if args.mutation in allowedDict[MUTATION]:
            paramsDict[MUTATION] = args.mutation
        else:
            print("Input Error: This problem can't work with this mutation")
            exit(1)

    if args.target:
        validateTarget(args.problem, args.target)
        paramsDict[TARGET] = args.target

    if args.algo not in ALLOWED_ALGO_NAMES:
        print("invalid algo!\n")
        return

    if args.parentSelection not in ALLOWED_PARENT_SELECTION_FUNC_NAMES:
        print("invalid parent selection function!\n")
        return

    if args.continuationRule not in ALLOWED_CONTINUATION_RULE_NAMES:
        print("invalid continuation rule function!\n")
        return

    if type(args.popsize) != int and not args.popsize.isdigit():
        print('Invalid population size, must be an int')
        return

    algoName = args.algo
    fitnessFuncName = paramsDict[FITNESS]
    parentSelectionName = args.parentSelection
    continuationRuleName = args.continuationRule
    target = paramsDict[TARGET]

    # init objects based on input
    fitnessFunction = FitnessFunction.factory(fitnessFuncName).calculate
    problem = Problem.factory(problemName=args.problem,
                              fitnessFunction=fitnessFunction,
                              target=target)
    crossoverFunction = Crossover.factory(paramsDict[CROSSOVER]).makeNewChild
    parentSelectionFunction = ParentSelection.factory(parentSelectionName).getCandidates
    continuationRuleFunction = ContinuationRule.factory(continuationRuleName).getNextGenAndPotentialParents
    mutationFunction = Mutation.factory(paramsDict[MUTATION]).mutate

    # init algo
    algo = Algorithm.factory(algoName=algoName,
                             popSize=int(args.popsize),
                             eliteRate=GA_ELITE_RATE,
                             crossoverFunc=crossoverFunction,
                             mutationRate=GA_MUTATION_RATE,
                             mutationFunction=mutationFunction,
                             parentSelectionFunction=parentSelectionFunction,
                             continuationRuleFunction=continuationRuleFunction,
                             problem=problem
                             )

    # declare the run parameters
    print(
        '\nRun parameters:\n'
        f'Problem: {args.problem}\n'
        f'Target: {target}\n'
        f'Algo: {args.algo}\n'
        f'Pop size: {args.popsize}\n'
    )
    if algoName == 'GeneticAlgorithm':
        print(
            f'Fitness: {fitnessFuncName}\n'
            f'Parent Selection: {parentSelectionName}\n'
            f'Crossover: {paramsDict[CROSSOVER]}\n'
            f'ContinuationRule: {continuationRuleName}\n'
            f'Mutation: {paramsDict[MUTATION]}\n'

        )

    # find a solution and print it
    solVec = algo.findSolution(GA_MAX_ITER)
    print(f'Solution = {problem.translateVec(solVec)}\n')

    # print summery of run
    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f'Total elapsed time in seconds: {elapsedTime}')
    print(f'This process took {elapsedTime * CLOCK_RATE} clock ticks')


if __name__ == '__main__':
    try:
        main()
    except Exception:
        traceback.print_exc()
