import collections
from typing import *
from collections import defaultdict

class Solution:
    # Make stone dict -> Search for each jewel
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.defaultdict(int)
        for stone in stones:
            freqs[stone] += 1
        count = 0
        for jewel in jewels:
            count += freqs[jewel]
        return count

    # Make jewel set -> Search for each stone
    # def numJewelsInStones(self, jewels: str, stones: str) -> int:
    #     jewel_types = set(jewels)
    #     count = 0
    #     for stone in stones:
    #         if stone in jewel_types:
    #             count += 1
    #     return count

s = Solution()
print(s.numJewelsInStones("aA","aAAbbbb"))