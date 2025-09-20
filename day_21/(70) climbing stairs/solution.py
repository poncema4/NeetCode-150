class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        prev = 1
        curr = 2

        for _ in range(3, n + 1):
            """
            prev = curr (ways for i - 1)
            curr = prev + curr (ways for i)
            """
            prev, curr = curr, prev + curr

        return curr