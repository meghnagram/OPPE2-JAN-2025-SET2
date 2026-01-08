def shuffle_sentence(sentence, order):
    """
    Shuffles the words of a three-word sentence according to the specified order.

    Args:
        sentence (str): The three-word sentence.
        order (tuple): The shuffling order.

    Returns:
        str: The shuffled sentence.

    Examples:
        >>> shuffle_sentence('apple banana orange', (0, 2, 1))
        'apple orange banana'
        >>> shuffle_sentence('cat dog mouse', (2, 1, 0))
        'mouse dog cat'
    """
    
    
    words = sentence.split()
    return f"{words[order[0]]} {words[order[1]]} {words[order[2]]}"
    # this can be extended to any number of words as follows
    # return " ".join([words[i] for in order])
    
# #Another problem

# def shuffle_sentence(sentence, order):
    
#     #list_from_str = []
#     list_from_str = sentence.split(' ')
#     newstr=''
#     for i in order:
#         newstr += list_from_str[i]+' '
#     return newstr.rstrip()

# Shuffle a Three Word Sentence
# Write a function shuffle_sentence(sentence, order) that takes a string sentence containing three words separated by spaces and a tuple order specifying the shuffling order.

# The function should return a string with the words of the sentence shuffled according to the specified order.

# NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

# Examples

# sentence = "apple banana orange", order = (0, 2, 1) -> "apple orange banana" Explanation: 0 - apple , 2 - orange, 1 - banana
# sentence = "cat dog mouse", order = (2, 1, 0) -> "mouse dog cat" Explanation: 2 - mouse, 1 - dog, 0 - cat
    
