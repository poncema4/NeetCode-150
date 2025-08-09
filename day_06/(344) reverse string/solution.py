from collections import List

class Solution:
    def reverseString(self, s: List[str]) -> List[str]:
        l_point = 0
        r_point = len(s) - 1

        while l_point < r_point:
            temp = s[l_point]
            s[l_point] = s[r_point]
            s[r_point] = temp

            l_point += 1
            r_point -= 1

        return s