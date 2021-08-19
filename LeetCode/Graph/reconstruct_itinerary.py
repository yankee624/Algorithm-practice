from typing import *
import collections

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(path: List[str]):
            if len(path) == total_length:
                return path
            next_nodes = graph[path[-1]][:]
            for idx, node in enumerate(next_nodes):
                graph[path[-1]].remove(node)
                path.append(node)
                ret = dfs(path)
                if ret is not None: return ret # Already found path
                # Met dead end -> backtrack
                path.pop()
                graph[path[-1]].insert(idx, node)

        total_length = len(tickets) + 1
        # Build graph
        graph = collections.defaultdict(list)
        for ticket in tickets:
            graph[ticket[0]].append(ticket[1])
        for node_list in graph.values():
            node_list.sort()
        # DFS
        result = dfs(["JFK"])
        return result

    # Why is this working?
    # def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    #     graph = collections.defaultdict(list)
    #     for a, b in sorted(tickets):
    #         graph[a].append(b)
    #     route = []
    #     def dfs(a):
    #         while graph[a]:
    #             # pop 했던거 기억했다가 다시 넣어줘야 하지 않나? 왜 작동하는거지?
    #             # 기존 지나왔던 경로는 무조건 정답에 포함된다는건데... 기존꺼 지우고 다시 가야하는 경우는 없나
    #             dfs(graph[a].pop(0))
    #         route.append(a)
    #
    #     dfs("JFK")
    #     return route[::-1]


s = Solution()
# print(s.findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
print(s.findItinerary([["JFK","b"],["b","c"],["b","d"],["d","e"],["e","b"]]))