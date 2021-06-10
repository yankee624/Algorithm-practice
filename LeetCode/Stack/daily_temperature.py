from typing import *

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        remaining = []
        for idx, temperature in enumerate(temperatures):
            while len(remaining) != 0 and temperatures[remaining[-1]] < temperature:
                item = remaining.pop()
                result[item] = idx - item
            remaining.append(idx)
        for item in remaining:
            result[item] = 0
        return result

s = Solution()
print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))
