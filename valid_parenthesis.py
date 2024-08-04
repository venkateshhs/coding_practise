def isValid(s: str) -> bool:
    # Dictionary to hold the mapping of closing to opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []

    print(f"Processing string: {s}")

    for char in s:
        print(f"Current character: {char}")

        if char in bracket_map:
            # Pop the top element if it exists, else assign a dummy value
            top_element = stack.pop() if stack else '#'
            print(f"Popped from stack: {top_element}")

            # Check if the mapping for this bracket is correct
            if bracket_map[char] != top_element:
                print(f"Mismatch found. Expected {bracket_map[char]}, but found {top_element}.")
                return False
            else:
                print(f"Match found. Stack after pop: {stack}")
        else:
            # It's an opening bracket, push it onto the stack
            stack.append(char)
            print(f"Stack after push: {stack}")

    # In the end, if the stack is empty, the brackets are valid
    print(f"Final stack: {stack}")
    return not stack

# Example usage:
print(isValid("()"))        # Output: true
print(isValid("()[]{}"))    # Output: true
print(isValid("(]"))        # Output: false
print(isValid("([)]"))      # Output: false
print(isValid("{[]}"))      # Output: true
