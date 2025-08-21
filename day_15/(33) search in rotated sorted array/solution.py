class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            # left half is sorted
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    # search right sorted portion
                    l = m + 1
                else:
                    # search left sorted portion
                    r = m - 1

            # right half is sorted
            else:
                if target < nums[m] or target > nums[r]:
                    # search left sorted portion
                    r = m - 1
                else:
                    # search right sorted portion
                    l = m + 1
            
        return -1