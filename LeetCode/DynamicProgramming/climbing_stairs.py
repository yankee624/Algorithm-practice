class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        ways = [0] * (n+1)
        ways[1] = 1
        ways[2] = 2
        for i in range(3, n+1):
            ways[i] = ways[i-1] + ways[i-2]
        return ways[n]

s = Solution()
print(s.climbStairs(3))


