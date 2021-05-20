class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(s: str) -> bool:
            return s == s[::-1]
        def expand_window(window_start: int, window_end: int) -> str:
            longest_palindrome = s[window_start:window_end+1]
            # for even length window, this while loop searches for initial palindrome
            while longest_palindrome != longest_palindrome[::-1]:
                window_start += 1
                window_end += 1
                if window_end >= len(s): return ""
                longest_palindrome = s[window_start:window_end+1]
            while window_end < len(s):
                if isPalindrome(s[window_start:window_end+1]):
                    # expand window as much as possible (maintaining palindrome)
                    while window_start-1 >= 0 and window_end+1 <= len(s)-1 and s[window_start-1] == s[window_end+1]:
                        window_start -= 1
                        window_end += 1
                        longest_palindrome = s[window_start:window_end + 1]
                # shift window right
                window_start += 1
                window_end += 1
            return longest_palindrome

        if len(s) <= 1:
            return s
        odd_window_longest_palindrome = expand_window(0, 0)
        even_window_longest_palindrome = expand_window(0, 1)
        return max(odd_window_longest_palindrome, even_window_longest_palindrome, key=len)


    # def longestPalindrome(self, s: str) -> str:
    #     char_list = list(s)
    #     max_len = 0
    #     answer = ""
    #     for i in range(len(char_list)):
    #         for j in range(i+max_len, len(char_list)):
    #             target = char_list[i:j+1]
    #             if target == target[::-1]:
    #                 if j-i+1 > max_len:
    #                     max_len = j-i+1
    #                     answer = "".join(target)
    #     return answer

s = Solution()
print(s.longestPalindrome("aacabdkacaa"))
