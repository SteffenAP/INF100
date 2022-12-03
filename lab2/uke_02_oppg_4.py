def find_first_longest_word(x1, x2, x3):
    len1 = len(x1)
    len2 = len(x2)
    len3 = len(x3)
    maxlen = max(len1, len2, len3)
    if maxlen == len1:
        print(x1)
    elif maxlen == len2:
        print(x2)
    elif maxlen == len3:
        print(x3)
        
find_first_longest_word("Game", "Action", "Champion")
find_first_longest_word("apple", "carrot", "ananas")
find_first_longest_word("Four", "Five", "Nine")