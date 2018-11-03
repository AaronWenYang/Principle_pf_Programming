# Generates a list L_indexes of 12 random numbers between 0 and 3 included,
# generates a list L_values of 15 distinct random numbers between 0 and 99 included,
# and iteratively builds a list resulting_list as follows:
# - if i_1, ..., i_k is the longest initial segment of L_indexes consisting of nothing but
#   distinct numbers, then add to resulting_list the elements of L_values of index i_1, ..., i_k;
# - remove from L_indexes and L_values the numbers that have been used during the previous step.
#
# Written by *** and Eric Martin for COMP9021

import sys
from random import seed, randint, sample


nb_of_indexes = 12
max_index = 3
upper_bound = 100

try:
     seed(input('Enter an integer: '))
except TypeError:
    print('Incorrect input, giving up.')
    sys.exit()

L_indexes = [randint(0, max_index) for _ in range(nb_of_indexes)]
L_values = sample(range(upper_bound), nb_of_indexes + max_index)
print('The generated lists of indexes and values are, respectively:')
print('  ', L_indexes)
print('  ', L_values)

resulting_list = []
import numpy
x=1
while len(L_indexes) > 0 :
    if len(L_indexes[:x+1]) == len(set(L_indexes[:x+1])) + 1 or x+1> len(L_indexes):
        small_list_indexes = numpy.array(L_indexes[:x])
        resulting_list[len(resulting_list):len(resulting_list)] = list(numpy.array(L_values)[small_list_indexes])
        for value in list(numpy.array(L_values)[small_list_indexes]):
            L_values.remove(value)
        L_indexes= L_indexes[x:]
        x=1
    else:
        x = x + 1

print('The resulting list of values is:')
print('  ', resulting_list)
