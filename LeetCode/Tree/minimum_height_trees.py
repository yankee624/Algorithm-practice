from typing import *
import collections


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = collections.defaultdict(list)
        for edge in edges:
            # bi-directional
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        leaf_nodes = set()
        for i in range(n):
            # leaf node has only one edge connected!
            if len(graph[i]) == 1:
                leaf_nodes.add(i)

        while n > len(leaf_nodes):
            next_leaf_nodes = set()
            # remove leaf nodes from the graph
            for leaf_node in leaf_nodes:
                n -= 1
                leaf_candidate = graph[leaf_node].pop()
                graph[leaf_candidate].remove(leaf_node)
                if len(graph[leaf_candidate]) == 1:
                    next_leaf_nodes.add(leaf_candidate)
            leaf_nodes = next_leaf_nodes

        return list(leaf_nodes)


s = Solution()
print(s.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]))  # 1
