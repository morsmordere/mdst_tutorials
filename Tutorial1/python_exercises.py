"""
Intro to python exercises shell code
"""

def is_odd(x):
    """
    returns True if x is odd and False otherwise
    """
    if x % 2 != 0:
        return True
    return False


def is_palindrome(word):
    """
    returns whether `word` is spelled the same forwards and backwards
    """
    left = 0
    right = len(word)-1
    while left < right:
        if word[left]!=word[right]:
            return False
        left += 1
        right -= 1
    return True


def only_odds(numlist):
    """
    returns a list of numbers that are odd from numlist

    ex: only_odds([1, 2, 3, 4, 5, 6]) -> [1, 3, 5]
    """
    nums = []
    for i in numlist:
        if is_odd(i):
            nums.append(i)
    return nums

def count_words(text):
    """
    return a dictionary of {word: count} in the text

    words should be split by spaces (and nothing else)
    words should be converted to all lowercase

    ex: count_words("How much wood would a woodchuck chuck"
                    " if a woodchuck could chuck wood?")
        ->
        {'how': 1, 'much': 1, 'wood': 1, 'would': 1, 'a': 2, 'woodchuck': 2,
        'chuck': 2, 'if': 1, 'could': 1, 'wood?': 1}
    """
    word_dict = {}
    words = text.lower().split()
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict
