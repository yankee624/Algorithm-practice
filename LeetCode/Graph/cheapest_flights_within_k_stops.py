import collections
import heapq
from typing import *


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for from_node, to_node, price in flights:
            graph[from_node].append((to_node, price))

        visited = [0] * n
        Q = [(0, k+1, src)] # cost, number of stops left, node
        while Q:
            cost, remaining_stops, node = heapq.heappop(Q)
            if dst == node:
                return cost
            # already visited in the past (with lower cost) + remaining stops was higher
            # -> No need to process this node anymore
            # Need this skipping mechanism to avoid exceeding time limit
            if visited[node] >= remaining_stops:
                continue
            visited[src] = remaining_stops

            if remaining_stops > 0:
                for to_node, price in graph[node]:
                    heapq.heappush(Q, (cost+price, remaining_stops-1, to_node))
        return -1


s = Solution()
print(s.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1))

