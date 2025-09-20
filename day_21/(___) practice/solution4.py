from typing import List
from collections import defaultdict

class Solution:
    def lookupTable(self, lon: List[int]) -> int:
        """
        lon: list of numbers 

        task: check how many pairs of indices i, j such that i <= j and the sum of them is equal to some power of 2
        edge: can include self reference indices
        """
        counts = defaultdict(int)
        total = 0

        for element in lon:
            counts[element] += 1
            for power in range(21):
                second_element = (2 ** power) - element
                total += counts[second_element]

        return total
    
c = Solution()
print(c.lookupTable([1, -1, 2, 3]))