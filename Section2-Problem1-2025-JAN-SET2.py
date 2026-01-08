
def is_palindrome(s: str) -> bool:
    '''
    Given a string, returns True if it reads the same forward and backward,
    ignoring spaces, capitalization, and punctuation.

    Eg.
    is_palindrome("A man, a plan, a canal, Panama!") -> True
    is_palindrome("racecar") -> True
    is_palindrome("hello") -> False

    Args:
        s (str): Input string.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    '''
    
    
    # Remove non-alphanumeric characters and convert to lowercase manually
    clean_s = ''.join(char.lower() for char in s if char.isalnum())

    # Compare the cleaned string with its reverse
    return clean_s == clean_s[::-1]

    
# #Another method:

# def is_palindrome(s: str) -> bool:
#     '''
#     Given a string, returns True if it reads the same forward and backward,
#     ignoring spaces, capitalization, and punctuation.

#     Eg.
#     is_palindrome("A man, a plan, a canal, Panama!") -> True
#     is_palindrome("racecar") -> True
#     is_palindrome("hello") -> False

#     Args:
#         s (str): Input string.

#     Returns:
#         bool: True if the string is a palindrome, False otherwise.
#     '''
#     newstr=''
#     for i in s:
#         if i.isalnum():
#             newstr +=i.lower() 
#     # print(newstr)
#     if newstr == newstr[::-1]:
#         return True
#     else:
#         return False
        
#     Check Palindrome - Advanced
# Write a function is_palindrome that takes a string as input and returns True if the string reads the same forward and backward considering only the alphabets and numbers (ignoring spaces, capitalization, and punctuation). Otherwise, it returns False.

# Ignore spaces, capitalization, and punctuation while checking.
# The function should not print anything.
# Complete the function definition only.
# Hint: use str.isalnum function to check if a character is alphabet or number

# NOTE: This is a function type question, you don't have to take input or print the output, just complete the required function definition.

# Example

# is_palindrome("A man, a plan, a canal, Panama!") -> True
# is_palindrome("racecar") -> True
# is_palindrome("hello") -> False
# is_palindrome("No lemon, no melon") -> False
