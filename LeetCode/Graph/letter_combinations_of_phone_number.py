from typing import *

class Solution:
    # Recursive
    def letterCombinations(self, digits: str) -> List[str]:
        digit_letter_mapping = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        combinations = []
        def dfs(idx: int, path: str):
            if idx == len(digits):
                combinations.append(path)
                return
            for letter in digit_letter_mapping[digits[idx]]:
                dfs(idx+1, path+letter)

        if not digits:
            return []
        dfs(0, "")
        return combinations

    # Simple iterations
    # def letterCombinations(self, digits: str) -> List[str]:
    #     if not digits:
    #         return []
    #     digit_letter_mapping = {
    #         "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
    #         "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    #     }
    #     combinations = [""]
    #     for idx, digit in enumerate(digits):
    #         letters = digit_letter_mapping[digit]
    #         new_combinations = []
    #         for comb in combinations:
    #             for letter in letters:
    #                 new_combinations.append(comb + letter)
    #         combinations = new_combinations
    #     return combinations

s = Solution()
print(s.letterCombinations("23"))