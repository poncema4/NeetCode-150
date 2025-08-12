class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        filtered = [ch.lower() for ch in s if ch.isalnum()]
        
        left = 0
        right = len(filtered) - 1

        while left < right:
            if filtered[left] != filtered[right]:
                return False

            left += 1
            right -= 1

        return True