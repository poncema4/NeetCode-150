from typing import List

class Solution:
    def power_of_two(self, nums: List[int]) -> int:
        count = 0
        for n in nums:
            if n > 0 and (n & (n - 1)) == 0:
                count += 1
        return count

c = Solution()
print(c.power_of_two([1, 2, 3, 4, 5, 8, 16, 20]))