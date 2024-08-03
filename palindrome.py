def is_palindrome(x):
    # Negative numbers are not palindromes
    if x < 0:
        return False

    # Create the reversed number
    original = x
    reversed_num = 0

    while x > 0:
        digit = x % 10
        print('digit', digit)
        reversed_num = reversed_num * 10 + digit
        print('reversed_num', reversed_num)
        x = x // 10
        print('x', x)

    # Check if the original number is the same as the reversed number
    return original == reversed_num

# Example usage:
print(is_palindrome(121))  # Output: True

