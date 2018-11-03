# Generates a list L_indexes of 12 random numbers between 0 and 3 included,
# generates a list L_values of 15 distinct random numbers between 0 and 99 included,
# and iteratively builds a list resulting_list as follows:
# - if i_1, ..., i_k is the longest initial segment of L_indexes consisting of nothing but
#   distinct numbers, then add to resulting_list the elements of L_values of index i_1, ..., i_k;
# - remove from L_indexes and L_values the numbers that have been used during the previous step.
#
# Written by Eric Martin for COMP9021

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
while L_indexes:
    used_indexes = set()
    i = 0
    while i < len(L_indexes) and L_indexes[i] not in used_indexes:
        index = L_indexes[i]
        resulting_list.append(L_values[index])
        used_indexes.add(index)
        i += 1
    for value in resulting_list[-i: ]:
        L_values.remove(value)
    L_indexes = L_indexes[i: ]

print('The resulting list of values is:')
print('  ', resulting_list)
