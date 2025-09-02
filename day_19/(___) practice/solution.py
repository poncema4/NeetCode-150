class Solution:
    def is_power_of_two(self, n: int) -> bool:
        return (n & (n - 1)) == 0

solution = Solution()    
print(solution.is_power_of_two(1))   # True
print(solution.is_power_of_two(2))   # True
print(solution.is_power_of_two(3))   # False
print(solution.is_power_of_two(16))  # True
print(solution.is_power_of_two(18))  # False