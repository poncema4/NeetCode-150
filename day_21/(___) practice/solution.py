from typing import List

class Solution:
    def arrayManipulation(self, array: List[int]) -> List[int]:
        n = len(array)
        new_array = [0 for _ in range(n)]
        for i in range(n):
            new_array[i] = array[i]
            if i > 0:
                new_array[i] += array[i-1]
            if i < n - 1:
                new_array[i] += array[i+1]
            
        return new_array
    
c = Solution()
print(c.arrayManipulation([4, 0, 1, -2, 3]))