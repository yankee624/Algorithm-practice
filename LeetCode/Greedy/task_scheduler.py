import collections
from typing import *
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = collections.Counter(tasks)

        heap = []
        for task, count in counts.items():
            heapq.heappush(heap, (-count, task))

        time = 0
        while heap:
            # generate n+1 sized chunk with n+1 most frequent tasks
            popped_tasks = [] # temp list to put the remaining tasks into heap again
            idx = 0
            while True:
                if idx == n+1:
                    break
                if heap:
                    count, task = heapq.heappop(heap)
                    # if only one remaining, no need to put it back again
                    if count != -1:
                        popped_tasks.append((count + 1, task))
                else:
                    # remaining part of the chunk will be idle (except final chunk)
                    break
                idx += 1
            # final chunk
            if not heap and not popped_tasks:
                time += idx
            else:
                time += n+1

            for count, task in popped_tasks:
                heapq.heappush(heap, (count, task))
        return time


s = Solution()
print(s.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))
