import re
import collections
class Solution:
    # Slicing based: very fast
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub("[^a-z0-9]", "", s)

        return s == s[::-1]

    # Deque based: moderate (faster than list based since pop(0) in list is O(n))
    # def isPalindrome(self, s: str) -> bool:
    #     s = s.lower()
    #     s = re.sub("[^a-z0-9]", "", s)
    #     chars = collections.deque(s)
    #     while len(chars) >= 2:
    #         if chars.pop() != chars.popleft():
    #             return False
    #     return True


s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))

