# Computes the hash code of a string x_0x_1...x_n
# (with x_0, x_1, ..., x_n being the ascii codes of the characters)
# as the number x_0a^n + x_1a^{n-1} + .... + x_n.
#
# Written by Eric Martin for COMP9021


from collections import defaultdict

def hash_code(word, base):
    code = 0
    for c in word:       
        code = base * code + ord(c)      
    return code

def hash_all_words(base):
    words_file = open('words.txt')
    codes = defaultdict(lambda: 0)
    for word in words_file:
        codes[hash_code(word[: -1], base)] += 1
    return sorted(list(codes.values()), reverse = True)

def find_best_bases(top_bases, bottom_hashes):
    hash_counts_per_base = []
    for base in range(2, 50):
        hash_counts = hash_all_words(base)
        hash_counts_per_base.append((hash_counts[ : bottom_hashes], base))
    return sorted(hash_counts_per_base)[: top_bases]

if __name__ == '__main__':
    print('Bottom 4 hashes for base of 2:')
    print(hash_all_words(2)[: 4])
    print('\nBest 6 bases up to 49 for bottom 4 hashes:')
    best_bases = find_best_bases(6, 4)
    for hashes, base in best_bases:
        print('{:2d} : {}'.format(base, hashes))
        
        
        
            
           

