class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        count = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in count:
                return [count[diff], i]

            count[n] = i