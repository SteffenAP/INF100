def find_longest_words(x1, x2, x3):
    len1 = len(x1)
    len2 = len(x2)
    len3 = len(x3)
    maxlen = max(len1, len2, len3)
    if maxlen == len1:
        print(x1)
    if maxlen == len2:
        print(x2)
    if maxlen == len3:
        print(x3)
        
find_longest_words("Game", "Action", "Champion")
find_longest_words("apple", "carrot", "ananas")
find_longest_words("Four", "Five", "Nine")