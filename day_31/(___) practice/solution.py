class Solution(object):
    def countSubsequence(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        count = 0

        for word in words:
            i = 0   # pointer for word, tracks which character we are looking for
            j = 0   # pointer for s, scans through the string

            # try matching all characters of word in order
            while i < len(word) and j < len(s):
                if word[i] == s[j]:
                    # found a match, move onto the next character in word
                    i += 1
                # always move forward in s (whether or not a match was found)
                j += 1

            # if we matched all characters in word, it is a subsequence and increment count
            if i == len(word):
                count += 1

        return count

c = Solution()
print(c.countSubsequence("abcde", ["a", "bb", "acd", "ace"]))