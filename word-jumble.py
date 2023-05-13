# Part 1
# Unscramble the words
def unscramble(jumble):
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

# pick out letters to be used in the final word using indices
def final_letters(jumbles, indices):
    valid_word_lists = [unscramble(jumble) for jumble in jumbles]
    letters_array = []

    for i, word in enumerate(valid_word_lists):
        for index in indices[i]:
            letters_array.append(word[0][index])

    return ''.join(letters_array)

# Part 2
# Using the letters and recursion, create valid word arrangements
def final_word_combinations(letters):
    if len(letters) == 1:
        return [letters]

    arrangements = []
    for i in range(len(letters)):
        current_letter = letters[i]
        remaining_letters = letters[:i] + letters[i+1:]
        sub_arrangements = final_word_combinations(remaining_letters)
        for arrangement in sub_arrangements:
            arrangements.append(current_letter + arrangement)

    return arrangements


if __name__ == "__main__":

    # Read the dictionary file into a set
    with open('words2', 'r') as f:
        dictionary = set([word.strip().lower() for word in f])

    jumbles = ['tefon', 'sokik', 'niumem', 'siconu']
    indices = [[2, 4], [0, 1, 3], [4], [3, 4]]
    valid_words = [unscramble(jumble) for jumble in jumbles]
    letters = final_letters(jumbles, indices)
    

    arrangements = final_word_combinations(letters)

    arrangement_list = []
    for arrangement in arrangements:
        arrangement_list.append(''.join(arrangement))

    # print(arrangement_list)



     # Get a list of two letter words and 6 letter valid words using the letters
    possible_finals = []
    for word in arrangement_list:
        if word[0:2] in dictionary and word[2:] in dictionary:
            if word not in possible_finals:
                possible_finals.append(word)

    print(f"Jumbles: {jumbles}")
    print(f"Solved words: {valid_words}")
    print(f"Final letters for solution: {letters}")
    print(f"Possible final words: {possible_finals}")


