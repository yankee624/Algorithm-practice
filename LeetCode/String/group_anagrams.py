from collections import Counter, defaultdict
from typing import *

class Solution:
    # Anagram becomes same word if sorted alphabetically
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for string in strs:
            result["".join(sorted(string))].append(string)
        return list(result.values())


    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     result = []
    #     counter_info = {}
    #     for idx, string in enumerate(strs):
    #         if idx == 0:
    #             counter_info[0] = Counter(string)
    #             result.append([string])
    #         else:
    #             target_counter = Counter(string)
    #             already_exist = False
    #             for result_idx, counter in counter_info.items():
    #                 if counter == target_counter:
    #                     result[result_idx].append(string)
    #                     already_exist = True
    #                     break
    #             if not already_exist:
    #                 counter_info[len(result)] = target_counter
    #                 result.append([string])
    #     return result




s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
