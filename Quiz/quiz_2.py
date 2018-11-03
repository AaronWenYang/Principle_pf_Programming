# Implements a function to encode a single strictly positive natural number that in base 2,
# reads as b_1 ... b_n, as b_1b_1 ... b_nb_n, and to encode a sequence of strictly positive
# natural numbers N_1 ... N_k with k >= 2 as N_1* 0 ... 0 N_k* where for all 0 < i <= k,
# N_i* is the encoding of N_i.
# Implements a function to decode a natural number N into a sequence of (one or more)
# strictly positive natural numbers according to the previous encoding scheme,
# or return None in case N does not encode such a sequence.
# Prompts the user to enter a strictly positive natural number, applies the decoding function,
# and prints out base 2 representations of both the encoding number and the decoded sequence
# for verification purposes.
#
# Written by *** and Eric Martin for COMP9021

import sys


def encode(*integers):
    return int('0'.join(''.join(c + c for c in bin(i)[2: ]) for i in integers), 2)
    

def decode(integer): 
    str_before_decode = str(int(bin(integer)[2: ]))
    a = ''
    list_new = []
    while len(str_before_decode) >= 2:
        if str_before_decode[:2] == '11':
            a = a + '1'
            str_before_decode = str_before_decode[2:]
            if len(str_before_decode) == 0:
                list_new.append(a)
            elif len(str_before_decode) == 1: return None
        elif str_before_decode[:2] == '00':
            a = a + '0'
            str_before_decode = str_before_decode[2:]
            if len(str_before_decode) == 0:
                list_new.append(a)
            elif len(str_before_decode) == 1: return None   
        elif str_before_decode[:2] == '01':
            str_before_decode = str_before_decode[1:]
            list_new.append(a)
            a = ''
        else: return None
    N=[]
    for str_after_encode in list_new:
        str_after_encode = int(str_after_encode,2)
        N.append(str_after_encode)
    return(N)

integer = input('Input a strictly positive integer: ')
if integer[0] == '0' or not integer.isdigit():
    print('Incorrect input, giving up!')
    sys.exit()
integer = int(integer)
decoding = decode(integer)
if decoding is None:
    print('Incorrect encoding!')
else:
    print('This encodes: ', decoding)
    print('Checking: ')
    print('  In base 2, {} is {}'.format(integer, bin(integer)[2: ]))
    print('  In base 2, {} is: [{}]'.format(decoding, ', '.join(bin(i)[2: ] for i in decoding)))
          

        
                
                
                
