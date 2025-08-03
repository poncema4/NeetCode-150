class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        s_hash = {}
        t_hash = {}

        for i in range(len(s)):
            s_hash[s[i]] = 1 + s_hash.get(s[i], 0)
            t_hash[t[i]] = 1 + t_hash.get(t[i], 0)

        return s_hash == t_hash
    
# Difficulty: Easy