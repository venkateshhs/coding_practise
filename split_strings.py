def split_into_pairs(s):
    # Append an underscore if the length of the string is odd
    if len(s) % 2 != 0:
        s += '_'

    # Use a list comprehension to collect pairs of characters
    pairs = [s[i:i+2] for i in range(0, len(s), 2)]

    return pairs

# Test cases
print(split_into_pairs('abc'))     # Output: ['ab', 'c_']
print(split_into_pairs('abcdef'))  # Output: ['ab', 'cd', 'ef']
