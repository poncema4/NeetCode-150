class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [1] * n

        prev = 1
        for i in range(n):
            res[i] = prev
            prev *= nums[i]

        post = 1
        for i in range(n-1, -1, -1):
            res[i] *= post
            post *= nums[i]

        return res
    
# Difficulty: Medium