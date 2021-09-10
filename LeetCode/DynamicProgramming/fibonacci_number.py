import collections


class Solution:
    result = collections.defaultdict(int)
    # Recursive
    # def fib(self, n: int) -> int:
    #     if n <= 1:
    #         return n
    #     if n in self.result:
    #         return self.result[n]
    #     self.result[n] = self.fib(n - 1) + self.fib(n - 2)
    #     return self.result[n]

    # Iterative
    def fib(self, n: int) -> int:
        self.result[0] = 0
        self.result[1] = 1
        for i in range(2, n+1):
            self.result[i] = self.result[i-1] + self.result[i-2]

        return self.result[n]


s = Solution()
print(s.fib(3))

