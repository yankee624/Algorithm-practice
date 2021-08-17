from typing import *
import itertools

class Solution:
    # DFS
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(current: List[int]):
            if len(current) == k:
                result.append(current[:])
                return

            # start 를 dfs 파라미터로 넘겨줘도 됨
            start = 1 if not current else current[-1]+1
            # remaining_numbers 리스트를 유지할 필요 없이 start만으로 가
            for num in range(start, n+1):
                current.append(num)
                dfs(current)
                current.pop()

        result = []
        dfs([])
        return result

    # one-liner
    # def combine(self, n: int, k: int) -> List[List[int]]:
    #     return list(itertools.combinations(range(1, n+1), k))

s = Solution()
print(s.combine(4, 2))