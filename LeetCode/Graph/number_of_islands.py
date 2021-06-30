import collections
from typing import *


class Solution:
    # Recursive DFS: A bit slower but cleaner code
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r: int, c: int):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        num_islands = 0
        for r, row in enumerate(grid):
            for c, node in enumerate(row):
                if node == "1":
                    num_islands += 1
                    dfs(r, c)
        return num_islands

    # Stack based DFS: A bit faster
    # def numIslands(self, grid: List[List[str]]) -> int:
    #     def dfs(r: int, c: int):
    #         stack = [(r, c)]
    #         grid[r][c] = "0"
    #         while stack:
    #             r, c = stack.pop()
    #             if r - 1 >= 0 and grid[r-1][c] == "1":
    #                 stack.append((r-1, c))
    #                 grid[r-1][c] = "0"
    #             if r + 1 < len(grid) and grid[r+1][c] == "1":
    #                 stack.append((r+1, c))
    #                 grid[r+1][c] = "0"
    #             if c - 1 >= 0 and grid[r][c-1] == "1":
    #                 stack.append((r, c-1))
    #                 grid[r][c-1] = "0"
    #             if c + 1 < len(grid[0]) and grid[r][c+1] == "1":
    #                 stack.append((r, c+1))
    #                 grid[r][c+1] = "0"
    #
    #     num_islands = 0
    #     for r, row in enumerate(grid):
    #         for c, node in enumerate(row):
    #             if node == "1":
    #                 num_islands += 1
    #                 dfs(r, c)
    #     return num_islands


    # Making graph explicitly: slow speed and high memory consumption
    # def numIslands(self, grid: List[List[str]]) -> int:
    #     lands = set()
    #     graph = collections.defaultdict(list)
    #     for r, row in enumerate(grid):
    #         for c, node in enumerate(row):
    #             if node == "1":
    #                 lands.add((r, c))
    #                 if r-1 >= 0 and grid[r-1][c] == "1":
    #                     graph[(r, c)].append((r-1, c))
    #                 if r+1 < len(grid) and grid[r+1][c] == "1":
    #                     graph[(r, c)].append((r+1, c))
    #                 if c-1 >= 0 and grid[r][c-1] == "1":
    #                     graph[(r, c)].append((r, c-1))
    #                 if c+1 < len(row) and grid[r][c+1] == "1":
    #                     graph[(r, c)].append((r, c+1))
    #     num_islands = 0
    #     while lands:
    #         num_islands += 1
    #         land = lands.pop()
    #         visited = []
    #         stack = [land]
    #         while stack:
    #             node = stack.pop()
    #             visited.append(node)
    #             for adj_node in graph[node]:
    #                 if adj_node not in visited:
    #                     stack.append(adj_node)
    #         for node in visited:
    #             lands.discard(node)
    #     return num_islands

s = Solution()
print(s.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
])) # 1
