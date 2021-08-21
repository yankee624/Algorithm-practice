from typing import *
import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Detect loop
        def dfs(node):
            # There was no loop containing the node in "visited"
            # -> Can skip this node
            if node in visited:
                return True
            if node in path:
                return False
            path.add(node)
            for next_node in graph[node]:
                # loop detected
                ret = dfs(next_node)
                if ret is False:
                    return ret
            path.remove(node)
            visited.add(node)
            return True

        if len(prerequisites) <= 1:
            return True
        # Graph construction
        graph = collections.defaultdict(list)
        for prerequisite in prerequisites:
            graph[prerequisite[0]].append(prerequisite[1])

        path = set()
        visited = set()
        for node in list(graph.keys()):
            ret = dfs(node)
            if ret is False:
                return False

        return True


s = Solution()
print(s.canFinish(5, [[0,1],[1,0]]))