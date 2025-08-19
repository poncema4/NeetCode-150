class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows = len(matrix)
        cols = len(matrix[0])
        l = 0
        r = rows * cols - 1

        while l <= r:
            m = (l + r) // 2
            row = m // cols
            col = m % cols
            mid_val = matrix[row][col]

            if mid_val < target:
                l = m + 1
            elif mid_val > target:
                r = m - 1
            else:
                return True

        return False