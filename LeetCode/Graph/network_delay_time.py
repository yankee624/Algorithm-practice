from typing import *
import collections
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for time in times:
            graph[time[0]].append((time[1], time[2]))

        dist = collections.defaultdict(int)
        heap = [(0, k)]

        while heap:
            time, node = heapq.heappop(heap)
            # Make dist to contain only shortest path
            # -> avoid updating dist values, priority values in the heap
            # (the first time node gets included in the heap, it is the shortest path)
            if node not in dist:
                dist[node] = time
                for next_node, edge in graph[node]:
                    heapq.heappush(heap, (time+edge, next_node))

        if len(dist) == n:
            return max(dist.values())
        return -1

s = Solution()
print(s.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))
