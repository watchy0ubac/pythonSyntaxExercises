# 1. For a list of words, print out each word on a separate line, but in all uppercase. How can you change a word to uppercase? Ask Python for help on what you can do with strings!
# 2. Turn that into a function, ***print_upper_words***. Test it out. (Don’t forget to add a docstring to your function!)
# 3. Change that function so that it only prints words that start with the letter ‘e’ (either upper or lowercase).
# 4. Make your function more general: you should be able to pass in a set of letters, and it only prints words that start with one of those letters.
    
#     For example:
# this should print "HELLO", "HEY", "YO", and "YES"

# print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
#                    must_start_with={"h", "y"})

def print_upper_words(words, must_start_with='e'):
    '''Takes a list of words and return each word individually and uppercased'''
    for word in words:
        for letter in must_start_with:
            if word[0] == letter.lower() or word[0] == letter.upper():
                print(f'{word.upper()}')

print_upper_words(["hello", "hey", "goodbye", "yo", "yes", 'eeyore'])
print('-------------------------------------------')

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})