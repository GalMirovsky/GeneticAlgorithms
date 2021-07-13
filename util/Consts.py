import string

import psutil

GA_POP_SIZE = 300  # ga population size
GA_MAX_ITER = 300  # maximum iterations

AGE_MIN_TO_BE_PARENT = 2
AGE_DIE = 20
CLOCK_RATE = psutil.cpu_freq().current * (2 ** 20)  # clock ticks per second

UNWANTED_CHARS = ('\t', '\n', '\x0b', '\x0c', '\r')

ALLOWED_CHARS = tuple(c for c in string.printable if c not in UNWANTED_CHARS)
LOWER_BOUND = 32
UPPER_BOUND = 126

BEST = 0

'''------------------GA-------------------'''
GA_ELITE_RATE = 0.1  # elitism rate
GA_MUTATION_RATE = 0.25  # mutation rate

'''------------------PSO------------------'''
COGNITIVE_WEIGHT = 2
SOCIAL_WEIGHT = 2

'''------------------DEFAULT_PARSER-------------------'''

DEFAULT_PROBLEM = 'StringMatching'
DEFAULT_ALGORITHM = 'GeneticAlgorithm'
DEFAULT_PARENT_SELECTION_FUNC = 'NaiveParentSelection'
DEFAULT_CONTINUATION_RULE = 'EliteRule'

'''------------------ALLOWED_PARSER_NAMES-------------------'''

ALLOWED_PROBLEM_NAMES = ('StringMatching', 'NQueens', 'Knapsack')
ALLOWED_ALGO_NAMES = ('GeneticAlgorithm', 'PSO', 'MinimalConflict')
ALLOWED_PARENT_SELECTION_FUNC_NAMES = ('NaiveParentSelection', 'RWS', 'SUS', 'DeterministicTournament',
                                       'StochasticTournament')
ALLOWED_CONTINUATION_RULE_NAMES = ('AgingRule', 'EliteRule')

'''--------------String Matching Parameters------------------'''
STRING_MATCHING_DEF_PRAMS = {
    'TARGET': 'Hello World!',
    'CROSSOVER': 'TwoPointCrossover',
    'FITNESS': 'AsciiDistance',
    'MUTATION': 'FlipMutation'
}

STRING_MATCHING_ALLOWED_PARAMS = {
    'CROSSOVER': ('SinglePointCrossover', 'TwoPointCrossover', 'UniformCrossover'),
    'FITNESS': ('AsciiDistance', 'BullsAndCows'),
    'MUTATION': ('FlipMutation')
}

'''--------------N Queens Parameters------------------'''
N_QUEENS_DEF_PRAMS = {
    'TARGET': 8,
    'CROSSOVER': 'OrderedCrossover',
    'FITNESS': 'DiagonalConflicts',
    'MUTATION': 'ScrambleMutation'
}

N_QUEENS_ALLOWED_PARAMS = {
    'CROSSOVER': ('PartiallyMatchedCrossover', 'OrderedCrossover'),
    'FITNESS': ('DiagonalConflicts'),
    'MUTATION': ('ScrambleMutation', 'ExchangeMutation')
}

'''--------------N Queens Parameters------------------'''

KNAPSACK_DEF_PRAMS = {
    'TARGET': 8,
    'CROSSOVER': 'UniformCrossover',
    'FITNESS': 'KnapsackFitness',
    'MUTATION': 'KnapsackFlipMutation'
}

KNAPSACK_ALLOWED_PARAMS = {
    'CROSSOVER': (
        'SinglePointCrossover', 'TwoPointCrossover', 'UniformCrossover', 'PartiallyMatchedCrossover',
        'OrderedCrossover'),
    'FITNESS': ('KnapsackFitness'),
    'MUTATION': ('KnapsackFlipMutation')
}

CROSSOVER = 'CROSSOVER'
MUTATION = 'MUTATION'
TARGET = 'TARGET'
FITNESS = 'FITNESS'
