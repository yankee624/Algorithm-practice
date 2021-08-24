import collections
import heapq
from typing import *


class Solution:
    # Time limit exceeded
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for from_node, to_node, price in flights:
            graph[from_node].append((to_node, price))

        Q = [(0, k+1, src)] # cost, number of stops left, node
        while Q:
            cost, stops, node = heapq.heappop(Q)
            if dst == node:
                return cost

            if stops > 0:
                for to_node, price in graph[node]:
                    heapq.heappush(Q, (cost+price, stops-1, to_node))
        return -1


s = Solution()
print(s.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0))

