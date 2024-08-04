class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        # Mapping of digits to corresponding letters
        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        def backtrack(index: int, path: str):
            # If the current combination is done
            if index == len(digits):
                combinations.append(path)
                return
            
            # Get the letters that the current digit maps to, and recurse
            possible_letters = phone_map[digits[index]]
            for letter in possible_letters:
                backtrack(index + 1, path + letter)

        combinations = []
        backtrack(0, "")
        return combinations
