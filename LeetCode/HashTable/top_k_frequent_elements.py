import collections
import heapq
from typing import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.defaultdict(int)
        for num in nums:
            freqs[num] += 1
        heap = []
        for num in freqs:
            heapq.heappush(heap, (-freqs[num], num))
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result

    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     freqs = collections.Counter(nums)
    #     return [e[0] for e in freqs.most_common(k)]


s = Solution()
print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2)) # [1, 2]
