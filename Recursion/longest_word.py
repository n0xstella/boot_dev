"""
Cthe find_longest_word function without a loop. It accepts string inputs, document, 
and optional longest_word, which is the current longest word and defaults to an empty string.

Check if the first word is longer than the current longest_word, then recur for the rest of the document.
Ensures there are no potential index errors.

Assumes that a "word" means a series of any consecutive non-whitespace characters.

For example, longest_word("How are you?") should return the string "you?".
"""


def find_longest_word(document, longest_word=""):
    word_list = document.split()

    if not word_list:
        return longest_word

    current_word = word_list[0]

    if len(current_word) > len(longest_word):
        longest_word = current_word

    rest_of_str = ' '.join(word_list[1:])
    result = find_longest_word(rest_of_str, longest_word)
    return result