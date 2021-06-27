class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        max_length = 1
        char_set = set()
        start = 0
        end = 0
        char_set.add(s[start])
        while end + 1 < len(s):
            # If repeated char, make window smaller by increasing first pointer
            if s[end+1] in char_set:
                # make window smaller
                char_set.remove(s[start])
                start += 1
            # If new char, make window larger by increasing second pointer
            else:
                char_set.add(s[end+1])
                end += 1
                max_length = max(max_length, end-start+1)
        return max_length

s = Solution()
print(s.lengthOfLongestSubstring("pwwkew")) # 3

