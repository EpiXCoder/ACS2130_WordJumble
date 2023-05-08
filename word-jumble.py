# Part 1
# Unscramble the words
def unscramble(jumble):
    # Read the dictionary file into a set
    with open('words2', 'r') as f:
        dictionary = set([word.strip().lower() for word in f])

    # Create a hash table for the dictionary words
    hashtable = {}
    for word in dictionary:
        key = ''.join(sorted(word))
        if key in hashtable:
            hashtable[key].append(word)
        else:
            hashtable[key] = [word]

    # Find all valid words in the jumble
    jumble_key = ''.join(sorted(jumble))
    if jumble_key in hashtable:
        valid_words = hashtable[jumble_key]
    else:
        valid_words = []
    
    return valid_words

#pick out letters to be used in the final word using indices
def final_letters():
    valid_word_lists = [unscramble(jumble) for jumble in jumbles]
    # valid_word_lists = [['often'], ['kiosk'], ['immune'], ['cousin']]
    letters_array = []

    for i, word in enumerate(valid_word_lists):
        for index in indices[i]:
            letters_array.append(word[0][index])

    # print(letters_array)
    return letters_array

# Part 2
# Using the letters, create valid word pairs
def create_word_pairs():
    letters_array = final_letters()
    word_pairs = []
    with open('words2', 'r') as file:
        word_list = [line.strip().lower() for line in file]
    
    # Get a list of two letter words and 6 letter valid words using the letters
    two_letter_words = [word for word in word_list if len(word) == 2]
    six_letter_words = [word for word in word_list if len(word) == 6]

    # Pair up the words
    for word1 in two_letter_words:
        for word2 in six_letter_words:
            if sorted(list(word1 + word2)) == sorted(letters_array):
                word_pairs.append((word1, word2))

    return word_pairs



def jumble_solution():
    result = create_word_pairs()

# Print the resulting word pairs
    for pair in result:
        print(pair)

# Define the jumbles and indices
jumbles = ['tefon', 'sokik', 'niumem', 'siconu']
indices = [[2, 4], [0, 1, 3], [4], [3, 4]]
jumble_solution()