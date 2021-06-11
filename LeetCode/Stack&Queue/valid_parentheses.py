class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match_dict = {')':'(', '}':'{', ']':'['}
        for char in s:
            if char in match_dict.values():
                stack.append(char)
            else:
                if len(stack) == 0 or match_dict[char] != stack.pop():
                    return False
        return len(stack) == 0

s = Solution()
print(s.isValid("()[]{}"))
