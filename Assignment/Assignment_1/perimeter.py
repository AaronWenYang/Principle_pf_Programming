from itertools import permutations as perm
import re

input_letters = input('Enter between 3 and 10 lowercase letters : ')

list_all = []

for lenth_sub_list in range(1,len(input_letters)+1):
    sub_list_inorder = perm(input_letters,lenth_sub_list)
    list_all += sub_list_inorder
print(list_all)
list_all = list(set(list_all))
print(list_all)

def list_to_str(listA):
    strA = ''
    for letter_in_listA in listA:
        strA = strA + letter_in_listA
    return strA

with open('wordsEn.txt','r') as wordsEn:
    list_found_all_same = []
    for a_word_in_file in wordsEn.readlines(): 
        for list_of_letter_all in list_all:
            str_of_letter = list_to_str(list_of_letter_all)
            if len(a_word_in_file) == len(str_of_letter)+1:   
                same_word = re.findall(str_of_letter, a_word_in_file)   
                if same_word != [] :
                    list_found_all_same.append(same_word[0])
 

#####################

#####################
# with open('wordsEn.txt','r') as wordsEn:
#     for a_word_in_file in wordsEn.readlines():
#         for str_made_by_letters in list_all_str:
#             if a_word_in_file == str_made_by_letters + '\n':
#                 list_found_all_same.append(a_word_in_file.strip())
if list_found_all_same  == []:
    print('No same word!')
elif list_found_all_same  != []:
    print(list_found_all_same)
  
dict_letter_value = {'a':2, 'b': 5, 'c' :4, 'd': 4, 'e': 1, 'f': 6, 'g': 5, 'h': 5, 'i': 1, 'j': 7, 'k': 6, 'l': 3, 'm': 5, 'n': 2, 'o': 3, 'p': 5, 'q': 7, 'r': 2, 's': 1, 't': 2, 'u': 4, 'v': 6, 'w': 6, 'x':7, 'y': 5, 'z' :7}
dict_word_score = {}
word_score = 0
for same_word in list_found_all_same:
    score_of_word = 0
    for index_of_letter in range(len(same_word)):
        score_of_letter = dict_letter_value[same_word[index_of_letter]]
        score_of_word = score_of_word + score_of_letter
    dict_word_score[same_word] = score_of_word
 
print(dict_word_score)
score_list = []
for word_have_score in dict_word_score:
    score_list.append(dict_word_score[word_have_score])
max_score = max(score_list)
wordlist_max_score = []
for word_have_score in dict_word_score:
    if dict_word_score[word_have_score] == max_score:
        wordlist_max_score.append(word_have_score)
print(wordlist_max_score)
for word_result in wordlist_max_score:
    print(word_result)
         
         
         
        

        