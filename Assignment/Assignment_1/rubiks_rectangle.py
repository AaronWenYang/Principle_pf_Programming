from collections import deque
from math import factorial
import sys

def f1(l):                      #for row exchange
    l.reverse()
    return l

def f2(l):                      #for right circular shift
    l.appendleft(list(l)[3])
    l.append(list(l)[5])
    l.rotate(4)
    l.pop()
    l.pop()
    l.rotate(4)
    return l

def f3(l):                      #for middle clockwise rotation
    l.rotate(-1)
    l.appendleft(list(l)[5])
    l.rotate(4)
    l.append(list(l)[6])
    l.rotate(-1)
    l.popleft()
    l.rotate(-4)
    l.popleft()
    l.rotate(3)
    return l

def deq_to_str(d):
    s_of_d = str(list(d)[0])+str(list(d)[1])+str(list(d)[2])+str(list(d)[3])+str(list(d)[4])+str(list(d)[5])+str(list(d)[6])+str(list(d)[7])
    return s_of_d

def str_to_deq(s):
    d_of_s = deque(list(s))
    return d_of_s


try:
    ss = input('Input final configuration :')
    B = ss.replace(' ', '')
    C = sorted(list(B))
    if len(B) != 8:
        raise ValueError
    elif C != ['1','2','3','4','5','6','7','8']:
        raise ValueError
except ValueError:
    print('Incorrect configuration , giving up . . . ')
    sys.exit()
    
A = str(B)

str_0 = '12345678'
dict_result = {'12345678' : 0}
dict_temporary = {str_0 : 0}
list_temporary = ['12345678']
while A not in dict_result:
    
    for str_temporary in  list_temporary:
        
        deque_1 = f1(str_to_deq(str_temporary))
        str_1 = deq_to_str(deque_1)
        if str_1 not in dict_result:
            dict_result[str_1] = dict_result[str_temporary] + 1
            dict_temporary[str_1] = dict_result[str_temporary] + 1
            list_temporary.append(str_1)


        deque_2 = f2(str_to_deq(str_temporary))
        str_2 = deq_to_str(deque_2)
        if str_2 not in dict_result:
            dict_result[str_2] = dict_result[str_temporary] + 1
            dict_temporary[str_2] = dict_result[str_temporary] + 1
            list_temporary.append(str_2)


        deque_3 = f3(str_to_deq(str_temporary))
        str_3 = deq_to_str(deque_3)
        if str_3 not in dict_result:
            dict_result[str_3] = dict_result[str_temporary] + 1
            dict_temporary[str_3] = dict_result[str_temporary] + 1
            list_temporary.append(str_3)


        dict_temporary.pop(str_temporary)
        list_temporary = list_temporary[1:]
        
        
        
print('{}  steps are needed to reach the final configuration . '.format(dict_result[A]))

    





