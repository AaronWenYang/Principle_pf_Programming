# Prompts the user for an arity N (a nonnegative integer) and a term
# where the function symbols are assumed to consist of nothing but alphabetic
# characters and underscores, with spaces allowed at the beginning
# and around parentheses and commas.
# Checks that the term is syntactically correct according to the definition of a term
# and also in that all function symbols are of arity N or 0.
#
# Written by *** and Eric Martin for COMP9021


import sys


def is_syntactically_correct(term, arity):
    
    list_input_limit = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','_',',',' ','(',')']
    list_letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    s = list(term.replace(" ", ""))
    number_of_variaty = int(arity)
    list_index = list(range(len(s)))  
    list_after_zip = list(map(list,zip(s,list_index)))   
    list_index_of_open_paren = []
    list_index_of_close_paren = []
    list_index_of_comma = []
    list_index_of_letters = []
    list_index_of_element_before_open_paren = []
    
    for index_of_elments in range(len(s)):
        if list_after_zip[index_of_elments][0] == '(':
            list_index_of_open_paren.append(list_after_zip[index_of_elments][1])
        elif list_after_zip[index_of_elments][0] == ')':
            list_index_of_close_paren.append(list_after_zip[index_of_elments][1])
        elif list_after_zip[index_of_elments][0] == ',':
            list_index_of_comma.append(list_after_zip[index_of_elments][1])
        elif list_after_zip[index_of_elments][0] in list_letter:
            list_index_of_letters.append(list_after_zip[index_of_elments][1])
    list_index_of_all_paren = sorted(list_index_of_open_paren + list_index_of_close_paren)

    
    def no_adjacent_comma():
        index_of_index_comma = 0
        if s.count('(') == s.count(')') == s.count(',') == 1:
                return True
        while index_of_index_comma <= len(list_index_of_comma)-2:                                 #5
            if list_index_of_comma[index_of_index_comma] == list_index_of_comma[index_of_index_comma +1] - 1:
                return False
                break
            elif index_of_index_comma == len(list_index_of_comma)-2 and list_index_of_comma[index_of_index_comma] != list_index_of_comma[index_of_index_comma +1] - 1:
                return True
                break
            else: 
                index_of_index_comma = index_of_index_comma +1
                
    if arity == 0 and set(s).issubset(set(list_letter)):
        return True
        
    while  s.count('(') > 0 and s.count(')') > 0:
        if set(s).issubset(set(list_input_limit)):                                                           #1 meet the input limit
            if s[0] in list_letter :                                                                         #2 function format requirement 2 : function start with a letter
                if len(list_index_of_open_paren) == len(list_index_of_close_paren):                          #3 function format requirement 3 : number of open parens is same as that of close parens 
                    for index_of_open_paren in list_index_of_open_paren:
                        list_index_of_element_before_open_paren.append(index_of_open_paren-1)
                    if set(list_index_of_element_before_open_paren).issubset(set(list_index_of_letters)):    #4 function format requirement 4 : should exist a letter ahead of each paren 
                        if list_index_of_comma != []:                                                        #5 function format requirement 5 : a function with multiple varieties must use commas to separate each variety
                            if no_adjacent_comma():                                                          #6 function format requirement 6 : commas are not adjacent to each other
                                list_find_first_closeparen = list_index_of_open_paren + list_index_of_close_paren[:1]
                                sorted_list_find = sorted(list_find_first_closeparen)
                                index_of_last_openparen_before_close = sorted_list_find.index(list_index_of_close_paren[0]) -1
                                list_between_deepest_paren = s[list_index_of_all_paren[index_of_last_openparen_before_close]:list_index_of_all_paren[index_of_last_openparen_before_close +1]]
                                if number_of_variaty == list_between_deepest_paren.count(',') + 1:           #7 count the number of varieties 
                                    s = s[:list_index_of_all_paren[index_of_last_openparen_before_close]]+list('a'*(list_index_of_all_paren[index_of_last_openparen_before_close +1]- list_index_of_all_paren[index_of_last_openparen_before_close]+1))+s[list_index_of_all_paren[index_of_last_openparen_before_close +1]+1:]
                                    list_index = list(range(len(s)))  
                                    list_after_zip = list(map(list,zip(s,list_index)))   
                                    
                                    list_index_of_open_paren = []
                                    list_index_of_close_paren = []
                                    list_index_of_comma = []
                                    list_index_of_letters = []
                                    list_index_of_element_before_open_paren = []
                                    
                                    for index_of_elments in range(len(s)):
                                        if list_after_zip[index_of_elments][0] == '(':
                                            list_index_of_open_paren.append(list_after_zip[index_of_elments][1])
                                        elif list_after_zip[index_of_elments][0] == ')':
                                            list_index_of_close_paren.append(list_after_zip[index_of_elments][1])
                                        elif list_after_zip[index_of_elments][0] == ',':
                                            list_index_of_comma.append(list_after_zip[index_of_elments][1])
                                        elif list_after_zip[index_of_elments][0] in list_letter:
                                            list_index_of_letters.append(list_after_zip[index_of_elments][1])
                                    list_index_of_all_paren = sorted(list_index_of_open_paren + list_index_of_close_paren)
                                    
                                    if s.count('(') == 0 and s.count(')') == 0:
                                        return True
                                        break
                                    else:continue
                                else :
                                    return False
                                    break
                            elif no_adjacent_comma() == False : 
                                return False
                                break
                            else :
                                return False
                                break
                        elif list_index_of_comma == []: 
                            if number_of_variaty == 1 :
                                return True
                                break
                            elif number_of_variaty != 1 :
                                return False
                                break
                    else:
                        return False
                        break
                else:
                    return False
                    break
            else:
                return False
                break            
        else:
            return False
            break


try:
    arity = int(input('Input an arity : '))
    if arity < 0:
        raise ValueError
except ValueError:
    print('Incorrect arity, giving up...')
    sys.exit()
print('A term should contain only letters, underscores, commas, parentheses, spaces.')
term = input('Input a term: ')
if is_syntactically_correct(term, arity):
    print('Good, the term is syntactically correct.')
else:
    print('Unfortunately, the term is syntactically incorrect.')
