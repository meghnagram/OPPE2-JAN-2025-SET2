def same_sign(a, b):
    """
    Checks whether two numbers have the same sign.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        bool: True if the numbers have the same sign, False otherwise.

    Examples:
        >>> same_sign(10, 20)
        True
        >>> same_sign(-5, -15)
        True
        >>> same_sign(0, 0)
        True
        >>> same_sign(10, -20)
        False
        >>> same_sign(0, 10)
        False
    """
    
    
    return ((a < 0) and (b < 0) or (a > 0) and (b > 0) or a == b ==0)
    
# #Another Method:

# def same_sign(a, b):
#     num1=int(a)
#     num2=int(b)
    
#     if (num1==0 and num2==0) or (num1<0 and num2<0) or (num1>0 and num2>0):
#         return True
#     else:
#         return False


# Check if both numbers have the same sign
# Write a function same_sign that checks whether two given numbers have the same sign. Consider three cases:

# Both numbers are strictly positive.
# Both numbers are strictly negative.
# Both numbers are zero.
# The function should return True if the numbers have the same sign; otherwise, it should return False.

# NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

# Examples

# same_sign(10, 20) -> True
# Explanation: Both numbers are strictly positive.
# same_sign(-5, -15) -> True
# Explanation: Both numbers are strictly negative.
# same_sign(0, 0) -> True
# Explanation: Both numbers are zero.
# same_sign(10, -20) -> False
# Explanation: The numbers have different signs.
# same_sign(0, 10) -> False
# Explanation: One number is zero, and the other is strictly positive.

