from entities.mutations.Mutation import Mutation

from util.Util import getValidIndexes


class ExchangeMutation(Mutation):

    def mutate(self, vec):
        vecSize = len(vec)
        # get two random indexes and exchange them
        index1, index2 = getValidIndexes(vecSize)

        temp = vec[index1]
        vec[index1] = vec[index2]
        vec[index2] = temp

        return vec
