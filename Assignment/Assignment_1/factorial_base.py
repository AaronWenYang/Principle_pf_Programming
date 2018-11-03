from math import factorial as fact
import sys

try:
    A = int(input('Input a nonnegative integer :'))
    if A < 0:
        raise ValueError
except ValueError:
    print('Incorrect input , giving up . . . ')
    sys.exit()

copyA = A
list_n = []
k = 1
n = 0
if A >0:
    while k in range(1,A):
        if fact(k) < A < fact(k +1):
            while k>= 1 and A >= 0 and n in range(0,10) :
                if fact(k) * n < A < fact(k) * (n+1):
                    A = A - fact(k) * n
                    k = k -1
                    list_n.append(n)
                    n = 0
                elif fact(k) * n == A :
                    list_n.append(n)
                    for num_of_zeros in range(k-1):
                        list_n.append(0)
                    A = A - fact(k) * n
                    k = k - 1
                elif A == 0:
                    break
                else:
                    n += 1
        elif fact(k) == A:
            list_n.append(1)
            for num_of_zeros in range(k-1):
                list_n.append(0) 
            break
        else :
            k += 1
elif A == 0 :
    list_n = [0]
        
result_num = ''
for idx_list_n in range(len(list_n)):
    result_num += str(list_n[idx_list_n])

print('Decimal {} reads as {} in factorial base .'.format(copyA,result_num))








